---
name: jse-report-downloader
description: >
  Downloads financial reports, SENS announcements, and presentations for JSE-listed
  companies. Use this skill whenever the user asks to download, fetch, get, pull, or
  update documents for a company. Also trigger when the user says "get the latest
  results", "download the annual report", "fetch SENS", "update [company]'s documents",
  "check for new filings", or any variation of retrieving financial documents. Also
  trigger automatically after jse-company-discovery completes to download initial
  documents. This skill reads company.json to know where to look and never re-explores
  from scratch — that's jse-company-discovery's job.
---

# JSE Report Downloader (dispatcher)

This skill is a **thin dispatcher**. The actual download work runs in the
**`jse-report-downloader` subagent** (`.claude/agents/jse-report-downloader.md`) so that
the heavy, noisy machinery — browser navigation, redirect resolution, cookie harvesting,
HTTP fetches, byte-level validation, text extraction — happens in an **isolated context
window** and never consumes the main thread. The full operating procedure (the two-phase
discovery→download method, the GOLDEN RULE that the PDF is the deliverable, validation,
naming, manifest updates, coverage gaps) lives in the subagent's system prompt — it is
NOT repeated here, and you should NOT perform that work inline.

## What to do when this skill triggers

1. **Cheap prerequisite check (main context).** Is the company onboarded? If there is no
   `companies/[slug]/company.json`, run **`jse-company-discovery`** first (and then
   `jse-skill-builder`), because the downloader assumes a mapped company. Don't explore
   IR sites here yourself.

2. **Delegate to the subagent.** Call the **Task** tool with `subagent_type:
   "jse-report-downloader"` and a prompt that contains:
   - the company **slug**(s);
   - **what to fetch** — e.g. "latest annual + interim + any new SENS", a specific
     document, or "incremental: everything published since `last_checked`";
   - any **known source URLs / patterns** already in `company.json` (saves it a lookup).

   Launch one subagent per company; if several companies were requested, send them as
   parallel Task calls in a single message so they run concurrently.

3. **Relay the result.** The subagent returns a compact report: documents saved
   (original + sidecar), what was already current, and any **coverage gaps** (each with a
   direct URL + size). Surface that to the user as-is — especially the gaps, which are the
   one-click backfill list. If the subagent returns `NEEDS_ONBOARDING` or
   `NEEDS_REDISCOVERY`, run `jse-company-discovery` / `jse-skill-builder` and re-delegate.

## Why a subagent (not inline)

A full download run produces pages of browser DOM, redirect chains, header dumps and
validation logs. Keeping all of that in the main conversation is exactly what was starving
later analysis work of context. Isolating it means only the outcome (saved / current /
gaps) re-enters the main thread. The subagent inherits this project's `CLAUDE.md`, so the
principles ("numbers are sacred", "source everything", "never ask the user to fetch what
you can retrieve") still bind it.
