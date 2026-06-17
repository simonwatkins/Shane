---
name: jse-sector-retail
description: >
  Sector-analysis lens for South African retailers (food, general/apparel and pharmacy/health &
  beauty), loaded on top of jse-analyst to add retail-specific depth. Use whenever the user
  analyses, reviews, compares or asks about a JSE-listed retailer or its results — e.g. Shoprite,
  Pick n Pay, Boxer, Woolworths, Spar, Mr Price, TFG, Truworths, Pepkor, Clicks, Dis-Chem. Also
  trigger on words like retail, retailer, supermarket, grocer, like-for-like, LFL, same-store,
  trading margin, trading density, sales per square metre, space growth, footprint, markdown,
  shrinkage, private label, store card, credit retailer, online/omnichannel, Sixty60, Single Exit
  Price, IFRS 16 leases. This skill adds the retail equation of value, LFL/space/margin
  interpretation, the right valuation lenses, retail risk flags and the SA consumer/regulatory
  context. It does NOT restate the general metrics table, the Citation Standard, SA macro context,
  the bare metric lists in references/sector-metrics.md, or the workflow — inherited from jse-analyst.
---

# JSE Sector Lens — Retail (South Africa)

A **bolt-on lens for `jse-analyst`**. It does not run on its own and it does not repeat the
general engine — it supplies only what is distinctive about analysing a retailer.

## Inheritance contract (read first)

`jse-analyst` owns everything universal and you MUST NOT restate it here: the general metrics
table, HEPS extraction, prior-period comparison discipline, the Citation Standard and Provenance
appendix, the 12-point general risk scan, SA macro/tax/BEE context, the workflow, and the
output-format rules. The **bare retail metric lists** — `Retail (Food)` and
`Retail (General / Clothing)` in `references/sector-metrics.md` — **do not reprint them;
interpret them.**

This skill is the **interpretation layer**. Apply it inside the `jse-analyst` workflow:

- **Step 3 (metrics):** after the general table, add the retail KPIs below and *read* them.
- **Step 4 (valuation):** use the retail valuation lenses below; suppress the multiples flagged.
- **Step 6 (risk scan):** add the retail-specific flags below to the general checklist.

Pair with the company skill if one exists (e.g. `jse-shoprite`, `jse-woolworths`, `jse-clicks-group`,
`jse-dischem`). Inherit all sourcing rules — every figure carries a `Source` tag and provenance
entry per the Citation Standard.

## Scope — when this applies

ICB Industry: **Consumer Staples (Food/Drug retailers)** and **Consumer Discretionary (General
retailers)**. Major JSE names by sub-segment (verified Jun 2026):

| Sub-segment | Names |
|---|---|
| Food / grocery | Shoprite (Checkers, Usave), **Boxer** (now separately JSE-listed), Pick n Pay, Spar, Woolworths Food |
| General / apparel | Mr Price, The Foschini Group (TFG), Truworths, Pepkor (Pep, Ackermans), Woolworths Fashion/Beauty/Home |
| Pharmacy / health & beauty | Clicks Group, Dis-Chem |

Encode every time:

1. **Pick the sub-segment lens** — food (defensive volumes, negative working capital), apparel
   (gross margin + markdown + credit), pharmacy (scripts + front-shop + SEP regulation). Mixing them
   up misreads the business.
2. **Multi-geography & separate listings.** Woolworths (SA + Australia), Shoprite (SA + rest-of-
   Africa), Spar (SA + Ireland/Switzerland after the **Poland exit**). **Boxer is now separately
   listed** — don't double-count it inside Pick n Pay. State which entity/geography you cite.

## 1. Value drivers — what actually moves the P&L

A retailer is a **thin-margin, high-throughput, working-capital business**; value compounds through
space × productivity × margin × capital turns, funded by a negative cash cycle.

> Value ≈ sustainable **ROIC above WACC**, compounded by **profitable space growth** and **LFL
> productivity**, with **negative working capital** funding the roll-out.

The engine:

- **Sales growth = like-for-like (LFL) + net space growth.** Decompose *every* sales figure into the
  two, then split LFL into **volume vs internal selling-price inflation**, and compare that inflation
  to **CPI / food CPI**. LFL strips new-store noise and is the true health signal.
- **Gross margin → trading/operating margin.** Margins are thin (food trading margin often ~5–7%;
  apparel gross margins high but markdown-exposed), so small margin moves swing profit hugely —
  **operating leverage on a thin base** cuts both ways.
- **Working capital is the hidden engine.** Supermarkets run **negative working capital** (suppliers
  fund inventory; customers pay cash) → a cash float that funds expansion. Inventory days, payable
  days and the cash-conversion cycle matter more here than almost anywhere.
