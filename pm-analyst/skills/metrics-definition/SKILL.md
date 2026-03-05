---
name: metrics-definition
description: "Define North Star Metrics, input metrics, guardrail metrics, and dashboards with precise operational definitions. Classify the business game (Attention, Transaction, Productivity), validate against 7 criteria, and design audience-appropriate dashboard views."
---

# Metrics Definition

Define metrics with surgical precision. Every metric gets an operational definition — plain English plus SQL pseudocode — so there is never ambiguity about what is being measured, how, or why.

## The Three Business Games

Before defining any metric, classify the business into one of three games (Sean Ellis, *Hacking Growth*). The game determines what your North Star Metric should capture:

### 1. Attention Game
**What it measures**: How much time or attention customers give to your product.
**Who plays it**: Ad-supported businesses, content platforms, social networks.
**Examples**:
| Company | North Star Metric |
|---------|------------------|
| Facebook | Daily Active Users |
| Spotify | Time Spent Listening |
| YouTube | Minutes Watched |
| TikTok | Daily Active Users x Avg Session Duration |
| Netflix | Monthly Hours Streamed per Subscriber |

**NSM pattern**: `[Time-based metric] per [time period]` — captures depth of engagement.

### 2. Transaction Game
**What it measures**: How many transactions flow through your platform.
**Who plays it**: Marketplaces, e-commerce, fintech, SaaS with usage-based pricing.
**Examples**:
| Company | North Star Metric |
|---------|------------------|
| Amazon | Number of Purchases per Month |
| Uber | Weekly Rides Completed |
| Airbnb | Nights Booked |
| Stripe | Payment Volume Processed |
| Shopify | Gross Merchandise Volume |

**NSM pattern**: `[Transaction count or volume] per [time period]` — captures platform velocity.

### 3. Productivity Game
**What it measures**: How efficiently customers accomplish their goals.
**Who plays it**: Workflow tools, collaboration software, developer tools, B2B SaaS.
**Examples**:
| Company | North Star Metric |
|---------|------------------|
| Slack | Messages Sent in Channels per Org per Week |
| Notion | Weekly Active Editors per Workspace |
| Figma | Weekly Collaborative Sessions |
| GitHub | Weekly Code Push Events |
| Canva | Designs Exported per Week |

**NSM pattern**: `[Tasks completed or output created] per [user/team] per [time period]` — captures value delivered.

## The 7 Validation Criteria for a North Star Metric

Every NSM candidate must pass ALL seven criteria:

