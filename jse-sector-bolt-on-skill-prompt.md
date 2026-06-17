# Prompt — Design a JSE sector "bolt-on" lens skill

> Paste everything below the line into a Cowork session in the **JSE Financial Reports**
> space and let the **skill-creator** skill run it. It builds one sector "bolt-on" lens
> at a time, starting with **mining**. The structure is reusable: to add another sector,
> rerun it and swap the worked example.

---

## Role and goal

You are building a **sector bolt-on lens** for this fund's JSE equity-research system. The
general analyst (`jse-analyst`) already produces a full, sourced financial report for **any**
company. A bolt-on adds **only what is special about one industry** — it never repeats what
the general skill already does.

Build the lens for the **Mining** sector now, as the first instance of a **reusable pattern**.
Output the real file: `.claude/skills/jse-sector-mining/SKILL.md`.

Work in this order: (1) read the existing skills to lock the contract, (2) write the lens to
the template below using the mining content provided, (3) run the Definition-of-Done check.

## Step 1 — Read first, then build to the EXISTING interface (do not invent a new one)

This hook is already specified in the codebase — your job is to make it real, not redesign it.
Before writing anything, read:

- `.claude/agents/jse-analyst.md` — especially **Step 3** (sector-lens routing), **Step 4**
  (valuation), **Step 6** (risk scan), and the "Sector lens skills (bolt-ons)" note.
- `.claude/skills/jse-analyst/references/sector-metrics.md` — the **bare metric list** per
  sector (incl. Mining). **You must NOT restate this list** in the lens.
- `CLAUDE.md` — identity, SA context, and formatting rules (ZAR units, bps, dates).

Hard contract the lens must satisfy:

1. **Name & path:** exactly `jse-sector-<icb_sector lowercased>`. Mining → folder
   `.claude/skills/jse-sector-mining/`, file `SKILL.md`.
2. **Routing:** the `jse-analyst` subagent loads it **by exact name via the Skill tool** in
   its Step 3, keyed off the `icb_sector` field in `companies/<slug>/company.json`
   (`icb_sector: "Mining"` → `jse-sector-mining`). It must therefore be invocable by that
   exact name; do not rely on fuzzy chat triggers for the analyst path.
3. **It is a content-bearing knowledge lens — NOT a dispatcher.** Unlike `jse-analyst` and
   `jse-report-downloader`, this is lightweight interpretation knowledge, so it is a **single
   `SKILL.md` with no subagent and no extra tools**. The analyst reads it as a lens.
4. **It augments exactly three analyst steps** — Step 3 (metric interpretation), Step 4
   (valuation lenses), Step 6 (risk flags) — plus a value-drivers framing. It owns no other
   part of the workflow.
5. **Keep the analyst's lens registry consistent.** The analyst notes which lenses are
   "Currently available" — ensure `jse-sector-mining` is listed there (for mining it already
   is; for any future sector, add it).

## Step 2 — The anti-duplication boundary (the whole point of this exercise)

Ownership is strict. If a line could apply to *any* company, it does **not** belong in the lens.

| Lives in… | Owns… |
|---|---|
| `jse-analyst` (general) | The standardised metrics table, the 10-step workflow, the Citation Standard, cross-source reconciliation, the general risk checklist, output formats. |
| `references/sector-metrics.md` (shared) | The **bare primary/secondary metric list** per sector (Mining: AISC, production volumes, reserve & resource statement, realised vs benchmark price, capex/unit, etc.). |
| **The bolt-on lens (what you write)** | **Only:** (a) **value drivers** — the equation of value for the sector; (b) **KPI interpretation** — how to read those metrics, the linkages, what good/bad looks like; (c) **valuation lenses** — which multiples/methods to use and why; (d) **sector-specific risk flags** beyond the general checklist; (e) **SA-specific sector context**. |

Two rules to enforce on yourself:

- **Do not reprint the metric list.** Reference it ("the Mining list in `sector-metrics.md`")
  and interpret it. Listing AISC again = failure.
