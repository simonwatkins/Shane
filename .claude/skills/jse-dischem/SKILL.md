---
name: jse-dischem
description: >
  Research skill for Dis-Chem Pharmacies Limited (JSE: DCP), South Africa's #2 retail
  pharmacy and health & beauty retailer (after Clicks) plus a large pharmaceutical
  wholesale/distribution business. Use this skill whenever the user mentions Dis-Chem,
  Dischem, DCP, Baby City, The Local Choice (TLC), Dis-Chem Life, "X, bigly labs",
  Better Rewards, CEO Rui Morais, or asks about Dis-Chem's results, HEPS, dividends,
  pharmacy market share, wholesale, or its ecosystem/healthcare strategy. Also trigger
  for Clicks-vs-Dis-Chem competitive comparisons. Knows where to find Dis-Chem's financial
  documents, the reporting schedule, the document hosting/URL pattern, and the analytical
  framework. NOTE: Dis-Chem's year-end is END FEBRUARY (Clicks/CLS is end-August).
---

# Dis-Chem (DCP) Research

## Quick Reference
- **JSE code:** DCP  |  **ISIN:** ZAE000227831  |  **Reg:** 2005/009766/06
- **Sector:** Retail pharmacy / health & beauty + pharmaceutical wholesale & distribution
- **Year-end:** **End February** (FY2026 = 12 months to 28 Feb 2026). NOT a 52/53-week calendar.
- **Reporting currency:** ZAR (small Namibia + Botswana subsidiaries)
- **IR / results:** https://dischemgroup.com/investors/financial-results/
  (also https://dischemgroup.com/investors/results-and-presentations/)
- **IR email:** investorrelations@dischem.co.za
- **Key people:** Chairman J.S. Mthimunye; CEO **Rui Morais** (since Jul 2023, ex-CFO);
  CFO **Julia Pope** (CA(SA)); founders the Saltzmans (IL Saltzman retiring 30 Jun 2026).
  Auditors **Forvis Mazars**.
- **Closest peer:** **Clicks Group (JSE: CLS)** — see [[jse-clicks-group]]. Clicks is the
  market leader; Dis-Chem is the challenger telling the more "modern/ecosystem" growth story.

## Group Structure (two reporting segments + emerging ecosystem)
1. **Retail** — Dis-Chem pharmacy stores (dispensary + front-shop health, beauty, personal care),
   **Baby City** (baby), and **The Local Choice (TLC)** franchise pharmacies. ~316 retail pharmacy
   + 42 baby stores at FY2026; TLC franchises 240 -> 280.
2. **Wholesale** — Dis-Chem Distribution / CJ Distribution: supplies own stores **and** external
   independent pharmacies + TLC franchisees. Larger revenue line than retail in gross terms
   (FY2026 wholesale R34.0bn vs retail R36.6bn; large intra-group elimination).
3. **Ecosystem (emerging, loss-making upfront)** — **"X, bigly labs"** (data/analytics/AI,
   commercial decision intelligence, app/e-commerce) and **Dis-Chem Life** (financial services,
   launched Nov 2025). FY2026 ecosystem spend R445m (R330m to X, bigly labs).

## Where to Find Documents
- **Landing:** https://dischemgroup.com/investors/financial-results/ — tabbed by year (2026,
  2025, ...) and split into **ANNUAL** (AFS, Analyst Presentation, Webcast) and **INTERIM** sections.
- **Hosting:** documents live on **thevault.exchange** (Dis-Chem group_id = **6262**). The anchor
  on the IR page is a base64-encoded `/wp-json/the-vault/...` redirect.
  Direct pattern: `https://thevault.exchange/?get_group_doc=6262/<docid>-<DocName>.pdf`
  - FY2026 AFS: `.../6262/1780031707-FY2026AnnualFinancialStatements.pdf`
  - FY2026 Analyst Presentation: `.../6262/1780031786-FY2026AnalystPresentation.pdf`
- **Mirrors / SENS:** sharedata.co.za (DCP glossies + SENS), Moneyweb SENS, Sharenet, Listcorp,
  MarketScreener. Use these to confirm SENS short-form results and dividend declarations.

### Downloading the PDFs (binary channel = browser; see [[jse-report-downloader]])
`web_fetch` returns text only and bash `curl` is proxy-blocked, so use **Claude in Chrome**:
1. Navigate to https://dischemgroup.com/investors/financial-results/ ; open the year tab.
2. Click the document anchor — the tab navigates to the thevault.exchange PDF (Chrome PDF viewer).
3. Save it: either fetch same-origin (`fetch(location.href)->blob->a.download`) OR click the PDF
   **viewer's download button** (top-right). **Important:** thevault.exchange allows only ONE
   scripted auto-download per site before Chrome's "download multiple files" gate blocks the rest;
   the **viewer download button bypasses that gate**, so prefer it for the 2nd+ file (or have the
   user click Allow once).
4. Files land in the Chrome download dir (point it at the project folder); move/rename to the
   convention and run `pdftotext -layout` for the sidecar.

## Sector-Specific Metrics (Pharmacy + Health & Beauty + Wholesale)
Lead with: **group / retail / wholesale revenue growth**, **like-for-like (comparable) store
revenue growth** (esp. comparable pharmacy), **retail vs wholesale split**, **total income margin**
(group ~30.8%; retail ~31%), **EPS / HEPS** and — crucially for Dis-Chem — **HEPS excluding
non-recurring items / property gains / ecosystem investment** (management leads on the adjusted
view). Then dividend (historically ~highish payout; CUT in FY2026), market share (volume) gains,
store counts (retail pharmacy, Baby City, TLC franchises), Better Rewards loyalty metrics, and
ecosystem spend (X, bigly labs + Dis-Chem Life) with expected payback year. Wholesale: split own-
store vs external (independents + TLC).

