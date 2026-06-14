# Creating Skills — A Guide for Non-Developers

A skill is a markdown document that teaches Claude how to do a recurring task
your way. No code, no software background needed. **If you can write an email
briefing a junior analyst, you can write a skill.**

---

## Anatomy of a skill

One folder, one file: `.claude/skills/<skill-name>/SKILL.md`

```markdown
---
name: ic-meeting-note-formatter
description: Formats rough IC meeting notes into AllWeather's standard
  minutes. Use when the user pastes meeting notes or mentions "IC notes".
---

# IC Meeting Note Formatter

You convert rough notes from investment committee meetings into the fund's
standard minute format.

## Output format
1. Header — date, attendees, chair
2. Decisions taken — numbered, one sentence each
3. Actions — table: Action | Owner | Due date
...

## Rules
- Never invent content; mark ambiguity "[unclear — confirm]".
- Keep numbers exactly as written.
```

Three parts, all plain English:

| Part | What it does | Tip |
|---|---|---|
| `description` | How Claude decides *when* to use the skill | List the trigger phrases people actually say |
| Instructions | *What* to do — format, steps, structure | Write it like a brief to a new team member |
| Rules | Guardrails — what never to do | Be explicit: "never invent", "always cite" |

## The easy way: ask Claude to write it

You don't even write the file yourself. In Cowork, describe what you want:

> "Create a skill that formats rough IC meeting notes into our standard
> minutes: decisions taken, actions with owners and dates, dissenting views,
> and follow-ups. It must never invent content."

Claude scaffolds the folder and file. Then:

1. **Read it.** Open the generated SKILL.md — it's just a document. Edit any
   line you'd phrase differently.
2. **Test it.** Paste real (or realistic) input and check the output.
3. **Refine it.** Spot something wrong? Tell Claude: "also flag any company in
   a closed period" — it updates the skill.

That loop — generate, test, refine — is the whole craft.

## What makes a good skill

- **One job.** "Format IC notes" beats "handle all meeting admin".
- **A described trigger.** The `description` is how it fires automatically —
  include the casual phrasings ("tidy up my notes", "format these minutes").
- **Your standards encoded.** The JSE analyst skill carries the fund's rules:
  numbers are sacred, cite every figure, always show prior-period comparisons.
  Skills are how house style becomes automatic.
- **Honest guardrails.** Tell it what to do when information is missing
  ("write TBC and flag it") so it never papers over gaps.

## Ideas for your first skill

Broker-note summariser (your format, your fields) · results-day checklist
runner · SENS announcement triager · model-update changelog writer · client
letter first-drafter · compliance pre-clearance checker.

## Reference: the live demo from the presentation

The IC note formatter built on stage, plus the messy input notes used, are in
`presentation/fallback/demo-b-skill/` and
`presentation/fallback/demo-b-rough-ic-notes.txt`. Copy the pattern.
