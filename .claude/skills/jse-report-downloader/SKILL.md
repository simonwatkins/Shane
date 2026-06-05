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

# JSE Report Downloader

## Purpose

Downloads financial documents from known sources (mapped in company.json) and saves
them locally with consistent naming. Updates the manifest so we always know what we have.
The workflow is fully automatic — no dragging, dropping, copy-pasting, or manual
downloads by the user.

## Golden rule: always preserve the original

**Save the ORIGINAL document (PDF/PPTX/XLSX) as the source of truth, and ALSO save a
plain-text extraction (`.txt`) sidecar next to it.** Never save text only.

- The original preserves what text extraction loses — financial-statement tables, charts,
  diagrams, footnotes, and audited layout. We must always be able to go back to it.
- The `.txt` sidecar makes the document fast to search, quote, and diff, and is what the
  analyst uses for keyword location before verifying numbers against the original.
- The two files share the same stem (only the extension differs) so they are obviously a
  pair.

## Prerequisites

- Company must already exist in `companies/[slug]/company.json`
- If it doesn't, trigger `jse-company-discovery` first

## How to Fetch (automatic, in order of preference)

1. **Direct download** of a known document URL via web fetch / bash (`curl`/`wget` only
   for allowlisted document hosts) — save the raw bytes to disk.
2. **Browser automation (Claude in Chrome)** when the IR page is JavaScript-rendered or
   the link is generated client-side: navigate, find the document link, trigger the
   download, then move/rename the file into the right subdirectory. This is also the
   fallback when a host blocks direct programmatic download.
3. **MCP connectors** (SharePoint / Google Drive / email) if configured — check there for
   documents the fund already holds before going to the public web.
4. **Web search fallback** for documents not linked on the IR site (especially SENS).

Asking the user to download something manually is an absolute last resort.

## Workflow

### Step 1: Read company.json

Load the company's metadata to get document source URLs.

### Step 2: Determine What to Download

Check the manifest for what we already have. Identify gaps:
- Do we have the most recent annual report?
- Do we have the corresponding interim?
- Are there SENS announcements we haven't captured?
- Is there a recent investor presentation?

### Step 3: Download & Store Each Document (original + text sidecar)

For each document:

1. **Fetch and save the original file** to the appropriate subdirectory using the naming
   convention below. Keep the native format (`.pdf`, `.pptx`, `.xlsx`).
2. **Generate the text sidecar** with the same stem and a `.txt` extension:
   - PDFs: `pdftotext -layout "<file>.pdf" "<file>.txt"` (poppler) — `-layout` best
     preserves column/table alignment. If poppler isn't available, use the **pdf** skill.
   - If the PDF is image-only (no extractable text), OCR it for the sidecar (e.g.
     `ocrmypdf` or the pdf skill's OCR path) and flag that the sidecar is OCR-derived.
   - PPTX/XLSX: extract text via the **pptx** / **xlsx** skills.

**File naming convention (original and sidecar share the stem):**
```
[company-slug]-[type]-[period]-[date].pdf      ← original (source of truth)
[company-slug]-[type]-[period]-[date].txt      ← text extraction sidecar

Examples:
shoprite-annual-report-fy2025-20250902.pdf  +  shoprite-annual-report-fy2025-20250902.txt
shoprite-interim-results-h1-2026-20260303.pdf  +  .txt
shoprite-trading-statement-fy2025-20250715.pdf  +  .txt
shoprite-sens-cautionary-20260301.pdf  +  .txt
shoprite-investor-presentation-fy2025-20250902.pptx  +  .txt
```

**Save to the appropriate subdirectory:**
- Annual reports → `annual-reports/`
- Interim results → `interim-reports/`
- Trading statements → `trading-statements/`
- SENS → `sens-announcements/`
- Investor presentations → `investor-presentations/`
- Press releases → `press-releases/`

### Step 4: SENS Search

Even if the company hosts its own SENS archive, also search the web:
- "[Company] SENS announcement [current year]"
- "[Company] trading statement [current year]"
- "[Company] cautionary announcement"
- "[Company] dividend declaration [current year]"

Download any new announcements not already in our local archive (original + sidecar).

### Step 5: Update the Manifest

After each successful download, update `manifest.json` (via `jse-manifest-manager`).
Record BOTH the original path and the text sidecar path:

```json
{
  "companies": {
    "shoprite": {
      "documents": {
        "shoprite-annual-report-fy2025-20250902.pdf": {
          "type": "annual_report",
          "period": "FY2025",
          "date_published": "2025-09-02",
          "date_downloaded": "2026-06-05T10:30:00Z",
          "path": "companies/shoprite/annual-reports/shoprite-annual-report-fy2025-20250902.pdf",
          "text_path": "companies/shoprite/annual-reports/shoprite-annual-report-fy2025-20250902.txt",
          "text_source": "pdftotext -layout",
          "source_url": "https://...",
          "pages": 142,
          "file_size_mb": 8.3
        }
      }
    }
  }
}
```

The manifest is keyed on the **original** filename. `text_path` points to the sidecar;
`text_source` records how it was produced (`pdftotext -layout`, `ocr`, `pptx-skill`, etc.)
so the analyst knows how much to trust the text vs the original.

### Step 6: Verify Downloads

After downloading, verify each pair:
- **Original is real:** first bytes are `%PDF` (or a valid PPTX/XLSX zip header), not an
  HTML error page; file size reasonable (>100KB for a real report).
- **Sidecar is usable:** the `.txt` is non-empty and contains expected tokens (company
  name, "headline earnings", period). If empty, the PDF was likely image-only — OCR it
  and regenerate the sidecar.
- Re-attempt download if the first attempt got an error page.

### Step 7: Report

Summarise what was downloaded:
- X new documents downloaded for [Company] (original + text each)
- Y documents already up to date
- Z documents could not be found or downloaded (with reasons)

Offer to proceed to analysis if new documents were downloaded.

## Incremental Updates

When asked to "check for updates" or "refresh":
1. Check `last_checked` date in company.json
2. Only search for documents published after that date
3. Download new items only (original + sidecar)
4. Update `last_checked` timestamp

## Handling Download Failures

Many company IR pages serve documents through JavaScript loaders or require specific
referrer headers, and some hosts block direct programmatic download (e.g. a proxy 403).
If a direct download fails:

1. Switch to browser automation (Claude in Chrome) to render the page and click through
   to the document — this also defeats most direct-download blocks.
2. Note the failure in company.json under a `download_notes` field.
3. Search for the same document via alternative sources (company name + document title).
4. If the site structure has clearly changed, trigger `jse-company-discovery` to re-map
   it and `jse-skill-builder` to update the company skill.
5. If only the text could be captured (e.g. via web fetch) but not the original binary,
   save the text sidecar, set `text_source` accordingly, and record a `coverage_gap`
   noting the original is still outstanding — so we know to backfill the PDF later.
6. Only as an absolute last resort, after exhausting all automated options, flag to the
   user: "I couldn't download [document] automatically. The link is [URL]."
