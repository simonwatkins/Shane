---
name: jse-sector-luxury
description: >
  Sector-analysis lens for JSE-listed luxury-goods companies, loaded on top of jse-analyst to add
  luxury-specific depth. Use whenever the user analyses, reviews, compares or asks about Richemont
  (CFR) or any luxury / premium-brand business — jewellery, watches, leather goods, fashion maisons.
  Also trigger on words like luxury, luxury goods, jewellery, watches, maison, Cartier, Van Cleef,
  hard luxury, soft luxury, organic sales growth, like-for-like, China demand, tourist flows. This
  lens adds the luxury value drivers, the constant-FX organic-growth KPIs, the right valuation
  lenses and luxury-specific risk flags. It does NOT restate the income-statement framework, the
  Citation Standard, SA macro context, or the analysis workflow — those are inherited from
  jse-analyst.
---

# JSE Sector Lens — Luxury Goods (Richemont)

A **bolt-on lens for `jse-analyst`**. It does not run on its own. Unlike most JSE constituents,
luxury is a **global demand story** (China/Asia, US, Europe, Japan) with strong **pricing power**
and a **EUR/CHF** cost-currency dynamic — read it on organic growth and brand strength, not SA macro.

## Inheritance contract (read first)

`jse-analyst` owns everything universal and you MUST NOT restate it: the general metrics table,
HEPS discipline, prior-period comparisons, the Citation Standard and Provenance appendix, the
general risk scan, SA macro/tax context, workflow and output rules. This skill is the
**interpretation layer** for Steps 3/4/6. Every figure carries a `Source` tag. **Name this lens in
the deliverable** ("Sector lens: `jse-sector-luxury`").

## Scope — when this applies

Primary JSE name: **Richemont (CFR)** — Swiss group, **SIX Swiss primary / JSE secondary**, reports
in **EUR**, FY end **31 March**. Structure to encode every time:

1. **Two engines.** **Jewellery Maisons** (Cartier, Van Cleef & Arpels, Buccellati) — the structural
   winner, high-margin, brand-controlled distribution — and **Specialist Watchmakers** (IWC,
   Jaeger-LeCoultre, Vacheron Constantin, Piaget, etc.) — higher-quality but more cyclical and more
   wholesale-exposed. Plus "Other" (fashion/accessories) and the online distributor **YOOX
   Net-a-Porter (YNAP)**, long loss-making and subject to disposal. Analyse the segments separately.
2. **Currency.** Revenue in USD/CNY/JPY/EUR; cost base skewed to **CHF/EUR** (Swiss manufacturing) — a
   strong franc is a margin headwind. Always split the **organic (constant-FX)** move from the FX move.

## 1. Value drivers — what actually moves the P&L

> Earnings ≈ organic sales growth (price × volume × mix) × operating leverage, ± FX translation,
> with brand equity setting pricing power.

- **Organic sales growth at constant exchange rates** — the single most-watched number; strip FX and M&A.
- **Regional demand — China/Asia-Pacific is the swing factor** (mainland + tourist spend in HK/Macau/
  Europe/Japan); plus the US, Europe and Japan. Tourist-flow and FX shifts move where the Chinese
  consumer buys.
- **Jewellery vs Watches divergence** — branded jewellery is taking share and is more resilient; watches
  carry wholesale/grey-market cyclicality. The mix shift lifts group margin.
- **Pricing power & brand equity** — ability to take price without losing volume; the core moat.
- **Channel mix — retail vs wholesale vs online** — the structural shift to **direct-to-client (retail)**
  improves control, data and margin but adds operating leverage (and lease cost).
- **Operating leverage & FX translation** — high fixed retail/marketing base; CHF/EUR strength compresses
  reported margin even when volumes hold.

## 2. KPIs and how to read them

