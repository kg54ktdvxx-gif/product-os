---
name: growth-engines
description: "Growth loop design, North Star Metric framework, and Product-Led Growth playbook. Covers viral, content, paid, and sales loops with quantitative modeling. Includes activation optimization, free-to-paid conversion, expansion revenue, and product-led sales hybrid motions."
---

# Growth Engines

## Overview

This skill covers the three pillars of sustainable growth: growth loops that compound over time, North Star Metrics that align the organization, and Product-Led Growth mechanics that use the product itself as the acquisition and conversion engine.

Growth tactics (a blog post, a Product Hunt launch, a referral bonus) are components. Growth engines are the systems that connect them into repeatable, measurable loops. This skill designs engines, not tactics.

## When to Use

- Designing growth mechanisms for a new or existing product
- Choosing and validating a North Star Metric
- Building PLG motions: free-to-paid conversion, self-serve onboarding, expansion revenue
- Reducing reliance on paid acquisition
- Diagnosing why growth has stalled
- Transitioning from sales-led to product-led (or adding PLG as a layer)

---

## Part 1: Growth Loops

A growth loop is a closed system where the output of one cycle becomes the input of the next. Unlike funnels (which leak and need refilling), loops compound. Every growth investment should be evaluated as a loop: does the output feed back in?

### Loop Anatomy

Every growth loop has four components:

1. **Input**: What triggers the loop? (new user, content created, purchase made)
2. **Action**: What does the user do? (creates content, invites colleague, completes project)
3. **Output**: What result is produced? (shareable artifact, referral, data that improves product)
4. **Reinvestment**: How does the output become the next input? (shared content attracts new users, referral becomes a new input)

### The Four Loop Types

#### 1. Viral Loops
Users create artifacts in the product that get shared externally, bringing new users back.

**Mechanism**: User creates in-product → artifact is shared externally (email, social, embed) → viewer sees artifact → viewer signs up to create their own

**Quantitative model**:
- Users per cycle: N
- Artifacts created per user per cycle: A
- Share rate (% of artifacts shared externally): S
- View-to-signup conversion rate: C
- **Loop coefficient** = A x S x C
- **Cycle time**: Time from signup to first share

**Strong example — Loom**:
- User records a video (A = 3 videos/week)
- 80% of videos are shared via link (S = 0.80)
- 5% of unique viewers sign up (C = 0.05)
- Loop coefficient = 3 x 0.80 x 0.05 = 0.12
- Every 100 users generate 12 new users per week
- Cycle time: ~3 days (record on Monday, colleague signs up by Thursday)

**Weak example — "Go viral on TikTok"**:
- No specific creation mechanism tied to product usage
- Share rate depends on content quality, not product value
- No conversion path from viewer to user
- Loop coefficient: undefined (this is not a loop, it is a prayer)

**Requirements**: Product must create shareable artifacts as a natural part of usage. Sharing must benefit the sharer (not feel like spam). The artifact must demonstrate product value to the viewer.

#### 2. Content Loops
Users or the company create content that attracts new users via search or social discovery.

**Mechanism**: Content created → indexed by search engines / shared on social → discovered by potential users → user signs up → (optionally) creates more content

**Quantitative model**:
- Content pieces per month: P
- Average monthly organic traffic per piece (after 6 months): T
- Traffic-to-signup conversion rate: C
- **Monthly new users from content** = P x T x C
- This is technically a flywheel (linear scaling, not exponential) unless users create content too

**Strong example — HubSpot**:
- 100+ blog posts per month (P = 100)
- Average post gets 500 monthly visits after 6 months (T = 500)
- 2% conversion to free tool signup (C = 0.02)
- Monthly new users from content = 100 x 500 x 0.02 = 1,000
- Content compounds: older posts keep generating traffic

**Weak example — "Start a blog"**:
- No keyword strategy
- No conversion mechanism (no CTA, no free tool, no lead magnet)
- No distribution plan beyond "publish and hope"
- Expected traffic per post: ~10 visits/month

**Requirements**: Searchable problem space with keyword volume. Ability to create content consistently. Clear conversion path from content reader to product user.

#### 3. Paid Loops
Revenue from customers funds acquisition of new customers, creating a self-funding growth engine.

**Mechanism**: Acquire customer via paid channel → customer generates revenue → portion of revenue reinvested in acquisition → acquire more customers

**Quantitative model**:
- Revenue per customer per period: R
- % of revenue reinvested in acquisition: I
- CAC per new customer: CAC
- **Loop coefficient** = (R x I) / CAC
- Loop is sustainable when coefficient >= 1.0
- Loop is profitable when coefficient > 1.0

