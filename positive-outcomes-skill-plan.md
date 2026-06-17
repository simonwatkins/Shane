# Plan — Customising the JSE Analyst skill for AllWeather

**Tagline:** *"Investing in positive outcomes."*
**Date:** 2026-06-17
**Status:** Draft for approval (3 residual decisions open)

## Confirmed design choices

| Decision | Choice |
|---|---|
| What "positive outcomes" means | **Real-world impact lens** — assess the company's actual outcomes for SA society/environment |
| How it interacts with the analysis | **Dedicated separate section** — objective core (metrics, valuation, risk, reconciliation) stays untouched |
| Whether it changes conclusions | **Soft** — surface tensions where financials and impact diverge; **no pass/fail verdict** |
| Definition of "positive" | **SA-specific outcomes** framework (below) |
| Section name | **"Positive-Outcomes Assessment"** |
| Quick mode | **Included as a condensed version** — built only from filings already on disk, zero extra web searches, gaps logged as coverage gaps |

## Design principle

The objective core of the skill stays completely untouched. The philosophy lives in one
walled-off section, bound by the **same Citation Standard** as everything else: every impact
claim is sourced to a filing/page or marked "Not disclosed." No unsourced positive spin —
that is the safeguard that stops the tagline from becoming marketing inside a research note.

## What gets added: a "Positive-Outcomes Assessment" section

Inserted as **section 8.5** (after Management Commentary, before Questions for Further
Research). SA-anchored framework — six categories, each with sourced indicators:

| Category | Indicators (sourced or "Not disclosed") |
|---|---|
| **Employment** | Total headcount & net change YoY; youth/learnership intake; minimum wage vs living-wage benchmark |
| **Transformation / B-BBEE** | B-BBEE contributor level; black & black-women ownership %; management/board diversity; ESD spend |
| **Financial inclusion / access** | Sector-relevant reach (unbanked served, affordable products, rural/township footprint) |
| **Infrastructure & energy resilience** | Own/renewable generation, load-shedding mitigation, water stewardship |
| **Local economic linkage** | Local procurement %, SMME/supplier development, localisation |
| **Environmental footprint** | Scope 1/2/3 disclosure & emissions-intensity trend; water; just-transition exposure |

Closing **"Tensions & Trade-offs"** subsection (the "soft, no verdict" choice in action):
explicitly names where financials and impact pull apart — e.g. HEPS growth driven by
headcount cuts, margin gains from offshoring, coal cash flows vs transition risk. It states
the tension and stops. No rating, no mandate verdict.

The section defers to existing **sector lenses** where they overlap (e.g. mining's
water/transition flags) rather than duplicating them.

## Where the changes physically go

1. **`.claude/agents/jse-analyst.md`** — add the new analysis step + Tensions subsection, and
   add impact-source priority (integrated/sustainability report, B-BBEE certificate) to the
   read order. The real method lives here.
2. **`references/positive-outcomes-framework.md`** — new reference file holding the full
   category/indicator definitions (keeps the subagent prompt lean; same pattern as
   `sector-metrics.md`).
3. **`jse-analyst/SKILL.md`** (dispatcher) — one-line note so the section is part of the
   standard deliverable.

### Quick-mode behaviour (confirmed)

In quick runs the **Positive-Outcomes Assessment** is still produced, but **condensed**:
built only from filings already on disk, **zero extra web searches** (respects the quick-mode
web cap), with any unavailable indicators logged as coverage gaps for a later deep run to
backfill — rather than skipped entirely. Quick means narrower scope, not lower rigour: the
Citation Standard still binds.

## Residual decision (one open — needed before implementation)

1. **Document sourcing.** Impact data lives in the Integrated Annual Report / sustainability
   report / B-BBEE certificate, which the downloader may not currently fetch. **Add these to
   the standard download set?** (Recommended: yes — otherwise the section is mostly "Not
   disclosed.")

## Next step

On a yes / adjustments to the one remaining decision, implement the three file edits above.
