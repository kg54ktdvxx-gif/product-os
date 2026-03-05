---
name: gtm-strategy
description: "Full go-to-market strategy framework: beachhead identification, ICP definition, channel strategy, messaging, GTM motion selection, and launch planning. Consolidates beachhead-segment, ideal-customer-profile, gtm-strategy, and gtm-motions into a single end-to-end GTM planning skill."
---

# GTM Strategy

## Overview

This skill covers the complete go-to-market strategy process: from identifying your beachhead market segment through defining your ideal customer profile, selecting the right GTM motion, choosing channels, crafting messaging, and building a launch plan with success metrics.

A GTM strategy is not a marketing plan. It is the deliberate choice of who to serve first, how to reach them, what to say, and how to measure whether it is working. Every decision cascades from the beachhead.

## When to Use

- Planning a new product launch from scratch
- Entering a new market segment or geography
- Repositioning after a pivot or major product change
- Creating a GTM plan for a new feature or tier
- Evaluating whether to change your GTM motion (e.g., sales-led to PLG)
- Choosing your first customers when starting from zero

---

## Part 1: Beachhead Segment Selection

Your beachhead is the single market segment you will dominate first. It is not your total addressable market. It is the smallest group of customers who share the same pain, talk to each other, and will become your reference base for expansion.

### Selection Criteria

Evaluate every candidate segment against four criteria. Score each 1-5 and multiply — a segment must score well on ALL four, not just one or two.

#### 1. Burning Pain (Weight: High)
- The problem is daily, not annual
- Current workarounds are expensive, fragile, or embarrassing
- The cost of inaction is increasing (regulatory pressure, competitive threat, scaling pain)
- Users will describe the problem unprompted in interviews
- **Red flag**: If prospects say "that would be nice to have," this is not a burning pain

#### 2. Willingness to Pay (Weight: High)
- Budget exists or can be created (ROI justifies new budget)
- Decision-maker has authority to approve without committee
- Price point matches perceived value of problem
- No free alternative that is "good enough" (beware open source and spreadsheets)
- **Red flag**: If "we would use it if it were free" — willingness to use is not willingness to pay

#### 3. Winnability (Weight: Medium)
- You can reach 60-70% of the segment in 12-18 months
- Competitors are absent, complacent, or poorly positioned for this segment
- You have a structural advantage (technology, distribution, expertise, brand)
- Segment is small enough to dominate but large enough to matter ($5M-50M SAM is typical for a beachhead)
- **Red flag**: If you need to outspend an incumbent to win, this is not winnable

#### 4. Referral Potential (Weight: Medium)
- Customers in this segment talk to each other (conferences, Slack groups, subreddits)
- Solving the problem for one customer creates demand from their peers
- Success stories in this segment are credible to adjacent segments
- Network effects or collaboration features amplify word-of-mouth
- **Red flag**: If customers are isolated and never discuss tools, referral potential is zero

### Concrete Beachhead Examples

| Company | Beachhead | Why It Worked |
|---------|-----------|---------------|
| Slack | Game development studios | Small teams, high collaboration needs, tech-forward, strong referral networks at GDC |
| Facebook | Harvard students | Dense social graph, strong identity, FOMO-driven adoption, natural expansion to other Ivies |
| Stripe | Developer side projects | Developers choose tools, no procurement process, massive word-of-mouth in dev communities |
| Figma | Small design agencies | Collaboration pain acute, no budget for enterprise tools, designers talk to designers |
| HubSpot | Marketing teams at SMBs (10-50 employees) | Inbound philosophy resonated, free tools drove adoption, marketers are vocal community |

### Process

1. **List 5-10 candidate segments** using firmographic + behavioral dimensions (not just industry)
2. **Score each** on the four criteria (1-5 scale, be honest — use interview data, not assumptions)
3. **Multiply scores** (not add — a zero on any dimension kills the segment)
4. **Validate the top 2-3** with at least 10 customer discovery interviews per segment
5. **Select one** — singular focus wins. Do not hedge with "we will serve segments A, B, and C"

---

## Part 2: Ideal Customer Profile (ICP)

The ICP is the detailed description of your best-fit customer within the beachhead. It is not a demographic list — it is a decision-making guide that tells sales, marketing, and product who to prioritize.

### ICP Framework

#### Demographics / Firmographics
- Company size (employees AND revenue — they tell different stories)
- Industry vertical and sub-vertical
- Geographic region and any regulatory context
- Company stage (seed, Series A-C, growth, public)
- Technology stack and infrastructure maturity
- Department and reporting structure of the buyer

#### Behaviors
- How they discover solutions (Google search, peer recommendations, analyst reports, communities)
- Buying process: who initiates, who evaluates, who approves, who blocks
- Decision timeline: days (self-serve) vs weeks (committee) vs months (enterprise procurement)
- Tool adoption style: early adopter, fast follower, or laggard
- Switching behavior: how often they change tools and what triggers a switch