**Strong example — SaaS with 3:1 LTV:CAC**:
- Monthly revenue per customer: $200
- Reinvestment rate: 30% ($60/customer/month)
- CAC: $400
- After 7 months, each customer has funded their own replacement plus margin
- Loop coefficient over 12 months = ($200 x 12 x 0.30) / $400 = 1.8

**Weak example — VC-funded blitz scaling**:
- CAC = $500, monthly revenue = $20, payback = 25 months
- Funded by venture capital, not revenue
- Not a loop — it is a burn rate with a growth label

**Requirements**: Unit economics must work (LTV > 3x CAC). Payback period must be < 12 months for the loop to spin fast enough. Must have predictable paid channels (not just "spend more on Facebook").

#### 4. Sales Loops
Happy customers become references, case studies, and referral sources that reduce CAC for future customers.

**Mechanism**: Close customer → customer achieves success → customer provides case study / reference / referral → case study / reference accelerates next deal → close next customer faster

**Quantitative model**:
- Customers willing to be references: R% of total
- Deals influenced by references per quarter: D
- CAC reduction from reference-influenced deals: CR%
- **Loop impact** = D x CR% x average CAC = CAC savings per quarter

**Strong example — Salesforce**:
- Every enterprise customer has a dedicated success manager
- Success → case study → used in 40% of new enterprise deals
- Reference-influenced deals close 30% faster with 20% higher close rate
- Effective CAC reduction: 25% on reference-influenced deals

**Requirements**: Customer success function that drives measurable outcomes. Willingness of customers to be public references. Sales process that can incorporate references at the right moment.

### Loop Prioritization

| Factor | Viral | Content | Paid | Sales |
|--------|-------|---------|------|-------|
| Speed to results | Medium (3-6 mo) | Slow (6-12 mo) | Fast (days) | Slow (6-12 mo) |
| Compound effect | Exponential | Linear-to-compound | Linear | Linear |
| Capital required | Low | Medium | High | High |
| Product dependency | Very high | Low | Low | Medium |
| Defensibility | High (network effects) | Medium (SEO moats) | Low (anyone can bid) | High (relationships) |

**Prioritize**: Choose the loop with the highest coefficient AND the shortest cycle time that your product can support today. Do not design a viral loop for a product with no shareable artifacts.

---

## Part 2: North Star Metric

The North Star Metric (NSM) is a single, customer-centric KPI that reflects the value your product delivers and serves as a leading indicator of long-term business success.

### What the NSM is NOT

These are the most common mistakes. Reject any candidate that falls into these traps.

- **NSM is NOT revenue.** Revenue is a lagging indicator. It tells you what happened, not what will happen. Revenue can grow while value delivery collapses (price increases, annual contracts masking churn).
- **NSM is NOT a vanity metric.** Total registered users, page views, app downloads — these measure volume without value. A million signups with 2% activation is not success.
- **NSM is NOT an OKR.** OKRs are time-bound targets. The NSM is a persistent measure of value delivery. You can SET an OKR to improve the NSM, but they are different constructs.
- **NSM is NOT DAU/MAU by default.** DAU only works as an NSM if daily active use IS the value delivery (social networks, communication tools). For a tax preparation app, DAU is meaningless — annual completions matter.
- **NSM is NOT multiple metrics.** "North Stars" (plural) defeats the purpose. One metric forces prioritization. If everything is a priority, nothing is.

### The Three Business Games

Before selecting an NSM, classify your product into one of three games. The game determines what kind of metric makes sense.

#### 1. The Attention Game
Your product monetizes user time and attention. More engagement = more value for users AND the business.

| Company | North Star | Why |
|---------|-----------|-----|
| Spotify | Time spent listening | Listening = value delivery. More listening → more data → better recommendations → more listening |
| YouTube | Minutes watched | Watch time = content consumption = ad revenue. Better than "views" because it rewards quality |
| TikTok | Time spent in feed | Feed engagement = content discovery = creator incentive → more content → more engagement |

#### 2. The Transaction Game
Your product facilitates transactions. More transactions = more value delivered and captured.

| Company | North Star | Why |
|---------|-----------|-----|
| Airbnb | Nights booked | A booked night = value delivered to both host and guest. Better than "searches" or "listings" |
| Shopify | GMV (Gross Merchandise Value) | Merchant revenue = merchant success = Shopify's success |
| Uber | Rides completed | Completed ride = value delivered. Better than "rides requested" (includes cancellations) |

#### 3. The Productivity Game
Your product helps users accomplish tasks more efficiently. More tasks completed efficiently = more value.

