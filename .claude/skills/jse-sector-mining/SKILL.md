---
name: jse-sector-mining
description: >
  Sector-analysis lens for South African mining & resources companies, loaded on top of
  jse-analyst to add mining-specific depth. Use whenever the user analyses, reviews,
  compares or asks about a JSE-listed miner or its results — e.g. Anglo American, BHP,
  Glencore, Gold Fields, AngloGold Ashanti, Sibanye-Stillwater, Impala Platinum (Implats),
  Northam Platinum, Valterra Platinum (formerly Anglo American Platinum / Amplats), Kumba
  Iron Ore, Exxaro, African Rainbow Minerals (ARM), Harmony Gold, Thungela Resources. Also
  trigger on words like mining, miner, PGM, platinum group metals, gold, platinum, palladium,
  rhodium, coal, iron ore, manganese, chrome, AISC, all-in sustaining cost, production update,
  ore reserves, resources, SAMREC, grade, recovery, life-of-mine. This skill adds value
  drivers, KPI interpretation, the correct valuation lenses, mining-specific risk flags, and
  the SA mining regulatory regime. It does NOT restate the income-statement framework, the
  Citation Standard, SA macro context, or the analysis workflow — those are inherited from
  jse-analyst.
---

# JSE Sector Lens — Mining & Resources (South Africa)

A **bolt-on lens for `jse-analyst`**. It does not run on its own and it does not repeat the
general engine — it supplies only what is distinctive about analysing a miner.

## Inheritance contract (read first)

`jse-analyst` owns everything universal and you MUST NOT restate it here: the income-statement
framework and general metrics table, HEPS extraction, prior-period comparison discipline, the
Citation Standard and Provenance appendix, the 12-point general risk scan, SA macro/tax/BEE
context, the workflow, and the output-format rules.

This skill is the **interpretation layer**. Apply it inside the `jse-analyst` workflow:

- **Step 3 (metrics):** after the general table, add the mining KPIs below and read them, not
  just tabulate them. The bare metric list lives in `references/sector-metrics.md` (Mining);
  this skill is how to interpret it.
- **Step 4 (valuation):** use the mining valuation lenses below; suppress the multiples flagged.
- **Step 6 (risk scan):** add the mining-specific flags below to the general checklist.

Pair with the company skill if one exists (e.g. `jse-kumba`). Inherit all sourcing rules — every
figure still carries a `Source` tag and provenance entry per the `jse-analyst` Citation Standard.

## Scope — when this applies

ICB Industry: **Basic Materials → Mining**. Major JSE-listed names (verified Jun 2026):

| Sub-sector | Names |
|---|---|
| Gold | AngloGold Ashanti, Gold Fields, Harmony Gold, Pan African Resources |
| PGMs (platinum group metals) | Valterra Platinum (ex-Anglo American Platinum / Amplats), Impala Platinum (Implats), Northam Platinum, Sibanye-Stillwater (PGM + gold) |
| Bulk & energy | Kumba Iron Ore, Exxaro (coal), Thungela Resources (coal), plus manganese/chrome producers |
| Diversified | Anglo American, BHP, Glencore, African Rainbow Minerals (ARM) |

Two things to encode every time:

1. **Names change — verify, don't assume.** Anglo American Platinum became **Valterra Platinum
   (JSE: VAL)** on demerger from Anglo American (completed 31 May 2025). **Anglo American** is
   mid-restructuring toward a copper + iron-ore portfolio (demerged Valterra, exiting De Beers,
   steelmaking coal and nickel) — analyse the *go-forward* portfolio, not the historical one.
2. **Listing & currency vary.** Several are dual-listed (Anglo, BHP, Glencore — LSE/ASX primary,
   JSE secondary; Gold Fields and AngloGold also NYSE). State which listing's results you cite.

## 1. Value drivers — what actually moves the P&L

A miner is a **price-taker**; earnings are leveraged to factors largely outside management control:

> Earnings ≈ (realised price − unit cash cost) × volume, less sustaining capex, royalties and tax.

- **Realised commodity price** (a *basket* price for PGMs across Pt/Pd/Rh/Au). Exogenous and volatile.
- **Volume** — production and *sales* can differ within a period (stockpile/ inventory movements,
  smelter run-rate, logistics); reconcile produced vs sold.
- **Unit cost** — see AISC below.
- **USD/ZAR** — most SA miners sell in USD (or USD-linked prices) but incur ZAR costs, so a
  **weaker rand widens margins** (the classic "rand hedge") and a stronger rand compresses them.
  Always separate the *price* effect from the *FX* effect when explaining an earnings move.
