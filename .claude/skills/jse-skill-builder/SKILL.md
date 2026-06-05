---
name: jse-skill-builder
description: >
  Auto-generates company-specific skills after a new company is onboarded. Use this
  skill whenever jse-company-discovery finishes onboarding a new company, or when the
  user asks to "create a skill for [company]", "build a lookup for [company]",
  "make [company] easier to research", or any variation of creating reusable research
  shortcuts for a specific company. This skill writes a SKILL.md that encodes
  everything we learned during discovery so future interactions with this company
  are instant — Claude never has to re-explore the IR website or guess where
  documents live. Also use to UPDATE a company skill when a website changes and a
  download breaks.
---

# JSE Skill Builder

## Purpose

After discovering a new company, this skill writes a company-specific SKILL.md that
encodes all the knowledge we gathered: where documents live, what the reporting schedule
looks like, which metrics matter for this sector, and how to navigate this company's
particular IR website quirks.

This is the "institutional memory" mechanism. Instead of re-exploring a company's website
every time, we write down what we found and Claude loads it instantly next time.

## When to Trigger

- Automatically after `jse-company-discovery` completes
- When the user asks to create or update a company-specific skill
- When a download fails due to a website change and we need to update the skill

## Workflow

### Step 1: Read company.json

Load all metadata gathered during discovery.

### Step 2: Generate the SKILL.md

Write to `.claude/skills/jse-[company-slug]/SKILL.md` (this path is required for the
skill to auto-trigger in Cowork):

```markdown
---
name: jse-[company-slug]
description: >
  Research skill for [Company Name] ([JSE Code]), a [Sector] company listed on the
  JSE. Use this skill whenever the user mentions [Company Name], [JSE Code],
  [common abbreviations], or asks about [specific products/brands if applicable].
  This skill knows where to find all financial documents, the reporting schedule,
  and the right analytical framework for this company. Also trigger for [list
  well-known subsidiaries or brands].
---

# [Company Name] Research

## Quick Reference
- **JSE Code:** [code]
- **Sector:** [sector]
- **Year-end:** [month]
- **Reporting currency:** [currency]
- **IR Website:** [url]

## Where to Find Documents

### Annual Reports
- **URL:** [url]
- **Navigation:** [e.g. "Click 'Financial Results' in the top nav, then scroll to
  'Annual Financial Statements'"]
- **File format:** PDF, typically named [pattern]
- **Typical publication:** [X weeks after year-end]

### Interim Results
- **URL:** [url]
- **Navigation:** [instructions]
- **Typical publication:** [X weeks after interim date]

### Trading Statements
- **Primary source:** SENS
- **Search pattern:** "[Company] trading statement"
- **Typical timing:** 2-3 weeks before results

### SENS Announcements
- **Company archive:** [url if available]
- **Fallback:** Web search "[Company] SENS [year]"

### Investor Presentations
- **URL:** [url]
- **Notes:** [any specific navigation needed]

## Sector-Specific Metrics
[Pull the primary + secondary metrics for this sector from
.claude/skills/jse-analyst/references/sector-metrics.md]

## Known Quirks
[Anything unusual discovered during exploration:]
- [e.g. "Website uses JavaScript document loader — direct PDF links change each
  reporting period; use browser automation"]
- [e.g. "Reports dual-listed figures in USD on LSE website, ZAR on JSE"]
- [e.g. "Interim results called 'Half-Year Results' not 'Interim'"]

## Reporting Calendar
- **H1 results:** Expected [month], typically published [month + X weeks]
- **FY results:** Expected [month], typically published [month + X weeks]
- **Trading statements:** Usually [X weeks] before results

## Last Updated
[Date this skill was last verified/updated]
```

### Step 3: Install the Skill

Save the generated SKILL.md to `.claude/skills/jse-[company-slug]/SKILL.md`. Cowork picks
up skills from this directory automatically.

### Step 4: Update the Manifest

Record in manifest.json (via jse-manifest-manager) that a skill was generated:

```json
{
  "companies": {
    "shoprite": {
      "skill_generated": true,
      "skill_path": ".claude/skills/jse-shoprite/SKILL.md",
      "skill_last_updated": "2026-06-05T10:00:00Z"
    }
  }
}
```

### Step 5: Report

Tell the user: "Created a research skill for [Company]. Next time you mention [Company]
or [JSE Code], I'll know exactly where to find everything without searching."

## Updating Skills

When a download fails because a website has changed:
1. Re-run discovery for the affected document source
2. Update company.json with new URLs/navigation
3. Regenerate the skill with updated information
4. Note the change in the skill's "Last Updated" and "Known Quirks" sections

## Quality Criteria

A good company skill should mean that:
- Claude can find and download any document type for this company without web searching
- The correct sector-specific metrics are applied automatically
- The reporting calendar is accurate to within 2 weeks
- Any website navigation quirks are documented so downloads don't fail
