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
The workflow is **fully automatic and unattended** — no dragging, dropping, copy-pasting,
manual downloads, or permission prompts.

## GOLDEN RULE: the PDF is the deliverable. Text is never a substitute.

**For every document you MUST save the ORIGINAL binary (PDF/PPTX/XLSX) as the source of
truth, AND a plain-text `.txt` sidecar next to it.** A `.txt` on its own is a FAILED
download, not a completed one.

- The original preserves what text extraction loses — financial-statement tables, charts,
  footnotes, audited layout. We must always be able to go back to it.
- The `.txt` sidecar makes the document fast to search, quote and diff.
- The two files share the same stem; only the extension differs.

If you cannot obtain the binary, you do NOT mark the document as downloaded. You record an
explicit `coverage_gap` with the direct URL and file size and surface it to the user
(see "If the binary truly can't be saved"). Storing the text and moving on is the exact
mistake this rule exists to prevent.

## Architecture: TWO DISTINCT PHASES — discovery, then download

The browser is good at rendering JavaScript and resolving where a PDF actually lives. It is
**bad** at unattended bulk downloading: it blocks multi-file downloads and raises permission
dialogs that stall an unattended run. So we split the job in two and never mix them:

- **Phase 1 — Discovery (browser):** use the headless browser ONLY to navigate, render JS,
  and resolve each report's final `.pdf` URL. Collect URLs, cookies, and the page each link
  was found on. **Do NOT click any download link in the browser.**
- **Phase 2 — Download (out-of-band HTTP):** fetch each resolved URL with a direct HTTP
  request (curl or Python `requests`), one at a time, carrying the Phase-1 cookies/headers.

This separation is what makes the flow run unattended: the browser never triggers a
download, so the multi-file-download block and permission dialogs are never reached.

> Why not bare `curl` with no headers? IR sites gate document URLs. A cold request with no
> cookies, no `User-Agent`, and no `Referer` typically returns `403` or an HTML login/error
> page instead of the PDF. Phase 1 exists precisely to harvest the cookies and the referring
> page URL so Phase 2's HTTP request looks like a real browser continuing the same session.

## Prerequisites

- Company must already exist in `companies/[slug]/company.json`.
- If it doesn't, trigger `jse-company-discovery` first.
- Before fetching externally, check any configured **MCP file connector**
  (SharePoint / Google Drive / Box / email). If the fund already holds the document, take it
  from there and skip both phases for that file.

---

## Phase 1 — Discovery (browser only): resolve URLs, harvest cookies

Goal: produce a **discovery list** — one entry per target document — with everything Phase 2
needs. Nothing is downloaded here.

### 1.1 Build the target list
Read `company.json` for document source URLs and patterns. Check the manifest for gaps:
latest annual report? corresponding interim? new SENS? recent investor presentation? IR
filenames change year to year — never assume last year's slug.

### 1.2 Navigate and resolve each final PDF URL (browser)
For each target, in the browser (Claude in Chrome):
1. `tabs_context_mcp` (createIfEmpty) → get a tabId; `navigate` the tab to the IR results /
   announcements page where the document is linked (e.g.
   `https://www.clicksgroup.co.za/results/`). Let JavaScript render.
2. Resolve the link to its **final `.pdf`** URL:
   - Read the rendered DOM / anchors to find the report link.
   - If the visible control is a "Download" button or a redirector (not a direct `.pdf`),
     resolve it to the underlying `.pdf` — follow `href`/`data-*` attributes and any HTTP
     redirects to the terminal URL. Use a GET-and-cancel fetch in the page to follow
     redirects and read the final `response.url` and `Content-Type` WITHOUT saving anything:
     ```js
     // resolve only — do NOT download. REPL has no top-level await: stash on window.
     window.__r=null;
     fetch(URL,{method:'GET'}).then(r=>{window.__r={finalUrl:r.url,status:r.status,type:r.headers.get('content-type')};r.body&&r.body.cancel&&r.body.cancel();});
     'started';
     // follow-up call:
     JSON.stringify(window.__r)   // expect {finalUrl:"...pdf", status:200, type:"application/pdf"}
     ```
   - Record the **finalUrl** (the value you will hand to Phase 2), not the button URL.
3. **Note the Referer:** record the page URL the link was found on (the IR page you
   navigated to). Phase 2 sends this as the `Referer` header.