#### Jobs to Be Done (JTBD)
- **Functional JTBD**: What task are they trying to accomplish? (e.g., "reduce time spent on manual data entry from 10 hours/week to 1 hour/week")
- **Emotional JTBD**: How do they want to feel? (e.g., "confident that my reports are accurate before presenting to the board")
- **Social JTBD**: How do they want to be perceived? (e.g., "seen as the person who modernized our team's workflow")
- **Success metrics**: How do THEY measure whether the job is done well?

#### Needs and Pain Points
- Top 3-5 specific pain points with quantified impact (hours lost, revenue at risk, error rates)
- Current workarounds and their costs (both financial and emotional)
- Barriers to solving the problem (budget, politics, technical debt, inertia)
- What they have tried before and why it failed

#### Disqualification Criteria
Equally important — who is NOT a good fit:
- Too small to afford the product
- Too large to get value from your current feature set
- In a regulated industry you cannot serve yet
- Using a deeply embedded competitor they will not switch from
- Buying for a use case your product does not address

---

## Part 3: GTM Motion Selection

The GTM motion is how you acquire and expand customers. The right motion depends on your average selling price (ASP), product complexity, and buyer type.

### Motion Decision Framework

| Signal | Product-Led (PLG) | Sales-Led | Community-Led | Partner-Led |
|--------|-------------------|-----------|---------------|-------------|
| ASP | < $10K/yr | > $25K/yr | < $5K/yr | > $50K/yr |
| Buyer | End user (bottom-up) | Executive (top-down) | Practitioner | Channel/reseller |
| Complexity | Low (self-serve) | High (needs demo/POC) | Medium (peer learning) | High (implementation) |
| Sales cycle | Hours to days | Weeks to months | Days to weeks | Months to quarters |
| Best for | High-volume, low-touch | High-value, high-touch | Trust-dependent | Market coverage |

### Product-Led Growth (PLG)
- Users try before they buy — free tier, freemium, or free trial
- Product IS the primary acquisition and conversion engine
- Sales assists (does not drive) high-value deals
- **When to use**: End user has authority to adopt, product value is obvious in < 5 minutes, low switching cost
- **When NOT to use**: Enterprise procurement required, product requires configuration/integration, compliance-heavy industries

### Sales-Led
- Sales team drives pipeline from prospecting through close
- Marketing generates leads; sales converts them
- **When to use**: High ASP (> $25K), complex buying committee, product requires demo to understand value
- **When NOT to use**: High volume of small deals, no budget for sales team, product is self-explanatory

### Community-Led
- Community is the primary acquisition channel — users find you through peers
- Content, events, and community programs drive awareness and trust
- **When to use**: Strong practitioner community exists, trust is a key buying factor, product is used by communities of practice (developers, designers, data scientists)
- **When NOT to use**: Target buyers do not participate in communities, product is invisible/back-office

### Partner-Led
- Partners (resellers, consultants, platforms) drive distribution
- Your product is embedded in or sold alongside partner offerings
- **When to use**: Market is fragmented, you need geographic or vertical coverage you cannot build, product is complementary to established platforms
- **When NOT to use**: You need direct customer relationships, margins cannot support partner commissions

### Hybrid Motions
Most successful companies blend motions as they scale:
- **PLG + Sales (Product-Led Sales)**: Free tier acquires users → product usage data identifies expansion opportunities → sales team closes upsell. Atlassian, Slack, and Figma all use this.
- **Community + PLG**: Community builds trust and awareness → PLG converts interested users → community retains and expands. HashiCorp, dbt Labs.
- **Inbound + Outbound**: Content and SEO generate inbound leads → outbound targets high-value accounts that match ICP but have not found you yet. HubSpot's own motion.

---

## Part 4: Channel-Market Fit

Not all channels work for all products. Channel-market fit is as important as product-market fit.

### Channel Selection Framework

| Channel | Best For | Typical CAC | Time to Results | Resource Intensity |
|---------|----------|-------------|-----------------|-------------------|
| SEO / Content | Products with searchable problems | $50-300 | 6-12 months | Medium (writers, SEO) |
| Paid Search (SEM) | High-intent buyers with clear keywords | $100-500 | Days to weeks | Medium (budget + optimization) |
| Paid Social | B2C, consumer apps, awareness | $20-200 | Days to weeks | Medium (creative + budget) |
| LinkedIn (organic) | B2B thought leadership | $0-50 | 3-6 months | Low (time only) |
| LinkedIn (paid) | B2B lead gen with tight targeting | $200-800 | Weeks | High (budget) |
| Product Hunt / launches | Developer tools, consumer apps | $0-20 | Day 1 spike | Low (one-time prep) |
| Community (Reddit, Discord, Slack) | Developer tools, niche products | $10-50 | 3-6 months | Medium (time, authenticity) |
| Partnerships / integrations | Platform-adjacent products | $100-400 | 3-6 months | High (BD, integration work) |
| Outbound sales | Enterprise, high-ASP | $500-2000+ | Weeks to months | High (SDRs, AEs) |
| Referral programs | Products with natural share moments | $20-100 | 1-3 months | Low (program setup) |
| Events / conferences | Industry-specific B2B | $300-1000 | Months | High (booth, travel, content) |

