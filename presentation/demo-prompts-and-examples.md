# Demo Prompts & Example Library

Everything you'll type on stage, plus a library the audience can take away. Prompts are in
`code blocks` so you can copy them cleanly. **Rehearse from this file; paste, don't type.**

---

## Demo A — background analysis (kick off slide 3, harvest slide 19)

**Setup:** switch to Cowork in the JSE workspace. Paste, hit enter, leave it running.
Local documents only — no live web (don't depend on venue Wi-Fi).

```
Compare Clicks and Dis-Chem's latest results: revenue, HEPS, margins and returns
versus the prior corresponding period, with your view on relative momentum. Cite
every number to its source document and page. Note any difference in reporting
periods. Save the note as markdown in analyst-notes.
```

**One-liner to say as it starts:** *"I've just asked it to compare two retailers' results,
citing every number — we'll come back to it."* Then switch back to slides.

**Harvest (slide 19):** open the saved note. Walk two or three cited figures. Point out it
flagged the **six-vs-twelve-month** mismatch itself.

**Fallback:** `fallback/demo-a-clicks-vs-dischem.md` (pre-generated). Open it and narrate as
if live if anything stalls.

---

## Demo B — build a skill from scratch, live (slides 20–22)

### Step 1 — engage the room (slide 20)
Ask: *"If you were teaching a junior to read a mining result, what would you have them look
at first?"* Take 2–3 answers (you'll hear: production, costs, commodity price, net debt,
dividend). Then say *"let's write exactly that down"* and paste:

```
Create a skill for analysing JSE mining-company results. It should pull, for the
current period and the prior corresponding period: revenue, EBITDA and EBITDA margin,
headline earnings and HEPS, net debt and net-debt-to-EBITDA, free cash flow, and the
dividend. Always show the prior-period comparison and the change. Flag commodity-price
and rand/USD sensitivity. Cite every figure to its document and page. Never invent a
number — write "not disclosed" where it is missing. Save it as a skill in the workspace.
```

### Step 2 — read it back (slide 21)
Open the generated `SKILL.md`. Read 3–4 lines aloud. *"That's the whole thing — it's a
document a person can read."*

### Step 3 — run it
```
Apply the mining-results skill to the latest results we have for a mining company,
and write a short cited analysis.
```
(If no mining docs are downloaded yet, this is fine to show as "it would now go and fetch
them" — or pre-download one miner before the session. See fallback below.)

### Step 4 — the Excel ask (slide 22)
```
Now turn that into a mining peer comparison as a formatted Excel workbook: one row per
company, the metrics as columns, a second tab for ratios and red-flags (leverage,
margin trend), conditional formatting on net-debt-to-EBITDA. Keep every figure cited.
```

### Refinement prompts (show how the loop works, if time)
```
Also flag any company currently in a closed/prohibited dealing period.
```
```
Add a one-line plain-English takeaway under each company.
```

**Fallbacks:**
- Pre-built skill: `fallback/jse-mining/SKILL.md` — paste its contents if live generation misfires.
- Sample workbook: `fallback/mining-peer-comparison-ILLUSTRATIVE.xlsx` — open if the Excel step stalls.

---

## Prompt library — for the audience to take away

Group these on a handout or read a few aloud. They show range without needing a demo.

**Get up to speed on a company**
```
Tell me about Shoprite — latest results, the headline numbers versus the prior period,
and the three things management flagged. Cite your sources.
```

**Compare two names**
```
Compare Mr Price and Woolworths on revenue growth, gross margin and trading density,
latest reported period. Cite every figure and note any period mismatch.
```

**Summarise a document you drop in**
```
Summarise this results PDF in one page: the numbers that moved, why, and what's
changed since last period. Mark anything you're inferring as an estimate.
```

**Find what's new**
```
What SENS announcements have these names published in the last 7 days, and which look
material? List source and date for each.
```

**Draft in house style**
```
Draft an IC one-pager on Capitec from our latest note: thesis, key metrics vs pcp,
risks, and what would change our mind. Informational only, cite everything.
```

**Build the team a capability**
```
Create a skill that turns a results PDF into our standard one-page summary: headline
metrics vs pcp, margin bridge, management guidance, and risk flags. Never invent a
number; cite each one.
```

**Check yourself**
```
Re-read your last answer and list every figure you stated, with the document and page
it came from. Flag any you cannot source.
```

---

## Prompting tips (the 60-second version for the room)

- **Brief it like a junior analyst.** State the goal, the format, and the guardrails.
  Vague in, vague out — most "AI mistakes" are briefing mistakes.
- **One job per ask.** Narrow beats broad. It also keeps the context clean (avoids the
  "dumb zone").
- **Always demand sources.** "Cite every number to document and page" turns a black box
  into something you can spot-check.
- **Give it an honest out.** Tell it to write "not disclosed / TBC" rather than guess.
- **Iterate.** Generate → read → correct in plain English → repeat. That loop *is* the skill.
- **Right tool for the job.** Judgement and drafting → the model. Exact, repeatable maths →
  ask it to use code.

---

## Fallback index (have these open in a window)

| If this breaks… | Open this |
|---|---|
| Demo A doesn't finish | `fallback/demo-a-clicks-vs-dischem.md` |
| Mining skill won't generate | `fallback/jse-mining/SKILL.md` (paste contents) |
| Excel step stalls | `fallback/mining-peer-comparison-ILLUSTRATIVE.xlsx` |
| IC-note demo (if you use the original) | `fallback/demo-b-skill/SKILL.md`, `fallback/demo-b-rough-ic-notes.txt` |
| PowerPoint misbehaves | the PDF export of the deck |
