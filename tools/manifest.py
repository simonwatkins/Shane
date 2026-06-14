#!/usr/bin/env python3
"""Deterministic manifest tooling for the JSE research workspace.

manifest.json is a GENERATED artifact. NEVER hand-edit it.

Source of truth:
  - companies/<slug>/company.json   (per-company metadata + document records)
  - the document files actually on disk

manifest.json is a pure function of those inputs, written ATOMICALLY (temp file ->
re-parse guard -> os.replace) with a timestamped backup, so a truncated/partial
write can never land. This is what makes corruption structurally impossible.

Commands
  rebuild    Regenerate manifest.json from every company.json + a disk scan.
  validate   Validate every company.json and manifest.json. Non-zero exit on error.
  add-doc    Add/update one document record in a company.json, then rebuild.
  migrate    One-time: fold legacy manifest.json document metadata into each company.json.

Typical use:
  python3 tools/manifest.py rebuild
  python3 tools/manifest.py validate
  python3 tools/manifest.py add-doc naspers \\
      --folder annual-reports \\
      --file naspers-integrated-report-fy2025.txt \\
      --type integrated_report --period FY2025 --date-published 2025-06-23 \\
      --source-url https://... --text-source "web_fetch"
"""
import argparse
import datetime
import glob
import json
import os
import shutil
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # workspace root
COMPANIES_DIR = os.path.join(ROOT, "companies")
MANIFEST = os.path.join(ROOT, "manifest.json")
GLOBALS = os.path.join(ROOT, "_manifest_globals.json")
BACKUP_DIR = os.path.join(ROOT, ".manifest-backups")
MAX_BACKUPS = 15

DOC_FOLDERS = [
    "annual-reports", "interim-reports", "trading-statements",
    "sens-announcements", "investor-presentations", "press-releases",
    "analyst-notes",
]

# Fields copied from company.json into the generated per-company manifest summary.
SUMMARY_FIELDS = [
    "name", "jse_code", "a2x_code", "related_entity", "sector",
    "financial_year_end", "reporting_currency", "trading_currency",
    "skill_path", "skill_generated", "onboarded", "last_updated",
    "next_expected_results", "coverage_gaps",
]

try:
    import jsonschema  # type: ignore
    HAVE_JS = True
except Exception:
    HAVE_JS = False

COMPANY_SCHEMA = {
    "type": "object",
    "required": ["name"],
    "properties": {
        "name": {"type": "string"},
        "jse_code": {"type": "string"},
        "reporting_currency": {"type": "string"},
        "financial_year_end": {"type": "string"},
        "documents": {
            "type": "object",
            "additionalProperties": {
                "type": "object",
                "required": ["type", "period", "path"],
                "properties": {
                    "type": {"type": "string"},
                    "period": {"type": "string"},
                    "path": {"type": "string"},
                    "date_published": {"type": "string"},
                    "source_url": {"type": "string"},
                    "original_saved": {"type": "boolean"},
                    "analysed": {"type": "boolean"},
                },
                "additionalProperties": True,
            },
        },
    },
    "additionalProperties": True,
}


