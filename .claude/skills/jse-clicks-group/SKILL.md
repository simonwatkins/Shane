---
name: jse-clicks-group
description: >
  Research skill for Clicks Group Limited (JSE/A2X: CLS), South Africa's market-leading
  health, wellness & beauty retailer and #1 retail pharmacy chain, plus UPD, the country's
  leading pharmaceutical wholesaler/distributor. Use this skill whenever the user mentions
  Clicks, Clicks Group, CLS, UPD (United Pharmaceutical Distributors), The Body Shop SA,
  Sorbet, UniCare, ClubCard, or asks about Clicks' results, HEPS, dividends, pharmacy market
  share, private label, store/pharmacy rollout or remuneration. Also trigger for comparisons
  with Dis-Chem (JSE: DCP). This skill knows where to find all Clicks financial documents,
  the reporting schedule, the URL patterns, and the right analytical framework.
  NOTE: this is the South African retailer Clicks Group (JSE: CLS) — NOT the UK "Click"/
  unrelated brands, and NOT to be confused with Dis-Chem (its closest competitor).
---

# Clicks Group (CLS) Research

## Quick Reference
- **JSE & A2X code:** CLS  |  **ISIN:** ZAE000134854  |  **ADR:** CLCGY (CUSIP 18682W205)
- **Registration:** 1996/000645/06  |  **Income tax no.:** 9061/745/71/8
- **Sector:** Retail — Health, Wellness & Beauty + Pharmaceutical Wholesale/Distribution (defensive)
- **Year-end:** **31 August** (NOT a 52/53-week retail calendar — fixed calendar year-end)
- **Reporting currency:** ZAR (almost entirely SA; small foreign-subsidiary translation only)
- **IR / results:** https://www.clicksgroup.co.za/results/
- **Media centre:** https://www.clicksgroup.co.za/media-centre/press-releases/
- **Integrated report:** https://www.clicksgroup.co.za/iar2025/ (pattern: /iar<YYYY>/)
- **Registered:** Cnr Searle and Pontac Streets, Cape Town, 8001
- **Key people:** Chairman Mfundiso Njeke (MJN Njeke, from 30 Jan 2025); CEO Bertina Engelbrecht
  (since Jan 2022); CFO **Gordon Traill** (GD Traill, CA). Auditors KPMG Inc.; JSE sponsor Investec;
  IR consultants Tier 1 IR (ir@tier1ir.co.za).
  WARNING: Older web sources name Michael Fleming as CFO — that is OUT OF DATE. Current CFO is Gordon Traill.

## Group Structure (two reporting segments)
1. **Retail** — Clicks (health/wellness/beauty front-shop + in-store pharmacy), The Body Shop SA,
   UniCare (incl. 24-hour specialised pharmacies), Sorbet (corporate + franchise salons),
   180 Degrees (marketing/media services).
2. **Distribution (UPD)** — United Pharmaceutical Distributors: full-range pharmaceutical wholesaler
   (fine wholesale to Clicks, private hospitals, independent pharmacies) + bulk/preferred-supplier
   distribution. Low-margin, high-volume; trading margin ~2.5-3.3%.

## Where to Find Documents

### Annual results (year to 31 August; published ~late October)
- **Landing:** https://www.clicksgroup.co.za/results/
- **Announcement (SENS short-form):** `.../wp-content/uploads/<YYYY>/10/CGL-<YYYY>-Annual-results-announcement.pdf`
- **Analyst booklet:** `.../<YYYY>/10/CGL-<YYYY>-Annual-results-analyst-booklet-1.pdf`
- **Analyst presentation:** `.../<YYYY>/10/CGL-<YYYY>-Annual-results-analyst-presentation.pdf`
- FY2025 example: `https://www.clicksgroup.co.za/wp-content/uploads/2025/10/CGL-2025-Annual-results-announcement.pdf`

### Interim results (six months to ~28 Feb; published ~late April)
- **Announcement:** `.../<YYYY>/04/CGL-<YYYY>-Interim-results-announcement-1.pdf`
- **Analyst booklet:** `.../<YYYY>/04/CGL-<YYYY>-Interim-results-analyst-booklet.pdf`
- **Analyst presentation:** `.../<YYYY>/04/CGL-<YYYY>-Interim-results-analyst-presentation.pdf`
- H1 FY2026 example: `https://www.clicksgroup.co.za/wp-content/uploads/2026/04/CGL-2026-Interim-results-announcement-1.pdf`