| # | Criterion | Test Question | Fail Example |
|---|-----------|---------------|--------------|
| 1 | **Measures value delivered** | Does it reflect value the CUSTOMER receives, not just business output? | Revenue (that's value extracted, not delivered) |
| 2 | **Captures vision** | Does improving this metric move toward the company's long-term vision? | "Support tickets resolved" for a product aiming to eliminate support needs |
| 3 | **Leading indicator** | Does improving this metric predict future revenue and growth? | "Quarterly revenue" (lagging — by the time you see it, it's too late) |
| 4 | **Measurable** | Can you actually collect this data reliably today? | "Customer delight score" with no instrumentation |
| 5 | **Controllable** | Can product/engineering/marketing teams influence this metric? | "GDP growth" (real, but you can't move it) |
| 6 | **Not revenue** | Is this metric distinct from revenue or a direct revenue proxy? | "MRR" or "ARPU" (these are outputs, not drivers) |
| 7 | **Not vanity** | Does a change in this metric necessarily mean the product improved? | "Total registered users" (counts the dead along with the living) |

### NSM Anti-Patterns

**NSM is NOT revenue**: Revenue is a lagging indicator of value delivered. If your NSM is "MRR," you've picked a scoreboard metric, not a driver. Revenue follows from delivering value; measure the value.

**NSM is NOT a vanity metric**: "Total users" or "total downloads" only go up. They tell you nothing about whether your product is healthy today. A good NSM can go DOWN, and when it does, that's a signal to act.

**NSM is NOT an OKR**: OKRs are time-bound goals ("increase X by Y% in Q3"). Your NSM is the permanent metric you optimize against. You can SET OKRs around your NSM, but the NSM itself is not an OKR.

**NSM is NOT multiple metrics**: By definition, there is ONE North Star. If you have three, you have zero — because the team will optimize whichever is easiest to move, not whichever matters most.

## Metrics Constellation: NSM + Inputs + Guardrails

A complete metrics framework has three layers:

### Layer 1: North Star Metric (1 metric)
The single metric that captures core value delivery. See above.

### Layer 2: Input Metrics (3-5 metrics)
Metrics that DRIVE the North Star. These are the levers teams pull. They map roughly to the AARRR funnel:

| Input Category | What It Measures | Example |
|---------------|-----------------|---------|
| **Acquisition** | Are new users finding the product? | Weekly new signups from organic channels |
| **Activation** | Are new users experiencing core value? | % of signups who complete onboarding AND perform core action within 7 days |
| **Retention** | Are activated users coming back? | Week-4 retention rate (% of activated users active in week 4) |
| **Revenue** | Are retained users paying? | Monthly expansion revenue per account |
| **Referral** | Are users bringing others? | % of new signups from referral links |

Each input metric should be:
- **Easier to move** in the short term than the NSM itself
- **Directly contributing** to the NSM outcome (causal, not just correlated)
- **Owned by a specific team** that can influence it

### Layer 3: Guardrail Metrics (2-4 metrics)
Metrics that MUST NOT degrade while optimizing the NSM or input metrics. These prevent Goodhart's Law from destroying your product.

| Guardrail | Why It Matters | Example Threshold |
|-----------|---------------|-------------------|
| **Quality** | Optimizing speed shouldn't break the product | Error rate < 0.1%, p99 latency < 2s |
| **Support load** | Growth shouldn't overwhelm support | Support tickets per 1,000 users < 15 |
| **Churn** | Acquisition shouldn't mask retention problems | Monthly logo churn < 3% |
| **User satisfaction** | Engagement hacks shouldn't annoy users | NPS > 40, CSAT > 4.2/5 |

## Metric Definition Precision Protocol

Every metric — whether NSM, input, or guardrail — must be defined with this level of precision:

### The 7 Components of a Complete Metric Definition

```
## Metric: [Name]

**Plain English Definition**: [One sentence a non-technical stakeholder understands]

**Operational Definition**: [SQL pseudocode or exact calculation]

**Numerator**: [For ratios — what's on top]
**Denominator**: [For ratios — what's on bottom]

**Edge Cases**:
- [What counts? What doesn't?]
- [How do you handle X?]

**Known Limitations**:
- [What this metric can't tell you]
- [Situations where it's misleading]

**Data Source**: [Which table/system/event]
```

### Example: Weak vs Strong Metric Definition

**Weak definition**:
> "Daily Active Users — the number of active users per day."

This is circular. What is "active"? Does opening the app count? What about bots? What timezone? This definition will produce arguments.

**Strong definition**:
> **DAU** = `COUNT(DISTINCT user_id) FROM events WHERE event_date = [date] AND event_type IN ('page_view', 'action_performed', 'content_created') AND user_id NOT IN (SELECT user_id FROM internal_users UNION SELECT user_id FROM bot_accounts)`. Excludes sessions shorter than 3 seconds (bounce filter). Timezone: UTC day boundary. Deduplication: by user_id (cross-device users counted once via identity graph). Known limitation: does not capture SDK-only usage (API integrations without UI sessions). Data source: `analytics.events` table, populated by Segment.

### Example: Ratio Metric

**Metric: Week-1 Activation Rate**

**Plain English**: Of users who signed up this week, what percentage completed the core value action within 7 days?

**Operational Definition**:
```sql
-- Numerator: users who signed up AND performed core action within 7 days
SELECT COUNT(DISTINCT s.user_id)
FROM signups s
JOIN events e ON s.user_id = e.user_id
WHERE e.event_type = 'core_action_completed'
  AND e.event_timestamp BETWEEN s.signup_timestamp
      AND s.signup_timestamp + INTERVAL '7 days'

-- Denominator: users who signed up in the period
-- (excluding users who signed up less than 7 days ago — incomplete window)
SELECT COUNT(DISTINCT user_id)
FROM signups
WHERE signup_date <= CURRENT_DATE - INTERVAL '7 days'
```

**Edge Cases**:
- Users who sign up, churn, and re-sign up: count based on FIRST signup only
- Users who performed core action BEFORE signup (e.g., anonymous usage): count as activated
- Signups in last 7 days: EXCLUDED from denominator (incomplete observation window)

**Known Limitations**:
- Does not distinguish between users who activated on day 1 vs day 7 (time-to-activate is a separate metric)
- "Core action" may need redefinition as the product evolves

**Data Source**: `signups` table + `analytics.events` table

## Common Metric Definition Traps

### 1. Changing Definitions Mid-Analysis
If you redefine "active user" halfway through a cohort analysis, your before/after comparison is meaningless. Lock definitions before analysis begins. If you must change, re-run the entire analysis with the new definition.

### 2. Not Excluding Internal Users
Your team uses the product. Depending on team size and user base, internal usage can skew metrics by 1-20%. Always maintain an `internal_users` exclusion list and apply it consistently.

### 3. Timezone Ambiguity
"Daily" means different things in UTC, PST, and the user's local timezone. Pick one (usually UTC for backend metrics, user-local for engagement metrics) and document it. A user who's active at 11pm PST on Tuesday and 1am PST on Wednesday is either 1 DAU or 2 DAU depending on your timezone choice.

### 4. Double-Counting Cross-Device Users
A user on phone and laptop is one user, not two. If you count by device_id, you're inflating DAU by 20-40%. Use an identity graph or user_id (requires login) for accurate counts.

### 5. Survivorship Bias
"Average revenue per user" looks great when your low-value users churn — the average goes up even though your business is shrinking. Always pair averages with counts and look at the distribution.

### 6. The Denominator Problem
"Feature adoption rate" of 60% sounds great — until you realize the denominator is "users who visited the settings page" (5% of users). The real adoption rate is 3%. Always define your denominator explicitly and check that it represents the population you intend.

## Dashboard Design

### Information Hierarchy

Dashboards serve different audiences. Design for the decision-maker, not for completeness.

**Executive Dashboard** (5-7 metrics, monthly review):
- North Star Metric with trend
- Revenue metrics (MRR, growth rate, churn)
- One or two input metrics that explain the NSM trend
- Key guardrail (NPS or CSAT)

**Team Dashboard** (5-7 metrics, weekly review):
- The input metrics the team owns
- Feature-specific metrics for current initiatives
- Guardrails relevant to the team's domain
- Experiment results for active tests

**Ops Dashboard** (5-7 metrics, daily/real-time):
- Error rates, latency, uptime
- Support ticket volume and response time
- Deployment frequency and failure rate
- Anomaly alerts

### Dashboard Layout Template

```
+-----------------------------------------------+
|  NORTH STAR: [Metric Name] — [Current Value]  |
|  Trend: [arrow] [X%] vs last [period]          |
+---------------------+-------------------------+
|  Input Metric 1     |  Input Metric 2         |
|  [Value] [Spark]    |  [Value] [Spark]        |
+---------------------+-------------------------+
|  Input Metric 3     |  Input Metric 4         |
|  [Value] [Spark]    |  [Value] [Spark]        |
+---------------------+-------------------------+
|  GUARDRAILS: [Metric] [Status] [Metric] [St]  |
+-----------------------------------------------+
|  BUSINESS: [MRR] [CAC] [LTV] [Payback]        |
+-----------------------------------------------+
```

### Alert Thresholds

Every dashboard metric needs three thresholds:

| Level | Meaning | Response Time | Example |
|-------|---------|---------------|---------|
| **Warning** | Metric outside normal range | Review within 24h | DAU down 10% WoW |
| **Alert** | Metric significantly degraded | Investigate within 4h | Error rate > 1% |
| **Critical** | Business-threatening anomaly | Immediate response | Payment processing down |

### Review Cadence

| Cadence | What to Review | Who |
|---------|---------------|-----|
| **Daily** | Ops health, anomaly alerts | On-call, eng leads |
| **Weekly** | Input metrics, experiment results, feature adoption | Product team |
| **Monthly** | NSM, business metrics, OKR progress | Leadership + product |
| **Quarterly** | Metric recalibration, strategy alignment | Exec team |

### Good Metric Criteria (Ben Yoskovitz, *Lean Analytics*)

Every metric on a dashboard must pass these four tests:

1. **Understandable**: Creates a common language. If people argue about what it means, it fails.
2. **Comparative**: Shown over time, not as a snapshot. "5,000 DAU" means nothing; "DAU up 12% MoM" means something.
3. **Ratio or Rate**: Rates are more revealing than absolute numbers. "50 new users" vs "3.2% conversion rate."
4. **Behavior-changing**: The golden rule — "If a metric won't change how you behave, it's a bad metric." If DAU drops 20% and nobody does anything different, why is it on the dashboard?

### 8 Metric Types to Know

| Type | Opposite | Key Insight |
|------|----------|-------------|
| **Actionable** | Vanity | Only actionable metrics change behavior |
| **Quantitative** | Qualitative | Quant says WHAT; qual says WHY — you need both |
| **Exploratory** | Reporting | Explore data to uncover unexpected insights |
| **Leading** | Lagging | Leading indicators enable faster learning cycles |

**Vanity metrics** are not useless — they're useful for PR, fundraising, and morale. But they must NEVER be the primary metric on a team dashboard. If "total registered users" is your north star, you have a vanity north star.

## Recommended Tools

| Category | Tools | Best For |
|----------|-------|----------|
| **Product Analytics** | Amplitude, Mixpanel, PostHog, Heap | Event-based user behavior analysis |
| **SQL Dashboards** | Looker, Metabase, Mode, Redash | Custom queries on warehouse data |
| **Ops Monitoring** | Datadog, Grafana, New Relic | Infrastructure and performance health |
| **Experimentation** | LaunchDarkly, Optimizely, Eppo, Statsig | A/B tests and feature flags |
| **Customer Feedback** | Productboard, Dovetail, Sprig | Qualitative signals alongside quant |

## References

- [The North Star Framework 101](https://www.productcompass.pm/p/the-north-star-framework-101)
- [Are You Tracking the Right Metrics?](https://www.productcompass.pm/p/are-you-tracking-the-right-metrics)
- [The Ultimate List of Product Metrics](https://www.productcompass.pm/p/the-ultimate-list-of-product-metrics)
- [AARRR (Pirate) Metrics: The 5-Stage Framework](https://www.productcompass.pm/p/aarrr-pirate-metrics)
- [The Google HEART Framework](https://www.productcompass.pm/p/the-google-heart-framework)
- Sean Ellis, *Hacking Growth* — Business Games framework
- Ben Yoskovitz, *Lean Analytics* — Good metric criteria