def now_iso():
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def atomic_write_json(path, obj):
    """Write JSON atomically: temp file -> re-parse guard -> backup -> os.replace."""
    d = os.path.dirname(path) or "."
    os.makedirs(d, exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=d, suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            json.dump(obj, f, indent=2, ensure_ascii=False)
            f.write("\n")
        # Guard: the temp file MUST parse before we let it replace the real file.
        with open(tmp, encoding="utf-8") as f:
            json.load(f)
        if os.path.exists(path):
            os.makedirs(BACKUP_DIR, exist_ok=True)
            ts = now_iso().replace(":", "").replace("-", "")
            shutil.copy2(path, os.path.join(BACKUP_DIR, "%s.%s.bak" % (os.path.basename(path), ts)))
        os.replace(tmp, path)  # atomic on the same filesystem
    finally:
        if os.path.exists(tmp):
            os.remove(tmp)
    _prune_backups(os.path.basename(path))


def _prune_backups(basename):
    if not os.path.isdir(BACKUP_DIR):
        return
    backups = sorted(glob.glob(os.path.join(BACKUP_DIR, basename + ".*.bak")))
    for old in backups[:-MAX_BACKUPS]:
        try:
            os.remove(old)
        except OSError:
            pass


def load_json(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def company_json_path(slug):
    return os.path.join(COMPANIES_DIR, slug, "company.json")


def discover_companies():
    slugs = []
    for p in sorted(glob.glob(os.path.join(COMPANIES_DIR, "*", "company.json"))):
        slugs.append(os.path.basename(os.path.dirname(p)))
    return slugs


def validate_company(slug, data):
    errors = []
    if HAVE_JS:
        v = jsonschema.Draft7Validator(COMPANY_SCHEMA)
        for e in sorted(v.iter_errors(data), key=lambda x: list(x.path)):
            loc = "/".join(str(x) for x in e.path)
            errors.append("%s: %s" % (loc or "<root>", e.message))
    else:
        if "name" not in data:
            errors.append("<root>: missing required 'name'")
        for fn, meta in (data.get("documents") or {}).items():
            if not isinstance(meta, dict):
                errors.append("documents/%s: not an object" % fn)
                continue
            for req in ("type", "period", "path"):
                if req not in meta:
                    errors.append("documents/%s: missing '%s'" % (fn, req))
    return errors


def scan_disk_docs(slug):
    """Relative paths (companies/<slug>/<folder>/<file>) of all doc files on disk."""
    found = set()
    base = os.path.join(COMPANIES_DIR, slug)
    for folder in DOC_FOLDERS:
        for p in glob.glob(os.path.join(base, folder, "*")):
            if os.path.isfile(p):
                found.add(os.path.relpath(p, ROOT).replace(os.sep, "/"))
    return found


def load_globals():
    if os.path.exists(GLOBALS):
        return load_json(GLOBALS)
    return {"last_global_refresh": None, "watchlist": []}


# ---------------------------------------------------------------------------
# commands
# ---------------------------------------------------------------------------

def cmd_rebuild(args):
    g = load_globals()
    companies = {}
    problems = []
    calendar = []

    slugs = discover_companies()
    for slug in slugs:
        data = load_json(company_json_path(slug))
        problems += validate_company(slug, data)

        docs = data.get("documents", {}) or {}
        tracked = set()
        for m in docs.values():
            if isinstance(m, dict):
                tracked.add(m.get("path"))
                tracked.add(m.get("text_path"))  # sidecar is tracked, not orphaned
        on_disk = scan_disk_docs(slug)
        missing = sorted(
            fn for fn, m in docs.items()
            if isinstance(m, dict) and m.get("path")
            and not os.path.exists(os.path.join(ROOT, m["path"]))
        )
        untracked = sorted(on_disk - tracked)

        entry = {k: data[k] for k in SUMMARY_FIELDS if k in data}
        entry["documents"] = docs
        entry["document_count"] = len(docs)
        if missing:
            entry["_missing_files"] = missing
            problems.append("%s: %d document record(s) point to files that do not exist on disk" % (slug, len(missing)))
        if untracked:
            entry["_untracked_files"] = untracked
            problems.append("%s: %d file(s) on disk have NO metadata record in company.json" % (slug, len(untracked)))
        companies[slug] = entry

        ner = data.get("next_expected_results")
        if isinstance(ner, dict) and ner.get("expected_date"):
            calendar.append({
                "company": slug,
                "expected_date": ner["expected_date"],
                "type": ner.get("type", ""),
                "notes": ner.get("notes", ""),
            })

    calendar.sort(key=lambda x: x["expected_date"])

    manifest = {
        "manifest_version": 2,
        "generated_at": now_iso(),
        "generated_by": "tools/manifest.py rebuild - GENERATED FILE, DO NOT HAND-EDIT",
        "source_of_truth": "companies/<slug>/company.json + files on disk",
        "last_global_refresh": g.get("last_global_refresh"),
        "watchlist": g.get("watchlist", []),
        "company_count": len(companies),
        "reporting_calendar": calendar,
        "companies": companies,
    }
    if problems:
        manifest["_integrity_warnings"] = problems

    atomic_write_json(MANIFEST, manifest)
    print("rebuilt manifest.json: %d companies, %d documents, %d calendar entries"
          % (len(companies),
             sum(c["document_count"] for c in companies.values()),
             len(calendar)))
    if problems:
        print("\nintegrity warnings (%d):" % len(problems))
        for p in problems:
            print("  - " + p)
    else:
        print("no integrity warnings.")
    return 0


def cmd_validate(args):
    ok = True
    for slug in discover_companies():
        errs = validate_company(slug, load_json(company_json_path(slug)))
        if errs:
            ok = False
            print("INVALID company.json [%s]:" % slug)
            for e in errs:
                print("  - " + e)
    # manifest must at least parse
    try:
        load_json(MANIFEST)
        print("manifest.json parses OK")
    except Exception as e:
        ok = False
        print("manifest.json INVALID: %s" % e)
    if ok:
        print("all company.json files valid.")
        return 0
    return 1


def cmd_add_doc(args):
    cpath = company_json_path(args.slug)
    if not os.path.exists(cpath):
        print("error: %s does not exist. Onboard the company first." % cpath)
        return 1
    data = load_json(cpath)
    rel_path = "companies/%s/%s/%s" % (args.slug, args.folder, args.file)
    if not os.path.exists(os.path.join(ROOT, rel_path)):
        print("warning: target file not found on disk: %s" % rel_path)
    rec = {
        "type": args.type,
        "period": args.period,
        "date_published": args.date_published,
        "date_downloaded": now_iso(),
        "path": rel_path,
        "text_path": rel_path,
        "original_saved": args.original_saved,
        "analysed": args.analysed,
    }
    if args.source_url:
        rec["source_url"] = args.source_url
    if args.text_source:
        rec["text_source"] = args.text_source
    data.setdefault("documents", {})[args.file] = rec
    data["last_updated"] = now_iso()
    errs = validate_company(args.slug, data)
    if errs:
        print("refusing to write - resulting company.json would be invalid:")
        for e in errs:
            print("  - " + e)
        return 1
    atomic_write_json(cpath, data)
    print("added document record to %s" % cpath)
    return cmd_rebuild(args)


def cmd_migrate(args):
    if not os.path.exists(MANIFEST):
        print("no manifest.json to migrate from.")
        return 1
    legacy = load_json(MANIFEST)
    legacy_companies = legacy.get("companies", {})
    moved = 0
    for slug, block in legacy_companies.items():
        cpath = company_json_path(slug)
        if os.path.exists(cpath):
            data = load_json(cpath)
        else:
            # seed a minimal company.json from the manifest identity fields
            data = {k: block[k] for k in
                    ("name", "jse_code", "sector", "financial_year_end",
                     "reporting_currency", "trading_currency", "related_entity")
                    if k in block}
            data.setdefault("name", slug)
            print("seeded new company.json for %s (had none)" % slug)
        for key in ("documents", "next_expected_results", "coverage_gaps",
                    "analyst_notes", "skill_path", "skill_generated", "onboarded"):
            if key in block:
                data[key] = block[key]
        data["last_updated"] = now_iso()
        atomic_write_json(cpath, data)
        moved += 1
    print("migrated %d companies' metadata into their company.json files." % moved)
    print("now run: python3 tools/manifest.py rebuild")
    return 0


def main(argv=None):
    p = argparse.ArgumentParser(description="Deterministic manifest tooling (generated index).")
    sub = p.add_subparsers(dest="cmd", required=True)

    sub.add_parser("rebuild", help="Regenerate manifest.json from company.json files + disk scan.")
    sub.add_parser("validate", help="Validate all company.json and manifest.json.")
    sub.add_parser("migrate", help="One-time: fold legacy manifest doc metadata into company.json files.")

    a = sub.add_parser("add-doc", help="Add/update a document record in a company.json, then rebuild.")
    a.add_argument("slug")
    a.add_argument("--folder", required=True, choices=DOC_FOLDERS)
    a.add_argument("--file", required=True)
    a.add_argument("--type", required=True)
    a.add_argument("--period", required=True)
    a.add_argument("--date-published", dest="date_published", required=True)
    a.add_argument("--source-url", dest="source_url", default=None)
    a.add_argument("--text-source", dest="text_source", default=None)
    a.add_argument("--original-saved", dest="original_saved", action="store_true")
    a.add_argument("--not-analysed", dest="analysed", action="store_false")
    a.set_defaults(analysed=True, original_saved=False)

    args = p.parse_args(argv)
    return {
        "rebuild": cmd_rebuild,
        "validate": cmd_validate,
        "add-doc": cmd_add_doc,
        "migrate": cmd_migrate,
    }[args.cmd](args)


if __name__ == "__main__":
    sys.exit(main())
