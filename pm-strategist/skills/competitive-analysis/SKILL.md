---
name: competitive-analysis
description: "Consolidated competitive analysis knowledge — competitor profiling with specific data, Porter's Five Forces, PESTLE macro-environment analysis, SWOT with mandatory actions, and Ansoff Matrix for growth direction. Includes instructions to use WebSearch for real competitor data."
---

# Competitive Analysis

## Philosophy

Competitive analysis is not a list of logos. It's a dynamic map of forces, incentives, and strategic positions that reveals where you can win and where you'll get crushed.

**Rules:**
1. Use WebSearch to gather real data. Competitor pricing from the user's memory is not intelligence.
2. Every claim about a competitor must cite a source or be flagged as assumption.
3. Analysis must lead to action. "Competitor X is strong" is observation. "Competitor X's strength in enterprise creates an opening for us in mid-market because they ignore <$50K deals" is analysis.

---

## Part 1: Competitor Analysis Framework

### Data to Gather (Per Competitor)

Use WebSearch and WebFetch to find as much of this as possible:

| Category | Specific Data Points | Where to Find |
|----------|---------------------|---------------|
| **Company** | Founded, HQ, employee count, leadership team | LinkedIn, Crunchbase, company About page |
| **Funding** | Total raised, last round, valuation, investors | Crunchbase, PitchBook, press releases |
| **Product** | Core features, platform/integrations, tech stack | Product pages, docs, changelog |
| **Pricing** | Tiers, per-seat/usage costs, enterprise pricing | Pricing page, G2, sales conversations |
| **Customers** | Logos, segment focus, estimated count, case studies | Website, G2 reviews, press releases |
| **Traction** | Revenue (if public), growth rate, employee growth | SEC filings, news, LinkedIn headcount trends |
| **Reviews** | G2/Capterra scores, common praise, common complaints | G2, Capterra, TrustRadius, Reddit, HN |
| **Hiring** | Open roles by department, seniority, location | Job boards, LinkedIn, careers page |
| **Strategy signals** | Recent launches, acquisitions, partnerships, messaging changes | Blog, press, social media |

### Hiring as a Strategic Signal

Job postings reveal where competitors are investing BEFORE they ship:
- Hiring ML engineers? They're building AI features 6-12 months out.
- Hiring enterprise sales reps in EMEA? They're expanding geographically.
- Hiring a Head of Platform? They're building an ecosystem.
- Cutting engineering and hiring sales? They're shifting from product-led to sales-led.

### Competitor Profile Template

For each of 3-5 direct competitors:

```
## [Competitor Name]
**Founded**: [year] | **HQ**: [city] | **Employees**: [count] | **Funding**: [total, last round]

**What they do**: [one-sentence positioning]
**Who they serve**: [primary segment, company size, use case]
**How they charge**: [pricing model, tiers, price points]

**Strengths** (with evidence):
1. [Strength] — [evidence: review score, feature, market share]

**Weaknesses** (with evidence):
1. [Weakness] — [evidence: negative reviews, missing feature, complaints]

**Recent moves**: [last 6 months of notable activity]

**Threat to us**: [specific ways they could win our target customers]
**Our advantage over them**: [specific, defensible — not "better UX"]
```

### Competitive Dynamics (Beyond Individual Competitors)

Don't just profile competitors — understand the system:

- **Convergence patterns**: Are competitors becoming more similar over time? (Feature parity → commoditization → price competition)
- **Strategic groups**: Which competitors cluster around similar strategies? Where are the gaps between clusters?
- **Potential entrants**: Who could enter this market? Adjacent players (e.g., Salesforce entering your niche), platform players (e.g., Microsoft bundling your category), well-funded startups
- **Ecosystem dynamics**: Are there platform shifts that could change the competitive structure? (e.g., AI enabling new categories of tools)
- **Win/loss patterns**: Why do customers choose Competitor X over you? Why do they choose you over Competitor X? This is the most valuable competitive data.

---

## Part 2: Porter's Five Forces

Evaluate industry structure and profitability potential. Rate each force: **High / Medium / Low** with specific evidence.

### 1. Competitive Rivalry