- **Capital intensity & returns.** Space growth consumes capex; the test is **return on new space /
  ROIC vs cost of capital**. Cash-generative formats (Boxer, Mr Price's cash model) compound faster.

Three structural levers: **LFL productivity**, **profitable space-growth runway**, and **margin &
cost control** (private label, supply-chain scale, shrinkage).

## 2. KPIs and how to read them

Add these to the general table and interpret direction — do not just list them. (F = food,
A = apparel/general, P = pharmacy.)

| KPI | How to read it | What a move signals |
|---|---|---|
| **LFL / same-store (all)** | Strip new space; split volume vs internal selling-price inflation; compare to CPI | Positive **volume** in a weak consumer = share gains. **Deflation** (SA food, Nov–Dec 2025) compresses nominal LFL even on good volumes — read real, not nominal. |
| **Selling-price inflation vs CPI (F)** | Pricing power & positioning | Pricing *below* CPI with rising volume = winning the value end; pricing *above* CPI and losing volume = stress. |
| **Trading / operating margin (all)** | Thin base → small moves matter; watch the gross-to-trading bridge | Margin gain on positive operating leverage is high quality; margin held only via price investment is not. |
| **Gross margin + markdown rate (A)** | The apparel swing factor is clearance/markdown | Rising markdowns = buying errors or weak demand; high **full-price sell-through** is the quality signal. |
| **Inventory days & cash cycle (all)** | Rising inventory *ahead of* sales = markdown/waste risk | Negative working capital funding new stores is the model working; its erosion is an early warning. |
| **Space growth & return on new space / trading density (all)** | Roll-out runway × productivity | New space at *declining* sales-per-sqm destroys value even as total sales "grow". |
| **Online contribution & profitability (all)** | Growth optionality, often margin-dilutive (last mile) | Read the *trajectory to profitability*, not just penetration (Checkers Sixty60, Woolies Dash, Mr Price online). |
| **Credit sales % & bad debt (A, P)** | Store cards = a lending book bolted onto retail | Read it like a mini-bank (bad-debt ratio, NCA affordability). **Cash-based models (Mr Price) carry far less of this risk.** |

Margin-defence levers to watch across all: **private-label penetration, shrinkage (theft hits a thin
margin directly), and supply-chain cost as % of sales.**

## 3. Valuation methodology

Use the lenses retail actually trades on; flag the ones that mislead.

- **P/E and EV/EBIT on the operating retail business — PRIMARY**, cross-checked against **LFL
  momentum, space runway and trading-density trend**. Quality compounders (Shoprite; Mr Price
  historically) earn premium P/Es — rate the *durability* of LFL + profitable space, not one year.
- **Mind IFRS 16 when using EV/EBITDA.** IFRS 16 capitalises leases → inflated EBITDA, a lease
  liability in "net debt", and rent replaced by depreciation + interest. Compare peers on a
  **consistent pre/post-IFRS 16 basis**; prefer **EV/EBIT** or **rent-adjusted / EBITDAR** metrics;
  "net debt/EBITDA" is not comparable across differing lease intensity — state the basis.
- **Sum-of-the-parts** where a **credit book / financial-services arm** exists (Woolworths Financial
  Services JV with Absa; apparel store cards) and for **multi-geography** names (Woolworths SA +
  Australia; Shoprite SA + Africa; Spar SA + Europe). Value the retail and the credit/offshore legs
  separately — and **don't double-count a separately-listed subsidiary** (Pick n Pay's stake in
  **Boxer**).
- **ROIC vs WACC, FCF and dividend/buyback** — the compounding test; retail cash generation funds
  distributions. Use **lease-adjusted ROIC**.
- **SUPPRESS / down-weight: P/B** (asset-light; book ≠ value — leases and brand dominate) and **naïve
  EV/EBITDA** that ignores the IFRS 16 distortion.

## 4. Sector-specific risk flags (extend jse-analyst Step 6)

- **SA consumer health (the binding macro)** — real disposable income, unemployment, rates/debt
  service, fuel and food inflation, social-grant dependence, and **two-pot** withdrawals (a temporary
  spending lift, then normalisation).
- **Credit-book quality (apparel/pharmacy)** — bad-debt/impairment trend on store cards, NCA
  affordability rules, provisioning; a deteriorating book can swamp retail profit.
- **Margin pressure** — wage settlements, **electricity/diesel (load-shedding generator cost)**, rent
  escalations, rand-driven import costs (apparel, general merchandise, fuel), and competitive price
  investment.
- **Inventory / markdown & shrinkage** — over-stocking into a slowdown, fashion-risk markdowns
  (apparel), fresh-food waste, and rising theft/shrinkage.
- **Expansion & geography** — value-destructive new space or M&A; **offshore missteps** (Shoprite's
  earlier Africa write-downs; Woolworths' **David Jones** Australia write-down; **Spar's Poland
  exit/loss**); FX translation.
- **Channel & disruption** — online/last-mile economics, q-commerce, and **discounter encroachment**
  (Boxer, Pep) on incumbents.
- **Supply chain / systems & cyber** — distribution-centre disruption, **ERP/SAP migrations** (Spar's
  well-documented SAP issues), Transnet/port delays on imports, and POS/cyber outages.
