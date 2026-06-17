---
name: jse-analyst
description: >
  Analyses downloaded financial documents for JSE-listed companies. Use this skill
  whenever the user asks to analyse, review, summarise, compare, or evaluate a
  company's financial results. Also trigger when the user asks "how did [company]
  do", "what are [company]'s numbers", "analyse [company]'s results", "compare
  [company] to last year", "flag risks for [company]", "prepare IC notes for
  [company]", "pull [company]'s numbers", or any question about a company's financial
  performance, metrics, valuation, or outlook. Trigger for HEPS extraction, SA-specific
  metrics, and reporting-period comparisons. This skill works on documents already
  downloaded to the local workspace — it reads from companies/[slug]/ and never searches
  the web during analysis. If documents are missing, it triggers jse-report-downloader
  first. Output is held to a strict, verifiable Citation Standard: a Source tag on every
  table row, inline page-level footnotes, a per-figure Provenance & Verification appendix,
  and a Sources list of full deep-link URLs.
---

# JSE Analyst (dispatcher)

This skill is a **thin dispatcher**. The actual analysis runs in the **`jse-analyst`
subagent** (`.claude/agents/jse-analyst.md`) so that the heavy reading — full annual
reports, interim PDFs, presentations and sidecars, plus figure extraction and
reconciliation — happens in an **isolated context window** and leaves the main thread free.
The full method (source-of-truth gate, the 10 analysis steps, the sector-lens routing, the
four-mechanism Citation Standard, the Definition-of-Done checklist) lives in the subagent's
system prompt. Do NOT do the analysis inline here.

Your job in the main context is the small amount of work the subagent **cannot** do —
namely talk to the user — and then orchestrate.

## Step 0 — Confirm the deliverable format (MUST happen here, before delegating)

A subagent cannot ask the user anything mid-run, so the output format must be settled in
the main context first. **Unless the user already stated a format in their request**, ask
via the **AskUserQuestion** tool. Offer at minimum:
- **Word document (.docx)** — formatted report saved to `companies/[slug]/analyst-notes/`.
- **Answer in the chat** — concise prose + tables, no file.

Where relevant also offer **Excel (.xlsx)** (data table to model further) and
**PowerPoint (.pptx)** (IC slide). If the user already named a format, skip the question
and honour it.

## Step 1 — Delegate to the subagent

Call the **Task** tool with `subagent_type: "jse-analyst"` and a prompt containing:
- the company **slug**;
- the **analysis request** (full results review / specific metric / period comparison /
  IC notes / risk scan);
- the **output format chosen in Step 0** (`docx` / `chat` / `xlsx` / `pptx`).
- the execution **`mode`** (`deep` | `quick`) and an explicit **`tool_call_budget`** for
  the financials/outlook/KPI extraction — **6 in quick mode, 8 in deep** (the subagent caps
  itself to whichever is tighter; see its "Tool-call budget" section). When you fan out
  several workers, give each its own budget so the slow financials leg cannot stall the run.

The subagent enforces the source-of-truth gate, reads the local originals + sidecars,
loads the matching `jse-sector-<x>` lens, extracts the standardised metrics, does
valuation / reconciliation / risk / commentary, and produces the deliverable under the
Citation Standard.

## Step 2 — Handle the subagent's return

- **If it returns `MISSING_DOCUMENTS`** (sources not on disk): run
  **`jse-report-downloader`** (which itself delegates to its download subagent) to fetch
  the named documents, then **re-invoke the `jse-analyst` subagent** with the same brief.
  Do not try to analyse from un-saved web text — that gate exists for a reason.
- **If it returns a completed analysis:**
  - file deliverable (`docx`/`xlsx`/`pptx`) → share it with **present_files** and add a
    short chat summary (period, headline metrics + direction, risk flags, guidance check);
  - `chat` deliverable → relay the prose + tables.

## Why a subagent (not inline)

Reading several multi-hundred-page PDFs to extract and reconcile figures is the single
biggest consumer of context in this workspace — and it used to run in the same thread that
also had to hold the downloader's output. Isolating analysis in its own subagent means the
main thread keeps only the question, the format choice, and the finished deliverable. The
subagent inherits this project's `CLAUDE.md`, so "numbers