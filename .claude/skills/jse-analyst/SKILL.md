---
name: jse-analyst
description: >
  Analyses downloaded financial documents for JSE-listed companies. Use this skill
  whenever the user asks to analyse, review, summarise, compare, or evaluate a
  company's financial results. Also trigger when the user asks "how did [company]
  do", "what are [company]'s numbers", "analyse [company]'s results", "compare
  [company] to last year", "flag risks for [company]", "prepare IC notes for
  [company]", "pull [company]'s numbers", or any question about a company's financial
  performance, metrics, valuation, or outlook. Trigger for HEPS extraction, SA-specific
  metrics, and reporting-period comparisons. This skill works on documents already
  downloaded to the local workspace — it reads from companies/[slug]/ and never searches
  the web during analysis. If documents are missing, it triggers jse-report-downloader
  first. Output is held to a strict, verifiable Citation Standard: a Source tag on every
  table row, inline page-level footnotes, a per-figure Provenance & Verification appendix,
  and a Sources list of full deep-link URLs.
---

# JSE Analyst

## Purpose

Produces structured financial analysis from locally downloaded documents. This is the
analytical engine — it reads PDFs/PPTX/XLSX, extracts metrics, compares periods, adds
valuation context, flags risks, and presents findings in the fund's standardised format.

## Prerequisites

- Documents must be downloaded locally (in `companies/[slug]/`)
- If the required documents aren't available, trigger `jse-report-downloader` first
- Check `manifest.json` to see what's available before starting

## Workflow

### Step 1: Inventory Available Documents

Read the manifest for this company. Identify: annual/interim reports we have, any
corresponding investor presentation, recent SENS, and internal analyst notes in
`analyst-notes/`.

### Step 2: Read the Documents

Each document is stored as an **original** (PDF/PPTX/XLSX) plus a **`.txt` sidecar**
(see `text_path` in the manifest). Use them deliberately:
- Use the **text sidecar** for fast keyword search and to locate where a figure lives.
- **Read the ORIGINAL file for anything that depends on tables, financial statements,
  charts or diagrams.** Text extraction can drop or scramble table structure, so always
  confirm reported numbers against the original (use the pdf / pptx / xlsx skills). If the
  manifest shows `text_source: ocr`, treat the sidecar as low-confidence and rely on the
  original.

Read in priority order (use the pdf / pptx / xlsx skills as appropriate):
1. Annual report / interim report (primary source of truth)
2. Investor presentation (management commentary and normalised figures)
3. Trading statement (guidance verification)
4. SENS announcements (supplementary context)
5. Analyst notes (internal fund perspective)

### Step 3: Extract Standardised Metrics

Apply the sector-appropriate framework. Load the company's skill (if generated) and the
sector reference at `references/sector-metrics.md` to get the right metrics list.

#### General Framework (all companies)