### Filename inconsistency — ALWAYS scrape /results/ first
The slug changes year to year. Examples seen on the server:
- FY2024 interims: `CGL-2024-Interims-Results-announcement.pdf` (note "Interims", capital R varies)
- FY2025 interims: `CGL-2025-Interims-Results-Announcement.pdf`
- FY2026 interims: `CGL-2026-Interim-results-announcement-1.pdf` (note "Interim", trailing "-1")
- Older (pre-2023) PDFs live under `/wp-content/uploads/2022/09/` with legacy names
  (e.g. `Clicks-Group-Annual-Results-2022-Analyst-Presentation-FINAL.pdf`).
Do not hard-code the filename — fetch https://www.clicksgroup.co.za/results/ and extract the live
links, OR confirm the exact slug before fetching. The folder is reliably `<YYYY>/10/` (annual) and
`<YYYY>/04/` (interim).

### SENS / trading statements
- Clicks does NOT routinely issue trading statements (earnings have stayed within the 20% HEPS
  threshold that triggers a mandatory SENS trading statement). Watch SENS for dividend declarations,
  director dealings, and any guidance. Mirrors: Moneyweb SENS, Listcorp, SharaData/Sharenet.
- Moneyweb SENS example (H1 FY2026): search "Clicks Group Limited Unaudited Interim Group Results"
  on moneyweb.co.za/mny_sens/.

### Press coverage (prioritise per fund house preference)
- **Business Day** (businessday.co.za) and **Financial Mail** (financialmail.businessday.co.za) —
  both premium/paywalled but fetchable via web fetch. Business Day's consumer writer is Nompilo Zulu;
  Financial Mail runs "The Finance Ghost" investing column which covers Clicks regularly.
- Also useful: Moneyweb, Daily Investor, IOL Business Report, Bizcommunity, Trade Intelligence.

## Sector-Specific Metrics (Health & Beauty Retail + Pharma Distribution)
Lead with: **group / retail / distribution turnover growth**, **comparable-store (like-for-like)
growth**, **selling price inflation vs CPI**, **retail pharmacy market share** (24.9% at H1 FY2026),
**total income margin** and **trading margin (bps)** — Clicks' preferred profit metric is **trading
profit / trading margin** (group ~9-10%; retail ~10.5%; UPD ~2.5-3.3%). Then **HEPS / diluted HEPS**
(management guides on DILUTED HEPS), dividend (65% payout target; interims paid ~July, finals ~Jan),
**ROE / ROIC** (industry-leading; ROE ~45-49%), **private label contribution** (target 35% of front-
shop sales), **ClubCard** active membership + % of sales + cashback, store/pharmacy count vs the
**1,200 medium-term store target**, weighted trading area, inventory days. Report retail by category:
Pharmacy, Front-shop health, Beauty & personal care, General merchandise. Report UPD by: fine
wholesale (Clicks / private hospitals / independents) vs bulk/preferred-supplier wholesale.

## Known Quirks
- **Buybacks flatter HEPS.** Headline EARNINGS and HEPS growth diverge because of an active buyback
  programme (~R750m/yr). E.g. H1 FY2026: headline earnings +6.4% but HEPS +8.1%. Always cite BOTH
  and note buybacks as the bridge. The Finance Ghost specifically flagged this.
- **Trading margin is the headline profit metric**, not EBIT/EBITDA. Group trading margin is reported
  to one decimal; movements quoted in bps.
- **UPD distorts group margins.** UPD is large-turnover/thin-margin, so group total income margin and
  trading margin are dragged down by distribution mix. Analyse Retail and Distribution segments
  separately; the segmental note gives per-segment trading profit and margins.
- **Single Exit Price (SEP)** of medicines: the annual SEP adjustment (regulated) materially affects
  UPD/pharmacy revenue and distribution margin. A low SEP increase compresses distribution margin.
- **WMS / systems risk (current).** A delayed Warehouse Management System rollout at the Cape Town DC
  cut ~R175m (0.9%) of retail turnover over the FY2026 festive season. IT/supply-chain execution is a
  live risk item to track. ("System failure and price wars hit Clicks festive trading" — BD, Jan 2026.)
- **No 52/53-week calendar** (unlike Shoprite/Woolworths/Mr Price). FY2024 vs FY2025 comparatives are
  clean, but FY2024 contained an extra trading day vs FY2023 — management quoted comparable-store
  growth "excluding the additional trading day."
- **Unicorn Pharmaceuticals** was disposed in FY2024 — strip it out for clean FY2025 pharmacy/retail
  growth (reported +3.2% pharmacy incl. Unicorn vs +6.9% excl.).
