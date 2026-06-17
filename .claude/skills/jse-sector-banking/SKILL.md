---
name: jse-sector-banking
description: >
  Sector-analysis lens for South African banks, loaded on top of jse-analyst to add
  banking-specific depth. Use whenever the user analyses, reviews, compares or asks about a
  JSE-listed bank or its results — e.g. Standard Bank, FirstRand (FNB / RMB / WesBank), Absa,
  Nedbank, Capitec, Investec, African Bank, TymeBank, Discovery Bank, OM Bank. Also trigger
  on words like bank, banking, NII, net interest income, NIM, net interest margin, endowment,
  credit loss ratio, CLR, impairments, cost-to-income, jaws, CET1, RWA, advances, deposits,
  IFRS 9, ECL, Stage 3, ROE vs COE, Pillar 3, two-pot, FATF grey-listing. This skill adds the
  banking equation of value, KPI interpretation, the correct valuation lenses (P/B vs ROE),
  banking-specific risk flags and the SA prudential/conduct regime. It does NOT restate the
  general metrics table, the Citation Standard, SA macro context, the bare metric list in
  references/sector-metrics.md, or the analysis workflow — those are inherited from jse-analyst.
---

# JSE Sector Lens — Banking (South Africa)

A **bolt-on lens for `jse-analyst`**. It does not run on its own and it does not repeat the
general engine — it supplies only what is distinctive about analysing a bank.

## Inheritance contract (read first)

`jse-analyst` owns everything universal and you MUST NOT restate it here: the general metrics
table, HEPS extraction, prior-period comparison discipline, the Citation Standard and Provenance
appendix, the 12-point general risk scan, SA macro/tax/BEE context, the workflow, and the
output-format rules. The **bare banking metric list** lives in `references/sector-metrics.md`
(Banking) — **do not reprint it; interpret it.**

This skill is the **interpretation layer**. Apply it inside the `jse-analyst` workflow:

- **Step 3 (metrics):** after the general table, add the banking KPIs below and *read* them —
  the linkages, what good/bad looks like — rather than tabulating them.
- **Step 4 (valuation):** use the banking valuation lenses below; suppress the multiples flagged.
- **Step 6 (risk scan):** add the banking-specific flags below to the general checklist.

Pair with the company skill if one exists (e.g. `jse-capitec`). Inherit all sourcing rules —
every figure still carries a `Source` tag and provenance entry per the `jse-analyst` Citation
Standard.

> **A bank breaks the general template.** EBITDA, EV, net debt and free cash flow are
> meaningless for a bank (debt and deposits are raw material, not financing). Suppress those
> rows of the general table and replace them with the framework below.

## Scope — when this applies

ICB Industry: **Financials → Banks**. Major JSE-listed names (the PwC "big six", verified Jun 2026):

| Tier | Names |
|---|---|
| Big universal banks | Standard Bank Group, FirstRand (FNB / RMB / WesBank), Absa Group, Nedbank Group |
| High-ROE retail bank | Capitec Bank Holdings |
| Specialist / dual-listed | Investec (plc + Ltd; banking + Wealth & Investment) |
| Challenger / digital / new | African Bank, TymeBank, Discovery Bank (inside Discovery), **OM Bank** (Old Mutual, launched late 2025) |

Two things to encode every time:

1. **Year-ends differ — line up like with like.** Standard Bank, FirstRand, Absa and Nedbank are
   **December** year-ends (results ~March & August); **Capitec is February** (results ~September &
   April); **Investec is March**. Never compare an interim to a full year by accident.
2. **Currency & listing vary.** **Investec reports in GBP** (dual-listed Investec plc/LSE +
   Investec Ltd/JSE) — state the currency and give a ZAR equivalent. Standard Bank consolidates a
   large **Africa Regions** footprint and a strategic **ICBC** relationship; FirstRand has a UK
   business (Aldermore/MotoNovo). State which entity's numbers you cite.

## 1. Value drivers — what actually moves the P&L