| Metric                          | Current Period | Prior Period | Change | % Change |
|---------------------------------|----------------|--------------|--------|----------|
| Revenue / Turnover (R'm)        |                |              |        |          |
| Gross Profit (R'm)              |                |              |        |          |
| Gross Margin (%)                |                |              |        |     bps  |
| EBITDA (R'm)                    |                |              |        |          |
| EBITDA Margin (%)               |                |              |        |     bps  |
| Operating Profit / EBIT (R'm)   |                |              |        |          |
| Operating Margin (%)            |                |              |        |     bps  |
| HEPS (cents)                    |                |              |        |          |
| EPS (cents)                     |                |              |        |          |
| DPS (cents)                     |                |              |        |          |
| Payout Ratio (%)                |                |              |        |          |
| NAV per Share (cents)           |                |              |        |          |
| Net Debt / (Cash) (R'm)         |                |              |        |          |
| Net Debt / EBITDA (x)           |                |              |        |          |
| ROE (%)                         |                |              |        |     bps  |
| ROIC (%)                        |                |              |        |     bps  |
| FCF (R'm)                       |                |              |        |          |
| Cash Conversion (%)             |                |              |        |          |

- Margins and returns show **basis point (bps)** change, not % change.
- Mark estimated/calculated figures with `(e)` and show the calculation.

#### Sector-Specific Additions

Load `references/sector-metrics.md` and add the primary + secondary metrics for the
company's sector (Banking, Retail (Food / General), Mining, Telco, Property/REIT,
Insurance, Industrials).

### Step 4: Valuation Context (when enough data is available)

Note that these require a current share price — search for it when relevant, and flag
that prices found via search may be delayed (there is no live JSE feed here).
- Trailing P/E (using HEPS)
- EV / EBITDA
- Dividend yield
- Price-to-book (using NAV per share)
Frame all valuation output as informational, not advice.

### Step 5: Cross-Source Reconciliation

If multiple sources are available, compare the same metric across them:
- Annual report vs investor presentation (presentations often use normalised figures)
- Reported vs trading-statement guidance (is HEPS within the guided range?)
- Company figures vs analyst model estimates (if available)

Flag discrepancies with magnitude and likely cause (rounding <0.5% acceptable;
normalised vs reported; treatment of associates/JVs/discontinued ops). Official priority:
annual report > presentation > analyst model.

### Step 6: Risk Scan

Check all documents for:
- [ ] Going-concern language (audit report and notes)
- [ ] Qualified or modified audit opinion
- [ ] Material related-party transactions
- [ ] Subsequent events post balance-sheet date
- [ ] Restatement of prior-period figures
- [ ] Changes in accounting policy or estimates
- [ ] Significant impairments or write-downs
- [ ] Covenant breaches or waivers
- [ ] Working-capital deterioration (debtors days, inventory days trends)
- [ ] Increase in share-based compensation as % of earnings
- [ ] Auditor change
- [ ] Director resignations around reporting date

### Step 7: Management Commentary Summary

Extract and summarise: outlook statement (verbatim key phrases, attributed), capital
allocation priorities (dividends, buybacks, capex, M&A), strategic initiatives and
progress, risks identified by management, guidance for next period.

### Step 8: Produce the Analysis

Structure the output as:
0. **Verifiable citations throughout** — every figure, target, quote and risk fact carries
   a source per the Citation Standard below. Sourcing is enforced via FOUR mechanisms, ALL
   mandatory on every deliverable (see "Citation Standard" and "Definition of Done"):
   (a) a **Source column / ref-tag on every data-table row**; (b) **inline footnotes with
   page numbers** at the point of each claim (where the output format supports footnotes);
   (c) a **per-figure Provenance & Verification appendix table**; and (d) a **Sources list
   of full, clickable deep-link URLs** (never truncated).
1. **Executive Summary** — 2-3 paragraphs: what happened, what matters, what to watch
2. **Standardised Metrics Table** — full table from Step 3, **with a Source column**
3. **Sector-Specific Metrics** — additional metrics for this sector, **with a Source column**
4. **Valuation Context** — multiples from Step 4 (note price source/date)
5. **Trading Statement Verification** — was reported HEPS within the guided range?
6. **Cross-Source Reconciliation** — discrepancies found
7. **Risk Flags** — anything triggered, with severity rating
8. **Management Commentary** — summarised outlook and strategy
9. **Questions for Further Research / Management** — 3-5 items to investigate
10. **SENS Summary** — material announcements in the analysis period
11. **Provenance & Verification Appendix** — the per-figure table defined in the Citation
    Standard, so the PM can audit any number in one click
12. **Sources** — numbered list with full deep-link URLs + local paths

### Step 9: Update the Manifest

Mark documents as analysed (via jse-manifest-manager):
```json
{
  "analysed": true,
  "analysis_date": "2026-06-05T11:00:00Z",
  "analysis_summary": "FY2025 results in line with guidance. HEPS +11.5%. No risk flags."
}
```

### Step 10: Save the Analysis

Save to `companies/[slug]/analysis-[period]-[date].md` so it can be referenced later
without re-analysing. For a presentation deliverable, use the pptx skill; for a data
table to be manipulated further, use the xlsx skill.

## South African Context (apply throughout)

- **Currency:** ZAR by default; state the reporting currency and give a ZAR equivalent
  where a company reports in USD/EUR (e.g. Naspers/Prosus, some miners).
- **Dual listings:** state which listing's results are referenced (JSE vs LSE/ASX).
- **Standards:** IFRS plus King IV governance and JSE Listings Requirements.
- **Tax:** SA corporate rate 27% (from 28%, for years of assessment ending on/after
  31 March 2023); note material deferred-tax impacts.
- **BEE:** note ownership structures and their effect on effective shareholding.
- **Sector nuances** are detailed in `references/sector-metrics.md`.

## Citation Standard

Sourcing is not optional decoration — it is how the PM trusts and acts on the analysis.
Cite inline, at the point of the claim, naming the document and (where determinable) the
page. Exercise judgement: you cannot footnote every word, but the items below must always
carry a citation.

### Always cite
- **Specific figures, metrics, ratios and growth rates** presented as fact (revenue,
  margins, HEPS, ROIC, net debt, like-for-like, etc.).
- **Targets, guidance and any forward-looking management statement** (e.g. a medium-term
  margin target, capex guidance, store-rollout plans).
- **Direct quotes and paraphrased management commentary** (outlook, capital allocation).
- **Risk-relevant facts**: impairments, going-concern wording, covenant breaches/waivers,
  restatements, audit-opinion modifications, related-party transactions, subsequent events.
- **Anything non-obvious, surprising, or that a PM might challenge or trade on.**
- **Every calculated/derived figure** — mark `(e)`, show the working, and cite the source
  inputs.

### Need not cite
- General or well-known context, standard definitions, common-knowledge macro.
- Your own synthesis, reasoning and judgement — but label it as such (e.g. "On balance,
  this suggests…") so it is never mistaken for a sourced fact.

### Provenance discipline (the rule that matters most)
Cite the document the fact **actually came from** — never a more authoritative-sounding
one. A figure from an investor presentation, SENS announcement, trading statement,
earnings call, or your own calculation must **not** be attributed to the annual report.
If a target or guidance appears only in the interim results or an earnings call, cite that
source, not the annual report. When the same metric differs across sources, cite each and
flag the discrepancy (see Cross-Source Reconciliation).

### The four mandatory mechanisms (how the PM verifies)

A bulk "Sources" list at the end is NOT sufficient on its own — it forces the reader to
hunt. Every deliverable must let the PM trace any single number to its origin in one step,
using ALL FOUR of the following:

**1. Source ref-keys + a Sources list of full deep-link URLs.**
   Assign each source a short key (S1, S2, …). The Sources list gives, per key, the document
   title, period, **full clickable URL to the exact PDF/SENS** (the `source_url` in the
   manifest — never a truncated "site.co.za/…" stub) and the local path. Example:
   - `S1 — WHL H1 FY2026 interim short-form announcement (SENS), 3 Mar 2026.`
     `https://www.woolworthsholdings.co.za/wp-content/uploads/2026/03/whlfy26.pdf`
     `(local: companies/woolworths/interim-reports/woolworths-interim-fy2026-sfa.txt)`

**2. A Source tag on every data-table row.** Add a final `Source` column to every metrics /
   divisional / scenario table, carrying the ref-key and page, e.g. `S1, p.3`. No data row
   ships without one. Derived rows cite their inputs, e.g. `(e) S1 p.3 + S3 p.47`.

**3. Inline footnotes with page numbers** at the point of each claim, when the output format
   supports footnotes (Word/PDF do — use the docx skill's footnote feature). The footnote
   names document + page, e.g. "HEPS rose 9.6% to 167.4cps.¹" → "¹ S1, p.3 (financial
   overview)." In prose-only/markdown output, use a parenthetical inline cite instead:
   "(S1, p.3)".

**4. A Provenance & Verification appendix table** — the master audit trail. One row per key
   figure presented, with these columns:

   | # | Figure (as presented) | Value | Reported / Derived | Source key | Doc & page/section | URL | Retrieved |
   |---|-----------------------|-------|--------------------|-----------|--------------------|-----|-----------|
   | 1 | H1 FY2026 HEPS | 167.4cps | Reported | S1 | Interim SFA, financial overview (p.3) | <full URL> | 2026-06-05 |
   | 2 | H1 FY2025 HEPS (comparative) | 152.7cps | Derived: 167.4 ÷ 1.096 | S1 | from +9.6% growth disclosed (p.3) | <full URL> | 2026-06-05 |

   Every `(e)` figure MUST show its arithmetic in the "Reported / Derived" column.

### Locating and pinning the page
1. Find the claim using the `.txt` sidecar (fast keyword search), then **verify the figure
   and its page in the original PDF** before citing — sidecars may not carry reliable pages.
2. Inline format examples:
   - "trading margin of 5.9% (S1, p.3)"
   - "medium-term trading-margin target of 6% (S2, slide 12 / results call 3 Mar 2026)"
   - "EBITDA R14,550m (e) = operating profit R12,450m + D&A R2,100m (S3, p.47)"
3. If a page genuinely cannot be pinned down, cite document + named section (e.g. "Outlook
   statement") rather than dropping the cite — and say so in the provenance table.
4. For figures obtained via web search (e.g. live share price, consensus target), cite the
   site and access date, and flag staleness; never present a searched figure as if it came
   from a company filing.

### Definition of Done — Citation Checklist (run before delivering)
Do not hand over the analysis until every box is ticked:
- [ ] Every data-table row has a `Source` column entry (ref-key + page).
- [ ] Every figure/target/quote/risk-fact in prose carries an inline footnote or cite.
- [ ] Every `(e)` figure shows its arithmetic and cites its input source(s).
- [ ] The Provenance & Verification appendix lists every key figure presented.
- [ ] The Sources list uses FULL clickable URLs (deep links to the exact file), not stubs.
- [ ] Each cite names the document the fact ACTUALLY came from (presentation ≠ annual report).
- [ ] Searched/market figures are labelled with source + access date + staleness note.
- [ ] No number anywhere in the document lacks a traceable origin.

### Output-format notes (docx / xlsx / pptx)
- **docx:** use real Word **footnotes** for mechanism 3 (the docx skill's `FootnoteReferenceRun`
  / `footnotes` map). Add the `Source` column to every table; put the Provenance appendix as a
  landscape table near the end; make Sources URLs live hyperlinks. If the available docx
  toolchain cannot emit footnotes, substitute superscript ref-keys in-text (e.g. "…167.4cps^S1p3")
  and keep mechanisms 1, 2 and 4 in full — verifiability must never depend on footnote support.
- **xlsx:** add a `Source` and `Source URL` column on every data sheet, plus a dedicated
  `Sources` tab keyed S1, S2, …; derived cells carry a comment showing the formula/inputs.
- **pptx:** footnote each data slide with the ref-key + page; include a final Sources slide
  with full URLs; keep the Provenance table as an appendix slide or linked spreadsheet.

## Analysis Principles

1. **Never hallucinate a number.** If a metric isn't in the documents, say "Not
   disclosed" or "Not found in available documents."
2. **Always show working for calculated figures.** e.g. "EBITDA = Operating profit
   R12,450m + D&A R2,100m = R14,550m (e)".
3. **Prior period from the same document when possible** — the annual report's
   comparatives are more reliable than last year's report separately (restatement risk).
4. **Attribute everything.** "Per the FY2025 annual report, page 23" / "per the investor
   presentation, slide 14."

## Compliance

- Frame analysis as "for informational purposes", not investment advice.
- Note when data (especially share prices) may be stale.
- Flag if the company is in a closed/prohibited dealing period for the fund.
- If extracted PDF tables look garbled, flag it and suggest verification.
