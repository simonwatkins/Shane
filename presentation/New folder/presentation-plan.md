# AllWeather Capital — Claude Adoption Presentation: Plan

**Runtime:** 45 minutes (incl. Q&A) · **Audience:** Mixed — PMs, analysts, leadership
**Presenter:** Simon Watkins · **Status:** Draft for review

---

## 1. Title options

1. **"An All-Weather Analyst: Bringing Claude into the Investment Process"** ← recommended (plays on the fund name; positions Claude as a team member, not a tool)
2. "From Chat to Colleague: Claude at AllWeather Capital"
3. "Research That Finds Itself: Automating JSE Coverage with Claude"

Subtitle for any of the above: *Milestone 1 — the JSE research workspace, live.*

---

## 2. Objectives (what the room should leave believing)

1. Claude + Cowork can do real, multi-step research work autonomously — not just chat.
2. The JSE workspace is working **today**: documents found, downloaded, catalogued, analysed, with sources cited.
3. Skills are plain-English instruction files. **Anyone on the team can write one** — proven live.
4. There is a concrete, low-risk adoption path that fits AllWeather's SharePoint estate.

---

## 3. Run of show (45:00)

| Time | Segment | Notes |
|---|---|---|
| 00:00–02:00 | Title, hook, agenda | Hook: "This morning I asked one sentence and got an IC-ready analysis. I'll do it again live, right now." |
| 02:00–04:00 | **Kick off Demo A** (background analysis) | Type the prompt on screen, hit enter, *leave it running*. One sentence of setup, no waiting. |
| 04:00–10:00 | Claude 101 | Claude / Cowork / skills / MCP in plain English (slides 3–6) |
| 10:00–18:00 | Case study: the JSE research workspace | Architecture, the 5 skills, what got automated, glance at Demo A progress mid-section ("it's downloaded the interims, now reading them") |
| 18:00–26:00 | **Demo B: build a skill live** | Skill-creation demystified — audience watches a non-developer artefact get written and trigger |
| 26:00–30:00 | **Demo A results** | Return to the finished analysis; walk through metrics, sourcing, pcp comparisons |
| 30:00–36:00 | Adoption roadmap for AllWeather | Setup steps, SharePoint integration, milestones, governance |
| 36:00–45:00 | Q&A | 9 min; have backup slides ready (security, cost, accuracy, compliance) |

**Key staging trick:** Demo A starts at minute 2 and is harvested at minute 26 — ~24 minutes of background runtime, nobody watches a spinner.

---

## 4. Slide-by-slide outline (~18 slides + backups)

**1. Title** — title, date, presenter.
**2. Agenda + the promise** — "By minute 30 you'll have watched Claude analyse a JSE company end-to-end and watched me build a new capability for it in five minutes."
**3. What Claude is** — frontier AI model; chat vs *agentic* use; can read, write, browse, run code. One diagram, no jargon.
**4. What Cowork is** — Claude with hands: a folder on your machine it can read/write, a browser it can drive, connectors to your systems. Screenshot of this workspace.
**5. What a skill is** — a markdown file of instructions Claude loads when relevant. Show 10 lines of a real SKILL.md on screen. Tagline: *"If you can write an email to a junior analyst, you can write a skill."*
**6. What MCP connectors are** — plugs into SharePoint, Outlook, Slack. One logo diagram. Sets up the roadmap section.
**7. Case study intro** — the problem: JSE coverage = hours of finding/downloading/re-keying before analysis starts.
**8. Workspace architecture** — folder tree + the 5 skills (discovery → downloader → manifest → skill-builder → analyst). Simple pipeline diagram.
**9. What it does in practice** — "Tell me about Capitec" → onboard, fetch, analyse, cite. 10 companies currently tracked (Shoprite, Clicks, Dis-Chem, Woolworths, Naspers, FirstRand, Richemont, Mr Price, SPAR, Reinet).
**10. Principles that make it trustworthy** — numbers are sacred; source everything; flag estimates; always pcp comparisons. *This is the slide for leadership.*
**11. Demo B intro: skills demystified** — anatomy of a skill (name, description, instructions). No code.
**12. (Live) Build the skill** — switch to Cowork, build "IC Meeting Note Formatter" live (see §5.2). Slide is just the prompt being used, as a safety net.
**13. (Live) Trigger the skill** — paste rough meeting notes, watch formatted output.
**14. Demo A results walkthrough** — switch back to the finished analysis.
**15. Adoption roadmap** — 4 milestones (see §7).
**16. Setup: what it actually takes** — condensed bootstrapping checklist (see §6). Message: half a day of IT setup, not a project.
**17. SharePoint integration** — working folder in a synced SharePoint library + SharePoint MCP for existing research (see §6.4).
**18. Ask + next steps** — nominate 2 pilot analysts, approve SharePoint library, schedule week-2 follow-up. Then Q&A.

