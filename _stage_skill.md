---
name: jse-sector-mining
description: >
  Mining sector lens for jse-analyst. Loaded BY NAME (Skill tool) when a company's
  company.json has icb_sector "Mining", to add mining value drivers, KPI interpretation,
  valuation lenses and risk flags on top of the general analysis. Does not duplicate the
  general metrics table or the bare metric list in references/sector-metrics.md.
---

# Mining sector lens (bolt-on for jse-analyst)

## When this applies & what it adds
- Routes from `icb_sector: "Mining"`. Loaded **by name** (Skill tool) by the jse-analyst subagent at Step 3.
- Adds ONLY: value drivers, KPI interpretation (Step 3), valuation lenses (Step 4), risk flags (Step 6), and SA context. The metric **list** lives in `references/sector-metrics.md`; the general standardised table, the Citation Standard and the general risk checklist live in `jse-analyst`. Do not repeat them — interpret them.

## A. Value drivers — the equation of value for mining

Equity value ≈ **NPV of the life-of-mine (LOM) plan** at an assumed price deck **+** option value on resources not yet in the plan **−** rehabilitation/closure liabilities **−** net debt.

The P&L engine is: **realised price (mostly USD) × volume × grade × recovery − unit cost (AISC)**. For SA-cost / USD-revenue producers the **ZAR/USD rate** is a core swing factor — a weaker rand lifts margins (the "rand hedge"); always state the FX basis.

Three structural levers decide asset quality:
- **Cost-curve position** → survivability through the trough.
- **Reserve life & replacement** → longevity of the cash flows.
- **Capital intensity** of sustaining vs growth output → how much of EBITDA actually converts to FCF.

## B. KPI interpretation (augments analyst Step 3)

Read these on top of the Mining list in `references/sector-metrics.md` — do **not** relist it.

- **AISC vs realised price → unit margin.** AISC **percentile on the global cost curve** signals who survives a downturn. Confirm the **AISC definition** (World Gold Council standard vs company-defined) before any peer comparison.
- **Realised vs benchmark price** reflects product quality, sales timing, **provisional-pricing** adjustments and the hedge book → reconcile to the hedge note.
- **Reserve & resource statement (SAMREC; JORC for ASX/LSE dual-listings):** **reserve life = reserves ÷ annual production**; **reserve replacement < 100% = a depleting asset**. Separate genuine discovery from resource→reserve reclassification driven only by a higher price deck.
- **Grade & recovery** are the primary unit-cost drivers; structural grade decline is a cost headwind that volume cannot offset indefinitely.
- **Sustaining (SIB) vs growth capex split:** underspending SIB flatters near-term FCF but stores up production risk — check it against depletion.
- **Cash build/(drawdown) & gearing (ND/EBITDA)** usually **drive the dividend** in mining: many SA miners pay on a net-cash or gearing target, or a % of FCF, rather than a fixed payout.

## C. Valuation lenses (augments analyst Step 4)

- **P/NAV is the primary mining lens** — price ÷ NPV of the LOM DCF. **State the discount rate and the price deck**; the number is meaningless without them.
- **EV/EBITDA at spot AND at a normalised long-term deck** — a single-point multiple misleads across the cycle.
- **EV per in-situ resource (per oz / per tonne)** — for explorers and for optionality not yet in the mine plan.
- **FCF yield at spot vs consensus deck**, and **dividend yield read against the variable payout policy** (not a fixed-payout assumption).
- **Commodity-price and ZAR/USD sensitivity tables are essential, not optional.**
- **Pitfall:** trailing **P/E is near-useless at commodity-price extremes** — earnings are hyper-cyclical and impairment-laden. Prefer P/NAV and through-cycle EV/EBITDA over the analyst's default trailing P/E here.

## D. Sector-specific risk flags (augments analyst Step 6)

Beyond the analyst's general checklist (going concern, audit opinion, impairments, covenants, etc.), scan for:

- **Safety / regulatory stoppages:** fatalities and **Section 54/55 stoppages** under the Mine Health and Safety Act — a Section 54 can halt a shaft and is materially production-negative (very SA-specific).
- **Power:** Eskom load-shedding and electricity-tariff (**NERSA**) exposure; status of any self-generation plans.
- **Resource nationalism / tenure:** the **Mining Charter** (BEE ownership, the "once empowered, always empowered" dispute), **MPRDA** tenure (mining-right renewals/conversions), and the **state royalty** (Mineral & Petroleum Resources Royalty Act).
- **Environmental:** rehabilitation & closure provisions (adequacy and discount rate), water-use licences, **tailings storage facility (TSF) integrity** (post-Brumadinho scrutiny), acid mine drainage, and **carbon-tax** exposure.
- **Social / labour:** Social & Labour Plans (SLPs), community unrest, **Section 189** retrenchments, and **NUM / AMCU** wage cycles / strike risk.
- **Operating / market:** single-asset or deep-level concentration, grade depletion, hedge-book mark-to-market, by-product credits, and **country risk** for Africa-exposed names.

## E. SA-specific sector context

- Reserves/resources reported under **SAMREC** — reconcile to **JORC** for ASX/LSE dual-listings.
- **MPRDA + Mining Charter** govern tenure and ownership; a **state royalty** (Mineral & Petroleum Resources Royalty Act) and **carbon tax** apply.
- **Eskom / NERSA** power risk is structural, not merely cyclical.
- The **rand-hedge** dynamic means a weaker ZAR generally *helps* SA-cost, USD-revenue producers — always state the FX basis used.

## F. Common pitfalls / "don't get fooled"

- **Headline vs normalised earnings diverge sharply on impairments** (common in mining) — reconcile both; never quote one as the other.
- **"AISC" is not standardised** across companies — check the definition before comparing peers.
- **Reserve statements get restated when the price deck changes** — distinguish a price-driven restatement from real operational change.
