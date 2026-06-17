# JSE Research System — Guide

This Cowork space is a self-building research system for JSE-listed companies. It was
assembled by merging two earlier configurations into one coherent setup:

- A 5-skill self-building system (discovery → download → manifest → skill-builder →
  analyst), and
- A richer analyst brief (ROIC, valuation multiples, SA-specific context, compliance),

which were folded together. The analyst skill now carries the combined analytical depth;
the duplicate single-skill analysis file from the second config was retired to avoid
overlap.

## What it does

1. **Finds and downloads** annual reports, interims, trading statements, SENS, investor
   presentations and press releases from JSE companies' IR sites, SENS, and the public
   web — fully automatically (web fetch + browser automation; no dragging, dropping, or
   manual downloads).
2. **Self-builds.** The first time a company is mentioned, it explores the IR site once,
   then writes a company-specific skill that records exactly where everything lives so
   future lookups are instant. If a site changes and a download breaks, it re-discovers
   and updates that skill automatically.
3. **Analyses conversationally.** The PM just names a company; the right skills chain to
   find the documents, save them locally, and produce a sourced, standardised analysis.

## How a request flows

When the PM says *"Tell me about Capitec"*:

1. `CLAUDE.md` loads (identity, principles, structure).
2. Manifest check — Capitec not tracked yet.
3. `jse-company-discovery` — finds the IR site, maps document locations, writes
   `companies/capitec/company.json`, creates the folders.
4. `jse-skill-builder` — writes `.claude/skills/jse-capitec/SKILL.md` encoding what it
   learned.
5. `jse-report-downloader` — downloads the latest annual report, interims, trading
   statements and presentations; updates the manifest. Runs as a **dispatcher skill that
   delegates to the `jse-report-downloader` subagent**, so the browser/HTTP/validation
   work stays in an isolated context.
6. `jse-analyst` — reads the PDFs, extracts banking-sector metrics (NII, credit loss
   ratio, CET1, ROE, NIM, cost-to-income), compares periods, adds valuation context,
   flags risks, summarises commentary. Runs as a **dispatcher skill** that confirms the
   output format with you, then **delegates the heavy reading/analysis to the
   `jse-analyst` subagent**.
7. The PM gets a complete analysis — no searching, downloading, or uploading.

**Next time** Capitec is mentioned, the manifest shows it's tracked, the Capitec skill
loads, and questions are answered from local documents instantly. "Check for updates"
fetches only what's new since `last_checked`.

## Layout

```
JSE Financial Reports/          ← research root
├── CLAUDE.md                   ← always-loaded identity, principles, workflow
├── README.md                   ← this file
├── manifest.json               ← master index (starts empty)
├── .claude/
│   ├── agents/                 ← subagents (isolated contexts)
│   │   ├── jse-report-downloader.md   ← heavy download worker
│   │   └── jse-analyst.md             ← heavy analysis worker
│   └── skills/                 ← skills auto-load from here
│       ├── jse-company-discovery/
│       ├── jse-report-downloader/  ← thin dispatcher → subagent
│       ├── jse-manifest-manager/
│       ├── jse-skill-builder/
│       ├── jse-analyst/  (+ references/sector-metrics.md)  ← thin dispatcher → subagent
│       └── jse-<company>/          ← auto-generated, one per company
└── companies/                  ← downloaded documents + company.json per company
```

## Optional connectors

The system works on its own. If you connect SharePoint/Google Drive (internal models),
Outlook/Gmail (broker notes), Bloomberg (pricing/consensus), or Slack/Teams (alerts), the
skills will use them automatically; if absent, they're skipped silently.

## Getting started

Just name a company in chat — e.g. *"Tell me about Shoprite"* or *"Pull MTN's latest
numbers"*. To set up recurring coverage, add names to the `watchlist` in `manifest.json`
(or say "add Capitec to the watchlist") and ask for a "morning update" to refresh them.

## Compliance

Output is for informational purposes, not investment advice. Share prices obtained via
search may be delayed (no live JSE feed). The system flags closed/prohibited dealing
periods and garbled PDF extractions rather than presenting suspect numbers.
