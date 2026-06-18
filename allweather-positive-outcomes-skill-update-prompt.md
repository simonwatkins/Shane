# Prompt — customise jse-analyst for AllWeather ("Investing in positive outcomes")

> Paste the block below as a new message in this Cowork space to apply the change.

---

Update the **jse-analyst** skill so every analysis reflects AllWeather's investment
philosophy — our tagline is **"Investing in positive outcomes."** Edit BOTH files that
make up the skill: the dispatcher `.claude/skills/jse-analyst/SKILL.md` and the worker
`.claude/agents/jse-analyst.md` (the subagent holds the analysis method and output
structure, so most edits land there). Keep both in sync.

## Non-negotiable guardrail (read first)
This must SHARPEN analysis, not bias it. The positive-outcomes lens is **informational
only**: it is a distinct, clearly-labelled section that **never changes, gates, or
tie-breaks the investment conclusion**, and never overrides a financial figure. The
existing principles — *numbers are sacred*, *source everything*, *prior-period context*,
*evenhandedness*, the four-mechanism Citation Standard — remain fully binding and take
precedence in any conflict. Do not let the tagline leak into the financial sections or the
executive summary's verdict.

## What "positive outcomes" means here (two pillars)
Assess exactly two pillars, reported on their own terms (a **pure outcomes lens** — do NOT
filter to only financially-material items, and leave financial-materiality reads to the
standard financial sections):
1. **ESG / impact** — environmental, social and governance factors and measurable
   real-world impact (e.g. emissions/intensity and targets, energy/water, transition
   capex, governance quality, B-BBEE/transformation where disclosed).
2. **Stakeholder outcomes** — outcomes for customers, employees, communities and suppliers
   (e.g. employment and wages, safety, training, supplier/community programmes, product
   access/affordability), beyond shareholders.

## Add a dedicated output section
In the subagent's Step 8 output structure, insert a new standalone section
**"Positive Outcomes Assessment (ESG & Stakeholder)"** — placed AFTER the financial,
valuation, reconciliation and risk sections and clearly marked as a non-financial lens, so
it visibly sits apart from the investment view. The section must:
- Cover both pillars above, each with the company's disclosed evidence.
- Open with one line tying it to AllWeather's philosophy, then stay disciplined and
  evidence-bound (no marketing prose).
- **State thin or negative evidence plainly — never spin.** If a company discloses little,
  say "Not disclosed"; if it scores poorly, say so directly. Never manufacture a positive
  narrative to fit the tagline. Where disclosure is missing, also log it as a coverage gap
  to backfill.
- Keep AllWeather's house judgement labelled as judgement (e.g. "AllWeather view:").

## Evidence bar
Cite to a filing/SENS/page wherever the evidence exists, exactly like the rest of the
Citation Standard (ref-key + page, provenance appendix row, full-URL source). Where no
hard figure exists, **reasoned qualitative commentary is allowed but must be explicitly
marked as judgement**, not presented as a sourced fact. Estimates remain tagged `(e)` with
working. This section is bound by the same provenance discipline as every other section.

## Quick mode
The section is **always present in every mode**. In **quick mode** produce a **condensed
2–3 line** version drawn only from filings already on disk (no extra web searches; respect
the existing tool-call budget and the annual-results download floor). In **deep mode**
produce the full assessment. Update the quick-mode guidance so the worker reads the
sustainability/ESG and stakeholder/social sections of filings it is already opening rather
than adding new reads where avoidable.

## Also update
- The subagent's **Definition of Done — Citation Checklist**: add a line confirming the
  Positive Outcomes Assessment is present, evidence-bound, and that negatives/gaps are
  stated plainly.
- The **dispatcher SKILL.md** and the subagent's front-matter `description`: add a brief
  note that AllWeather analyses include a labelled, informational ESG & stakeholder
  positive-outcomes assessment that does not affect the financial conclusion.
- The output-format notes (docx/xlsx/pptx) so the new section renders correctly in each
  format (its own heading in docx; its own block/sheet where relevant).

## Verify before finishing
After editing, re-read both files end-to-end and confirm: (a) the financial conclusion is
untouched and still independent; (b) the guardrail wording is present and unambiguous;
(c) the two pillars, evidence bar, no-spin rule, quick-mode condensation and checklist
line are all in place; (d) nothing contradicts the existing CLAUDE.md principles. Report
what changed and quote the new guardrail paragraph back to me.