### 1.3 Harvest session cookies (once, before exiting the browser)
After resolving the links, capture the browser session cookies for the document host so
Phase 2 can present the same session:
```js
document.cookie   // read on the document host's origin
```
For HttpOnly cookies that `document.cookie` can't see, read them via the browser's network /
cookie inspection on the relevant origin. Store the full `Cookie:` header string.

### 1.4 Output of Phase 1 — the discovery list
Produce a structured list (keep it in working memory / a temp JSON) like:
```json
[
  {
    "slug": "clicks-group",
    "type": "annual-results", "period": "fy2025", "date": "20251023",
    "final_url": "https://.../clicks-annual-2025.pdf",
    "referer": "https://www.clicksgroup.co.za/results/",
    "cookies": "SESS=abc; cf_clearance=xyz",
    "presigned": false,
    "subdir": "annual-reports"
  }
]
```
Mark `presigned: true` for any URL containing an expiry/signature (e.g. S3 `X-Amz-Expires`,
`Signature`, `Expires`, `token=`). **Presigned/expiring links must be downloaded in Phase 2
immediately after discovery** (see ordering note below), not batched at the end.

**Logging (Phase 1):** for each target log one line —
`DISCOVERED <type> <period> -> <final_url> (referer=<page>, presigned=<bool>)`.
Log cookie harvest as `COOKIES captured for <host> (<n> cookies)`.

---

## Phase 2 — Download (out-of-band HTTP): one file at a time

Goal: turn each discovery-list entry into a validated original PDF on disk, plus a `.txt`
sidecar. Use direct HTTP (curl or Python `requests`) in sandbox bash. **Never the browser.**

### Ordering
- Process the list **sequentially — one request per file.** Do not parallelise; one
  in-flight request at a time keeps the flow simple and ensures no multi-download behaviour.
- **Presigned/expiring URLs first**, and as soon as possible after discovery, because their
  signatures time out. If a presigned link is already in the list when Phase 2 starts, fetch
  it before the non-expiring ones.

### 2.1 Fetch the original
Send a request that mimics the Phase-1 browser session. Required on every request:
- **Follow redirects:** `curl -L`.
- **Cookies:** the `Cookie:` string harvested in Phase 1.
- **User-Agent:** a realistic desktop browser UA (match the browser used in Phase 1).
- **Referer:** the discovery page URL recorded for this document.

curl form:
```bash
curl -L --fail-with-body \
  -A "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36" \
  -e "<referer>" \
  -H "Cookie: <cookie-string>" \
  -H "Accept: application/pdf,*/*" \
  -D /tmp/headers.txt \
  -o "<target>.pdf" \
  "<final_url>"
```
Python `requests` form (equivalent; preferred if you need to branch on headers):
```python
import requests
h = {
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                "(KHTML, like Gecko) Chrome/124.0 Safari/537.36",
  "Referer": referer,
  "Cookie": cookie_string,
  "Accept": "application/pdf,*/*",
}
r = requests.get(final_url, headers=h, allow_redirects=True, timeout=60)
open(target_pdf, "wb").write(r.content)
content_type = r.headers.get("Content-Type", "")
```
Save into the right subdirectory using the naming convention (below).

**Logging (download start):** `DOWNLOAD start <target.pdf> <- <final_url>`.

### 2.2 VALIDATE every file (two independent checks)
A file counts as a real PDF only if BOTH pass:
1. **Content-Type is `application/pdf`** — from the response headers (`/tmp/headers.txt`
   last block for curl, or `r.headers["Content-Type"]` for requests). A `text/html`
   content-type means you were served a login/error page.
2. **Magic bytes** — the file begins with `%PDF`:
   ```bash
   head -c4 "<target>.pdf"   # must print: %PDF
   file "<target>.pdf"       # must say: PDF document
   ```
Also sanity-check size (>100KB for a report; SENS short-forms here ~0.9–1.5MB, booklets
~6–7MB). An 800-byte "PDF" is an error page.

**On failure (either check fails):**
- Log `VALIDATE FAIL <target.pdf> (content_type=<ct>, head=<bytes>) url=<final_url>`.
- The "PDF" is almost certainly HTML (error/login/gating). **Retry once** — re-fetch with
  the same headers (for a gated page, re-run Phase 1 resolution for just that URL to refresh
  cookies, since the session may have expired). If a presigned URL 403s, its signature
  likely expired — re-discover that one link and re-fetch immediately.
- If the retry also fails, stop on that file, record a `coverage_gap`, and move to the next.

**On success:** log `VALIDATE OK <target.pdf> (<kb>kb, application/pdf, %PDF)`.

