---
name: jse-manifest-manager
description: >
  Maintains the master research manifest — the single source of truth for what
  documents we have, what's missing, and what's due for refresh. Use this skill
  when the user asks "what do we have", "what's missing", "status of our research",
  "show me the manifest", "what companies do we track", "what needs updating",
  "what reports are due", "give me an overview", or any question about the state
  of our research data. Also trigger when any other skill needs to read or write
  the manifest. This skill is the librarian — it knows where everything is and
  what's overdue.
---

# JSE Manifest Manager

## Purpose

The manifest is the single source of truth. It tracks every company we cover, every
document we've downloaded, when we last checked for updates, and what's expected next.
This skill reads and writes the manifest and provides status reports.

## Manifest Location

`manifest.json` at the research root (this Cowork folder).

## Manifest Structure

```json
{
  "manifest_version": 1,
  "last_global_refresh": "2026-06-05T08:00:00Z",
  "companies": {
    "shoprite": {
      "name": "Shoprite Holdings Limited",
      "jse_code": "SHP",
      "sector": "Retail",
      "financial_year_end": "June",
      "last_updated": "2026-06-05T10:30:00Z",
      "skill_generated": true,
      "skill_path": ".claude/skills/jse-shoprite/SKILL.md",
      "next_expected_results": {
        "type": "FY2026 Annual Results",
        "expected_date": "2026-09-15",
        "notes": "Typically 10-12 weeks after June year-end"
      },
      "documents": {
        "shoprite-annual-report-fy2025-20250901.pdf": {
          "type": "annual_report",
          "period": "FY2025",
          "date_published": "2025-09-01",
          "date_downloaded": "2026-06-05T10:30:00Z",
          "path": "companies/shoprite/annual-reports/...pdf",
          "text_path": "companies/shoprite/annual-reports/...txt",
          "text_source": "pdftotext -layout",
          "source_url": "https://...",
          "analysed": true,
          "analysis_date": "2026-06-05T11:00:00Z"
        }
      },
      "coverage_gaps": [
        "No H1 2026 interim results yet — expected Feb 2026, may have been published"
      ]
    }
  },
  "watchlist": ["shoprite", "capitec", "firstrand", "naspers", "mtn"],
  "reporting_calendar": [
    {
      "company": "shoprite",
      "event": "FY2026 Annual Results",
      "expected": "2026-09-15",
      "status": "pending"
    }
  ]
}
```

## Operations

### Status Report

When asked "what do we have" or "show status":
1. Read manifest.json
2. For each company, summarise: total documents, most recent document and its date,
   coverage gaps, next expected results
3. Present as a clean summary table

### Gap Analysis

When asked "what's missing" or "what needs updating":
1. For each company check: is the most recent annual report present (vs year-end)? Is
   the corresponding interim present? Have we checked SENS in the last 7 days? Are any
   calendar items now overdue?
2. Produce a prioritised action list

### Reporting Calendar

Maintain a forward-looking calendar of expected results dates. Sources:
- Financial year-end month + typical publication lag (8-12 weeks for annuals, 6-8 weeks
  for interims)
- Trading statements (typically 2-3 weeks before results)
- Company guidance on results publication dates (if found during discovery)

### Watchlist Management

The watchlist defines which companies get checked during a global refresh.
- "Add [company] to the watchlist" → add to watchlist array
- "Remove [company] from the watchlist" → remove
- "Show the watchlist" → display with summary status for each

### Global Refresh

When asked to "refresh everything" or "morning update":
1. For each company on the watchlist: search for new SENS since last_updated; check if
   any expected results have been published
2. Download any new documents found (via jse-report-downloader)
3. Update the manifest
4. Present a summary: "3 new documents found across 2 companies"

### Document Verification

Periodically verify that local files still exist and are readable:
1. Walk every path recorded in the manifest
2. Flag any missing files (deleted externally?)
3. Flag any files on disk that aren't in the manifest (manually added?)

## Concurrency Safety

The manifest is a single JSON file. When updating: read current state → apply changes →
write the complete updated state. Never partially update — always write the full file.

## Manifest Migrations

If the manifest structure changes (new fields, renamed keys), handle gracefully:
- Add new fields with sensible defaults
- Don't remove old fields without explicit instruction
- Record the schema in the `manifest_version` field
