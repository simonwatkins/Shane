---
name: jse-company-discovery
description: >
  Discovers and onboards new JSE-listed companies into the research workspace. Use this
  skill whenever the user mentions a JSE company we haven't tracked before, asks to "add"
  or "onboard" a company, mentions a company name that doesn't appear in manifest.json,
  or asks about any South African listed company for the first time. Also trigger when the
  user says things like "start covering [company]", "what do we have on [company]",
  "look into [company]", or any variation suggesting we should begin tracking a company.
  This skill handles the initial exploration: finding the IR website, mapping where
  documents live, creating the local folder structure, and writing company.json so that
  future lookups are instant and never require re-exploration.
---

# JSE Company Discovery

## Purpose

When we encounter a company for the first time, this skill does the one-time exploration
work: finds the investor relations website, maps the document structure, determines the
reporting calendar, and saves everything so we never have to do this again.

## Workflow

### Step 1: Check If We Already Track This Company

Read `manifest.json` at the research root. If the company exists, skip discovery — hand
off to `jse-report-downloader` or `jse-analyst` instead.

### Step 2: Identify the Company

Search the web for:
- "[Company name] JSE investor relations"
- "[Company name] annual results JSE"
- "[Company name] JSE listing code"

Establish:
- **Full legal name** (e.g. "Shoprite Holdings Limited")
- **JSE code** (e.g. "SHP")
- **Sector** (Banking, Retail, Mining, Telco, Property, Insurance, Industrial, Other) — also save this as `icb_sector`, the routing key `jse-analyst` uses to auto-load the matching `jse-sector-<x>` lens (e.g. "Mining" → `jse-sector-mining`)
- **Reporting currency** (ZAR unless otherwise)
- **Financial year-end** month
- **Dual listings** if any (LSE, ASX, etc.)

### Step 3: Map the IR Website

Navigate to the company's investor relations page. Use web fetch first; if the page is
JavaScript-heavy and returns an empty shell, use the browser automation tools (Claude in
Chrome) to render it and read the real content. Find and record URLs for:
- Annual reports / integrated reports
- Interim / half-year results
- Trading statements
- SENS announcements (some companies host their own archive)
- Investor presentations / results booklets
- Press releases
- Annual financial statements (sometimes separate from the integrated report)

**Important:** Many SA company IR pages use JavaScript-heavy document libraries. Record
the base URL patterns, e.g.:
- `https://www.shopriteholdings.co.za/investors/results.html`
- `https://www.capitecbank.co.za/investor-relations/financial-results/`

Note the URL pattern for individual documents if discoverable (helps future downloads).

### Step 4: Create the Local Structure

```
companies/[company-slug]/
├── company.json
├── annual-reports/
├── interim-reports/
├── trading-statements/
├── sens-announcements/
├── investor-presentations/
├── press-releases/
└── analyst-notes/
```

The `company-slug` is lowercase, hyphenated (e.g. "shoprite", "pick-n-pay",
"anglo-american-platinum").

### Step 5: Write company.json

```json
{
  "name": "Shoprite Holdings Limited",
  "slug": "shoprite",
  "jse_code": "SHP",
  "sector": "Retail",
  "icb_sector": "Retail",
  "sub_sector": "Food Retail",
  "reporting_currency": "ZAR",
  "financial_year_end": "June",
  "dual_listings": [],
  "ir_website": "https://www.shopriteholdings.co.za/investors.html",
  "document_sources": {
    "annual_reports": {
      "url": "https://www.shopriteholdings.co.za/investors/results.html",
      "notes": "PDFs linked under 'Annual Financial Statements' section"
    },
    "interim_reports": {
      "url": "https://www.shopriteholdings.co.za/investors/results.html",
      "notes": "Same page, under 'Interim Results'"
    },
    "trading_statements": {
      "url": null,
      "notes": "Published via SENS, no dedicated page"
    },
    "sens": {
      "url": "https://www.shopriteholdings.co.za/investors/sens.html",
      "notes": "Company hosts own SENS archive"
    },
    "investor_presentations": {
      "url": "https://www.shopriteholdings.co.za/investors/results.html",
      "notes": "Results presentations linked alongside financial statements"
    },
    "press_releases": {
      "url": "https://www.shopriteholdings.co.za/media/press-releases.html",
      "notes": ""
    }
  },
  "key_metrics_framework": "retail",
  "discovered_at": "2026-06-05T10:00:00Z",
  "last_checked": "2026-06-05T10:00:00Z",
  "notes": "Reports typically published 6-8 weeks after year-end"
}
```

### Step 6: Update the Master Manifest

Hand off to `jse-manifest-manager` (or write directly) to add the company to
`manifest.json`:

```json
{
  "companies": {
    "shoprite": {
      "name": "Shoprite Holdings Limited",
      "jse_code": "SHP",
      "sector": "Retail",
      "documents": {},
      "last_updated": "2026-06-05T10:00:00Z"
    }
  }
}
```

### Step 7: Trigger the Skill Builder

After discovery, trigger `jse-skill-builder` to write a company-specific skill to
`.claude/skills/jse-[slug]/SKILL.md` that encodes everything we just learned, so future
interactions with this company are instant.

### Step 8: Report to the User

Summarise what was found:
- Company identified and classified
- IR website mapped with X document sources found
- Local folder structure created
- Ready to download documents (offer to proceed immediately)

## Error Handling

- If the IR website can't be found, note this in company.json and flag to the user.
  Some smaller companies have poor IR pages. Record whatever partial information is
  available.
- If the company isn't JSE-listed, tell the user. Don't create the structure.
- If the company is dual-listed, note the primary listing and any differences in where
  documents are published.