A bank is a **leveraged, regulated spread-and-fee business**. Equity (~6–8% of assets) is thin,
so small swings in margin or credit move ROE hard. The value equation is the warranted-multiple
identity:

> Justified **P/B ≈ (ROE − g) ÷ (COE − g)** — a bank creates value only when **ROE clears its
> cost of equity (COE)**; the size of that spread, on a growing book, sets the multiple.

The earnings engine:

- **Net interest income (NII) = average interest-earning assets × NIM.** NIM is driven heavily by
  the **endowment effect** — capital and non-rate-paying transactional deposits earn the repo
  rate, so a **higher SARB repo rate widens NII** and a cutting cycle compresses it. Always split
  an NII move into *endowment* (rates) vs *balance-sheet growth* vs *margin/mix management*.
- **Non-interest revenue (NIR)** — transactional fees, card, insurance, trading. Capital-light and
  annuity-like; a rising NIR/total-income ratio is usually a quality-of-earnings positive.
- **Operating jaws** = revenue growth − cost growth. Positive jaws → falling cost-to-income →
  operating leverage. Negative jaws are an early warning.
- **Impairments = credit loss ratio (CLR) × advances** — the through-the-cycle swing factor.
- Sequence: NII + NIR − opex = **pre-provision operating profit (PPOP)**; − impairments − tax =
  earnings. PPOP is the franchise's shock-absorber against the credit charge.

Three structural levers: **endowment / rate sensitivity** (cyclical), **credit-cycle position**
(survivability), and **capital generation & return** (CET1 headroom → dividends + buybacks).

## 2. KPIs and how to read them

Add these to the general table and interpret direction — do not just list them.

| KPI | How to read it | What a move signals |
|---|---|---|
| **NIM + endowment** | Decompose into endowment (repo), mix and pricing | Rising repo lifts NIM mechanically; a stable *endowment-adjusted* margin shows real franchise pricing power. A NIM fall in a cutting cycle is not necessarily weakness. |
| **CLR vs through-the-cycle (TTC) range** | Each bank guides a TTC band (e.g. Standard Bank ~70–100 bps; Absa ~75–100 bps). Read reported CLR against *its own* band and the stage mix | Above range = stress (usually unsecured / SA consumer). *Below* range late-cycle can mean under-provisioning or large overlays releasing — probe sustainability. |
| **Cost-to-income (CTI) & jaws** | SA majors target low-50s%; Capitec structurally lower | Falling CTI on positive jaws = operating leverage. Watch IT/cyber build and amortisation inflating "good" cost. |
| **CET1 vs board target range** | Compare to the bank's *target*, not just the SARB minimum + buffers (Pillar 2A, conservation, D-SIB) | CET1 **above** target funds ordinary + special dividends and buybacks; **below** target = capital-build/raise risk and dividend pressure. |
| **ROE vs COE** | The master ratio. SA bank COE is high (~15–18%) given the sovereign yield | ROE − COE > 0 creates value and earns a premium P/B; sub-COE divisions trade below book. Sector ROE ≈ 15% (2025) → ≈ 16% (2026e). |
| **Advances & deposit growth** | Quality over quantity; watch the secured (mortgage/VAF) vs **unsecured** mix and loan-to-deposit funding | Fast unsecured growth *into* a weak consumer is a red flag, not a positive. |
| **Stage 3 (NPLs) & coverage** | IFRS 9 staging; watch Stage 2→3 migration and coverage by stage | Rising migration + thinning coverage = deterioration ahead of the CLR catching up. |

Capitec-specific: it runs the sector's highest ROE and lowest CTI — judge it on **active-client
growth, NIR per client and unsecured-book CLR**, not on the universal-bank template.

## 3. Valuation methodology

Use the lenses banks actually trade on; flag the ones that mislead.