- **Grade & recovery** — orebody quality; falling grade or recovery raises unit cost mechanically.
- **SA operational swing factors** (often the difference between hitting and missing guidance):
  **Eskom** electricity (load-shedding/curtailment, above-inflation tariffs), **Transnet** Freight
  Rail & port capacity (binds bulk exporters — iron ore, coal, manganese, chrome), water security,
  and labour/community relations.

## 2. KPIs and how to read them

Add these to the general table and interpret direction — do not just list them.

| KPI | What it is | Good direction | What a move signals |
|---|---|---|---|
| **AISC** (all-in sustaining cost, per oz / per t) | Cash cost to produce *and* sustain output | Lower | Compare AISC vs realised price = cash margin/unit. Rising AISC on flat price = squeeze (cost inflation, grade decline, stronger rand). Cost-curve position (1st/2nd quartile) decides who survives a trough. |
| **Production vs guidance** | Output against the year's guided range | Meet/beat | A miss flags operational trouble (stoppages, load-shedding, geology). Watch for mid-year guidance cuts. |
| **Realised price vs benchmark/spot** | Price achieved vs index | Near/above | A discount signals product mix, quality/penalty discounts, timing lags or hedging. |
| **Reserves & resources / life-of-mine** (SAMREC) | Remaining mineable inventory | Stable/growing | Falling reserves or LoM without replacement = depletion. Reserve replacement ratio <100% = shrinking business. |
| **Grade** (g/t, %) & **recovery** (%) | Orebody richness; processing yield | Higher | Lower grade raises cost; recovery gains offset it. |
| **Stripping ratio** (open pit, waste:ore) | Waste moved per unit ore | Lower/stable | Rising ratio lifts near-term unit cost. |
| **Net cash / (debt)** & gearing | Balance-sheet resilience | Net cash / low | Miners need a fortress balance sheet to survive price troughs; judge through-cycle, not at peak. |

PGM-specific: basket price per 4E/6E oz. Gold-specific: the **rand gold price** (the key margin
driver for high-ZAR-cost SA producers such as Harmony).

## 3. Valuation methodology

Use the lenses the sector actually trades on; flag the ones that mislead.

- **P/NAV (price-to-net-asset-value) — PRIMARY.** NAV = DCF of life-of-mine cash flows at an
  assumed commodity-price and USD/ZAR deck, less net debt and rehabilitation liabilities. The share
  trades as a multiple of NAV (e.g. 0.8× = a 20% discount). **Always state the price deck and
  discount rate** — NAV is highly sensitive to both.
- **EV/EBITDA and FCF yield — run at BOTH spot and consensus/normalised prices** (and at spot vs
  forward FX). A miner can look cheap on spot and expensive on long-run prices, or vice versa.
  Always disclose the price/FX assumptions used.
- **FCF yield through the cycle** and **capex intensity** — split sustaining vs expansionary
  (growth) capex; growth capex depresses near-term FCF but builds NAV.
- **Dividend** — many SA miners run a **policy-linked / variable payout** (a % of headline earnings
  or of FCF), so the dividend swings with the cycle. Do **not** annualise a peak-cycle dividend as
  if sustainable.
- **SUPPRESS / down-weight: trailing P/E as the primary anchor.** Earnings and HEPS swing violently
  with commodity prices and FX — a low trailing P/E at the top of the cycle is a classic value trap,
  and a high P/E at the trough can mark a recovery. Use **mid-cycle / normalised** earnings instead.
  Headline P/B is also weak here (book value ≠ orebody value) — prefer P/NAV.

## 4. Sector-specific risk flags (extend jse-analyst Step 6)

In addition to the general 12-point scan, check for:

- **Safety stoppages** — Section 54/55 notices under the Mine Health and Safety Act (a Section 54
  halts a shaft/operation → lost production days); **fatalities** (human cost, ESG, and
  licence-to-operate). Quantify production days lost.
- **Rehabilitation & decommissioning provisions** (IAS 37) and whether the **rehab trust is fully
  funded** — closure liabilities are large, rising, and discount-rate sensitive; under-provisioning
  is a hidden liability.
- **Reserve depletion** / declining life-of-mine without a replacement plan.
- **Commodity hedging / derivatives** — caps upside and creates mark-to-market swings (relevant for
  some gold/PGM producers).
- **Power** — Eskom interruptions, load-curtailment agreements, self-generation capex, tariff hikes.
- **Logistics** — Transnet rail/port constraints capping export volumes (Kumba, Exxaro, Thungela,
  manganese/chrome); look for stockpiles building at the mine.