## Known Quirks (critical for not misreading the numbers)
- **Reported vs adjusted earnings diverge hugely.** FY2026 reported HEPS -17.4%, BUT that includes
  (a) heavy upfront ecosystem investment (R445m) and (b) the ABSENCE of a prior-year once-off
  PROPERTY GAIN. Excluding those, core retail PBT was +27.1% and group PBT (ex ecosystem +
  non-recurring) +20.1%. ALWAYS report reported AND management-adjusted, and name the two bridges
  (property gain base effect + ecosystem spend). This is the single biggest analytical trap.
- **Wholesale is huge but thin-margin** and partly internal — use the segment note and watch the
  intra-group elimination; don't double-count own-store wholesale.
- **Year-end is END FEBRUARY** — results ~late May (FY) and ~late October (H1 interim, six months
  to ~end August). Do NOT align periods with Clicks (Aug year-end); for like-for-like competitive
  reads, map Dis-Chem H1 (to Aug) against Clicks FY commentary windows carefully.
- **Founder transition risk** — Saltzman founders stepping back (IL Saltzman retiring Jun 2026);
  professional management under Morais. A recurring investor theme (see Financial Mail coverage).
- **Document hosting via thevault.exchange** with obfuscated redirect links + Chrome multi-download
  gate — see the download recipe above.
- **Dividend was CUT in FY2026** (total -17.3% to 45.34c; final -42.8% to 15.92c) to fund the
  ecosystem build — a key sentiment driver (shares fell ~8% on results day).

## Reporting Calendar
- **FY (annual) results:** ~late May (12 months to end Feb). FY2026: released 29 May 2026.
- **H1 (interim) results:** ~late October (six months to ~end Aug). H1 FY2026: ~late Oct 2025.
- **Interim dividend paid:** ~Nov/Dec; **final dividend:** ~Jul/Aug.
- **Next results due:** H1 FY2027 interim ~late October 2026 (six months to ~end Aug 2026).

## Latest Catalogued Figures (onboarding, 7 Jun 2026)
**FY2026 (12 months to 28 Feb 2026, audited; released 29 May 2026):** Group revenue +9.3% to
R42.8bn (retail +9.0% to R36.6bn, comp pharmacy +5.3%; wholesale +13.1% to R34.0bn). EPS 114.2c
(-17.1%), HEPS 113.7c (-17.4%); ex prior-year property gain EPS/HEPS -11.5%/-11.8%; core retail
PBT (ex ecosystem + non-recurring, ex property gain) +27.1%; group PBT (ex ecosystem + non-recurring)
+20.1%. Total income (ex property gain) +9.6% to R13.2bn; group margin 30.8%; retail margin 31.1%.
Ecosystem spend R445m (X, bigly labs R330m + Dis-Chem Life). Total dividend 45.34c (-17.3%); final
15.92c (-42.8%). Post-period (1 Mar-19 May 2026): revenue +9.0%, total income margin up to 32.0%.
(Source: FY2026 AFS + analyst presentation; corroborated by Business Explainer, 3 Jun 2026.)

## Analytical Notes Worth Pre-loading
- The bull case: strong underlying core-retail growth + operating leverage (LFL sales +5.3% vs LFL
  payroll +3.5%), market-share gains across all core categories (+1.1 ppt volume), Better Rewards
  traction, and an ecosystem (X, bigly labs + Dis-Chem Life) that management says turns net-positive
  from FY2027 — i.e. FY2026 is a deliberate investment trough.
- The bear case: reported earnings and dividend fell; valuation must be carried by faith in the
  ecosystem payback; founder transition; wholesale margin pressure; execution risk on Health Hub
  rollout and Dis-Chem Life (a retailer entering financial services).
- For the Clicks-vs-Dis-Chem debate (Financial Mail, "The Clicks conundrum", 30 Apr 2026): Dis-Chem
  is narrating the higher-growth, data-led, market-share-hungry story; Clicks is the higher-quality,
  higher-margin, defensive compounder. Watch relative LFL growth and margin trajectory.

## Local Files (this workspace)
- `companies/dischem/company.json`
- `companies/dischem/annual-reports/dischem-annual-financial-statements-fy2026-20260529.pdf` (+ .txt)
- `companies/dischem/investor-presentations/dischem-analyst-presentation-fy2026-20260529.pdf` (+ .txt)
- `companies/dischem/press-releases/dischem-fy2026-results-coverage-businessexplainer-20260603.txt`

## Coverage Gaps / To Backfill
- FY2026 SENS short-form results announcement (the audited AFS is captured; the SENS short-form with
  the summarised financial-summary table is a separate, lighter doc — grab from sharedata/Moneyweb).
- H1 FY2026 interim results + interim presentation (year tab "2026" INTERIM section on the IR page).
- Integrated Annual Report (IAR) and remuneration report once published.
- Prior-year comparatives (FY2025 AFS/presentation) for multi-year trend building.

## Last Updated
2026-06-07 — created on onboarding. FY2026 AFS (audited) + FY2026 analyst presentation downloaded as
originals (+ pdftotext sidecars); Business Explainer FY2026 coverage saved. Document hosting
(thevault.exchange group 6262) + download recipe verified. CEO Morais / CFO Pope / chair Mthimunye /
auditor Forvis Mazars confirmed from the FY2026 AFS.