- **P/B (price-to-book) read against ROE — PRIMARY.** Banks trade on a multiple of tangible book
  set by **sustainable ROE relative to COE**: justified P/B ≈ (ROE − g)/(COE − g). Plot ROE vs P/B
  across the big six — a high-ROE bank (Capitec) earns a premium P/B; a chronically sub-COE bank
  trades at a discount to book for a reason. Use **tangible** NAV (strip goodwill/intangibles).
- **P/E on normalised earnings — secondary.** Useful but distorted by the credit cycle: a *low*
  trailing P/E at the top of the cycle (impairments suppressed) is a classic value trap; pair it
  with mid-cycle CLR.
- **Dividend yield + total capital return.** SA banks run target **payout ranges** (broadly
  ~50–60% of earnings) plus **buybacks/specials when CET1 is above target** — so capital-return
  capacity keys off CET1 headroom, not just reported payout. More stable than a miner's dividend.
- **ROE − COE spread / economic profit and book-value growth** — the value-creation engine; track
  it by division.
- **Sum-of-the-parts** for the groups: Standard Bank (SA bank + Africa Regions + ICBCS +
  insurance/asset management), FirstRand (FNB + RMB + WesBank + UK), Investec (SA Ltd + UK plc +
  Wealth & Investment). Value the parts on their own ROE/multiples.
- **SUPPRESS / do not use: EV/EBITDA, Net debt/EBITDA, FCF yield, EBITDA margin.** A bank has no
  meaningful EV or EBITDA — deposits and wholesale debt are *raw material*, not capital structure.
  Quoting "net debt" on a bank is an error. Drop those general-table rows entirely.

## 4. Sector-specific risk flags (extend jse-analyst Step 6)

For a bank, "impairment" means **credit** (captured via the CLR), not the goodwill write-down the
general scan assumes — read Step 6 through that lens, and add:

- **Asset quality / credit migration** — Stage 2→3 migration, unsecured-book growth into a weak
  consumer, restructured/rescheduled loans, single-name and commercial-real-estate concentrations,
  and the **size and direction of IFRS 9 post-model overlays** (large judgemental adjustments can
  flatter or smooth the CLR — probe them).
- **Capital & liquidity** — CET1 drifting toward the target floor; LCR/NSFR trends; reliance on
  wholesale funding; AT1/Tier 2 refinancing and call risk.
- **Sovereign–bank "doom loop"** — SA banks hold large **SA government bond** portfolios, so a
  sovereign downgrade raises COE *and* marks down the bond book. The **SARB repo path** drives the
  endowment both ways.
- **Two-pot retirement system (since 1 Sep 2024)** — withdrawal flows affect deposits, transaction
  volumes and arrears; quantify the period impact.
- **Regulatory / conduct** — National Credit Act affordability & reckless-lending rules; **FSCA**
  conduct/TCF and Ombud rulings; **FATF grey-listing** (SA grey-listed Feb 2023 — track exit
  progress; it raises correspondent-banking and compliance cost); Basel 3.1 implementation by the
  SARB **Prudential Authority**.
- **Operational / cyber** — digital-channel outages, fraud, third-party/cloud concentration, and
  load-shedding resilience of branches/ATMs/data centres.
- **Africa / EM exposure** — currency convertibility and cash-repatriation, hyperinflation
  accounting (IAS 29) in some subsidiaries, and country/sovereign risk (widest at Standard Bank;
  ICBC shareholder + ICBCS trading-JV linkage to China).
- **Conduct provisions & litigation; model risk** (IFRS 9 ECL model changes can move earnings).

## 5. Accounting & regulatory regime (banking-specific)

- **IFRS 9** — expected-credit-loss (ECL) model: staging (1/2/3), significant-increase-in-credit-
  risk (SICR) triggers, and **management overlays / post-model adjustments**. Compare **coverage by
  stage** year-on-year; overlays are the single most judgemental line — reconcile movements.
- **Basel III (SARB Prudential Authority)** — CET1 / Tier 1 / Total capital, the leverage ratio,
  **LCR and NSFR**, RWA density, and **D-SIB** buffers. Banks set internal target ranges *above* the
  regulatory minimum + buffers; analyse against the target, not the floor.
