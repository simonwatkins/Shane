# AllWeather Capital — Claude Cowork Setup Guide

For IT and pilot analysts. Covers everything needed to reproduce the JSE research
workspace, from zero to a working install. Expect roughly half a day including
SharePoint admin steps.

---

## Part 1 — Install & access (IT, ~1 hour)

1. **Licences.** Claude Team or Enterprise plan with Cowork access (research
   preview). Confirm current availability and tier requirements at
   support.claude.com before purchasing.
2. **Install the Claude desktop app** on each pilot user's machine and sign in
   with the work account.
3. **Org settings.** In Admin settings → Capabilities, the org owner enables
   Cowork and network (web) access for the relevant users.

## Part 2 — Workspace folder (pilot analyst, ~30 min)

4. **Create the working folder.** This becomes the research root — folder tree,
   config, and skills all live inside it (see Part 4 for the SharePoint-backed
   location).
5. **Grant folder access.** In Cowork, select the folder when prompted. This is a
   one-time permission; Claude can then read and write only within it.
6. **Add `CLAUDE.md`** at the folder root. This is the workspace's "employee
   handbook": identity, principles (numbers are sacred, source everything),
   folder structure, formatting rules. Copy the JSE workspace version as a
   starting point.
7. **Skills location — important gotcha.** Skills must live in
   `.claude/skills/<skill-name>/SKILL.md` *inside the working folder*. Anywhere
   else and they will not auto-trigger.
8. **Copy the tooling.** `tools/manifest.py` maintains the document index
   (`manifest.json`). The manifest is generated — never edit it by hand; run
   `python3 tools/manifest.py rebuild` after changes.

## Part 3 — Permissions & browser (pilot analyst, ~20 min)

9. **Permission prompts.** On first use, Claude asks before reading/writing
   files, running commands, and fetching web pages. Approve within the working
   folder; you can grant per-action or per-session. Nothing happens silently.
10. **Web access.** Used for finding IR pages and SENS announcements. Controlled
    by the org setting from step 3.
11. **Claude in Chrome extension.** Some IR websites block simple fetches; the
    Chrome extension lets Claude drive a real, visible browser tab to navigate
    and download. Install from the Chrome Web Store, sign in, and connect when
    Cowork prompts. You can watch every action it takes.

## Part 4 — SharePoint integration (IT + org admin, ~1–2 hours)

12. **Create a dedicated SharePoint document library** (e.g. "JSE Research") in
    the research site.
13. **Sync it locally with OneDrive** on the pilot analyst's machine, and use the
    synced folder as the Cowork working folder (Part 2). Result: Claude works on
    local files, the whole team sees the same documents in SharePoint, and
    versioning/retention come free.
    - **Caveat:** avoid two people running Cowork against the same library at
      once — OneDrive sync conflicts. Start with one designated writer; others
      read via SharePoint.
14. **Connect the SharePoint MCP connector** (admin consent flow in Microsoft
    365). This lets Claude *read* the fund's existing research under
    `/Research/[Company Name]/` directly, in addition to the synced library.
15. **Optional next connectors:** Outlook (broker research and results emails),
    Teams (flagging material findings to the channel).

## Part 5 — Verification (pilot analyst, ~15 min)

16. **Smoke test 1:** ask "what companies are we tracking?" — confirm Claude
    reads the manifest.
17. **Smoke test 2:** ask "tell me about Shoprite" — confirm the company skill
    triggers and the analysis cites document names and pages.
18. **Smoke test 3:** paste rough meeting notes — confirm the IC note formatter
    skill triggers.
19. Run `python3 tools/manifest.py validate` — no errors expected.

## Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| Skills never trigger | Wrong location | Move to `.claude/skills/<name>/SKILL.md` inside the working folder |
| Downloads fail on an IR site | Site blocks plain fetches | Ensure Chrome extension is connected; Claude will fall back to browser automation |
| manifest.json looks wrong | Hand-edited or stale | Never hand-edit; `python3 tools/manifest.py rebuild` then `validate` |
| Claude can't see a file | Outside the working folder | Move/copy it in, or connect the relevant MCP connector |
| SharePoint files missing locally | OneDrive set to online-only | Mark the library folder "Always keep on this device" |
