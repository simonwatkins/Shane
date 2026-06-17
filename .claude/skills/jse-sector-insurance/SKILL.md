---
name: jse-sector-insurance
description: >
  Sector-analysis lens for South African insurers (life, short-term/P&C and composite), loaded
  on top of jse-analyst to add insurance-specific depth. Use whenever the user analyses, reviews,
  compares or asks about a JSE-listed insurer or its results — e.g. Discovery, Sanlam, Old Mutual,
  Momentum Group, OUTsurance, Santam, Clientèle, Sanlam-Allianz. Also trigger on words like
  insurer, insurance, life, short-term, P&C, embedded value, EV, VNB, value of new business,
  ROEV, combined ratio, claims ratio, loss ratio, expense ratio, persistency, lapses, solvency,
  SCR, SAM, IFRS 17, CSM, contractual service margin, underwriting, float, Vitality. This skill
  adds the insurance equation of value, EV/VNB and combined-ratio interpretation, the right
  valuation lenses (P/EV, appraisal value), insurance risk flags and the SA IFRS 17 / SAM regime.
  It does NOT restate the general metrics table, the Citation Standard, SA macro context, the bare
  metric list in references/sector-metrics.md, or the workflow — those are inherited from jse-analyst.
---

# JSE Sector Lens — Insurance (South Africa)

A **bolt-on lens for `jse-analyst`**. It does not run on its own and it does not repeat the
general engine — it supplies only what is distinctive about analysing an insurer.

## Inheritance contract (read first)

`jse-analyst` owns everything universal and you MUST NOT restate it here: the general metrics
table, HEPS extraction, prior-period comparison discipline, the Citation Standard and Provenance
appendix, the 12-point general risk scan, SA macro/tax/BEE context, the workflow, and the
output-format rules. The **bare insurance metric list** lives in `references/sector-metrics.md`
(Insurance) — **do not reprint it; interpret it.**

This skill is the **interpretation layer**. Apply it inside the `jse-analyst` workflow:

- **Step 3 (metrics):** after the general table, add the insurance KPIs below and *read* them.
- **Step 4 (valuation):** use the insurance valuation lenses below; suppress the multiples flagged.
- **Step 6 (risk scan):** add the insurance-specific flags below to the general checklist.

Pair with the company skill if one exists (e.g. `jse-discovery`). Inherit all sourcing rules —
every figure still carries a `Source` tag and provenance entry per the Citation Standard.

> **An insurer breaks the general template, and the model differs by type.** EBITDA/EV(enterprise)/
> net debt/FCF are meaningless; revenue is not "turnover". **Terminology trap: "EV" here means
> Embedded Value, never enterprise value.** Pick the right engine — life vs short-term vs composite.

## Scope — when this applies

ICB Industry: **Financials → Life Insurance / Non-life Insurance**. Major JSE names (verified Jun 2026):

| Type | Names |
|---|---|
| Composite / shared-value | **Discovery** (Health, Life, Invest, **Discovery Bank**, UK Vitality, Ping An Health JV) |
| Large diversified life | **Sanlam** (+ **SanlamAllianz** pan-African JV), **Old Mutual** (+ **OM Bank**), **Momentum Group** (ex-Momentum Metropolitan) |
| Short-term / P&C | **Santam** (largest SA short-term), **OUTsurance Group** (incl. Youi Australia) |
| Niche / other | Clientèle, Sygnia (asset manager), African-exposed cell captives (Guardrisk within Momentum) |

Encode every time:

1. **Which engine?** Life → embedded value + VNB. Short-term → combined ratio + float. Composite →
   **sum-of-the-parts**. Using the wrong one is the classic error.
2. **Geography & currency.** Old Mutual (SA + Africa), Sanlam (**SanlamAllianz** Africa JV is
   material), Discovery (SA + UK + China JV). State the reporting currency and give ZAR.

## 1. Value drivers — the equation of value (by type)

**Life insurer:** value ≈ **Embedded Value (EV)** + the franchise to write profitable new business.
EV = adjusted net worth (shareholder capital) **+** value of in-force (VIF — PV of future profits on
existing policies, net of the cost of capital). The growth engine is **Value of New Business (VNB)**
and its **margin** (VNB ÷ PV of new-business premiums). So life value = a *stock* (EV) + a *flow*
(VNB, capitalised). Earnings are **"experience vs assumptions"**: actual mortality/morbidity, lapses
and expenses better than the actuarial basis create positive **experience variances**; **basis
(assumption) changes** also flow through.

**Short-term / P&C insurer:** value ≈ **underwriting profit + investment return on float**.
Underwriting profit is set by the **combined ratio = claims (loss) ratio + expense ratio** — below
100% is an underwriting profit; the **float** (premiums held before claims are paid) earns an
investment return. Reserve adequacy underpins it all.

