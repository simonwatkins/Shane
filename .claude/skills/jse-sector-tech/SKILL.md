---
name: jse-sector-tech
description: >
  Sector-analysis lens for JSE-listed technology / consumer-internet holding companies,
  loaded on top of jse-analyst to add internet-platform and NAV depth. Use whenever the user
  analyses, reviews, compares or asks about Naspers (NPN) or Prosus (PRX), or any consumer-
  internet / technology platform business — e.g. food delivery (iFood, Delivery Hero, Swiggy),
  classifieds (OLX), fintech / payments (PayU), edtech, e-tail. Also trigger on words like
  tech, technology, internet, consumer internet, platform, marketplace, GMV, take-rate,
  Tencent, sum-of-the-parts, NAV discount, discount to NAV. This lens adds the operating
  platform KPIs, the NAV / SOTP + discount-to-NAV overlay, the right valuation lenses and the
  tech/China-exposure risk flags. It does NOT restate the income-statement framework, the
  Citation Standard, SA macro context, or the analysis workflow — those are inherited from
  jse-analyst.
---

# JSE Sector Lens — Technology / Consumer-Internet Holdings (Naspers / Prosus)

A **bolt-on lens for `jse-analyst`**. It does not run on its own and it does not repeat the
general engine — it supplies only what is distinctive about analysing a consumer-internet
platform holding company. **Pair it with the NAV discipline below**: Naspers/Prosus is part
operating-platform group, part listed-investment holding company, so it needs BOTH layers.

## Inheritance contract (read first)