- **Labour** — wage rounds, union action (NUM/AMCU), Section 189 retrenchments.
- **Community unrest, illegal mining (zama-zamas)**, surface-rights and land disputes.
- **Water-use licences; tailings-dam stability** (heightened scrutiny post-Brumadinho).
- **Carbon tax exposure**, Scope 1/2 emissions trajectory, and **just-energy-transition** risk for
  coal and energy-intensive PGM assets.
- **Regulatory / ownership** — mining-right renewals ("use it or lose it"), Mining Charter (BEE)
  compliance, royalty changes, resource-nationalism noise.

## 5. Accounting & regulatory regime (mining-specific)

- **SAMREC Code** — reporting of Mineral Resources & Reserves (competent-person signed); **SAMVAL
  Code** — valuation of mineral assets. Compare the reserve/resource statement year-on-year.
- **Reporting currency** — many report in **USD** (Anglo, BHP, Glencore, Gold Fields, AngloGold);
  state the currency and give a **ZAR equivalent** (per CLAUDE.md). Rand reporters include Kumba,
  Exxaro, Harmony, ARM, Sibanye, Northam.
- **Key accounting items:** rehabilitation/decommissioning provisions (IAS 37, discount-rate
  sensitive); **impairment testing** of mining assets (IAS 36) — very sensitive to price/FX/discount
  assumptions and common in downturns; capitalised **stripping** costs; exploration & evaluation
  (IFRS 6); inventory/stockpile valuation.
- **HEPS divergence** — under the SA headline-earnings definition, impairments and asset disposals
  are excluded, so in a write-down year **HEPS can diverge sharply from EPS**; reconcile and explain.
- **Regulators & rules:** DMRE (Dept of Mineral & Petroleum Resources); **MPRDA** (mining rights);
  **Mining Charter** (BEE ownership/procurement thresholds); **Mineral & Petroleum Resources Royalty
  Act** (royalty by formula, differing for refined vs unrefined output); Mine Health and Safety Act;
  NEMA (environmental authorisations).

## 6. Primary documents & cadence (for jse-report-downloader)

- **Quarterly production / operational updates (Q1–Q4)** — miners report *production* quarterly even
  when financials are half-yearly; these are price-sensitive and precede results. Capture all four.
- **Interim & annual results** (HEPS, AISC, dividend).
- **Annual Mineral Resource & Reserve statement (SAMREC)** — in or alongside the integrated report.
- **Integrated annual report** and a **standalone sustainability/ESG report** (safety, emissions,
  water, community).
- **Trading statements / production-guidance updates (SENS)** — guidance changes are material.
- **Capital markets / investor days.**

Record in each miner's `company.json` which of these the IR site publishes and where, so the
downloader fetches the quarterly updates and reserve statement, not just the annual report.

## 7. Five questions a mining specialist asks management

1. Where does each operation sit on the **industry cost curve**, and what is the AISC trajectory net
   of grade decline and the rand assumption?
2. What is the **reserve life and replacement plan** (brownfield vs M&A), and the capex needed just
   to sustain current production?
3. How much production was lost to **Section 54 stoppages, load-shedding and Transnet** this period,
   and what is the mitigation (self-generation, rail slots, stockpiles)?
4. What **commodity-price and USD/ZAR assumptions** underpin the impairment tests and the dividend,
   and how sensitive are they?
5. What is the **rehabilitation liability**, is the trust fully funded, and what is the closure /
   just-transition plan for end-of-life and coal/PGM assets?

## Sub-sector nuances

- **Gold** (AngloGold, Gold Fields, Harmony, Pan African): rand gold price is the key margin lever
  for high-ZAR-cost SA producers (Harmony is the highest-leverage rand hedge); deep-level
  safety/seismicity; hedging generally rare. Value on P/NAV + FCF.
- **PGMs** (Valterra, Implats, Northam, Sibanye PGM): basket price (Pt, Pd, Rh + Au) and auto/
  industrial demand drive earnings; energy-intensive smelting makes them load-shedding-sensitive;
  watch smelter run-rate, refined-vs-produced inventory build, and volatile rhodium.
- **Bulk & energy** (Kumba iron ore; Exxaro & Thungela coal; manganese/chrome): **Transnet rail &
  port is the binding constraint**; export parity vs domestic pricing; quality premiums/discounts
  (lump vs fines; coal calorific value). Coal carries an energy-transition/ESG valuation discount.
- **Diversified** (Anglo American, BHP, Glencore, ARM): build value up segment-by-segment. Anglo is
  mid-restructuring — model the go-forward copper/iron-ore portfolio. Glencore carries a large
  **marketing/trading** earnings stream with a different (volume/volatility) driver to mining.

## Last updated

2026-06-14 — constituents verified via web search (Valterra/ex-Amplats rename and Anglo American
restructuring confirmed). Re-verify names and listings before relying on the trigger list.