**Composite (Discovery, Sanlam, Old Mutual, Momentum):** a **sum-of-the-parts** — life EV +
short-term combined-ratio business + asset management (AUM × fee margin) + banking (Discovery Bank /
OM Bank) + health/Vitality + Africa/EM. Value each part on its own metric.

Universal levers across all types: **new-business volume & margin, persistency, mortality/morbidity
experience, expenses, investment return, and capital/solvency efficiency.**

## 2. KPIs and how to read them

Add these to the general table and interpret direction — do not just list them.

| KPI | How to read it | What a move signals |
|---|---|---|
| **VNB & VNB margin** | The life growth engine; margin = mix/pricing/cost quality | Volume-led VNB at *falling* margin is lower quality than a margin-led rise. Check the discount-rate/economic basis. |
| **Embedded value & ROEV** | EV is the life "book"; ROEV = EV earnings ÷ opening EV (the ROE analogue) | Decompose ROEV into VNB + expected unwind + **experience variances** + **assumption changes**. A big slug from assumption changes (not operating) is lower quality. |
| **Combined ratio (short-term)** | Split into claims (loss) and expense ratios | <100% = underwriting profit. Flattered by **prior-year reserve releases** or a benign CAT year = not sustainable — strip them. |
| **Persistency / lapses** | The quietest, deadliest life metric | Rising lapses destroy VIF (future profit walks out) and flag affordability stress — amplified by two-pot withdrawals. |
| **SAM solvency cover (SCR)** | The insurer's CET1 analogue, vs board target range | Above target funds dividends; drifting to the floor = capital concern / dividend risk. |
| **CSM & CSM release (IFRS 17)** | The new on-balance-sheet store of unearned future profit | CSM *building* (new business) vs *releasing* (earned) shows whether the future-profit reservoir fills or drains. IFRS 17 defers profit, so earnings lag VNB. |
| **Expense & experience variances** | Operating performance vs the basis | Results from operating experience beat results from basis changes — prize the former. |

## 3. Valuation methodology

Use the lens that matches the engine; flag the ones that mislead.

- **Life: Price-to-Embedded-Value (P/EV) and appraisal value — PRIMARY.** SA life insurers still
  publish **Group EV** (Sanlam reports **Group Equity Value, GEV**) alongside IFRS 17; the share
  trades as a multiple of EV (0.9× = a 10% discount). **Appraisal value = EV + a multiple of VNB**
  capitalises the new-business franchise. **Always state the risk-discount rate** — P/EV is
  meaningless without it.
- **Short-term: P/E and P/B with the combined ratio as the quality gauge.** A structurally sub-95%
  combined-ratio insurer (OUTsurance; Santam in good years) earns a premium; value on *normalised*
  underwriting + investment income.
- **Composite: sum-of-the-parts** — life on P/EV, short-term on combined ratio/P/E, asset management
  on P/AUM or P/E, banking on P/B, health/Vitality on earnings. Discovery is best read SOTP given the
  emerging Bank and Vitality franchises.
- **Distinguish IFRS, normalised/headline, and cash/EV earnings.** Dividends are paid from **cash** —
  under IFRS 17 the gap between IFRS profit and cash/EV generation matters; track it.
- **ROEV (life) and group ROE vs COE** — the value-creation test.
- **SUPPRESS / do not use: EV/EBITDA (and the word "EV" in the enterprise sense), Net debt/EBITDA,
  FCF yield, EBITDA margin.** Trailing P/E alone is distorted by investment-market swings and basis
  changes — pair it with EV/combined-ratio metrics.

## 4. Sector-specific risk flags (extend jse-analyst Step 6)

- **Reserve adequacy / IBNR** — under-reserving (short-term) or a weak life basis hides losses; watch
  reserve releases propping the combined ratio and adverse prior-year development.
- **Assumption / basis changes** — mortality, morbidity, lapse, discount-rate and expense bases. A
  swing into earnings from **basis changes** (vs experience) is a quality and credibility flag.
- **Persistency / lapse spike** — affordability-driven lapses (two-pot, consumer stress) erode VIF.
- **Catastrophe / weather & reinsurance** — SA floods, hail and fire (e.g. KZN floods) and the **cost
  and adequacy of reinsurance** (Santam especially); a rising climate-loss trend.
- **Investment / market & ALM risk** — equity, credit and rate exposure of shareholder *and*
  policyholder funds; SA-bond concentration; asset-liability mismatch.
- **Solvency (SAM) cover** trending to the target floor; **capital fungibility** across the group.
- **IFRS 17 comparability** — on transition **Sanlam and Momentum saw equity rise / liabilities fall,
  while Discovery and Old Mutual (which had recognised profit more aggressively) saw equity fall /
  liabilities rise** — so cross-insurer "profit" comparisons must be on a consistent basis.
- **New-venture losses** — **Discovery Bank** and **OM Bank** (loss-making to ~2028) drag otherwise
  profitable groups; separate them. New-business **strain** (cash cost of writing new policies) too.
