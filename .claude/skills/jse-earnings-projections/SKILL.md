---
name: jse-earnings-projections
description: >
  Builds a charted earnings-PROJECTION workbook for a JSE-listed company, showing how
  revenue, operating profit, headline earnings and dividends track across BULL, NEUTRAL
  and BEAR market scenarios. Use whenever the user asks to "project earnings", "forecast
  [company]", "build a projection", "bull/bear/base case", "scenario earnings", "show
  [company] in different markets", "what if the market turns", or wants charts/graphs of
  forward earnings for a JSE name (Shoprite, SPAR, Capitec, MTN, etc.). All currency
  figures are in millions of rands (R'm). Produces a styled .xlsx with native Excel
  charts. Pairs with jse-analyst (deeper model) and uses the same version-controlled
  assumptions inputs.
---

# JSE Earnings Projections (charted, Bull / Neutral / Bear)

## Purpose

Produce a clean, chart-led Excel workbook that answers one visual question: **how do a
company's earnings track in a bull, neutral or bear market?** It plots four projected
series across the FY anchor and the forward years, for each scenario:

- **Revenue** (R'm)
- **Trading / operating profit** (R'm)
- **Headline earnings** (R'm)
- **Dividend per share** (cents)

Scenarios are auto-ranked into **Bull** (best), **Neutral** and **Bear** (worst) by
projected headline earnings in the final forward year, and colour-coded
green / grey / red throughout the data tables and charts.

**All currency figures are in millions of rands (R'm).** Per-share figures are in cents
(the unit is named in every row/axis label). This rule is non-negotiable.

This is the lighter, visual companion to `jse-analyst` / `tools/build_model.py`: same
inputs, same financial logic, but the deliverable is charts rather than a full live-formula
model. Use this when the user wants to *see* the scenario spread; use `jse-analyst` when
they want the full driver-by-driver model.

## When to Trigger

- "Project / forecast [company]'s earnings", "build an earnings projection"
- "Show [company] in a bull / bear / neutral market", "scenario earnings", "base/bull/bear case"
- "Graph / chart the forward earnings", "what happens to earnings if the market turns"
- Any request for forward-looking earnings **with charts** for a JSE name

If the user instead wants the deep driver model (margins, finance, tax, leverage tab-by-tab),
route to **jse-analyst**. If they want a written note, pair this with **jse-analyst** /
`tools/build_note.py`.

## Inputs (version-controlled - never invent numbers)

The generator reads the SAME source of truth as the rest of the toolkit. It does **not**
create a new one:

- `assumptions/<slug>.json` - the company's FY anchor (**sacred reported actuals**) plus the
  scenario drivers. Supported templates: `retail-owned` (e.g. Shoprite) and
  `retail-wholesale` (e.g. SPAR).
- `macro/latest.json` - shared dated macro context (read only for the Cover context line).

**If `assumptions/<slug>.json` does not exist:** the company isn't set up for scenario work
yet. Do NOT fabricate drivers. Instead:
1. Run the normal chain in the main context - `jse-company-discovery` ->
   `jse-report-downloader` -> `jse-analyst` - so the FY anchor (sacred actuals) and a first
   set of scenario drivers get written to `assumptions/<slug>.json` (mirror the structure of
   `assumptions/shoprite.json` / `assumptions/spar.json`).
2. Then run this skill.

Every forward figure is an analyst estimate and is emitted marked `(e)`; the FY-anchor
figures derive from the cited reported actuals. "Numbers are sacred" still binds.

## Workflow

### Step 1 - Confirm scope (main context, before building)

Confirm with the user (one short question, only if ambiguous):
- Which company / companies (slugs).
- Output: this skill's default deliverable is the `.xlsx`. If they also want a slide or note,
  flag that you'll follow up with `pptx` / `jse-analyst`.

Defaults if unspecified: single company named, `.xlsx`, two forward years as defined in the
assumptions file.

### Step 2 - Ensure inputs exist

Check `assumptions/<slug>.json` for each requested company. If missing, do the onboarding
chain first (see Inputs above). If the user has just published new results, offer to refresh
the anchor/drivers via `jse-analyst` before projecting.

### Step 3 - Generate the workbook

```bash
# single company
python3 tools/build_projection.py <slug> --out "<slug>_earnings_projection.xlsx"

# multiple companies (each gets its own Data + Charts tabs)
python3 tools/build_projection.py <slug1> <slug2> \
    --title "<CODE1> & <CODE2> - Earnings Projections" \
    --out "earnings_projection.xlsx"
```

The workbook contains:
- **Cover** - how to read it, the ranked Bull/Neutral/Bear legend per company, the rationale,
  macro context line, disclaimer and a **Sources** line.
- **`<CODE> Data`** - the four metric tables (R'm / cents), scenarios as rows, periods as columns.
- **`<CODE> Charts`** - four native Excel charts: clustered columns for revenue, operating
  profit and DPS; a line chart for the headline-earnings trajectory. Bull = green,
  Neutral = grey, Bear = red.

### Step 4 - Verify (always)

```bash
python3 tools/verify_deliverable.py "<out>.xlsx"
```

Must report `"ok": true` (zero recalc errors). Spot-check that the FY-anchor headline
earnings ties to the reported HEPS x shares in the anchor block, and that Bull >= Neutral >=
Bear on terminal-year earnings (the generator prints this).

### Step 5 - Deliver

Save the `.xlsx` to the research root (or the user's folder), present it with
`present_files`, and give a one-line read of the spread (e.g. "FY2027e headline earnings
range R8.2bn bear -> R9.2bn bull"). Don't over-explain - the charts speak.

## Notes & conventions

- **Currency is always R'm**; per-share is cents. The axis/row labels state the unit.
- Scenario->stance is by **terminal-year headline earnings**, so it works for any scenario
  keys (A/Base/B, or named cases) - not hard-coded.
- The financial logic mirrors `tools/build_model.py` exactly, so this book and the full model
  never disagree. If you change a template's maths, change it in both.
- To add a company template (beyond retail-owned / retail-wholesale), extend
  `project_company()` in `tools/build_projection.py` and keep it in lock-step with
  `build_model.py`.
- This is deterministic tooling: **generate, never hand-roll** a one-off projection script.
