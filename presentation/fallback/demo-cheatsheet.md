# Demo cheat sheet (presenter only)

## Demo A — kick off at ~minute 2

Paste exactly:

> Compare Clicks and Dis-Chem's latest results: revenue, HEPS, margins and returns vs pcp, with your view on relative momentum. Cite every number. Save as a markdown note in analyst-notes.

- Leave it running. Glance at progress once mid-case-study (~minute 14).
- Harvest at ~minute 26.
- **If it fails:** open `fallback/demo-a-clicks-vs-dischem.md` and walk through it ("here's the same prompt run this morning").
- Talking points from the fallback run: Clicks H1 FY2026 turnover +7.4% to R24,872.2m, diluted HEPS +8.1%; Dis-Chem FY2026 revenue +9.3% to R42,825.8m but HEPS −17.3% on ecosystem spend. Period misalignment caveat (6m vs 12m, both to 28 Feb 2026) — Claude flags this itself, which is a good trust moment.

## Demo B — skill build at ~minute 18

Step 1 — show an existing SKILL.md (use jse-analyst, first ~10 lines).

Step 2 — paste exactly:

> Create a skill that formats rough IC meeting notes into our standard minutes: decisions taken, actions with owners and dates, dissenting views, and follow-ups for next meeting. It must never invent content and must keep numbers exactly as written.

Step 3 — open the generated SKILL.md, read 5 lines aloud.

Step 4 — paste the contents of `fallback/demo-b-rough-ic-notes.txt` with: "format these notes from Wednesday's IC".

- Expected wow-moments: the Richemont closed-period line should surface as a compliance flag; missing action owners get flagged.
- **If generation misfires:** copy `fallback/demo-b-skill/` into `.claude/skills/ic-meeting-note-formatter/` and continue from Step 3.

## Pre-flight (day before)

- [ ] Run Demo A prompt end-to-end on this machine; note runtime
- [ ] Confirm fallback files open
- [ ] Notifications off, display scaling/font up, Wi-Fi checked
- [ ] Slides + Cowork window switch rehearsed