- **Do not duplicate citation mechanics, the general table, or general risks.** Those bind the
  analyst already; the lens inherits them.

## Step 3 — The reusable template (every `jse-sector-<x>/SKILL.md` uses this skeleton)

```markdown
---
name: jse-sector-<x>
description: >
  <Sector> sector lens for jse-analyst. Loaded BY NAME (Skill tool) when a company's
  company.json has icb_sector "<X>", to add <sector> value drivers, KPI interpretation,
  valuation lenses and risk flags on top of the general analysis. Does not duplicate the
  general metrics table or the bare metric list in references/sector-metrics.md.
---

# <Sector> sector lens (bolt-on for jse-analyst)

## When this applies & what it adds
- Routes from icb_sector "<X>". Loaded by the jse-analyst subagent at Step 3.
- Adds ONLY: value drivers, KPI interpretation (Step 3), valuation lenses (Step 4),
  risk flags (Step 6), SA context. The metric LIST lives in references/sector-metrics.md;
  the general table and citation rules live in jse-analyst. Do not repeat them.

## A. Value drivers — the equation of value for this sector
## B. KPI interpretation (augments analyst Step 3)
## C. Valuation lenses (augments analyst Step 4)
## D. Sector-specific risk flags (augments analyst Step 6)
## E. SA-specific sector context
## F. Common pitfalls / "don't get fooled" (optional)
```

Keep it tight and high-signal — knowledge, not padding. No citation mechanics. Follow
`CLAUDE.md` formatting (ZAR `R'm`/`R'bn`, ratios to 1dp, margins in **bps**, dates `DD Month YYYY`).

## Step 4 — Worked example: fill the mining lens with THIS content

Write `jse-sector-mining/SKILL.md` using the skeleton above and the substance below.

**A. Value drivers.** Equity value ≈ NPV of the life-of-mine (LOM) plan at an assumed price
deck, plus option value on resources not yet in the plan, **less** rehabilitation/closure
liabilities and net debt. The P&L is driven by: realised commodity price (mostly USD) ×
volume × grade × recovery, **less** unit cost (AISC). For SA-cost / USD-revenue producers the
**ZAR/USD rate** is a core swing factor (a weaker rand helps margins — the "rand hedge"). Three
structural levers: position on the **global cost curve** (survivability), **reserve life &
replacement** (longevity), and **capital intensity** of sustaining vs growing output.

**B. KPI interpretation** (read on top of the Mining list in `sector-metrics.md`; do not
relist it):

- **AISC vs realised price** → unit margin. AISC **percentile on the cost curve** signals who
  survives a downturn. Confirm the AISC **definition** used (World Gold Council standard vs
  company-defined) before comparing peers.
- **Realised vs benchmark price** → product quality, timing, **provisional-pricing**
  adjustments, and any hedge book. Reconcile to the hedge note.
- **Reserve & resource statement (SAMREC; JORC for ASX/LSE dual-listings)** → **reserve life**
  = reserves ÷ annual production; **reserve replacement ratio** < 100% = a depleting asset.
  Distinguish genuine discovery from resource→reserve reclassification at a higher price deck.
- **Grade & recovery** → primary unit-cost drivers; structural grade decline is a cost
  headwind that volume cannot offset indefinitely.
- **Sustaining (SIB) vs growth capex split** → underspending SIB flatters near-term FCF but
  stores up production risk; check against depletion.
- **Cash build/(drawdown) & gearing (ND/EBITDA)** → in mining this usually **drives the
  dividend**, since many SA miners pay on a net-cash or gearing target / a % of FCF rather
  than a fixed payout.

**C. Valuation lenses** (augment analyst Step 4):

- **P/NAV is the primary mining lens** — price ÷ NPV of the LOM DCF. State the **discount
  rate and price deck**; the answer is meaningless without them.
- **EV/EBITDA at spot AND at a normalised long-term deck** — single-point multiples mislead
  across the cycle.