- **Regulatory** — National Credit Act (credit retailers), Consumer Protection Act, Competition
  Commission scrutiny of **long-term mall lease exclusivity**, health-product/**Single Exit Price**
  rules (pharmacy), sugar tax (food/beverage), and B-BBEE procurement.

## 5. Accounting & regulatory regime (retail-specific)

- **IFRS 16 (leases) — the key distortion.** Capitalises operating leases: higher EBITDA, a
  right-of-use asset and lease liability, rent → depreciation + interest. Always compare retailers on
  a consistent basis and prefer EV/EBIT or rent-adjusted metrics; treat lease liabilities explicitly
  when quoting "net debt".
- **Trading profit / trading margin** — most SA retailers present a normalised "trading profit";
  reconcile to IFRS operating profit and use it consistently for margin trends.
- **53-week years & calendar shifts** — a 53rd week or a shifting Easter/festive period distorts
  growth and LFL; adjust for comparability.
- **Store-card credit** — where a retailer runs a credit book (or a JV like **Woolworths Financial
  Services** with Absa), **IFRS 9 ECL** applies — read that book like a lender.
- **HEPS** — strip store-disposal/impairment items; reconcile headline to attributable.
- **Currency / geography** — Woolworths (ZAR + AUD), Shoprite (ZAR + African currencies), Spar (ZAR +
  EUR/CHF). State the currency; give a ZAR equivalent.

## 6. Primary documents & cadence (for jse-report-downloader)

- **Interim & annual results** — year-ends vary widely (many ~June/July; Mr Price ~March/April;
  Clicks ~August; **Dis-Chem ~February**); confirm each.
- **Festive / quarterly trading updates (SENS)** — many SA retailers issue a **Christmas/festive or
  Q1 sales update with LFL by division** — price-sensitive; capture them.
- **Results presentation / data pack** — divisional LFL, space, trading margin, online and credit
  metrics.
- **Trading statements** (HEPS ranges); AGM; capital-markets/investor days.

Record in each retailer's `company.json` where the IR site publishes the **festive/Q1 trading
update and divisional data pack**, so the downloader fetches them, not just the annual report.

## 7. Five questions a retail specialist asks management

1. **Decompose sales** — LFL vs space, and within LFL **volume vs internal selling-price inflation vs
   CPI**, by division (real growth and share, not nominal).
2. What is the **return on new space and the trading-density trend** — is the roll-out still
   value-accretive or is new space diluting productivity?
3. (Credit retailers) How is the **store-card book** performing — bad-debt ratio, provisioning, NCA
   affordability — and how much of profit is retail vs credit?
4. What is the **gross-to-trading-margin bridge** (pricing, mix, markdown, shrinkage, load-shedding,
   wages, rent), and the medium-term **trading-margin target**?
5. **Online economics and competitive position** — is online converging to profitability, and how is
   the discounter/q-commerce threat (Boxer, Pep, Sixty60) reshaping share?

## Sub-sector nuances

- **Food / grocery** (Shoprite, Spar, Woolworths Food, Pick n Pay, Boxer): defensive volumes,
  **negative working-capital float**, private label and supply-chain scale; LFL volume + selling-price
  inflation vs **food CPI** is the core read. **Shoprite** (Checkers/Sixty60 premiumisation + Usave
  value) is the share-gainer; **Spar** is a wholesale/**franchise** model (different margin shape; SAP
  and Poland-exit overhangs); **Boxer** (discounter, **separately JSE-listed**) is the high-growth
  value format.
- **General / apparel** (Mr Price, TFG, Truworths, Pepkor): **gross margin, markdown rate and
  full-price sell-through** dominate; the **cash vs credit mix** is pivotal — **Mr Price is largely
  cash** (lower bad-debt risk, faster cash cycle); fashion/inventory risk and rand-driven import costs;
  omnichannel.
- **Pharmacy / health & beauty** (Clicks, Dis-Chem): defensive **dispensary/script volumes** plus
  higher-margin front-shop health & beauty; **Single Exit Price (SEP)** caps pharma pricing, so margin
  comes from front-shop + dispensing fee + **wholesale/distribution** (UPD for Clicks; CJ/Dis-Chem
  distribution); loyalty (ClicksClubCard) and private label drive the moat; store roll-out runway is a
  key growth lever. Read scripts vs front-shop vs wholesale separately.
- **Multi-geography** (Woolworths SA + Australia; Shoprite rest-of-Africa; Spar Ireland/Switzerland):
  value and risk-rate the offshore leg separately; FX translation and a history of write-downs warrant
  caution.

## Last updated

2026-06-17 — constituents and structure verified via web search (Boxer now separately listed;
Shoprite SA LFL +1.9% with Nov–Dec 2025 food deflation; Spar Poland exit; Pepkor on the JSE). Re-verify
names, year-ends and listing structure before relying on the trigger list.