**Backup slides:** B1 Security & data handling (folder-scoped access, permission prompts, no training on your data — verify current Anthropic policy before presenting). B2 Cost (subscription tiers). B3 Accuracy & compliance (informational-only framing, source citation, human review). B4 Full bootstrapping guide (the detailed version of slide 16).

---

## 5. Demo scripts

### 5.1 Demo A — background analysis (kicked off minute 2, harvested minute 26)

Use a company already in the workspace (reliable). Best candidates: **Clicks Group** (6 docs — richest) or **Clicks vs Dis-Chem comparison** (more impressive, both tracked).

**Prompt (pre-written, typed live):**
> "Compare Clicks and Dis-Chem's latest results: revenue, HEPS, margins and returns vs pcp, with your view on relative momentum. Cite every number. Save as a markdown note in analyst-notes."

**Contingencies:**
- Rehearse the exact prompt beforehand and time it; if it finishes early, fine — it waits.
- Fallback: a pre-generated copy of the same output saved in `presentation/fallback/`, plus screenshots of it running.
- Don't include live web fetching in Demo A (venue Wi-Fi risk); local-document analysis only.

### 5.2 Demo B — build a skill live (~8 min)

**Skill:** "IC Meeting Note Formatter" — takes rough bullet notes from an investment committee meeting and produces the fund's standard minute format (decisions, actions w/ owners, dissents, follow-ups).

**Script:**
1. (1 min) Show an existing SKILL.md — "it's just a document."
2. (3 min) In Cowork, say: *"Create a skill that formats rough IC meeting notes into our standard minutes: decisions taken, actions with owners and dates, dissenting views, follow-ups for next meeting."* Watch it scaffold the skill.
3. (1 min) Open the generated SKILL.md, read 5 lines aloud — plain English.
4. (3 min) Paste pre-prepared rough notes (have these ready — 10 messy bullets from a fictional IC meeting), watch the skill trigger and format them.

**Why this skill:** relatable to everyone in the room, zero market-data dependency, fast to run, obviously non-technical.

**Contingency:** pre-built copy of the finished skill in `presentation/fallback/` to paste in if generation misfires.

### 5.3 Rehearsal checklist

- [ ] Full dry run with timer, twice
- [ ] Demo A prompt tested on this machine same week
- [ ] Fallback outputs generated and saved
- [ ] Rough IC notes prepared for Demo B
- [ ] Second monitor/screen-share layout tested (slides + Cowork side-by-side or fast app-switch)
- [ ] Notifications off, font size up

---

## 6. Bootstrapping content (feeds slide 16 + the written setup guide)

Document what you actually did, as the step-by-step guide:

### 6.1 Install & access
1. Claude desktop app installed; appropriate plan with Cowork access (research preview).
2. Sign-in with work account; org admin enables Cowork / network access (Admin settings → Capabilities for Team/Enterprise).