### 2.3 Generate the `.txt` sidecar (same stem)
Only after the binary validates:
- Preferred: `pdftotext -layout "<file>.pdf" "<file>.txt"` (poppler) in sandbox bash; if
  poppler is missing, use the **pdf** skill.
- Image-only PDF: OCR for the sidecar and flag it as OCR-derived.
- PPTX/XLSX: extract text via the **pptx** / **xlsx** skills.

**Naming (original and sidecar share the stem):**
```
[slug]-[type]-[period]-[date].pdf   ← original (source of truth)
[slug]-[type]-[period]-[date].txt   ← text sidecar
e.g. clicks-group-annual-results-fy2025-20251023.pdf  +  .txt
```
**Subdirectories:** annual reports → `annual-reports/`; interims → `interim-reports/`;
trading statements → `trading-statements/`; SENS → `sens-announcements/`; presentations →
`investor-presentations/`; press → `press-releases/`.

---

## SENS search (feeds Phase 1)
Even with an IR archive, also web-search "[Company] SENS [year]", "trading statement",
"cautionary", "dividend declaration". Resolve anything new to its final `.pdf` URL in
Phase 1, then download it in Phase 2 like any other document.

## Update the manifest (via jse-manifest-manager)
Key the entry on the **original** filename. Record:
```json
"clicks-group-annual-results-fy2025-20251023.pdf": {
  "type": "annual_results", "period": "FY2025",
  "date_published": "2025-10-23", "date_downloaded": "<ISO>",
  "path": "companies/clicks-group/annual-reports/clicks-group-annual-results-fy2025-20251023.pdf",
  "text_path": "companies/clicks-group/annual-reports/clicks-group-annual-results-fy2025-20251023.txt",
  "text_source": "pdftotext -layout",
  "source_url": "https://...", "referer": "https://...",
  "content_type_verified": "application/pdf", "magic_bytes_verified": true,
  "pages": 16, "file_size_mb": 0.93,
  "original_saved": true
}
```
`original_saved` MUST be `true` for a completed download, and that requires BOTH validation
checks to have passed. If it is `false`, there must be a matching `coverage_gap`.

## Run-level self-check (do not skip)
For every results/report/presentation document for this company:
- Original exists at `path`; `file` reports `PDF document`; first bytes `%PDF`; size sane.
- The download's response Content-Type was `application/pdf` (recorded above).
- Sidecar `.txt` is non-empty and contains expected tokens (company name, "headline
  earnings", the period).

If any results doc has only a `.txt` and no `coverage_gap`, the run is INCOMPLETE — fix
before reporting done.

## Report
- X documents saved as ORIGINAL + sidecar (list with sizes).
- Y already up to date.
- Z could not be saved → list each with its direct URL, size, and recorded coverage_gap.

## If the binary truly can't be saved
Only after Phase 2 (with refreshed cookies on retry) has genuinely failed:
1. Save the `.txt` sidecar so the content is at least searchable.
2. Set `original_saved: false` and add a `coverage_gap`:
   `"FY2025 annual results ORIGINAL PDF outstanding — https://...(0.93MB). HTTP fetch returned
   <status/content-type>; text sidecar only; retry discovery+download."`
3. In `company.json`, record an accurate `download_note` (the real reason — e.g. "403 even
   with session cookies; site may require additional gating"), NOT a guessed one.
4. Surface it to the user with the exact URL(s) and size(s) so it's one click to backfill.
Never silently present a text-only capture as the archived document.

## Incremental updates
"Check for updates" / "refresh": read `last_checked` in company.json; in Phase 1 resolve
only documents published after it; download those originals (+ sidecars) in Phase 2; update
`last_checked`.

## Handling download failures
IR pages often use JS loaders / generated links. If a specific document won't download:
1. Confirm you're in the right phase: **resolution problems** (can't find the `.pdf`) are
   Phase 1 — re-navigate and re-render in the browser. **Fetch problems** (403/HTML/empty)
   are Phase 2 — refresh the cookies via a quick Phase-1 re-resolution and re-fetch.
2. Re-check the live filename on the results page (slugs change each period).
3. For presigned links, treat 403 as an expired signature: re-discover and re-fetch at once.
4. Search alternative sources (company name + document title), resolve in Phase 1, fetch in
   Phase 2.
5. If the site structure changed, trigger `jse-company-discovery` to re-map and
   `jse-skill-builder` to update the company skill.
6. Record the coverage_gap (above). Asking the user to fetch manually is the absolute last
   resort, only after both phases are exhausted.