### How to Choose Channels

1. **Start with the buyer's behavior**: Where does your ICP go when they have the problem you solve? That is your channel.
2. **Match channel to ASP**: You cannot afford $800 CAC on a $50/month product. Channel CAC must be < 1/3 of first-year revenue.
3. **Sequence channels**: Start with 1-2 channels. Master them before adding more. Channel sprawl kills startups.
4. **Use WebSearch**: Research competitor GTM strategies, channel benchmarks for your industry, and pricing intelligence. Do not guess — find data.

---

## Part 5: Messaging

### Positioning Statement Template
For [target segment] who [JTBD / pain point], [product] is the [category] that [key benefit]. Unlike [primary alternative], [product] [key differentiator].

**Example**: For Series A SaaS companies who spend 10+ hours per week manually tracking customer onboarding, OnboardFlow is the customer success platform that automates onboarding workflows end-to-end. Unlike spreadsheets and Notion templates, OnboardFlow reduces time-to-value by 60% and cuts churn by 25% in the first 90 days.

### Messaging by Stakeholder

| Stakeholder | Cares About | Message Focus |
|-------------|-------------|---------------|
| End User | Daily workflow improvement | "Save 2 hours per day on [task]" |
| Manager | Team productivity and visibility | "See your entire team's [metric] in one dashboard" |
| Executive | Business impact and ROI | "Reduce [cost] by X% in 90 days" |
| IT / Security | Integration, compliance, security | "SOC 2 compliant, SSO, deploys in < 1 hour" |
| Finance / Procurement | Total cost, contract flexibility | "Transparent pricing, no long-term contracts, ROI in 60 days" |

### Messaging Anti-Patterns
- **Feature-first messaging**: "We have AI-powered analytics" — so what?
- **Superlative claims**: "The most powerful platform" — unverifiable and generic
- **Internal jargon**: "Unified data mesh with semantic layer" — customers do not care about your architecture
- **Benefit without proof**: "Save time" — how much? Compared to what? Prove it.

---

## Part 6: Success Metrics

### Launch Metrics (first 30 days)
| Metric | What It Tells You | Target Range |
|--------|-------------------|--------------|
| Signups / Leads | Top-of-funnel interest | Depends on channel mix |
| Activation rate | % who reach first value moment | > 40% for PLG, > 60% for sales-led |
| Channel attribution | Which channels drive quality | Identifies winners early |
| CAC by channel | Cost efficiency | Must be < 1/3 of first-year revenue |

### Growth Metrics (30-90 days)
| Metric | What It Tells You | Target Range |
|--------|-------------------|--------------|
| Week 1 retention | Early product-market fit signal | > 60% |
| Time to value | How fast users get benefit | < 5 minutes for PLG, < 1 day for sales-led |
| NPS / CSAT | Customer satisfaction | NPS > 30 |
| Pipeline velocity | Sales cycle speed | Decreasing over time |

### Steady-State Metrics (90+ days)
| Metric | What It Tells You | Target Range |
|--------|-------------------|--------------|
| Monthly retention | Product stickiness | > 95% for B2B SaaS |
| Net Dollar Retention | Expansion revenue health | > 110% |
| CAC Payback Period | Unit economics health | < 12 months |
| LTV:CAC Ratio | Growth efficiency | > 3:1 |

---

## Output Format

When executing this skill, deliver:

1. **Beachhead Segment** — with scoring rationale against all four criteria
2. **ICP** — demographics, behaviors, JTBD, pain points, disqualification criteria
3. **GTM Motion** — primary motion with rationale, secondary motion if applicable
4. **Channel Strategy** — 2-4 channels ranked by expected CAC with justification
5. **Positioning & Messaging** — statement, stakeholder-specific messages, proof points
6. **Success Metrics** — launch, growth, and steady-state metrics with targets
7. **90-Day Execution Roadmap** — month-by-month plan with owners and milestones

## Research Instructions

Use WebSearch actively during execution:
- Search for competitor GTM strategies and positioning
- Pull channel benchmark data for the target industry
- Research pricing models of comparable products
- Find community discussions about the problem space (Reddit, HN, industry forums)
- Look for recent analyst reports or market sizing data

Do not rely on assumptions when data is available. Cite sources for all market data and competitive claims.

---

## References

- Geoffrey Moore, *Crossing the Chasm* — beachhead market strategy
- April Dunford, *Obviously Awesome* — positioning framework
- Clayton Christensen, *Competing Against Luck* — Jobs to Be Done theory
- Product Compass GTM frameworks and templates