| Signal | High Rivalry | Low Rivalry |
|--------|-------------|-------------|
| Competitor count | Many, similar size | Few, one dominant |
| Market growth | Slow/declining (zero-sum) | Fast-growing (positive-sum) |
| Differentiation | Low (commoditized) | High (distinct positioning) |
| Fixed costs | High (volume pressure) | Low |
| Exit barriers | High (can't leave) | Low |
| Pricing behavior | Frequent discounting, price wars | Stable pricing |

**So what**: High rivalry = margins compressed, focus on differentiation or cost leadership. Low rivalry = protect the status quo, don't trigger competitive response unnecessarily.

### 2. Supplier Power

In tech, "suppliers" includes cloud providers, API vendors, data providers, talent market, and open-source communities.

| Signal | High Power | Low Power |
|--------|-----------|-----------|
| Concentration | Few dominant suppliers | Many alternatives |
| Switching costs | High (integration depth) | Low (commodity) |
| Forward integration | Supplier could compete with you | Unlikely |
| Your dependency | Critical component | Nice-to-have |

**So what**: High supplier power = diversify suppliers, negotiate long-term contracts, consider building in-house. OpenAI dependency is supplier power.

### 3. Buyer Power

| Signal | High Power | Low Power |
|--------|-----------|-----------|
| Concentration | Few large buyers | Many fragmented buyers |
| Switching costs | Low (easy to leave) | High (deep integration) |
| Price sensitivity | Budget-constrained, ROI-focused | Value-driven, less price-sensitive |
| Information | Full visibility into alternatives | Limited awareness |

**So what**: High buyer power = invest in switching costs (integrations, data lock-in, workflow embedding), customer success, and measurable ROI.

### 4. Threat of Substitutes

Substitutes are NOT competitors — they're different products that solve the same problem. Excel is a substitute for project management software. Hiring a person is a substitute for automation software.

| Signal | High Threat | Low Threat |
|--------|-----------|-----------|
| Substitute quality | Good enough | Clearly inferior |
| Substitute cost | Cheaper or free | More expensive |
| Switching effort | Easy | Hard (workflow change) |
| Improvement rate | Substitutes improving fast | Stagnant |

**So what**: High substitute threat = articulate clear value over the substitute (not just vs. competitors), make switching from substitute easy, position against the substitute explicitly.

### 5. Threat of New Entrants

| Signal | High Threat | Low Threat |
|--------|-----------|-----------|
| Capital requirements | Low (SaaS, open-source) | High (hardware, regulation) |
| Technical barriers | Low (well-understood tech) | High (proprietary, patents) |
| Network effects | Weak | Strong |
| Distribution | Open (PLG, marketplaces) | Locked (enterprise relationships) |
| Regulation | Permissive | Restrictive (licensing, compliance) |

**So what**: High entry threat = compete on execution speed, build switching costs, invest in brand. Low entry threat = don't get complacent, watch for disruption from adjacent categories.

### Five Forces Summary Table

```
| Force | Rating | Key Driver | Strategic Implication |
|-------|--------|-----------|----------------------|
| Rivalry | H/M/L | [why] | [what to do] |
| Supplier Power | H/M/L | [why] | [what to do] |
| Buyer Power | H/M/L | [why] | [what to do] |
| Substitutes | H/M/L | [why] | [what to do] |
| New Entrants | H/M/L | [why] | [what to do] |

Industry Attractiveness: [High / Medium / Low]
```

---

## Part 3: PESTLE Analysis

Assess macro-environmental factors. The rule: **cite data, not vibes.** "AI is a trend" is useless. "ChatGPT reached 100M users in 2 months, and enterprise AI spending grew 38% YoY in 2024 (IDC)" is useful.

### For Each Factor, Provide:

| Factor | Specific Trend/Event | Impact on Us (H/M/L) | Opportunity or Threat? | Required Action |
|--------|---------------------|----------------------|----------------------|-----------------|

### Political
Government policies, trade regulations, political stability, tax incentives, sanctions.
- Be specific to your market and geography
- Include regulatory direction (not just current state)

### Economic
GDP growth, interest rates, inflation, consumer spending, VC funding climate, enterprise budgets.
- How does the current economic environment affect buying decisions?
- Are customers expanding or cutting budgets in your category?

### Social
Demographic shifts, cultural attitudes, workforce trends, consumer behavior changes.
- Remote work adoption, generational preferences, trust dynamics
- "Social" doesn't mean "social media" — it means societal trends

### Technological
Emerging technologies, infrastructure changes, platform shifts, AI/ML capabilities.
- What technology shifts create new possibilities or threats?
- What platform changes (mobile, cloud, AI) could restructure the market?

### Legal
Data privacy (GDPR, CCPA, etc.), employment law, IP protection, industry-specific regulation.
- Compliance costs and timelines
- Regulatory trends that could create moats or barriers

### Environmental
Sustainability requirements, carbon reporting, ESG expectations.
- Relevant mainly for hardware, supply chain, energy-intensive computing, or B2B selling to ESG-conscious enterprises

---

## Part 4: SWOT Analysis (With Mandatory "So What")

The classic SWOT is often useless because teams list items without deriving actions. Every item MUST have an action.

### Format

```
| Category | Item | Evidence | So What (Action) |
|----------|------|----------|-------------------|
| Strength | [specific strength] | [data/proof] | [how to leverage] |
| Weakness | [specific weakness] | [data/proof] | [how to address or mitigate] |
| Opportunity | [specific opportunity] | [market signal] | [how to capture] |
| Threat | [specific threat] | [market signal] | [how to defend] |
```

### Cross-Reference Matrix

After listing items, cross-reference for strategic insights:

| | Strengths | Weaknesses |
|---|-----------|-----------|
| **Opportunities** | **ATTACK**: Use strengths to capture opportunities | **IMPROVE**: Shore up weaknesses to seize opportunities |
| **Threats** | **DEFEND**: Use strengths to mitigate threats | **AVOID**: Weaknesses + threats = danger zones. Fix or exit. |

### Anti-Patterns
- **Strength: "Great team"** — Not specific, not defensible. What specifically can your team do that others can't?
- **Weakness: "Limited resources"** — Every startup has limited resources. What SPECIFIC capability gap blocks your strategy?
- **Opportunity: "Growing market"** — Markets grow for competitors too. What specific shift favors YOUR approach?
- **Threat: "Big tech could enter"** — They could enter any market. What specific signal suggests they will, and how would their entry specifically affect you?

---

## Part 5: Ansoff Matrix (Growth Direction)

Use when evaluating growth options. Fill each quadrant with specific, actionable opportunities.

```
                    EXISTING PRODUCTS          NEW PRODUCTS
                 ┌─────────────────────┬─────────────────────┐
EXISTING         │  MARKET PENETRATION │ PRODUCT DEVELOPMENT │
MARKETS          │  Risk: Low          │ Risk: Medium        │
                 │  Timeline: 6-12 mo  │ Timeline: 12-18 mo  │
                 │                     │                     │
                 │  [specific plays]   │  [specific plays]   │
                 ├─────────────────────┼─────────────────────┤
NEW              │  MARKET DEVELOPMENT │   DIVERSIFICATION   │
MARKETS          │  Risk: Medium       │ Risk: High          │
                 │  Timeline: 12-24 mo │ Timeline: 24+ mo    │
                 │                     │                     │
                 │  [specific plays]   │  [specific plays]   │
                 └─────────────────────┴─────────────────────┘
```

**Strategic sequencing rule**: Master one quadrant before expanding to the next. Market penetration first (prove the core), then product development OR market development (not both), then diversification only when the core is dominant.

### Per Quadrant, Document:
- 2-3 specific opportunities
- Required investment and capabilities
- Expected timeline and revenue impact
- Risks and mitigation
- Success metrics

---

## Competitive Analysis Output Checklist

Before delivering competitive analysis, verify:

- [ ] Used WebSearch for current data (not relying on memory)
- [ ] Every competitor has specific, cited data points (pricing, funding, features)
- [ ] Competitive dynamics are analyzed, not just individual profiles
- [ ] Porter's Five Forces ratings are justified with evidence
- [ ] PESTLE cites specific data, not vague trends
- [ ] Every SWOT item has a "so what" action
- [ ] Analysis leads to clear strategic implications
- [ ] Gaps and assumptions are flagged with confidence levels

---

## Further Reading

- Competitive Strategy — Michael Porter
- Blue Ocean Strategy — W. Chan Kim & Renee Mauborgne
- The Innovator's Dilemma — Clayton Christensen
- Playing to Win — A.G. Lafley & Roger Martin
