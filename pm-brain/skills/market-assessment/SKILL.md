---
name: market-assessment
description: "Consolidated market assessment knowledge — TAM/SAM/SOM sizing with top-down and bottom-up math, market segmentation by JTBD, user segmentation from behavioral data, user personas, and customer journey mapping. Includes common sizing errors, segmentation with limited data, and journey optimization."
---

# Market Assessment

## Philosophy

Market assessment answers: **Is there a market worth winning, and can we win a meaningful piece of it?**

Bad market assessment: "The global SaaS market is $200B" (irrelevant to your actual opportunity).
Good market assessment: "There are approximately 14,000 B2B SaaS companies with 50-500 employees in North America, spending an average of $4,200/year on workflow tools. Our SAM is $58.8M. We can realistically capture 3-5% in year 1 based on our current go-to-market capacity."

**Rules:**
1. Always show the math. Every number needs a source or a formula.
2. Do both top-down AND bottom-up and reconcile the difference.
3. Segment by JTBD, not demographics. "SMBs" is not a segment. "Teams that need to ship marketing assets without a designer on staff" is a segment.
4. Market sizing is not a one-time exercise. Update as you learn.

---

## Part 1: Market Sizing (TAM / SAM / SOM)

### Definitions

- **TAM (Total Addressable Market)**: The total revenue opportunity if you captured 100% of the market. This is the ceiling — useful for investors, not for planning.
- **SAM (Serviceable Addressable Market)**: The portion of TAM you can realistically reach with your current product, geography, language, channels, and pricing. This is your ACTUAL market.
- **SOM (Serviceable Obtainable Market)**: The realistic share of SAM you can capture in 1-3 years given your go-to-market capacity, brand awareness, and competitive position. This is your PLAN.

### Top-Down Estimation

Start from a known market size and narrow down.

```
TAM = Industry market size (from analyst reports, government data, trade associations)
SAM = TAM x % applicable to your product/geo/segment
SOM = SAM x realistic market share (typically 1-5% for new entrants)
```

**Example:**
```
TAM: US project management software market = $6.7B (Gartner 2024)
SAM: Product teams at tech companies (50-500 employees) = ~18% of market = $1.2B
SOM: Realistic year-1 capture at 2% of SAM = $24M
```

**Weakness of top-down**: Analyst reports often inflate markets, include adjacent categories, and use different definitions. Always cross-validate.

### Bottom-Up Estimation

Build from unit economics.

```
SOM = (Number of reachable target customers) x (Realistic conversion rate) x (Annual revenue per customer)
SAM = (Total target customers in your segment) x (Annual revenue per customer)
TAM = (All potential customers across all segments) x (Annual revenue per customer)
```

**Example:**
```
Target companies fitting our ICP: 14,000 (from LinkedIn Sales Navigator filter)
Reachable via our channels in year 1: 4,200 (30% based on content reach)
Expected conversion rate: 3% (based on comparable PLG benchmarks)
Paying customers year 1: 126
Average ACV: $3,600 (Pro plan at $300/month)
SOM: 126 x $3,600 = $453,600

Total target companies: 14,000
SAM: 14,000 x $3,600 = $50.4M
```

### Reconciliation

Top-down and bottom-up rarely match. The DIFFERENCE is informative:

- **Bottom-up >> top-down**: Your market definition is too narrow, OR your pricing is high relative to the market
- **Top-down >> bottom-up**: Your reachable market is small relative to the total opportunity, OR your conversion assumptions are conservative (or the analyst report is inflated)
- **Within 2x of each other**: Reasonable alignment; use bottom-up for planning, top-down for context

### Market Sizing Anti-Patterns