| Company | North Star | Why |
|---------|-----------|-----|
| Slack | Messages sent in channels with 3+ participants | Multi-person channel messages = team collaboration = core value. Excludes DMs that could happen over email |
| Notion | Weekly active teams creating content | Team content creation = adoption beyond individual use = stickiness |
| Figma | Weekly active editors in shared files | Shared editing = collaboration = the reason to use Figma over local tools |

### Seven Validation Criteria

Score every NSM candidate against all seven. A candidate that fails any criterion should be rejected.

1. **Easy to Understand**: Can a new hire explain what this metric measures in one sentence?
2. **Customer-Centric**: Does this metric directly reflect value delivered to customers (not just company revenue)?
3. **Sustainable Value**: Does improving this metric create long-term habits, not just short-term spikes?
4. **Vision Alignment**: Does this metric represent progress toward the company's stated mission?
5. **Quantitative**: Is there a clear, unambiguous way to compute this number from existing data?
6. **Actionable**: Can product, engineering, and marketing teams take specific actions to improve it?
7. **Leading Indicator**: Does an increase in this metric predict future revenue growth (with evidence or strong reasoning)?

### Input Metrics

For every NSM, define 3-5 input metrics that are the levers driving it. Input metrics should be:
- **MECE**: Together, they explain nearly all movement in the NSM
- **Ownable**: Each input metric can be assigned to a specific team
- **Actionable**: Teams can run experiments to move each input metric
- **Measurable**: Can be tracked weekly or more frequently

**Example — Spotify (NSM: Time Spent Listening)**:
1. New user activation rate (% of signups who listen to 10+ songs in week 1)
2. Weekly active listeners (retained users returning each week)
3. Average session length (depth of each listening session)
4. Playlist creation rate (personalization → longer sessions)
5. Podcast adoption rate (new content format → incremental listening time)

### Counter-Metrics

For every NSM, define 1-2 counter-metrics that prevent Goodhart's Law ("when a measure becomes a target, it ceases to be a good measure").

**Example**: If NSM is "messages sent," the counter-metric might be "% of messages read" — preventing gaming via notification spam.

---

## Part 3: Product-Led Growth (PLG) Playbook

PLG is a GTM motion where the product itself drives acquisition, activation, conversion, and expansion. It is not "freemium" — it is a comprehensive go-to-market strategy.

### The PLG Funnel

Unlike sales-led funnels (marketing → MQL → SQL → close), PLG funnels are:

1. **Awareness**: User discovers product (content, referral, search)
2. **Signup**: User creates account (minimal friction — email only, or SSO)
3. **Activation**: User reaches "aha moment" — experiences core value for the first time
4. **Engagement**: User returns repeatedly, builds habits
5. **Conversion**: User hits a limit or need that triggers upgrade to paid
6. **Expansion**: User brings colleagues, increases usage, upgrades tier

### Activation: The Most Important Metric in PLG

Activation rate is the percentage of signups who reach the "aha moment" — the first experience of core value. This is the single highest-leverage metric in PLG because:
- Users who activate retain 3-5x better than those who do not
- Activation is the first step in every growth loop
- Improving activation has compound effects on every downstream metric

#### Finding the Aha Moment
The aha moment is NOT "completed onboarding." It is the specific action after which retention curves flatten (users stop churning at the same rate).

**Method**:
1. Pull cohort data: retention curves for users who did/did not perform specific actions in week 1
2. Find the action with the largest retention gap between "did" and "did not" groups
3. Validate with qualitative interviews: "When did you first realize this was valuable?"

**Examples**:
| Product | Aha Moment | Evidence |
|---------|-----------|----------|
| Dropbox | Install + save one file | Users who saved a file in week 1 retained at 2x the rate |
| Slack | Team sends 2,000 messages | Teams crossing this threshold had 93% retention |
| Facebook | 10 friends in 14 days | Users with 10 friends in 2 weeks became permanent users |
| Zoom | Host first meeting with 3+ participants | First successful multi-person meeting drove retention |

#### Optimizing Time-to-Value
Time-to-value is the elapsed time from signup to aha moment. Every hour of delay increases drop-off.

**Tactics**:
- **Reduce signup friction**: Name + email only. No phone number, no company name, no credit card.
- **Progressive profiling**: Ask for additional info AFTER the user has experienced value, not before.
- **Pre-configured templates**: Do not start users with a blank canvas. Show them what "done" looks like.
- **Interactive onboarding**: Guide users to the aha moment step-by-step. Measure completion rate of each step.
- **Skip the tutorial**: If possible, design the product so the first action IS the value delivery. Canva's first action is choosing a template — which IS designing.

### Free-to-Paid Conversion

The free tier is not charity — it is a conversion engine. Design limits that create natural upgrade moments.

#### Conversion Levers

