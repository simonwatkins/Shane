# An All-Weather Analyst — Full Spoken Script

**A first-person draft to build on.** This follows the deck (`an-all-weather-analyst-v3.pptx`)
slide by slide. It's written the way you might say it — read it aloud, then replace my
words with yours. Cues in **[brackets]** are actions, not lines to read. **[FILL: …]** marks
a fact only you can supply.

> Length note: read straight through this is ~37 minutes; with the two demos it lands around
> 45. It's deliberately a touch full so you can **cut to taste** rather than pad. Where you
> need to save time, the thinner slides (7–9, 25–26) are the first to trim.

---

## Slide 1 — Title *(0:00–0:30)*

Good morning, everyone — and thank you. Not just for your time, which I know is the scarcest
thing in this building, but for your trust. What I'm going to show you today is a new way of
working, and I don't take for granted that you've made the room for it.

Here's my promise for the next forty-five minutes. By the end, you'll have watched Claude
research two JSE-listed companies from a single sentence, end to end. You'll have seen exactly
where it can trip up — I'm not going to hide that. And you'll have watched us build a brand-new
capability together, live, from a sentence to a finished spreadsheet. No code involved.

Let me start with who I am, and why I'm the one standing here.

---

## Slide 2 — Where I'm coming from *(0:30–1:30)*

My name is Simon Watkins. I've been a software engineer for about twenty-five years, and I'm
a senior developer at Trayport in the UK, where I'm one of the lead developers on our
Automated Trading platform.