- **Direct PDF binaries** may be blocked by the sandbox proxy; fetch as extracted text via web fetch
  (the announcement PDFs return clean text), consistent with this workspace's text_source convention.
- **Disambiguation:** closest listed peer is **Dis-Chem (JSE: DCP)**, year-end Feb. Don't conflate the
  two; the Clicks-vs-Dis-Chem competitive dynamic is a recurring analyst theme.

## Reporting Calendar
- **Interim (H1) results:** ~late April (six months to ~28/29 Feb). H1 FY2026: 23 April 2026.
- **FY results:** ~late October (year to 31 Aug). FY2025: 23 October 2025; FY2026 expected ~late Oct 2026.
- **Interim dividend paid:** ~early July (H1 FY2026: 6 July 2026).
- **Final dividend paid:** ~late January (FY2025 final: 26 January 2026).
- **AGM:** typically January/February.
- **Next results due:** FY2026 annual results ~late October 2026 (year to 31 August 2026).

## Latest Catalogued Figures (as of onboarding, 7 Jun 2026)
**H1 FY2026 (6 months to 28 Feb 2026)** — turnover R24.9bn (+7.4%); retail +5.4% (comp +3.1%);
distribution +13.0%; trading margin 9.1% (maintained); HEPS 652.8c (+8.1%, headline earnings +6.4%);
interim dividend 258c (+8.4%); ROE 45.7%; 1,003 stores / 795 pharmacies; ClubCard 12.9m; retail
pharmacy share 24.9%. **FY2026 guidance: diluted HEPS +4% to +9%.** (Source: H1 FY2026 SENS, 23 Apr 2026.)

**FY2025 (year to 31 Aug 2025)** — turnover R47.8bn (+5.3%); retail +6.0%; trading margin 9.8%
(+60bps); diluted HEPS 1,361.7c (+14.1%); total dividend 886c (+14.2%, 65% payout); ROE 49.2%;
1,060 stores / 780 pharmacies; private label R9.7bn (+10.7%). (Source: FY2025 SENS, 23 Oct 2025,
KPMG-reviewed.)

## Analytical Notes Worth Pre-loading
- The bull case: defensive, cash-generative (R6.6bn FY2025 operating cash), industry-leading ROE,
  iconic ClubCard loyalty/data moat, structural pharmacy/private-label growth, disciplined capital
  return (65% payout + buybacks), clear runway to 1,200 stores.
- The bear case (per Financial Mail, Apr 2026): premium valuation (high-20s P/E) against decelerating
  growth; FY2026 guidance of 4-9% is "particularly weak"; HEPS growth partly engineered via buybacks;
  rotation out of defensive quality; Dis-Chem narrating a "more modern", market-share-hungry story.
- Watch items: WMS/IT execution at the Cape Town DC; competitive discounting; SEP medicine pricing;
  fuel/utility cost trajectory (partly hedged via solar + EV fleet); UPD hospital/independent channel
  weakness; Dis-Chem FY (to Feb 2026) results (due 29 May 2026) for relative performance read-across.

## Local Files (this workspace)
- `companies/clicks-group/company.json` — metadata, URL patterns, people.
- `companies/clicks-group/annual-reports/clicks-annual-results-fy2025-20251023.txt`
- `companies/clicks-group/interim-reports/clicks-interim-results-h1fy2026-20260423.txt`
- `companies/clicks-group/press-releases/clicks-businessday-news-analysis-engelbrecht-20260210.txt`
- `companies/clicks-group/press-releases/clicks-financialmail-finance-ghost-conundrum-20260430.txt`

## Coverage Gaps / To Backfill
- Original PDF binaries (announcement, analyst booklet, analyst presentation) not saved — proxy blocks
  binaries from clicksgroup.co.za; catalogued as extracted text. Backfill via Claude in Chrome if
  binaries are needed for the archive.
- FY2025 Integrated Annual Report (/iar2025/) and Annual Financial Statements (full AFS) not yet
  extracted — only the SENS short-form results. Remuneration report not yet captured.
- Analyst presentation/booklet for H1 FY2026 and FY2025 not yet extracted to text (divisional KPI
  detail, store roll-forward by format) — fetch if deeper segmental analysis is needed.

## Last Updated
2026-06-07 — created on onboarding. FY2025 annual results + H1 FY2026 interim results catalogued from
official SENS announcements; Business Day & Financial Mail coverage saved. URL patterns verified
against FY2024/FY2025/FY2026 releases. CFO corrected to Gordon Traill (web sources stale on Fleming).