### 6.2 Workspace setup
3. Create the working folder; grant Cowork folder access when prompted (one-time permission).
4. Add `CLAUDE.md` (identity, principles, structure) — the "employee handbook" for the workspace.
5. Skills live in `.claude/skills/` **inside the working folder** (path gotcha — wrong location = skills don't trigger).
6. Manifest tooling (`tools/manifest.py`) — generated index, never hand-edited.

### 6.3 Permissions & browser
7. File read/write permission prompts — what to expect, what to approve.
8. Web fetch/search enablement.
9. **Claude in Chrome extension** install + connect — needed for IR sites that block plain fetches; show the permission model (Claude acts in a visible browser tab).

### 6.4 SharePoint (AllWeather-specific)
10. Connect the **SharePoint MCP connector** (org admin consent flow).
11. **Recommended architecture:** the research root lives in a dedicated SharePoint document library, synced locally via OneDrive → Cowork gets file access, the whole team sees the same documents in SharePoint, versioning/retention come free. SharePoint MCP additionally used to *read* existing internal research under `/Research/[Company]/`.
    - Tradeoff to state honestly: OneDrive sync conflicts are possible if two people run Cowork against the same library simultaneously — start with one writer (pilot analyst) and everyone else reading via SharePoint.
12. Optional connectors next: Outlook (broker research), Teams (flagging findings).

### 6.5 Verification
13. Smoke test: "tell me about [tracked company]" → confirm skills trigger, manifest reads, analysis cites sources.

---

## 7. Adoption roadmap (slide 15)

| Milestone | Scope | Timeframe |
|---|---|---|
| **M1 — JSE research workspace** (this demo) | Workspace deployed to SharePoint library; 2 pilot analysts; watchlist = current coverage | Weeks 1–2 |
| **M2 — Connect the estate** | SharePoint MCP for internal models/notes; Outlook for broker research; team-wide read access | Weeks 3–6 |
| **M3 — Automate the rhythm** | Scheduled morning updates (SENS/new docs across watchlist); IC pack generation (PPTX/XLSX); custom skills written by analysts themselves | Weeks 6–10 |
| **M4 — Firm-wide rollout** | Beyond research: ops, compliance checks, IR monitoring; skill library governance; training session for all staff | Quarter 2 |

Each milestone gets its own one-page step-by-step guide (deliverables below).

---

## 8. Q&A prep (anticipate these)

- **Security/confidentiality:** folder-scoped access, explicit permission prompts, enterprise data policies → backup slide B1; verify current policy at docs.claude.com before the session.
- **Hallucination risk:** the CLAUDE.md principles (numbers sacred, source everything, flag estimates) + human review; show a cited output.
- **Cost:** backup slide B2.
- **"Will this replace analysts?"** — frame: it removes retrieval/re-keying, analysts keep judgement; the skill demo shows analysts *gaining* a capability.
- **Compliance:** informational-only outputs, no advice; dealing-period flags built into config.
- **"What happens when a website changes?"** — skill-builder self-heals: re-discovers and updates the company skill.

---

## 9. Deliverables to build next (after plan sign-off)

1. **PPTX deck** (~18 slides + 4 backups) — fund-appropriate clean design.
2. **Setup guide** (docx/md): the §6 bootstrapping steps, screenshots, written for IT + pilot analysts.
3. **Skill-creation guide** (md, 2 pages): anatomy of a skill + the Demo B walkthrough as a recipe.
4. **Demo fallback pack:** pre-generated Demo A output, pre-built Demo B skill, rough IC notes for pasting.
5. **One-page roadmap handout** for leadership.

---

## Open questions for Simon

1. Confirm Demo A company: Clicks vs Dis-Chem comparison, or single-name?
2. Does AllWeather have a slide template/brand to follow?
3. Who is the org admin for the SharePoint MCP consent flow — worth pre-arranging before M1?
4. Date of the session (affects "latest results" freshness for Demo A)?