If Trayport isn't a name you know, the scale might surprise you: something like **85% of
European utilities' derivatives trading flows across our platform.** [FILL: confirm against
Trayport's current approved wording.] Automated Trading is the part that lets algorithms
execute directly into those markets — and it plays a real role in the UK retail energy market
too. [FILL: one concrete line here about Automated Trading's role in UK retail energy — your
own knowledge, since I'd rather you say it than me guess a number.]

I tell you this for two reasons. First, we are a business that has embraced AI at every level
— not as a gimmick, but in how we build, test and run software every day. So I'm not selling
you something I haven't lived with.

And second — the caveat, and please hold me to it. I write financial software, but most of
the problems I solve are technical, not financial. My own understanding of finance is limited
next to yours. So where I get the finance wrong today, I ask for your patience, and frankly
your corrections. You are the experts in this room. I'm just the one who's seen what this
tool can do.

---

## Slide 3 — Three things I hope you'll leave believing *(2:00–3:00)*

Before I show you a single thing, let me be honest about what I'm hoping to achieve — three
things I'd like you to agree with by the time I sit down. Hold me to them.

**One: that this is real.** That the technology has crossed a line, and now delivers practical,
*measurable* value on an investment desk. Not a gimmick, not a toy for the enthusiasts in the
corner. Real work, real hours saved.

**Two: that it's for you — and that it compounds.** You do not need to be a technologist to use
any of this. And here's the part I care most about: with skills, you can take your own expertise
— the way *you* read a result, the checks *you* always run — write it down once, in plain
English, and reuse it on every similar problem you'll ever face. Your know-how stops living in
one person's head and becomes something the whole firm owns and builds on. Expertise that
compounds.

**And three: that it amplifies, it doesn't replace.** Nothing I show you today is about removing
analysts. It's about shortening the path from information to a decision — making good analysts
faster, and sharper. Think of it less as artificial intelligence and more as an *intelligence
amplifier.*

If I've done my job, you'll agree with all three by the time I finish. Let me show you why.

---

## Slide 4 — The next 45 minutes *(1:30–3:00)*

So here's where we're going. **[Advance to agenda. Then — before you talk through it — switch
to Cowork.]**

Actually, before I walk you through the plan, let me start something running. **[Paste the
Clicks-vs-Dis-Chem prompt into Cowork, hit enter.]** I've just asked Claude one sentence: to
compare two South African retailers' latest results, citing every single number. It's going to
work on that quietly in the background while we talk, and we'll come back to it later to see
what it produced. I'm not going to make you watch a progress bar.

**[Switch back to slides.]** Right — the plan. I'll tell you how we got here and what this
technology actually is. I'll show you the workspace I've built for exactly this kind of
research. We'll look honestly at the limits. We'll harvest that analysis I just kicked off,
we'll build a new skill together, and we'll finish with where I think this could go for
AllWeather Capital — and your questions.

---

## Slide 5 — How we got here, in three big steps *(3:00–5:15)*

Let me give you the short history of how we got here, because it explains why *now* is
different from the AI you may have tried a year or two ago and found underwhelming. There are
really three steps.

**Step one was what I'd call System One thinking.** If you've read any Daniel Kahneman — fast
thinking, the instant, intuitive, gut response. The early chatbots were like that. You typed
something, you got an answer straight back. Fluent, fast, often impressive — but one shot, no
plan, no memory. Brilliant party trick, unreliable colleague.

**Step two was agents.** This is where it learned to slow down. Instead of blurting an answer,
it learned to pause and *plan* — to break a task into steps, use tools, check its own work,
notice it had gone wrong, and try again. That's the slow, deliberate thinking. That's the leap
that turned a clever autocomplete into something that can actually do a job.

**Step three, where we are now, is skills.** This is the part I'm most excited to show you.
A skill is simply know-how you hand the model — your way of doing something — that it picks up
*only when a task needs it.* Your house style, your rules, on tap.

And when you combine all three — fast intuition, careful planning, and your own expertise on
demand — you don't have a chatbot any more. You have something much closer to a colleague.
The thing to take away is that **each of these steps made the tool do more of the work, and
made it easier to use, not harder.**

---

## Slide 6 — Trained on (almost) everything we've written *(5:15–6:15)*

One more thing about what's under the bonnet, because it matters for how you'll use it.

A model like Claude has been trained on an enormous breadth of human writing. And I mean
breadth. Calculus textbooks and cookery books. Annual reports and Sufi poetry. Case law,
clinical trials, computer code, and centuries of argument — all compressed into one system
that you talk to in plain English.

Here's why that's a genuine paradigm shift, and not just a bigger search engine. For decades,
the hard part of computing was operating the machine — knowing the syntax, the software, the
commands. That's gone. **The hard part now is simply knowing what to ask.** And that's a skill
this room already has in abundance. It makes things easier, not harder — and it means the
person who gets the most out of this won't be the best programmer. It'll be the best analyst.

---

## Slide 7 — What is Claude? *(6:15–7:15)*

So, quickly, what is this thing? Claude is a frontier AI model. In a chat window, it answers
questions. But used as an *agent* — which is what we'll do today — it completes tasks.

Concretely, it can do four things that matter for your work. It **reads** — annual reports,
interims, announcements, hundreds of pages at a time. It **writes** — analysis, notes, decks,
in your format every time. It **browses** — it'll find an investor-relations page and download
the filing. And it **runs code** — so calculations are checked, not guessed. The difference
that matters today is simple: chat *answers*; an agent *does*.

---

## Slide 8 — Cowork: Claude with hands *(7:15–8:15)*

The way it gets hands is a feature called Cowork. Think of it as Claude with hands.

It has three things. **A folder** on a machine that it can read and write — and nothing outside
it. **A browser** — a real, visible Chrome tab it can drive, for the IR sites that block simple
downloads. And **connectors** into your systems — SharePoint, Outlook, Teams — with your admin's
consent. And the line I want you to hold onto, because I know someone's already thinking it:
**every action sits behind a permission prompt. Nothing happens silently.** You watch it work.

---

## Slide 9 — Connectors: plug into your tools *(8:15–9:00)*

A quick word on those connectors, because they're how this stops being a clever toy and starts
being useful on *your* data. Connected once by an admin, Claude can read your internal research
in SharePoint, broker notes in Outlook, post findings to Teams, pull pricing from Bloomberg
where you're licensed. The point is that it can cite your internal models *alongside* the public
filings. For AllWeather, SharePoint becomes the system of record — and I'll come back to exactly
how that works near the end.

---

## Slide 10 — What it does, and where you stay essential *(9:00–10:30)*

Now, the question everyone is too polite to ask first, so let me ask it for you: *does this
replace us?*

No. And I want to be precise about why. What Claude is extraordinary at is the routine
eighty percent. Finding and reading the filings — hundreds of pages in minutes. Re-keying and
cross-checking the numbers, every one of them cited. Drafting that first pass in your house
format. It never tires, never cuts a corner, and it's ready before the market opens.

But look at the other column. Judgement. Conviction. The relationships with management and
clients. Accountability — your name on the call. The scepticism to know when a number simply
*feels* wrong. None of that is going anywhere. What changes is that you stop spending your
mornings retrieving and re-keying, and you start at the judgement — which is the part you're
actually paid for, and the part you're good at.

And *why now?* Because that second step I mentioned — the leap from chat to colleague — has
only just happened. The tools have crossed a line in the last year. This isn't early. It's
right on time.

---

## Slide 11 — Claude Cowork vs Copilot "Cowork" *(10:30–12:00)*

I want to be straight with you about the landscape, because I understand AllWeather is leaning
towards Microsoft's Copilot Frontier — and I'm not going to stand here and pretend that's the
wrong instinct.

Here's the honest picture. As of March this year, Microsoft ships something called **Copilot
Cowork**, through their Frontier programme. It is a genuine analogue to what I'm showing you —
same idea, multi-step, runs in the background, and it even uses the same word, "skills." In
fact, it runs several models under the bonnet, Claude among them. So in some configurations,
choosing Microsoft means you're *already running Claude.*

So where do they differ? Claude's strength is transparency and portability — the skills are
plain text you can read, version and share, with no platform lock-in. Microsoft's strength is
that it's native to the Microsoft 365 estate you already run. Both are real advantages.

My honest take — and this is the reassuring part, given where you're leaning — is that they are
**genuinely analogous.** The real choice is fit: your estate, your governance, how much
transparency you want. But the *way of working* I'm showing you today — agentic, skills-based,
human-in-the-loop — ports either way. So nothing you invest in understanding today is wasted,
whichever route you take. **[If pressed for detail, there's a fuller comparison in the backup
slides.]**

---

## Slide 12 — JSE coverage, before and after *(12:00–13:00)*

Let me bring this down to earth and show you what I actually built — for a job I know you do
every results season.

Before: a name reports. Someone finds the IR page, downloads the PDF, re-keys the numbers into
a model, and *only then* does the analysis begin. Hours per name, every season, before you've
had a single useful thought.

After: you say "tell me about Capitec," and the finding, the downloading, the cataloguing and a
first, fully-cited analysis happen on their own. The workspace I'll show you tracks ten JSE
names today — and every one of them was onboarded just by *asking*, not by building.

---

## Slide 13 — Five skills, one pipeline *(13:00–14:15)*

Under the bonnet, that's five small skills working as a pipeline. **Discovery** finds the
company's IR site and maps where the documents live. **Downloader** fetches the reports, the
announcements, the presentations — automatically. **Manifest** catalogues everything and tells
me what's missing or due. **Skill-builder** writes each company its *own* skill, so the next
time is instant. And **Analyst** produces the standardised, cited analysis from those local
documents.

It all lives in one shared folder — documents, index, skills, configuration. Portable,
inspectable, versioned. And my favourite part: if a website changes and a download breaks, the
workspace re-discovers the source and repairs its own skill. It heals itself.

---

## Slide 14 — Built to be trusted *(14:15–15:30)*

Now, this is the slide I'd ask leadership especially to sit with, because a research tool you
can't trust is worse than no tool at all.

Four rules are baked into this workspace. **Numbers are sacred** — never rounded, never
estimated; if it has to derive a figure, it marks it and shows the working. **Source
everything** — every figure cited to its document and its page. **Flag uncertainty** — a gap is
reported as "not disclosed," never quietly papered over. And **context always** — every number
against the prior period, with the change.

And the important part: these aren't good intentions I'm hoping it remembers. They're written
into the workspace's configuration and enforced on *every* analysis. That's the difference
between a demo and something you can actually put to work.

---

## Slide 15 — What "agentic" means — happening right now *(15:30–17:00)*

Let me glance at what we started earlier. **[Glance at Cowork.]** You can see it's already found
and read the interims, and it's working through the comparison now. **[Back to slides.]**

While it does, let me show you what "agentic" actually means, because it's the whole game. It's
working a loop — the same loop any of you would.

It **plans**: reads my request, checks what's already on disk, decides the next step. There's no
grand script; it's reasoning as it goes. It **acts** — and here's the subtle, important bit — it
loads the right skill *only when it needs it.* One skill at a time, one tool, one file; anything
it isn't using stays out of the way. And then it **checks, and repeats**: compares the result to
the goal, corrects, and carries on until the job is genuinely done.

Why does "only when needed" matter so much? Because attention is finite — even for a machine.
Load everything at once and quality actually drops. Which brings me, neatly, to the part of this
talk that nobody selling you AI likes to mention.

---

## Slide 16 — Demystifying skills *(17:00–18:00)*

But before the warnings — the good news, because I promised you no code. Every skill, however
clever it sounds, has just three parts, and all three are plain English.

There's the **description** — that's how it decides *when* to act. You write the phrases people
actually say: "format my IC notes," "tidy these minutes." There are the **instructions** — what
to do. That's just the brief you'd give a new team member: the sections, the order, the format.
And there are the **rules** — what never to do. "Never invent content." "Keep numbers exactly as
written." Guardrails, written down. That's it. That's a skill.

---

## Slide 17 — Skills: instructions, not software *(18:00–19:00)*

And here's a real one, from this workspace, on the screen. **[Gesture to the SKILL.md.]** I'm
not going to make you read it all, but look at any line. *[Read two or three lines aloud.]* It's
not code. It's a document. It's the sort of thing you'd write to a junior analyst to tell them
how you like a job done.

That's the line I'd love you to leave with: **if you can write an email briefing a junior
analyst, you can write a skill.** And as we'll see in a moment, you don't even have to write it
yourself — you can ask Claude to write the first draft, and then just read it back and correct it.

---

## Slide 18 — Four ways it can let you down *(19:00–21:00)*

So. The honest part. I'd be doing you a disservice if I only showed you the magic. There are
four ways this technology can let you down, and you should know all of them.

**One — what I call the dumb zone.** I just mentioned it. Attention is finite; cram too much in
at once and the quality falls. An overloaded model thinks worse — like a desk buried under so
much paper you can't find anything.

**Two — hallucination.** It can state a wrong number with complete, fluent confidence. And this
is the one that should worry a fund most: *fluent is not the same as correct.*

**Three — misalignment.** Ask it vaguely, and it will optimise for the wrong thing — confidently
solving a problem you didn't actually have. In my experience most so-called "AI failures" are
really *briefing* failures.

**Four — it's non-deterministic.** Ask the same question twice and you'll get slightly different
wording each time. That's wonderful for drafting, and completely wrong for anything that has to
reconcile to the penny.

Now — none of these are deal-breakers. Each one has a discipline that defangs it. That's the
next slide, and honestly it's the most important one in the deck.

---

## Slide 19 — …and how we keep it honest *(21:00–22:30)*

Here's how we tame each of those, and most of it is already built into the workspace.

Against hallucination: **cite every number to document and page** — so any figure is checkable
in seconds. Against the dumb zone: **keep the scope tight, load only the skill you need.**
Against non-determinism, and this is the key one for you: **send the exact maths to code, not
to the model.** A script gives you the same answer every single time. Against misalignment:
**brief it like a junior — explicit goals, explicit guardrails.** And underneath all of it:
**a human signs off before anything leaves the building.** The analyst owns the call. Always.

If you remember one sentence from this whole section, make it this: **deterministic where it
has to reconcile; non-deterministic where judgement helps.** Use each for what it's actually
good at, and the risks become very manageable.

---

## Slide 20 — Meanwhile, Claude was working *(22:30–25:30)*

Now — let's see what it's been doing while we talked. **[Switch to Cowork; open the saved note.]**

This is from that one sentence at the start: compare Clicks and Dis-Chem, cite every number.
Look at what came back. **[Walk two or three figures.]** Turnover, headline earnings, margin,
dividend — each one against the prior period, each one cited to a document and a page.

And here's the detail I love. **[Point to the caveat.]** Notice it flagged, *itself*, that the
two companies report over different periods — six months versus twelve. I didn't tell it to
watch for that. It raised the caveat on its own, exactly as a careful analyst would. That — that
right there — is the difference between a search engine and a colleague.

**[Pause. Take a question or two if the room has them.]** Any questions on that before I build
you a brand-new one from scratch?

---

## Slide 21 — Build a skill from scratch: mining *(25:30–28:00)*

Right. That one I prepared earlier, in a sense — the skills already existed. Let's build a
*new* capability, together, from nothing. And I'd like your help.

We're in mining-heavy territory on the JSE, so let's build a mining-results skill. So tell me —
**[to the room]** — if you were teaching a brand-new analyst to read a mining result, what's the
first thing you'd have them look at? **[Take two or three answers — you'll hear production,
costs, the commodity price, net debt.]**

