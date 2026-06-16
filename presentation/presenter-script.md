# An All-Weather Analyst — Presenter Script & Run of Show

**Talk:** Bringing Claude into the investment process · **Runtime:** 45 minutes incl. Q&A
**Presenter:** Simon Watkins · **Deck:** `an-all-weather-analyst-v3.pptx` (37 slides: 29 main + 8 backup)
**Audience:** Mixed — PMs, analysts, leadership at AllWeather

> This is the working script. The deck itself carries a condensed version of these
> notes in each slide's *notes pane* (use Presenter View). This document adds the
> connective narrative, the deeper explainers, the exact facts, and the timing plan.

---

## 1. Director's notes — what I changed and why (read this first)

You gave me a much richer outline than the original deck covered. The original was a
tight 45-minute, demo-led pitch. Your new material — a personal intro, the history of
AI, a limitations/"dumb zone" section, a Copilot comparison, a second live build, and
a data-sourcing section — is **all worth doing**, but together it's ~70–75 minutes of
content. So my job was sequencing and triage, not just adding slides.

**What I added (10 new slides), folded into the existing demo spine:**

- **Intro / Trayport** (slide 2) — credibility + the humility caveat you asked for.
- **How we got here** (slide 4) — System 1 → Agents → Skills → a colleague, in plain English.
- **Trained on everything** (slide 5) — the paradigm-shift reframing (easier, not harder).
- **What it does / where humans stay essential** (slide 9) — answers "will it replace us?".
- **Claude Cowork vs Copilot "Cowork"** (slide 10) — balanced, because leadership is leaning Copilot.
- **What "agentic" means, live** (slide 14) — narrates Demo A while it runs; sets up the dumb zone.
- **Know the limits** + **how we keep it honest** (slides 17–18) — the credibility core.
- **Excel output** (slide 22) and **where the data comes from** (slide 23).
- **What you'll have in your hands** (slide 26) — introduces the take-home guides.
- Plus 2 new **backups**: a Copilot deep-dive and deterministic-vs-non-deterministic.

I **re-skinned** the old "IC-note formatter" live demo into a **mining-results skill →
Excel** build (your call), and **re-pointed** the agenda timings.

**What I deliberately kept lean or moved to backup**, to protect 45 minutes:

- The Copilot bake-off detail → backup slide 28 (touch it for ~90s on the main slide).
- The old setup-detail and one-sentence-flow slides → backups.
- Deterministic-vs-non-deterministic gets one line on slide 18 + a full backup (29),
  rather than its own main slide.

**Your two must-lands** (your answers to me) drove the priorities: *it actually works*
(both demos are protected) and *the shift is real and safe* (the evolution + limitations
spine is now front-and-centre, not buried in Q&A).

**Honest opinion — where you were over-investing, and what was missing:**

- *Over-invested:* trying to teach the full Copilot comparison and a second from-scratch
  build AND a deep skills-anatomy tour. Any two of those fit; all three don't. I kept the
  mining build (highest energy, audience interaction) and made Copilot mostly a backup.
- *Was missing:* an explicit **"why now / why AllWeather"** beat (now the bottom of slide 9
  and the close), and a **safety/credibility** section strong enough for the leadership in
  the room (now slides 13, 17, 18). These are what turn a cool demo into a yes.
- *Watch-out:* you have **two live demos**. That's the single biggest time and risk
  factor. Demo A is de-risked by running in the background with a fallback; Demo B (mining)
  is the one that can over-run. Rehearse it to a hard 6-minute cap.

**Two things to confirm before the day:**

1. **Company name.** The deck says *AllWeather Capital* (matching your original). Your brief
   said *AllWeather Capital*. Tell me which is correct and I'll fix it everywhere.