- **EV per in-situ resource (oz/tonne)** — for explorers / optionality not in the mine plan.
- **FCF yield at spot vs consensus deck**, and **dividend yield** read against the variable
  payout policy.
- **Commodity-price and ZAR/USD sensitivity tables are essential**, not optional.
- **Pitfall to flag:** trailing **P/E is near-useless at commodity-price extremes** — earnings
  are hyper-cyclical and impairment-laden; prefer P/NAV and through-cycle EV/EBITDA.

**D. Sector-specific risk flags** (beyond the analyst's general Step 6 checklist):

- **Safety / regulatory stoppages:** fatalities and **Section 54/55 stoppages** under the Mine
  Health and Safety Act — a Section 54 can halt a shaft and is materially production-negative
  (very SA-specific).
- **Power:** Eskom load-shedding and electricity-tariff (NERSA) exposure; self-generation plans.
- **Resource nationalism / tenure:** Mining Charter (BEE ownership, the "once empowered, always
  empowered" dispute), MPRDA tenure (mining-right renewals/conversions), and the **state royalty**
  under the Mineral & Petroleum Resources Royalty Act.
- **Environmental:** rehabilitation & closure provisions (adequacy and discount rate), water-use
  licences, **tailings storage facility (TSF)** integrity (post-Brumadinho scrutiny), acid mine
  drainage; **carbon tax** exposure.
- **Social / labour:** Social & Labour Plans (SLPs), community unrest, Section 189
  retrenchments, and **NUM/AMCU** wage cycles / strike risk.
- **Operating / market:** single-asset or deep-level concentration, grade depletion, hedge-book
  mark-to-market, by-product credits, and **country risk** for Africa-exposed names.

**E. SA-specific context.** Reserves/resources reported under **SAMREC** (reconcile to **JORC**
for ASX/LSE dual-listings). **MPRDA + Mining Charter** govern tenure and ownership; a
**state royalty** (Mineral & Petroleum Resources Royalty Act) and **carbon tax** apply. **Eskom/NERSA** power risk is structural. The **rand-hedge**
dynamic means a weaker ZAR generally *helps* SA-cost, USD-revenue producers — state the FX basis.

**F. Pitfalls.** Headline vs normalised earnings often diverge sharply on **impairments** (common
in mining) — reconcile both. "AISC" is not standardised across companies — check the definition.
Reserve statements get **restated when the price deck changes** — distinguish that from real
operational change.

## Step 5 — Definition of Done (run this checklist before finishing)

- [ ] File at `.claude/skills/jse-sector-mining/SKILL.md`, named exactly `jse-sector-mining`.
- [ ] Loadable by `jse-analyst` via the Skill tool by that exact name; `icb_sector: "Mining"`
      routes to it.
- [ ] Contains **only** value drivers, KPI interpretation, valuation lenses, risk flags, and SA
      context — **no** restatement of the general metrics table or the `sector-metrics.md` Mining
      list (cross-check line by line).
- [ ] Explicitly augments analyst **Steps 3, 4, 6**; no citation mechanics duplicated.
- [ ] SA mining nuances present: Section 54, Mining Charter, SAMREC, Eskom/NERSA, state royalty,
      rehab/TSF, carbon tax.
- [ ] Section skeleton (A–F) is **sector-agnostic** so banking/retail/telco can reuse it.
- [ ] Analyst's "Currently available" lens list stays consistent (mining listed).
- [ ] Follows `CLAUDE.md` formatting; tight, no padding — every line is mining-special.

## Reusing this for another sector

Copy the A–F skeleton, replace the mining substance in Step 4 with that sector's value drivers /
KPI interpretation / valuation lenses / risk flags / SA context, name it
`jse-sector-<icb_sector>`, save under `.claude/skills/`, and add it to the analyst's "Currently
available" lens list. **Leave the bare metric list in `references/sector-metrics.md`** — the lens
only ever interprets it.