Good — that's exactly the skill. **[Paste the mining prompt.]** Watch what I'm actually doing
here: I'm just writing down, in plain English, how a mining analyst reads a result — revenue,
EBITDA and margin, headline earnings, net debt and net-debt-to-EBITDA, free cash flow, the
dividend, always versus the prior period, every figure cited, and flag the commodity-price and
rand sensitivity. That's not programming. That's *you*, talking — and once it's written down, it's ours to keep.

---

## Slide 22 — Watch it come to life *(28:00–30:00)*

Three things happen now. **[Narrate as they occur.]**

First, Claude writes the skill — a one-page document appears, and we can read it straight back;
it's the plain English we just spoke. Second, we point it at a miner — "apply it to the latest
results" — and it loads that brand-new skill and works the loop we talked about. And third,
we'll change the output entirely with one more sentence.

The point isn't the mining numbers. It's this: we wrote that skill *once* — and it now reads
every miner on the JSE, this results season and every one after. Describe how you read a result,
and the desk owns that method forever. **That's** the leverage: your expertise, written down once
and reused everywhere.

---

## Slide 23 — The same skill, delivered as Excel *(30:00–32:00)*

And here's that last sentence. Same skill, completely different output. **[Paste the Excel
prompt.]** "Now turn that into a mining peer comparison as a formatted Excel workbook — one row
per company, a ratios-and-flags tab, conditional formatting on the leverage."