| KPI | What it is | Good direction | What a move signals |
|---|---|---|---|
| **Organic / LFL sales growth (constant FX)** | Underlying demand ex-FX, ex-M&A | Higher | The real demand read; reported growth is distorted by EUR translation. |
| **Growth by region** (China/Asia, Americas, Europe, Japan, MEA) | Where demand is | Broad-based | China is the swing; watch tourist vs domestic split. |
| **Growth by channel** (retail / online / wholesale) | Distribution mix | Retail-led | Direct-to-client shift = better margin & data; wholesale weakness can flag channel destocking. |
| **Jewellery Maisons vs Specialist Watchmakers** — sales & operating margin | Segment performance | Jewellery-led | Mix toward jewellery lifts group margin and resilience. |
| **Gross & operating margin** | Profitability | Stable/expanding | Watch CHF/EUR FX, mix, and operating deleverage in a downturn. |
| **Inventory days / channel inventory** | Stock vs demand | Disciplined | Rising watch inventory / wholesale stuffing precedes markdowns and destocking. |
| **Cash conversion / FCF** | Cash quality | High | Luxury should be highly cash-generative; large retail capex and inventory can absorb it. |

## 3. Valuation methodology

- **EV/EBIT and P/E — PRIMARY**, at a structural **premium to the market** for quality compounders;
  benchmark vs LVMH, Hermès, Kering. State the FX and China-cycle assumptions behind the forecast.
- **FCF yield and EV/Sales** — EV/Sales captures brand strength where margins are temporarily depressed
  (e.g. YNAP drag); FCF yield checks cash quality.
- **DCF** on long-run growth and steady-state margin — luxury supports long explicit-growth periods given
  pricing power; sensitivity to the terminal China-demand assumption is high.
- **Mind the cycle** — the multiple expands in China up-cycles and de-rates in downturns; avoid anchoring
  on a peak-cycle multiple, and read inventory as a leading indicator.

## 4. Sector-specific risk flags (extend jse-analyst Step 6)

- **China demand & policy** — slowdown, property/wealth sentiment, "common prosperity"/anti-extravagance,
  and tourist-flow disruption are the dominant swing risks.
- **FX** — strong **CHF/EUR** margin headwind; USD/CNY/JPY translation on revenue.
- **Watch wholesale & grey market** — channel destocking, parallel imports and discounting hit the watch
  segment first; watch inventory build.
- **YNAP / online** — loss-making, disposal/held-for-sale accounting, execution risk on exit.
- **Inventory & obsolescence** — high-value, long-dated stock; mix and fashion risk in soft luxury.
- **Brand dilution / over-distribution** — protecting exclusivity vs chasing volume.
- **Governance / control** — the **Rupert family dual-class control** (Compagnie Financière Rupert holds
  the "B" registered shares / voting control); minority-voice and succession considerations.
- **Macro & tariffs** — luxury demand is discretionary and cyclical; trade tariffs affect US pricing.

## 5. Accounting & regulatory regime

- **Reporting currency EUR**; **CHF/EUR** cost exposure — separate translation from operating performance.
- **IFRS 16 leases** — a large directly-operated retail estate puts sizeable right-of-use assets and lease
  liabilities on the balance sheet; affects EBIT vs EBITDA comparability.
- **Inventory valuation** — high-value, slow-turning; check provisioning and any channel build.
- **Held-for-sale / disposal accounting** for YNAP — one-offs and impairments can distort reported earnings;
  read the underlying.
- **Dual listing** — SIX Swiss primary, JSE secondary; cite which listing's figures you use, give ZAR equiv.

## 6. Primary documents & cadence (for jse-report-downloader)

- **Half-year results (H1 to 30 Sep, reported ~Nov)** and **full-year results (FY to 31 Mar, reported ~May)**.
- **Q3 holiday-quarter sales update (~Jan)** — the key festive-season trading read.
- **AGM (~Sep)** and investor presentations; any **disposal / M&A** SENS (e.g. YNAP).
- Reports in EUR; capture the segment and regional growth tables, not just the group line.

## 7. Five questions a luxury specialist asks management

1. What is the **organic growth by region and channel**, and specifically the **China** trajectory
   (domestic vs tourist) and channel inventory?
2. What is driving the **Jewellery vs Watches** divergence, and how durable is the jewellery share gain?
3. How much growth is **price vs volume vs mix**, and how much pricing headroom remains?
4. What is the plan for **YNAP / online**, and the earnings/impairment impact of any disposal?
5. How is **FX (CHF/EUR)** being managed, and what is the steady-state operating margin assumption?

## Last updated

2026-06-18 — created. Re-verify Richemont's segment structure, the YNAP disposal status and the latest
regional growth via web search before relying on specifics.
