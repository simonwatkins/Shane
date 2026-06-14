---
name: jse-naspers
description: >
  Research skill for Naspers Limited (JSE: NPN) and its controlled international arm Prosus N.V.
  (Euronext Amsterdam & JSE: PRX). Use whenever the user mentions Naspers, Prosus, NPN, PRX,
  Koos Bekker, Fabricio Bloisi, or the group's holdings — Tencent, iFood, Just Eat Takeaway (JET),
  OLX, PayU, eMAG, Despegar, Swiggy, Meituan, Delivery Hero — or asks about the holdco NAV discount,
  the share-repurchase/buyback programme, ecommerce aEBITDA/aEBIT, core headline earnings, the CEO
  'moonshot' award, or Tencent stake value. Also trigger for Naspers/Prosus arbitrage and currency
  (rand/USD/CNY/BRL/EUR/INR) questions. This skill knows where the documents live, the reporting
  calendar, the URL patterns, and the right analytical framework.
  NOTE: Naspers reports in USD though it lists in ZAR; results are presented at the Prosus level with
  a parallel Naspers summary. ~80-85% of value is the Tencent stake.
---

# Naspers (NPN) / Prosus (PRX) Research

## Quick Reference
- **JSE code (Naspers):** NPN | **ISIN:** ZAE000015889 | **ADR:** NPSNY
- **Prosus:** Euronext Amsterdam & JSE: PRX | **ISIN:** NL0013654783
- **Sector:** Consumer-internet holding company (Tencent stake + global ecommerce ecosystem)
- **Year-end:** **31 March** | **Reporting currency:** **USD** (Naspers trades ZAR; Prosus trades EUR/ZAR)
- **Chair:** JP (Koos) Bekker | **CEO:** Fabricio Bloisi (Naspers & Prosus) | **CFO:** Nico Marais CA(SA)
- **Auditor:** Deloitte | **JSE sponsor:** Investec
- **Naspers IR:** https://www.naspers.com/investors | **Prosus IR:** https://www.prosus.com/investors
- **Registered (Naspers):** 40 Heerengracht, Cape Town, 8001 | **Prosus:** Gustav Mahlerplein 5, Amsterdam

## Structure (read this first)
Naspers controls Prosus; Prosus holds the Tencent stake and all international ecommerce. There is a
**cross-holding** (Prosus holds Naspers shares). Group financials are presented at the **Prosus** level,
with a **parallel Naspers summary**. Naspers funds its own buyback by **selling Prosus shares**. When
quoting figures, state whether they are Prosus-level or Naspers-level. ~**80-85% of see-through NAV is
Tencent** (HKEX: 0700; group held **23.5%** at the H1 FY2026 reporting period).

## Reporting calendar & where to find documents
- **Annual results** (year to 31 March): published **~late June** (FY2025 ~23 June 2025).
- **Interim results** (six months to 30 September): published **~late November** (H1 FY2026 on 24 Nov 2025).
- **>> FY2026 full-year results are due ~late June 2026 — capture them when released. <<**
- **Prosus results archive:** https://www.prosus.com/investors/financial-information/results
- **Naspers results archive:** https://www.naspers.com/investors/results-reports-events/results-reports-and-events-archive
- **SENS full report pattern:** https://senspdf.jse.co.za/documents/<YYYY>/jse/isse/PRXE/<TAG>.pdf (e.g. 1H26.pdf).
- **PDF URL roots** (scrape the archive page for the live slug — Prosus uses hy2026, Naspers uses hy-2026):
  - https://www.prosus.com/~/media/Files/P/prosus-corp-v2/results-reports-and-events-archive/latest-results/<period>/
  - https://www.naspers.com/~/media/Files/N/Naspers-Corp-V2/results-reports-and-events-archive/latest-results/<period>/