1. **Confusing TAM with revenue opportunity**: "Our TAM is $50B" means nothing for a seed-stage startup. Your SOM is what matters.
2. **Using TAM to justify anything**: "Even 1% of a $50B market is $500M!" This is not analysis — it's wishful thinking. WHY would you get 1%? What's your distribution? What's your conversion rate?
3. **Analyst report pass-through**: Copying a Gartner/Forrester number without validating methodology. Analyst reports define markets differently than you do. Read the methodology section.
4. **Static sizing**: Markets aren't fixed. Size the market today AND project 2-3 years out. Include growth drivers and potential contractions.
5. **Revenue-only sizing**: Some markets are better sized by VOLUME (users, transactions, events) than revenue. Usage-based businesses should think in units, not dollars.
6. **Ignoring existing spend**: If your target customers currently spend $0 on this problem (they use spreadsheets, or just don't solve it), your TAM calculation needs to be bottom-up from willingness-to-pay, not from existing market spend.

### Market Summary Table

```
| Metric | Current | Year 2 | Year 3 | Method | Confidence |
|--------|---------|--------|--------|--------|------------|
| TAM | $ | $ | $ | [source] | H/M/L |
| SAM | $ | $ | $ | [formula] | H/M/L |
| SOM | $ | $ | $ | [formula] | H/M/L |
| Target customers | # | # | # | [source] | H/M/L |
| Avg revenue/customer | $ | $ | $ | [basis] | H/M/L |
```

---

## Part 2: Market Segmentation

### Segment by JTBD, Not Demographics

**Wrong**: "Our segments are SMBs, mid-market, and enterprise."
These are company sizes, not segments. A 50-person startup and a 50-person law firm have completely different jobs-to-be-done.

**Right**: Segments defined by the PROBLEM they're trying to solve and the CONTEXT in which they solve it.

**Example for a design tool:**
- **Segment A: "Ship without a designer"** — Marketers at companies with 20-100 employees, no design team, creating social media assets and landing pages 3-5x per week.
- **Segment B: "Maintain brand consistency at scale"** — Brand managers at companies with 500+ employees, managing 10+ people who create content, enforcing brand guidelines.
- **Segment C: "Prototype ideas fast"** — Product managers at tech companies, creating mockups for stakeholder buy-in before involving engineering.

### Segmentation Criteria (the 4 tests)

A good segment must be:
1. **Measurable**: You can estimate its size and characteristics
2. **Accessible**: You can reach the segment through identifiable channels
3. **Substantial**: Large enough to justify serving (or strategically important as a beachhead)
4. **Differentiable**: Responds differently to your product/marketing than other segments

### Per-Segment Analysis Template

```
## Segment: [Name]
**Size**: [estimated # of companies/individuals, or % of total market]
**Growth**: [growing, stable, shrinking — and rate]

**Job to Be Done**: When [situation], I want to [action], so that [outcome].
**Frequency**: [how often they do this job]
**Current solution**: [what they use today]
**Willingness to pay**: [evidence or estimate]

**Why THIS segment first?**
- Pain intensity: [acute/moderate/mild]
- Reachability: [channels to reach them]
- Strategic value: [does winning here unlock adjacent segments?]
- Competitive gap: [are competitors underserving this segment?]

**Product fit**: [how well does current product serve them? what's missing?]
```

### Segmentation with Limited Data

When you don't have rich behavioral data (common at early stages):

1. **Interview-based segmentation**: Talk to 15-20 potential customers. After ~10, patterns emerge. Group by shared JTBD and context, not demographics.
2. **Competitor-review mining**: Read G2/Capterra reviews for competitors. Categorize reviewers by their use case and pain points. Segments emerge from how people describe their problems.
3. **Job board analysis**: Search for roles that would use your product. The job descriptions reveal the context, tasks, and tools of your potential segments.
4. **Community analysis**: Reddit, Slack communities, Discord servers, forums. What questions do people ask? What tools do they mention? What workflows do they describe?
5. **Search behavior**: Google Trends, keyword volumes, "People also ask" — reveals how the market frames the problem.

---

## Part 3: User Personas

Personas are segment archetypes brought to life. They make abstract segments concrete and memorable for the team.

### What Makes a Good Persona

**Weak persona**: "Sarah, 32, Marketing Manager. Likes social media. Wants to be more productive." (Generic, demographic-driven, no insight.)

**Strong persona**: "Sarah runs marketing at a 60-person fintech startup. She creates 15+ social media assets per week with Canva because she can't justify hiring a designer. Her biggest frustration: every asset takes 30 minutes because she starts from scratch each time — there's no brand template system, so her team's output looks inconsistent. She'd pay for a tool that let her set up brand templates once and have her team produce on-brand assets in 5 minutes, but only if onboarding takes less than an hour because she doesn't have time for training."

### Persona Template

For each persona (3-5 per product):

```
## [Name] — [one-line descriptor]
**Role**: [job title, team, company type/size]
**Context**: [day-to-day environment, constraints, tools they use]

**Primary JTBD**: When [situation], I want to [action], so that [outcome].
**Frequency**: [how often they encounter this job]

**Top 3 Pain Points**:
1. [Specific pain] — [impact and severity]
2. [Specific pain] — [impact and severity]
3. [Specific pain] — [impact and severity]

**Top 3 Desired Gains**:
1. [Outcome they want] — [how they'd measure success]
2. [Outcome they want] — [how they'd measure success]
3. [Outcome they want] — [how they'd measure success]

**Current solution**: [what they use today, what it costs, what they hate about it]
**Switching trigger**: [what would make them try something new?]
**Adoption barrier**: [what would prevent them from switching?]

**Unexpected insight**: [counterintuitive finding from research]

**Product fit**: [how well current product serves this persona, what's missing]
```

### Persona Anti-Patterns

- **Demographic-only personas**: Age, location, and hobbies don't predict product behavior. Focus on JTBD and context.
- **Aspirational personas**: Don't create personas for who you WISH your users were. Create them for who your users ARE.
- **Too many personas**: 3-5 is ideal. More than 7 means you haven't prioritized.
- **Persona without data**: If a persona isn't grounded in research (interviews, usage data, reviews), it's fiction. Label it as a hypothesis and validate.
- **Static personas**: Update personas as you learn. V1 personas from pre-launch should look different from V2 personas based on actual user behavior.

---

## Part 4: Customer Journey Mapping

Map the end-to-end experience from awareness through advocacy. The goal: find the moments where you win or lose customers.

### Journey Stages

| Stage | Key Question | Critical Metric |
|-------|-------------|-----------------|
| **Awareness** | How do they learn you exist? | Reach, impressions, brand recall |
| **Consideration** | What do they evaluate? What do they compare you to? | Website visits, comparison page views |
| **Acquisition** | How do they sign up or purchase? | Conversion rate, CAC |
| **Onboarding** | How quickly do they get to value? (Time-to-value) | Activation rate, time to first value |
| **Engagement** | How deeply and frequently do they use the product? | DAU/MAU, feature adoption, session depth |
| **Retention** | What keeps them? What might cause churn? | Retention cohorts, NRR, churn rate |
| **Advocacy** | When and why do they recommend you? | NPS, referral rate, reviews written |

### Per-Stage Documentation

For each stage:

```
| Element | Details |
|---------|---------|
| **Touchpoints** | [where user interacts: website, email, in-app, support, social] |
| **User actions** | [what they do] |
| **User thoughts** | [what they're thinking: "Is this worth my time?", "How does this compare to X?"] |
| **Emotions** | [excited, confused, frustrated, delighted, anxious] |
| **Pain points** | [friction, confusion, drop-off risks] |
| **Opportunities** | [how to improve experience at this point] |
```

### Critical Moments to Identify

1. **Aha Moment**: When does the user first experience core value? (Example: Slack — when your team has its first real conversation in a channel. Dropbox — when you access a file from a second device.)
2. **Moments of Truth**: Decision points where users commit or abandon. (Free trial day 1. First time product doesn't work as expected. First renewal.)
3. **Churn Triggers**: Where and why do users most commonly leave? (Failed onboarding. Unresponsive support. Competitor outreach. Budget review.)

### Journey Map Output Format

```
| Stage | Touchpoint | User Action | Emotion | Pain Point | Opportunity | Priority |
|-------|-----------|-------------|---------|------------|-------------|----------|
```

### Journey Optimization Priorities

After mapping, prioritize improvements by:
1. **Highest drop-off stages**: Where are you losing the most users?
2. **Highest-value moments**: Where does the user's perception of value form?
3. **Quickest wins**: What friction can be removed with minimal effort?
4. **Strategic alignment**: Which improvements reinforce your competitive positioning?

---

## Integrating Assessment Components

These four components feed each other:

```
Market Sizing → "Is the market big enough to matter?"
     ↓
Market Segmentation → "Which segments are most attractive?"
     ↓
User Personas → "Who specifically are we building for?"
     ↓
Customer Journey → "What's their experience from awareness to advocacy?"
     ↓
→ Back to Market Sizing: refine SOM based on journey conversion rates
```

### Red Flags in Market Assessment

- TAM cited without methodology = unreliable
- Segments defined only by company size = lazy segmentation
- Personas without research backing = fiction
- Journey maps without drop-off data = wishful thinking
- No bottom-up sizing = no grounding in reality
- Market "growing rapidly" without a specific rate = hand-waving

---

## Further Reading

- Crossing the Chasm — Geoffrey Moore
- The Mom Test — Rob Fitzpatrick
- Competing Against Luck — Clayton Christensen
- Obviously Awesome — April Dunford
- Inspired — Marty Cagan