**[The slide shows the structure — say so.]** What's on screen is an illustrative template — the
columns a mining analyst cares about: revenue, EBITDA margin, headline earnings, net debt to
EBITDA. The live build fills those with cited figures for the real names — Anglo, BHP, Sasol,
Gold Fields, Exxaro. From a sentence, to a skill, to a spreadsheet your team could use this
afternoon — and every number in it traceable to source. **[If the live workbook lands, open it.
If not, open the one in the fallback folder and carry on.]**

---

## Slide 24 — Where the data comes from *(32:00–34:00)*

A fair question at this point is: where is it getting all this from? Three places.

The **public web** — IR sites, SENS announcements, filings — fetched and filed by the download
skill I showed you, with the Chrome browser stepping in for the sites that block plain
downloads. Your **internal research** — the models and notes already in SharePoint — read in
place through a connector, no migration, nothing copied around. And anything you choose to
**connect** beyond that.

And once more, because it's the thing that makes this safe to adopt: **every fetch, every file
it writes, every connector sits behind a permission prompt.** Nothing happens that you didn't
allow and can't see.

---

## Slide 25 — The path from pilot to firm-wide *(34:00–35:15)*

So how would this actually roll out? Four steps, deliberately low-risk.

**Milestone one** — the workspace I showed you, live in a SharePoint library, two pilot
analysts, our current coverage as the watchlist. That's weeks, not quarters. **Milestone two** —
we connect the estate: your internal research, your broker notes, team-wide read access.
**Milestone three** — we automate the rhythm: morning updates on what's moved overnight, IC packs
generated for you, and analysts writing their *own* skills. And **milestone four** — firm-wide,
beyond research: operations, compliance checks, IR monitoring. Each milestone ships with its own
one-page guide.