| Lever | Mechanism | Example |
|-------|-----------|---------|
| Usage limits | Cap volume/frequency of core action | Dropbox: 2GB free, need more → pay |
| Collaboration limits | Free for individuals, pay for teams | Figma: 3 free projects, teams need Pro |
| Feature gates | Advanced features behind paywall | Notion: free for personal, pay for team workspace |
| Admin / security | Enterprise controls require paid tier | Slack: SSO, compliance, audit logs are paid |
| Support | Free = community, paid = priority support | Most SaaS products |
| History / storage | Limited retention on free tier | Slack: 90-day message history on free |

#### Conversion Design Principles
1. **Free must deliver real value** — if free users are unhappy, they will not convert, they will leave
2. **Upgrade trigger must be a natural workflow moment** — "you have hit your limit" at the moment the user needs more, not a random upsell popup
3. **Make the paid value obvious before the wall** — show what is behind the paywall (grayed out features, "upgrade to unlock" previews)
4. **Trial the paid tier** — let users experience paid features for 14 days so the downgrade feels like a loss

#### Conversion Benchmarks
| Model | Typical Free-to-Paid Rate | Good | Great |
|-------|--------------------------|------|-------|
| Freemium (broad free) | 2-5% | 5-7% | 7-10% |
| Free trial (14-30 day) | 15-25% | 25-40% | 40-60% |
| Reverse trial (start paid, downgrade to free) | 25-40% | 40-50% | 50-65% |
| Usage-based (pay as you grow) | 10-20% | 20-30% | 30%+ |

### Expansion Revenue

Expansion revenue (upselling and cross-selling existing customers) is the hallmark of efficient growth. Net Dollar Retention > 110% means you grow even without new customers.

#### Expansion Models

| Model | Mechanism | Best For |
|-------|-----------|----------|
| Seat-based | More users = higher bill | Collaboration tools (Slack, Figma) |
| Usage-based | More usage = higher bill | Infrastructure (AWS, Twilio, Snowflake) |
| Feature-based | Higher tier = more features | Product suites (HubSpot, Salesforce) |
| Platform | New modules / products | Ecosystem plays (Atlassian, Microsoft) |

#### Product-Led Sales (PLG + Sales Hybrid)

When to layer sales on top of PLG:
- **Signal**: Free/self-serve user hits a usage threshold that indicates enterprise-scale need
- **Trigger**: Usage-based signals (10+ users in one company, usage spike, admin feature inquiry)
- **Handoff**: Sales reaches out with context ("I noticed your team has been using X — want help with Y?")
- **Do NOT**: Cold-call free users who are happily self-serving. Only engage when signals indicate expansion potential or risk.

**PQL (Product-Qualified Lead) criteria**:
- Number of active users in the same company domain
- Usage volume approaching or exceeding free tier limits
- Engagement with paid feature previews or pricing page visits
- Admin/security feature inquiries
- Usage pattern matching ICP of high-LTV customers

---

## Output Format

When executing this skill, deliver:

1. **Growth Loop Design** — primary and secondary loops with quantitative estimates (coefficient, cycle time)
2. **North Star Metric** — with validation against 7 criteria, input metrics, and counter-metrics
3. **PLG Assessment** — whether PLG is appropriate, and if so: aha moment hypothesis, free-to-paid conversion design, expansion strategy
4. **Growth Model** — spreadsheet-ready projections showing loop impact over 6-12 months
5. **Experiment Backlog** — 5-10 prioritized experiments to validate growth assumptions

## Anti-Patterns

- **"Our growth strategy is content marketing"** — Content is a channel, not a strategy. What content? Distributed where? Converting how? With what measurement?
- **Designing 5 loops at once** — Master one loop before adding complexity. Spreading effort across 5 half-built loops produces zero loops.
- **NSM that changes quarterly** — The NSM is meant to be stable for 1-3 years. If you are changing it every quarter, you have not found the right one.
- **PLG without measuring activation** — If you do not know your activation rate, you do not know if PLG is working. Activation is the first thing to instrument.
- **Expecting immediate results from loops** — Loops compound. Month 1 looks disappointing. Month 6 looks inevitable. Set expectations accordingly.
- **Confusing virality with growth** — A viral moment (Product Hunt, HN front page) is a spike, not a loop. If the spike does not feed into a loop, traffic returns to baseline within a week.

---

## References

- Andrew Chen, *The Cold Start Problem* — network effects and viral growth
- Reforge Growth Series — growth loop frameworks
- Amplitude, *North Star Playbook* — NSM methodology
- Kyle Poyar / OpenView — PLG benchmarks and frameworks
- Lenny Rachitsky — growth loop examples and analysis
