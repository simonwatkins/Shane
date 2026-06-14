---
name: jse-mining
description: >
  Sector skill for analysing JSE-listed mining and resources companies. Use whenever the
  user asks to analyse, review or compare a miner's results, or mentions Anglo American,
  Anglo American Platinum (Amplats), BHP, Glencore, Sasol, Gold Fields, AngloGold Ashanti,
  Harmony, Impala Platinum (Implats), Sibanye-Stillwater, Exxaro, Kumba Iron Ore, African
  Rainbow Minerals, Northam, Thungela, or any JSE mining/resources name — even casually
  ("pull Sasol's numbers", "how did Amplats do"). Also trigger for tasks about commodity
  exposure, unit costs, production volumes, net-debt-to-EBITDA, or peer comparisons across
  miners. Reads documents already downloaded to companies/[slug]/; if they are missing it
  triggers jse-report-downloader first. Holds to the workspace Citation Standard: every
  figure cited to document and page, prior-period comparison always, estimates marked (e).
---

# JSE Mining & Resources Analyst

## Purpose

Produces standardised analysis of mining-company results from locally downloaded documents.
Miners are different from retailers or banks: earnings are driven by commodity price and
currency, balance-sheet strength (leverage) matters as much as profit, and operational
metrics (production, grade, unit cost) explain the numbers. This skill encodes that lens.

## Prerequisites

- Documents must be downloaded locally (`companies/[slug]/`). If missing, trigger
  `jse-report-downloader` first. Check `manifest.json` before starting.
- Never analyse from web-fetched text held only in context — save and register first.

## Metrics to extract (current period AND prior corresponding period, with % / bps change)

**Profitability & cash**
- Revenue / turnover (state currency — many miners report in USD)
- EBITDA and EBITDA margin
- Headline earnings and **HEPS** (the SA headline measure) — and basic/diluted EPS
- Free cash flow (operating cash flow less capex)
- Dividend per share (ordinary + special), and the dividend policy/cover

**Balance sheet & returns**
- Net debt (or net cash) and **net debt / EBITDA** (the key leverage gauge)
- Capex (sustaining vs expansionary, if split)
- ROCE / return on capital, where disclosed

**Operational (the "why" behind the numbers)**
- Production volumes by commodity (oz, t, Mt, boe) vs pcp
- Unit cost: AISC (gold/PGM), cash cost, or cost/tonne — vs pcp and vs guidance
- Realised prices vs benchmark; grade / recovery where given

## Rules (non-negotiable — the house standard)

1. **Numbers are sacred.** Never round, estimate or infer when the actual figure is in the
   document. Derived figures (e.g. EBITDA built up from segments) marked `(e)` with working.
2. **Cite everything** — every figure to its document and page.
3. **Prior-period comparison always.** Current, pcp, and the change. Margins/returns in **bps**.
4. **State the reporting currency** and give a ZAR view where the miner reports in USD; note
   the average vs closing rate used.
5. **Flag sensitivity.** A one-line read on commodity-price and rand/USD exposure — the two
   swing factors for SA miners. If the company gives a sensitivity table, cite it.
6. **Honest gaps.** Missing disclosure → "not disclosed", never papered over.
7. **Commodity cycle context.** Note where the result sits in the price cycle, factually
   (e.g. "PGM basket price down y/y per p.X") — not a price forecast.

## Output format

1. **Snapshot** — company, commodity, reporting period and currency, one-line result.
2. **Metrics table** — the metrics above, current vs pcp vs change, each row source-tagged.
3. **Operational read** — production and unit cost vs guidance; what drove the move.
4. **Balance sheet** — net debt / EBITDA, capex, dividend and cover.
5. **Sensitivity & risk** — commodity and currency exposure; project/▢SA-specific risks
   (Eskom/electricity, logistics/Transnet, regulatory, community/ESG).
6. **Provenance appendix** — per-figure document + page; Sources list with deep links.

## Peer comparison (when asked to compare miners)

Build one row per company with the metrics as columns; add a ratios/red-flags view
(leverage, margin trend, FCF yield). Only compare like reporting periods — flag any
mismatch explicitly. This is also the structure exported to Excel via the `xlsx` skill.

## SA-specific notes

- **Tax:** SA corporate rate 27%; note royalty regime and any deferred-tax swings.
- **Dual listings:** Anglo/BHP/Glencore also trade in London/Sydney — state which results
  set is referenced and the currency.
- **Operational risk:** electricity (Eskom), bulk logistics (Transnet), water, safety
  stoppages and community/ESG factors materially affect SA miners — surface them when disclosed.