---

## Slide 26 — Where the data lives: SharePoint *(35:15–36:15)*

One slide for the IT-minded, because I know AllWeather runs on SharePoint, and that's a strength
here, not an obstacle.

The research folder lives in a SharePoint library, synced locally through OneDrive. So Claude
works on fast local files, while the whole team sees the same documents in SharePoint, and you
get versioning and retention for free. Your existing research under each company folder is read
directly through the connector — no migration. The one honest caveat: start with a single
designated writer to avoid sync conflicts, and let everyone else read. That's it. No servers,
no new infrastructure.

---

## Slide 27 — What you'll have in your hands *(36:15–37:15)*

Now — I don't expect anyone to remember all of this. You won't have to, because it's all written
down, for two kinds of people.

There's an **Everyday Guide** — for every PM and analyst — what this is, how to ask it well, and
a prompt cheat-sheet, with no code anywhere in it. There's a **Builder's Guide** — for the
hands-on among you — the anatomy of a skill, the workspace, the connectors, the maintenance. And
there's the **live workspace** itself: this isn't a finished product I'm handing over, it's a
starting point, yours to use, copy and grow.

Because that's really the heart of it: this is a *collaboration.* We'll learn what works for
AllWeather together, and the guides and the skills will grow with us.

---

## Slide 28 — So, did we get there? *(37:00–37:45)*

