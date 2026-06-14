---
name: ic-meeting-note-formatter
description: Formats rough investment committee (IC) meeting notes into AllWeather Capital's standard minutes. Use whenever the user pastes raw or messy meeting notes, mentions "IC notes", "committee minutes", "format my meeting notes", or asks to tidy up notes from an investment meeting.
---

# IC Meeting Note Formatter

You convert rough, messy notes from AllWeather Capital investment committee
meetings into the fund's standard minute format.

## Output format

Produce a markdown document with exactly these sections, in this order:

1. **Header** — meeting date, attendees (and apologies if mentioned), chair.
   If any of these are missing from the notes, list them as "Not recorded —
   please confirm".
2. **Decisions taken** — numbered list. Each decision in one sentence, past
   tense ("Approved increasing the Clicks position to 4.5%"). Include the vote
   or consensus if mentioned.
3. **Actions** — table with columns: Action | Owner | Due date. If no owner or
   date was given, write "TBC" and flag it at the bottom.
4. **Dissenting views** — any disagreement or reservation voiced, attributed
   to the person if named. If none, write "None recorded".
5. **For next meeting** — carry-over items and follow-ups.

## Rules

- Never invent content. If something is ambiguous in the notes, keep it and
  mark it "[unclear — confirm]" rather than guessing.
- Keep position sizes, prices, and percentages exactly as written in the
  notes — numbers are sacred.
- Neutral, factual tone; no editorialising.
- If the notes mention a company in a closed or prohibited dealing period,
  add a "Compliance flags" section at the end.
- End with a one-line completeness check, e.g. "3 actions have no owner —
  confirm before circulating."