## Download channel note (IMPORTANT for this sandbox)
bash curl/wget are **proxy-blocked (403)**. To capture document text, use **mcp__workspace__web_fetch**
on the PDF URL — it returns the **extracted text** (Content-Type application/pdf) which can be saved as a
.txt sidecar (this is what jse-analyst reads). Large PDFs (>~25k tokens) are auto-saved by web_fetch to a
tool-results file — copy that file into the company folder rather than loading it into context. To save the
**binary original** PDF, use the **Claude-in-Chrome** browser download channel (web_fetch is text-only).

## What we have locally (as of 2026-06-07)
- interim-reports/naspers-prosus-interim-results-short-form-h1fy2026-20251124.txt — H1 FY2026 SENS short-form.
- annual-reports/naspers-summary-consolidated-financial-statements-fy2025-20250623.txt — FY2025 Naspers summary AFS.
- annual-reports/naspers-remuneration-report-fy2025.txt — FY2025 remuneration report (CEO single-figure + moonshot).
- **Outstanding:** FY2025 Prosus booklet/presentation; HY2026 full statements + media release (binary); **FY2026 full-year results (due ~late June 2026).**

## Key numbers already extracted (cite the sidecar + page)
**H1 FY2026 (6m to 30 Sep 2025, continuing ops, US$):** Revenue 3,623m (HY25 2,963m, +22%/+14% LC);
Ecommerce aEBITDA 530m (+70%); Ecommerce aEBIT 400m (+97%); Group aEBIT 250m (HY25 60m);
Core headline earnings 4,000m (+13%), core HEPS 179c (+24% — buyback-boosted); FCF 1,296m.
**FY2026 guidance:** Ecommerce revenue US$7.3-7.5bn; Ecommerce aEBITDA US$1.1-1.2bn (ex-JET).
**Three-year plan (CMD 25 Jun 2025):** >=2x Ecommerce revenue, 3x Ecommerce aEBITDA.
**Buyback (since Jun 2022):** >US$41bn returned; Prosus free-float -30%; combined discount narrowed ~25pp;
Prosus repurchased 892.7m N shares (US$30.1bn) -> +18% NAV/share accretion; Naspers leg US$11.5bn.

## CEO 'moonshot' award (remuneration report)
Face value **US$100m** at grant. Vests only if **BOTH**: (1) **combined Naspers/Prosus market cap (US$)
doubles or better within four years** and is maintained >=1 year (threshold by 30 June 2028); and
(2) **relative TSR over the four-year term beats the 50th percentile** of the peer group. FY2025 CEO
single-figure ~US$55.9m (~R1.01bn), ~1% fixed salary; remainder PSUs (~US$27.3m) + SARs (~US$27.2m).
Bloisi personally bought ~R500m of Prosus shares (July 2025) — alignment signal.

## Analytical framework
1. **Two legs, separately.** (a) Tencent stake (value, % held, Tencent's own results/regulation); (b) ecommerce
   ecosystem (revenue growth, aEBITDA/aEBIT, segment profitability: iFood, OLX, PayU, JET, eMAG).
2. **The discount is the story.** Always state see-through NAV, holdco discount (~30-35%), and buyback accretion.
   Distinguish Prosus discount vs Naspers discount (cross-holding makes them differ).
3. **iFood / Brazil watch.** FY27 iFood aEBITDA guided DOWN to US$100-150m due to price war (Meituan-backed
   Keeta, 99Food). Flag this as the main near-term ecommerce risk.
4. **Currency.** Present in USD; NAV is CNY/HKD-heavy (Tencent) + BRL (iFood) + EUR/INR. Naspers' ZAR share
   price adds a rand-translation overlay: weak rand flatters NPN, strong rand hurts — independent of assets.
5. **Compliance.** Informational only; not advice. Note search-derived prices/targets may be stale; no live JSE feed.

## Pitfalls
- Don't conflate Prosus-level and Naspers-level figures, or aEBITDA vs aEBIT (the group reports both).
- Tencent reports on a **31 December** year and in **RMB** — different period/currency from Naspers' 31 March/USD.
- "All operated businesses profitable" refers to the **ecommerce** segment, not the whole group's reported EBIT.
- Watch slug inconsistency (hy2026 vs hy-2026) — scrape the archive page; don't assume the filename.