Before I ask you for anything, let me go back to the three promises I made at the start.

**One — is it real?** You watched it research two companies end to end, every number cited, and
turn a single sentence into a peer-comparison spreadsheet. I'll let you be the judge — but I
think that's real.

**Two — is it for you, and does it compound?** We wrote a brand-new mining skill, together, in
plain English, in about two minutes. And here's the bit that matters: we wrote it *once,* and it
now reads every miner on the JSE — this results season, and every season after. That's your
expertise, captured and reused. That's the compounding.

**And three — does it amplify rather than replace?** Not one thing I showed you took the
judgement out of your hands. It just handed back the hours around it.

The same three I opened with. So — let me tell you what I'm actually asking for.

---

## Slide 29 — What we're asking for today *(37:15–45:00)*

So — three asks, and they're modest.

First, **nominate two pilot analysts.** Second, **approve a "JSE Research" SharePoint library
and the connector consent** — that's the one bit of IT and admin we need. And third, give me
**thirty minutes with you in week two** to review what the pilots produced. That's the whole ask.

I started by thanking you for your trust, and I'll end there too. You've trusted me with
forty-five minutes to show you something I genuinely believe will change how this desk works —
not by replacing the judgement that makes AllWeather good at what it does, but by handing you
back the hours you currently spend on everything *around* that judgement.

Thank you. I'd love to take your questions. **[Open the floor. Backups ready: Copilot in depth,
deterministic vs non-deterministic, security, cost, compliance, full setup.]**

---

### Appendix — if a demo misbehaves
Never debug on stage. Open the matching file in `fallback/`, say *"here's one it prepared
earlier,"* and keep moving. Exact prompts are in `demo-prompts-and-examples.md`; timing and
director's notes in `presenter-script.md`.