2. **The 85% Trayport figure.** Public sources say *"over 85% of European utilities'
   derivatives trading"* flows through Trayport (MarketsWiki; trayport.com). Confirm this
   matches Trayport's current approved external wording — and add your **UK retail-energy /
   Automated Trading** specifics on slide 2, which I left for you (I didn't want to assert a
   number I couldn't verify).

---

## 2. Run of show (45:00)

| Time | Slides | Segment | Note |
|---|---|---|---|
| 0:00–0:30 | 1 | Title + the promise | Warm open; thank them for trust |
| 0:30–1:30 | 2 | Who I am (Trayport) | Land the humility line |
| **1:30–2:30** | 3 | **Three objectives** | State the frame; you bookend it on slide 28 |
| **2:30–3:30** | 4 | Agenda — **and kick off Demo A** | Paste prompt, hit enter, **leave it running** |
| 3:30–6:00 | 5–6 | How we got here + the paradigm shift | The "shift is real" beat |
| 6:00–8:30 | 7–9 | What Claude / Cowork / connectors are | Brisk — concept already landed |
| 8:30–11:30 | 10–11 | Helps vs humans · Claude vs Copilot | "Why now"; be even-handed |
| 11:30–15:00 | 12–14 | The workspace I built + trust principles | Glance at Demo A on slide 15 |
| 15:00–16:30 | 15 | What "agentic" means (Demo A running) | Sets up the dumb zone |
| 16:30–18:30 | 16–17 | Skills demystified + a real SKILL.md | "Just a document" |
| 18:30–22:00 | 18–19 | The limits + how we stay honest | The credibility core |
| **22:00–25:00** | 20 | **Harvest Demo A** — cited result | The "it works" moment; take a Q |
| **25:00–31:00** | 21–23 | **Build a skill live: mining → Excel** | The crescendo; 6-min cap; land the "codify once, reuse everywhere" line |
| 31:00–35:30 | 24–26 | Data sourcing · roadmap · SharePoint | Compress; point don't read |
| 35:30–36:30 | 27 | What you'll have in your hands | Introduce the guides |
| **36:30–37:30** | 28 | **Three objectives, revisited** | The bookend/payoff — mirror slide 3 |
| 37:30–45:00 | 29 | The ask + Q&A | 3 asks, then open floor |

**Staging trick:** Demo A starts at minute ~2.5 and is harvested at minute ~22 — about
19 minutes of background runtime. Nobody watches a spinner.

**Bookend:** slide 3 states the three objectives; slide 28 returns to them and shows each was
delivered. The keeper thread to plant on slide 3, prove in the mining build (slides 21–22), and
land on slide 28: **codify your expertise once, reuse it everywhere — expertise that compounds.**

---

## 3. Demo staging

**Demo A — background analysis (Clicks vs Dis-Chem).** Local documents only (no live
web — venue Wi-Fi risk). Kick off on slide 4; harvest on slide 20. Exact prompt and the
pre-generated fallback are in `demo-prompts-and-examples.md` and `fallback/`.

**Demo B — live build (mining skill → Excel).** On slides 21–23. Write the prompt *with*
the room for engagement, then paste the rehearsed version. Pre-built fallback skill and a
sample workbook are in `fallback/` in case generation misfires. **Hard cap: 6 minutes.**

---

## 4. Segment-by-segment script

> Note: the deck gained two slides since this section was first drafted — a **Three objectives**
> slide at 3 and a **revisited** bookend at 28 — so everything from the old slide 3 shifted down
> by one. The headings below are grouped by theme; for exact per-slide numbering use the full
> spoken script in `presentation-script.md`, which is authoritative.

### Open + intro (slides 1–2)
Thank them for their time *and their trust* — you're asking them to let a new kind of tool
into the research process. State the promise once, plainly, then stop selling. On slide 2,
the 85% does the credibility work; the line that wins the room is the humility one — *"I
build the technology; my finance is self-taught; where I get it wrong, correct me."* The
experts relax, everyone else trusts you more.

### Kick off Demo A (slide 3)
The most important 60 seconds mechanically. Switch to Cowork, paste the prompt, hit enter,
and say one sentence: *"I've just asked it to compare two retailers' results, citing every
number — we'll come back to it."* Switch back to slides. Do **not** wait for it.

### How we got here (slides 4–5)
This is your "the shift is real" payload — keep it concrete and jargon-free.

- **System 1** — the early chatbots: fast, fluent, intuitive, but one shot, no plan, no
  memory. (If the room enjoys it, name-check Kahneman's "fast thinking".)
- **Agents** — it learns to *pause and plan*: break a task into steps, use tools, check its
  own work, keep going. "Slow thinking" arrives.
- **Skills** — it carries *your* know-how, and picks it up only when a task needs it.
- **Today** — combine all three and you don't have a chatbot, you have a colleague.

Then slide 5, the reframe: one model has read across the breadth of human writing — calculus
to cookbooks, annual reports to Sufi poetry. *The point:* the hard part is no longer
operating the tool, it's knowing what to ask — which makes things **easier, not harder**.
This is the line that converts anxiety into curiosity.

### What Claude / Cowork / connectors are (slides 6–8)
Brisk — the concept already landed. Chat answers, an agent *does*. Cowork = Claude with
hands (a folder, a browser, connectors) and **every action behind a permission prompt**.
Connectors set up the SharePoint story you'll close on.

### Helps vs humans · Claude vs Copilot (slides 9–10)
Slide 9 answers the unspoken question. It carries the routine 80% — finding, re-keying,
first drafts; **you** keep judgement, conviction, relationships, accountability, the call.
That's also your "why now": the tools have just crossed from chat to colleague.

Slide 10 — be scrupulously even-handed; leadership is leaning Copilot, so partisanship
costs you. The honest facts: Microsoft's **Copilot Cowork** (via the Frontier program,
launched March 2026) is a genuine analogue — same idea, it also uses "skills", and it runs
Claude among its models. Claude's edge is transparency and portability (plain-text skills,
no lock-in); Copilot's edge is being native to the M365 estate you already run. **The way
of working ports either way** — which makes today low-risk whichever route they choose.
(Full comparison: backup slide 28.)