- **Normalised vs IFRS earnings** — several banks present a **normalised** view (e.g. for group
  treasury/BEE-share schemes); reconcile normalised headline earnings to IFRS attributable, and use
  **HEPS** consistently. Under SA rules headline earnings already strip certain capital items.
- **Twin Peaks** regulation: Prudential Authority (in the SARB) for safety/soundness + **FSCA** for
  market conduct; plus King IV and JSE Listings Requirements.
- **Currency** — most are ZAR reporters; **Investec reports in GBP** — state it and give ZAR.

## 6. Primary documents & cadence (for jse-report-downloader)

- **Interim & annual results** — booklet + financial statements (mind the differing year-ends above).
- **Results presentation and the analyst "data pack" / results booklet** — divisional NII, NIR,
  CLR, CTI, NIM, RWA and capital tables. **This pack is the richest single source — always fetch it.**
- **Pillar 3 / Risk & Capital Management report** — capital, RWA, leverage, liquidity, encumbrance.
- **Pre-close / trading updates and trading statements (SENS)** — voluntary updates and HEPS ranges
  are price-sensitive.
- **Integrated & Pillar 3 annual reports**; AGM; investor/capital-markets days.

Record in each bank's `company.json` where the IR site publishes the **data pack and Pillar 3**, so
the downloader fetches them, not just the annual report.

## 7. Five questions a banking specialist asks management

1. What is the **endowment sensitivity** of NIM to a 100 bps SARB move, and how much of NII growth
   this period was rates (endowment) vs balance-sheet growth vs margin management?
2. Where are we in the **credit cycle** — Stage 2→3 migration, the unsecured/secured mix, and is the
   CLR sustainably within the TTC range or being flattered by overlay releases?
3. What is the **CET1 trajectory versus the board target range**, and the capital-return plan
   (ordinary + special dividend + buyback) given that headroom?
4. What is **ROE versus COE by division**, which businesses earn below COE, and what is the plan to
   fix or exit them?
5. Quantify **two-pot flows, the FATF grey-listing exit path, and SA-sovereign exposure** (bond
   book + COE) — the three SA-specific swing factors.

## Sub-sector nuances

- **Universal banks** (Standard Bank, FirstRand, Absa, Nedbank): diversified NII+NIR with large
  transactional franchises; value **sum-of-the-parts**. Standard Bank has the widest Africa Regions
  and ICBC linkage; FirstRand pairs FNB (retail/commercial), RMB (CIB) and WesBank (VAF) with a UK
  arm; Nedbank is wholesale-weighted with the ETI (Ecobank) associate; Absa is rebuilding its Africa
  story post-Barclays.
- **Capitec**: sector-leading ROE and lowest CTI; retail transactional + unsecured lending, now
  adding **business banking** (ex-Mercantile) and **insurance**; commands a premium P/B — watch the
  unsecured CLR and the move up-market. **February** year-end.
- **Investec**: dual-listed (LSE plc + JSE Ltd), **GBP** reporter; specialist banking + **Wealth &
  Investment**; read the UK and SA businesses separately.
- **Challengers / new entrants**: African Bank (unsecured, restructured legacy), **TymeBank**
  (digital, regional expansion), **Discovery Bank** (behavioural, *reaching operational breakeven
  before new-business acquisition cost* — analysed inside the Discovery group), and **OM Bank**
  (Old Mutual's late-2025 launch; guided **loss-making to ~2028**, needs ~2.5–3m clients to break
  even) — a structural new competitor for Capitec on the low-cost transactional segment.

## Last updated

2026-06-17 — constituents and CLR/ROE guidance verified via web search (PwC Major Banks Analysis
Mar 2026; OM Bank launch and 2028 break-even target; Discovery Bank operational breakeven).
Re-verify names, year-ends and TTC ranges before relying on the trigger list.