- **Conduct / regulatory** — FSCA conduct (TCF, commission reform), Prudential Authority, and — for
  Discovery Health — the **Council for Medical Schemes** (the medical scheme is member-owned, *not* a
  shareholder asset; the administrator earns the fee).

## 5. Accounting & regulatory regime (insurance-specific)

- **IFRS 17 (effective 1 Jan 2023) — the dominant change.** Insurance contracts carry a **Contractual
  Service Margin (CSM)** that defers profit and releases it as service is provided (**no day-one
  gain**), plus a **Risk Adjustment (RA)** for non-financial risk. The **CSM is a new store of
  value**; earnings are smoother but less tied to cash/EV — analyse CSM movement, RA and the
  coverage-unit release pattern. Comparatives were restated on transition.
- **Embedded Value supplementary reporting** — SA life insurers still publish **EV / Group Equity
  Value with VNB, ROEV and full economic-assumption sensitivities**: despite IFRS 17 this remains the
  primary *value* lens. Read the sensitivity tables (discount rate, equity, lapses).
- **SAM (Solvency Assessment & Management)** — SA's risk-based regime (Solvency II analogue): **SCR /
  MCR**, eligible **own funds**, and the **SCR cover ratio** vs the board target.
- **Twin Peaks** — Prudential Authority (SARB) + **FSCA** conduct; **Council for Medical Schemes** for
  health; King IV; JSE Listings.
- **Currency / geography** — Old Mutual (SA + Africa), Sanlam (**SanlamAllianz** Africa JV), Momentum
  Group (ex-Momentum Metropolitan), Discovery (SA + UK Vitality + Ping An Health China JV). State
  currency; give ZAR.

## 6. Primary documents & cadence (for jse-report-downloader)

- **Interim & annual results** — booklet + AFS. **June year-ends are common** (Discovery: June YE);
  confirm each insurer's date (Sanlam, Old Mutual, Momentum, OUTsurance, Santam).
- **The Embedded Value report / supplementary EV disclosure** — VNB, ROEV, EV sensitivities. **The
  single most important value document for a life insurer — always fetch it.**
- **IFRS 17 disclosures / CSM movement analysis** in the AFS.
- **New-business and operational updates** (life APE/PVNBP; short-term gross written premium).
- **Solvency & Financial Condition Report (SFCR)** where published; analyst data packs.
- Trading statements (HEPS ranges), AGM, capital-markets days.

Record in each insurer's `company.json` where the IR site publishes the **EV report and SFCR**, so
the downloader fetches them, not just the integrated report.

## 7. Five questions an insurance specialist asks management

1. What was **VNB and the VNB margin**, and how much of EV/CSM growth was *new business* vs expected
   unwind vs **assumption/basis changes**?
2. How are **persistency and lapses** trending given consumer stress and two-pot — and the VIF hit?
3. (Short-term) What is the **combined ratio ex-CAT and ex-prior-year reserve releases**, and is
   reserving adequate?
4. What is **SAM solvency cover vs target**, capital fungibility across the group, and the
   dividend/buyback capacity?
5. What are the **new-venture losses** (Discovery Bank / OM Bank / offshore) and the breakeven path —
   and how should we reconcile IFRS 17 earnings with cash/EV generation?

## Sub-sector nuances

- **Composite / shared-value — Discovery**: Vitality behavioural model across **Health** (administers
  the member-owned Discovery Health Medical Scheme — *scheme ≠ shareholder asset*; Council for Medical
  Schemes-regulated), **Life**, **Invest**, **Discovery Bank** (*at operational breakeven before
  new-business acquisition cost*), plus **UK Vitality** and the **Ping An Health (China)** JV. Read
  SOTP; watch new-business strain and the Bank's ramp. June year-end.
- **Large diversified life**: **Sanlam** — largest SA insurer; reports **Group Equity Value** with
  **non-covered** businesses ~60% of GEV (investment management, credit, **SanlamAllianz** pan-African
  JV). **Old Mutual** — SA + Africa; has launched **OM Bank** (loss to ~2028). **Momentum Group**
  (ex-Momentum Metropolitan; CEO Jeanette Marais) — Momentum (advised), Metropolitan (mass), Guardrisk
  (cell captive) and Momentum Investments.
- **Short-term / P&C**: **Santam** — largest SA short-term insurer; CAT/weather and reinsurance-cost
  sensitive; judge on the combined ratio. **OUTsurance Group** — direct model (plus **Youi** Australia
  and OUTsurance Life/Ireland); structurally low combined ratio and high ROE; the sector's strong
  recent performer.

## Last updated

2026-06-17 — constituents and IFRS 17 transition effects verified via web search (KPMG Insurance
Survey 2025; IFRS 17 equity impact differing by insurer; OM Bank break-even ~2028; Discovery Bank
operational breakeven; Sanlam GEV composition). Re-verify names, year-ends and the EV basis before
relying on the trigger list.