`jse-analyst` owns everything universal and you MUST NOT restate it: the income-statement
framework and general metrics table, HEPS extraction, prior-period comparison discipline, the
Citation Standard and Provenance appendix, the 12-point general risk scan, SA macro/tax/BEE
context, the workflow, and the output-format rules. This skill is the **interpretation layer**:
add the KPIs at Step 3, the valuation lenses at Step 4, the risk flags at Step 6. Every figure
still carries a `Source` tag and provenance entry. **Name this lens in the deliverable** ("Sector
lens: `jse-sector-tech`").

## Scope — when this applies

ICB: **Technology / Consumer Internet**. Primary JSE names: **Naspers (NPN)** and its majority-
owned, Amsterdam-listed international arm **Prosus (PRX, secondary on the JSE)**. Two structural
facts to encode every time:

1. **It is two things at once.** A *holding company* whose single largest asset is a stake in
   **Tencent** (held via Prosus), plus a portfolio of *operating* consumer-internet businesses
   (Food Delivery, Classifieds/OLX, Fintech/PayU, Etail, Edtech). Analyse the operating portfolio
   on platform KPIs AND the group on NAV / sum-of-the-parts.
2. **Reporting & currency.** Prosus reports in **USD**; Naspers is JSE-listed with a **ZAR** share
   price; Tencent reports in **CNY/HKD**. The Naspers↔Prosus cross-holding was simplified in 2023 —
   state the current structure you are analysing, and give a ZAR equivalent per CLAUDE.md.

## 1. Value drivers — what actually moves value

> Value ≈ (look-through value of listed stakes + fair value of unlisted assets) − net debt,
> then re-rated by the **discount to NAV** the market applies.

- **The Tencent stake** — historically the dominant driver of NAV; moves with Tencent's share
  price and China tech sentiment. Separate the Tencent effect from the operating portfolio when
  explaining a NAV move.
- **Discount to NAV** — Naspers/Prosus trade at a large discount to look-through NAV; the *change*
  in that discount drives shareholder return as much as NAV itself. Track the open-ended **share
  buyback** (historically funded by trimming Tencent) and its **NAV-per-share accretion**.
- **Operating-portfolio trajectory to profitability** — ecommerce revenue growth (organic, FX-
  neutral) and the swing of the consolidated ecommerce segment from losses to **trading profit**.
- **Capital allocation** — buyback vs M&A vs balance-sheet; the buyback is the primary
  discount-management tool.
- **FX** — USD (Prosus), ZAR (Naspers share price), CNY/HKD (Tencent), EUR/BRL/INR (operating assets).

## 2. KPIs and how to read them

Add to the general table and interpret direction — do not just list.

| KPI | What it is | Good direction | What a move signals |
|---|---|---|---|
| **Group / segment GMV** | Gross merchandise value transacted | Growing | The top of the funnel; pair with take-rate to get revenue. |
| **Ecommerce revenue growth (organic, FX-neutral)** | Like-for-like portfolio growth | Higher | Strip FX and M&A — reported growth flatters/penalises with currency and deals. |
| **Consolidated ecommerce trading profit / margin** | Operating profit of the e-commerce portfolio | Loss → profit | The whole equity story is the path to sustained profitability; watch the inflection by segment. |
| **Segment profitability** (Food Delivery, Classifieds, Fintech/PayU, Etail, Edtech) | Trading profit/loss per vertical | Improving | Identifies which verticals fund themselves vs burn cash. |
| **Take-rate** | Revenue ÷ GMV | Stable/rising | Pricing power / monetisation; a falling take-rate on rising GMV = competition. |
| **Tencent contribution** | Equity-accounted share of Tencent earnings | n/a | Large and non-cash; isolate from core operating performance. |
| **NAV per share & discount to NAV** | Look-through value vs price | Discount narrowing | The re-rating lever; track buyback accretion to NAV/share. |

## 3. Valuation methodology

- **Sum-of-the-parts / NAV — PRIMARY.** Tencent and other listed stakes at market; unlisted assets
  at last funding round, DCF or peer multiples; less net debt and the holding-company structure.
  **Always state the discount to NAV** and the date/price of the Tencent mark.
- **Discount-to-NAV analysis** — the share trades at a persistent discount; model the return from
  NAV growth AND discount change. Buyback accretion adds NAV per share when the share trades below NAV.
- **Look-through / core headline earnings** — Naspers reports **core headline earnings** (excludes
  Tencent one-offs, SBC, amortisation); use it, not statutory HEPS, for the operating read.
- **SUPPRESS consolidated trailing P/E** — distorted by equity-accounting of associates, non-cash
  fair-value moves and loss-making consolidated units; it does not describe the business.

## 4. Sector-specific risk flags (extend jse-analyst Step 6)

- **Tencent concentration & China risk** — single-asset dependence; Chinese tech regulation, VIE
  legal structure, gaming-licence approvals, US-China geopolitics and ADR/listing risk.
- **Discount persistence** — the NAV discount may not close despite buybacks; governance/structure
  is part of the cause.
- **Cash burn** — loss-making ecommerce verticals consuming capital; scrutinise the path and date to
  profitability and the funding need.
- **Capital-allocation / M&A** — value-destructive acquisitions; buyback funded by selling a
  compounding asset (Tencent) is a real trade-off.
- **FX translation** across USD/ZAR/CNY/EUR; **SA exchange control / inward-listing** mechanics.
- **Governance** — control structure, free-float, and the simplified (but still complex) cross-holding.

## 5. Accounting & regulatory regime

- **Associate equity-accounting** (IAS 28) for Tencent, Delivery Hero etc. — a large non-cash
  earnings line; reconcile to cash.
- **Core headline earnings** — a company-defined measure; check the bridge from HEPS and what is
  excluded (Tencent one-offs, SBC, amortisation, impairments).
- **Fair value of unlisted investments** (IFRS 9 / Level 3) — disclose the valuation basis and last
  mark date; sensitive to assumptions.
- **Reporting currency** — Prosus USD, Naspers ZAR; FY end **31 March**. Give a ZAR equivalent.

## 6. Primary documents & cadence (for jse-report-downloader)

- **Interim results (H1 to 30 Sep, reported ~Nov)** and **annual results (FY to 31 Mar, reported
  ~June)** — for BOTH Naspers and Prosus.
- **Trading updates / pre-close** and **NAV / buyback SENS announcements**.
- **Tencent quarterly results (HKEX)** — the single biggest NAV input; capture each quarter.
- **Capital Markets Day** and investor presentations.

## 7. Five questions a tech-holdco specialist asks management

1. What is the concrete plan to **narrow the discount to NAV**, and how much accretion has the
   buyback delivered per share?
2. Which ecommerce segments are **self-funding vs still burning**, and what is the dated path to
   group ecommerce trading profit?
3. What is the policy on **trimming Tencent to fund buybacks**, and the limit?
4. What is the **China-regulatory / VIE / geopolitical** exposure and the mitigation?
5. How is **capital allocated** between buybacks, M&A and the balance sheet, and what return hurdle applies?

## Last updated

2026-06-18 — created. Re-verify the Naspers/Prosus structure, the buyback status and the Tencent
stake size via web search before relying on specifics.