### The workspace + trust (slides 11–13)
Now show what you built. Before/after; the five-skill pipeline (discovery → downloader →
manifest → skill-builder → analyst); the self-healing line (a broken download triggers
re-discovery). Slow down on slide 13 — *numbers are sacred, source everything, flag
uncertainty, always prior-period context* — this is the slide leadership remembers.

### Agentic, live (slide 14)
Glance at Demo A: *"it's read the interims and it's comparing them now."* Explain the loop:
Plan → Act (loading the right skill **only when needed**) → Check → repeat. Then the
punchline that sets up the next section: attention is finite — load everything at once and
quality drops. *"Which brings me to the part nobody selling you AI wants to talk about."*

### The limits + staying honest (slides 17–18)
**This is what makes the rest believable.** Name the four honestly:

- **The dumb zone** — overload the context and it thinks worse. (That's *why* skills load
  on demand.)
- **Hallucination** — it can be confidently wrong; fluent ≠ correct.
- **Misalignment** — brief it vaguely and it optimises for the wrong thing. Most "AI
  failures" are briefing failures.
- **Non-determinism** — same prompt, slightly different wording; great for drafting, wrong
  for anything that must reconcile.

Then slide 18 — the discipline that defangs each: cite everything; keep scope tight; send
exact maths to **code** (deterministic, every time); brief it explicitly; human sign-off
before anything leaves. The keeper line: *deterministic where it must reconcile,
non-deterministic where judgement helps.*

### Harvest Demo A (slide 19)
Switch back. Show the finished note. Walk two or three cited figures and point out that it
flagged the six-vs-twelve-month mismatch **itself**. This is the "it actually works" moment
— let silence do some work, then take one or two questions. If it didn't finish, open the
fallback file; nobody will know.

### Build a skill live: mining → Excel (slides 20–22)
The crescendo. Ask the room: *"If you were teaching a junior to read a mining result, what
would you tell them to look at first?"* Capture a couple of answers, then paste the
rehearsed mining prompt. Read one line of the generated SKILL.md back to them — *"that's
it, that's the skill."* Point it at a miner. Then the Excel ask: *same skill, new output*.
Slide 22 is an **illustrative** template — say so; if the live workbook lands, show the real
one. **Cap this at 6 minutes** and move even if it's mid-thought.

### Close (slides 23–27)
Data sourcing (web/IR → download skill + Chrome → workspace; internal via SharePoint;
everything behind permission prompts). Roadmap M1–M4 — point, don't read. SharePoint as the
system of record. Then slide 26: the take-home guides and the message that *this is a
collaboration and a starting point*. Slide 27: the three asks — two pilot analysts, approve
the SharePoint library + consent, 30 minutes in week two — then open the floor.

---

## 5. Transitions (memorise these six)

1. Intro → history: *"So that's me. Let me show you what's actually changed, because it's
   not what most people think."*
2. History → workspace: *"That's the idea. Here's what it looks like when you point it at
   our actual job."*
3. Workspace → limits: *"…load everything at once and it gets worse — which brings me to
   the part nobody selling you AI likes to mention."*
4. Limits → Demo A result: *"With all of that said — here's what it produced while we've
   been talking."*
5. Demo A → Demo B: *"That one I prepared earlier. Now let's build a brand-new capability
   together, from nothing."*
6. Demo B → close: *"A sentence became a skill became a spreadsheet. So — where could this
   go for AllWeather?"*

---

## 6. Timing flex plan

**If you're running long (most likely):**
- Cut slide 8 (connectors) — fold into slide 23.
- Compress slides 11–12 to one minute total.
- Drop the audience question on slide 20; paste the prompt straight away.
- Trim Demo A walk-through (slide 19) to a single cited figure.

**If you're running short (rare):**
- Open the Copilot deep-dive (backup 28) and the determinism backup (29).
- Take more questions after slide 19.

**If a demo breaks:** open the matching file in `fallback/`, narrate it as if live ("here's
one it prepared earlier"), and keep moving. Never debug on stage.

---

## 7. Pre-flight (the morning of)

Notifications off · font scaling up in Cowork · Demo A prompt on the clipboard or in a
notes file · fallback folder open in a window · second screen / app-switch tested · water ·
the original `.pptx` closed so you present from v2. Full checklist in `prep-checklist.md`.
