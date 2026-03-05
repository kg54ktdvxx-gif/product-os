---
name: retention
description: "Retention strategy framework covering churn analysis, engagement scoring, reactivation triggers, habit formation (Hooked model), aha moment methodology, retention benchmarks, Net Dollar Retention, and pricing experiment frameworks (Van Westendorp, Gabor-Granger, conjoint analysis)."
---

# Retention Strategy

## Overview

Retention is the foundation of growth. No amount of acquisition fixes a retention problem. A product that retains users compounds growth from every channel. A product that does not retain users transforms every acquisition dollar into waste.

This skill covers: diagnosing why users leave, identifying what keeps them, designing systems that build habits, measuring retention health, and running pricing experiments to optimize the value exchange.

## When to Use

- Retention curves are declining or flat
- Churn is increasing and the cause is unclear
- You need to design engagement and reactivation systems
- Setting up retention metrics and benchmarks
- Preparing to run pricing experiments
- Transitioning from "grow at all costs" to "grow efficiently"

---

## Part 1: Churn Analysis

Churn is not one problem. It is a category of problems with different root causes and different solutions.

### Types of Churn

| Type | Definition | Root Cause | Solution Category |
|------|-----------|------------|-------------------|
| **Voluntary — never activated** | User signed up, never reached aha moment, left | Onboarding failure | Activation optimization |
| **Voluntary — activated then left** | User experienced value, then stopped using | Value diminished or competitor won | Product improvement, retention loops |
| **Voluntary — seasonal** | User leaves and returns cyclically | Product is needed periodically, not continuously | Reactivation campaigns, usage expansion |
| **Involuntary** | Payment failed, card expired, account issue | Billing infrastructure | Dunning campaigns, payment retry logic |
| **Hidden churn** | User is technically "active" but disengaged (opens app but does nothing meaningful) | Habit formation failure | Engagement scoring, re-engagement |

### Churn Analysis Framework

1. **Segment churn by cohort**: Monthly signup cohorts — is the problem getting worse or better over time?
2. **Segment churn by acquisition channel**: Are certain channels bringing low-quality users who churn faster?
3. **Segment churn by segment**: Are certain ICPs churning more than others? (This reveals bad ICP fit, not product problems.)
4. **Segment churn by lifecycle stage**: When in the customer lifecycle does churn happen? (Day 1? Day 30? Month 6? Renewal?)
5. **Segment churn by reason**: Exit surveys, cancellation flows, support tickets — what are they telling you?

### Churn by Lifecycle Stage

| Stage | Churn Signal | Likely Cause | Response |
|-------|-------------|-------------|----------|
| Day 0-3 | Never logs in after signup | Friction in signup or onboarding | Simplify onboarding, welcome email sequence |
| Day 3-14 | Logs in once, does not return | Did not reach aha moment | Optimize time-to-value, add guided onboarding |
| Day 14-30 | Used product a few times, then stopped | Value was not sustained or habit did not form | Add engagement hooks, notification strategy |
| Month 1-3 | Regular user, then gradual disengagement | Alternative found, need changed, or feature gap | Customer success outreach, feature improvement |
| Month 3-12 | Steady user, then abrupt cancellation | Budget cut, reorganization, or champion left | Protect against single-champion risk, demonstrate ROI |
| Renewal | Does not renew at end of contract | ROI was not demonstrated or communicated | Quarterly business reviews, usage reports, ROI emails |

---

## Part 2: Engagement Scoring

An engagement score predicts churn before it happens by tracking behavioral signals. Users do not wake up one day and cancel — they gradually disengage over weeks.

### Building an Engagement Score

1. **Identify key actions**: What do your most retained users do? List the top 5-10 actions that correlate with retention.
2. **Weight by predictive power**: Use correlation analysis to weight actions by how strongly they predict 30-day retention.
3. **Define thresholds**: Score users as Active (green), At-Risk (yellow), or Dormant (red) based on composite score.

### Example Engagement Score

| Action | Weight | Frequency Threshold (Active) | At-Risk | Dormant |
|--------|--------|------------------------------|---------|---------|
| Core action (e.g., create project) | 30% | 3+/week | 1/week | 0 in 14 days |
| Collaboration (e.g., invite team member) | 25% | 1+/month | 0 in 30 days | Never |
| Return visit | 20% | 4+/week | 1-2/week | 0 in 7 days |
| Feature depth (e.g., use advanced feature) | 15% | 1+/week | 1/month | Never |
| Content consumption (e.g., read help docs) | 10% | Any | None | N/A |

### Response Playbook by Score

| Score | State | Response |
|-------|-------|----------|
| Green (Active) | Healthy engagement | Expansion opportunities — upsell, cross-sell, referral program |
| Yellow (At-Risk) | Declining engagement | Trigger re-engagement: in-app message highlighting unused features, check-in email, customer success outreach |
| Red (Dormant) | Disengaged | Reactivation campaign: "We miss you" email with a specific reason to return, offer a call with CS, last-resort discount (use sparingly) |

### Reactivation Triggers

Design moments that bring users back:

| Trigger | Mechanism | Example |
|---------|-----------|---------|
| External event | Something happens outside the product that creates renewed need | Tax season for accounting software, new quarter for analytics tools |
| Product update | New feature that addresses a known pain point | "We added [feature you requested]" email |
| Social trigger | Colleague activity within the product | "[Name] shared a project with you" |
| Data trigger | Product has new data or insights to show | "Your weekly report is ready" (Grammarly, Spotify Wrapped) |
| Milestone | User anniversary, usage milestone | "You have been with us for 1 year — here is what you accomplished" |

### Reactivation Anti-Patterns

- **Blast emails to dormant users without understanding why they left.** This is not reactivation — it is spam. Segment dormant users by reason for disengagement and tailor the message.
- **Discount as first resort.** Discounting trains users to disengage in order to get a deal. Use discounts only for involuntary churn recovery (payment failed) or as a last resort for high-value accounts.
- **"We miss you" without a reason to return.** The user left for a reason. Address that reason or do not bother. "We miss you" without "and here is what changed" is noise.
- **Reactivation before diagnosis.** Before launching a reactivation campaign, understand WHY users left. If the product has a fundamental problem, reactivation just cycles users through the same broken experience.

---

## Part 3: Habit Formation

Products that become habits do not need reactivation campaigns. The Hooked Model (Nir Eyal) provides a framework for designing habit-forming product experiences.

### The Hooked Model: Trigger, Action, Reward, Investment

#### 1. Trigger
Something prompts the user to open the product. External triggers (notifications, emails) transition to internal triggers (boredom, anxiety, curiosity) over time.

| Trigger Type | Example | Design Principle |
|-------------|---------|------------------|
| External — earned | PR mention, word of mouth | Build something worth talking about |
| External — owned | Push notification, email | Use sparingly, be relevant, allow opt-out |
| External — paid | Ad, sponsored content | Acquire users, but do not depend on this for retention |
| Internal — emotion | "I wonder if anything changed" | Associate product with a recurring emotional state |
| Internal — routine | "Every Monday morning I check my dashboard" | Anchor to existing routines |

**Key principle**: External triggers get users in the door. Internal triggers keep them. The goal is to transition from external to internal triggers within the first 30 days.

#### 2. Action
The simplest behavior in anticipation of a reward. The action must be simpler than the user's current alternative.

**Design principle**: Reduce friction to the absolute minimum. Fogg's Behavior Model: Behavior = Motivation x Ability x Trigger. You cannot always increase motivation, but you can always reduce friction (increase ability).

Examples:
- Duolingo: Tap "Start" on a 5-minute lesson (vs sit down with a textbook)
- Twitter/X: Open app and scroll (vs seek out news sources)
- Notion: Click "New page" and start typing (vs open Word, create file, save to folder)

#### 3. Reward
The payoff that satisfies the user's need and creates a desire to repeat.

| Reward Type | Satisfies | Example |
|-------------|-----------|---------|
| Tribe (social) | Social validation, belonging | Likes, comments, team acknowledgment |
| Hunt (information) | Curiosity, discovery | Feed refresh, new content, search results |
| Self (mastery) | Competence, completion | Progress bar, streak, level up |

**Variable rewards** are more engaging than predictable ones. The user does not know exactly what they will find, which creates anticipation. This is why social feeds are more addictive than static dashboards.

#### 4. Investment
Something the user puts in that makes the product more valuable over time: data, content, reputation, customization, or social connections. Investment increases switching cost and primes the next trigger.

Examples:
- LinkedIn: Every connection makes the network more valuable
- Spotify: Every song liked improves recommendations
- Notion: Every document created is an asset stored in the platform
- Salesforce: Every deal logged is data the company depends on

### Habit Design Checklist

| Question | If Yes | If No |
|----------|--------|-------|
| Is there a recurring trigger (external or internal)? | Good — ensure frequency matches use case | Design one — email digest, push notification, scheduled report |
| Is the core action simpler than alternatives? | Good — protect simplicity | Reduce friction — fewer clicks, less cognitive load |
| Does the user get a reward after the action? | Good — add variability if possible | Add immediate feedback — confirmation, insight, progress |
| Does the user invest something that makes the product better? | Good — this builds moat | Design investment — customization, data entry, content creation |

---

## Part 4: Retention Benchmarks

Use these benchmarks to calibrate expectations. Benchmarks vary dramatically by product type — comparing a social network's retention to a B2B SaaS tool is meaningless.

### By Product Type

| Product Type | Day 1 Retention | Day 7 Retention | Day 30 Retention | Monthly Logo Retention |
|-------------|----------------|----------------|-----------------|----------------------|
| Consumer social | 40-60% | 25-40% | 15-25% | N/A (free) |
| Consumer subscription | 60-75% | 40-55% | 25-35% | 92-96% |
| Mobile game | 30-50% | 15-25% | 5-15% | N/A (free) |
| B2B SaaS (SMB) | 80-90% | 65-80% | 50-70% | 94-97% |
| B2B SaaS (Enterprise) | 90-95% | 85-90% | 80-90% | 97-99% |
| Marketplace (buyer side) | 30-50% | 20-35% | 10-20% | N/A |
| Marketplace (seller side) | 50-70% | 40-60% | 30-50% | N/A |

### Key Retention Metrics

#### Logo Retention (Customer Retention Rate)
Percentage of customers retained, regardless of revenue change.
- Formula: (Customers at end of period - New customers during period) / Customers at start of period
- Target: > 90% monthly for B2B SaaS, > 95% for enterprise

#### Net Dollar Retention (NDR)
Revenue retained including expansion, contraction, and churn. The single most important metric for SaaS businesses.
- Formula: (Starting MRR + Expansion - Contraction - Churn) / Starting MRR
- Target: > 100% means you grow without new customers. > 110% is good. > 130% is elite (Snowflake, Twilio).
- Benchmark: Median public SaaS is ~110%. Best-in-class is 130%+.

#### DAU/MAU Ratio
Measures how frequently monthly users engage daily. Higher = stickier product.
- Formula: Daily Active Users / Monthly Active Users
- Benchmark: 20-25% is average for consumer apps. 50%+ is elite (WhatsApp, Instagram).
- For B2B: WAU/MAU (Weekly Active Users / Monthly Active Users) is more appropriate. Target: > 60%.

#### Gross Dollar Retention (GDR)
Revenue retained EXCLUDING expansion. Measures pure retention without the masking effect of upsells.
- Formula: (Starting MRR - Contraction - Churn) / Starting MRR
- Target: > 85% for SMB, > 95% for enterprise
- If GDR is low but NDR is high, you are masking a retention problem with aggressive upselling

---

## Part 5: The Aha Moment Methodology

The "aha moment" is the specific user action or milestone after which retention dramatically improves. Finding and optimizing for this moment is the single highest-leverage retention activity.

### How to Find the Aha Moment

1. **List candidate actions**: Every significant action users take in their first 7 days (created first project, invited a team member, connected an integration, exported a report, etc.)

2. **Cohort analysis**: For each candidate action, split users into two cohorts: "did this action in week 1" and "did not do this action in week 1." Compare day 30 retention.

3. **Find the action with the largest retention gap**: The action where the "did" cohort retains at 2-3x the rate of the "did not" cohort is your aha moment.

4. **Validate with qualitative research**: Interview retained users: "When did you first realize this was valuable?" Interview churned users: "What were you hoping to accomplish that you didn't?"

5. **Set the threshold**: The aha moment is not just the action but the amount. Facebook's was "10 friends in 14 days," not just "add a friend." Slack's was "2,000 messages," not just "send a message."

### Optimizing for the Aha Moment

Once identified, make it the single most important goal of the onboarding experience:

- **Measure time-to-aha**: How long does it take the median user to reach the aha moment?
- **Reduce steps**: Every unnecessary step between signup and aha moment is a drop-off point. Eliminate ruthlessly.
- **Guide users there**: Onboarding checklists, tooltips, and email nudges should all drive toward the aha moment.
- **Remove distractions**: Features that are not on the path to the aha moment should be hidden from new users (progressive disclosure).
- **Celebrate arrival**: When the user reaches the aha moment, acknowledge it. "You just [action] — here is why that matters."

---

## Part 6: Pricing Experiment Frameworks

Pricing is a retention lever because it directly affects the value exchange. Overpricing causes churn. Underpricing leaves money on the table AND signals low value. The right price is the one that aligns perceived value with captured value.

### Van Westendorp Price Sensitivity Meter

**When to use**: Early-stage pricing research, understanding price range for a new product or tier.

**Method**: Ask four questions to a sample of target customers:

1. "At what price would you consider this product to be too expensive — so expensive that you would not consider buying it?"
2. "At what price would you consider this product to be expensive — but you might still consider buying it?"
3. "At what price would you consider this product to be a bargain — a great buy for the money?"
4. "At what price would you consider this product to be too cheap — so cheap that you would question its quality?"

**Analysis**: Plot cumulative distribution curves for each question. Key intersections:
- **Point of Marginal Cheapness** (PMC): "Too cheap" crosses "expensive" — price floor
- **Point of Marginal Expensiveness** (PME): "Too expensive" crosses "bargain" — price ceiling
- **Indifference Price Point** (IDP): "Expensive" crosses "bargain" — most common "fair" price
- **Optimal Price Point** (OPP): "Too cheap" crosses "too expensive" — minimum resistance

**Recommended price range**: Between PMC and PME, with IDP as the starting point.

**Sample size**: Minimum 100 respondents for reliable results. Segment by ICP — pricing sensitivity varies dramatically by segment.

### Gabor-Granger Direct Pricing Test

**When to use**: Testing specific price points when you have a shortlist of 3-5 candidate prices.

**Method**:
1. Show the product description to a target customer
2. Ask: "Would you buy this at $X?" (start with the highest price)
3. If no: show the next lower price and ask again
4. If yes: record the price and ask about purchase likelihood (definitely, probably, might, probably not)
5. Repeat with a sample of 200+ target customers

**Analysis**: Plot willingness-to-buy at each price point. Calculate revenue-maximizing price = price x (% who would buy at that price) x (expected volume).

**Advantage over Van Westendorp**: Gives you a specific demand curve, not just a range. Better for finalizing pricing.

### Conjoint Analysis

**When to use**: When pricing depends on feature bundles — "how much more would they pay for Feature X?"

**Method**:
1. Define 3-5 attributes (features, price, support level, usage limits)
2. Create attribute levels (e.g., price: $20, $40, $60; storage: 10GB, 100GB, unlimited)
3. Generate product profiles (combinations of attribute levels)
4. Ask respondents to rank or choose between profiles
5. Statistical analysis reveals the relative importance of each attribute and the willingness to pay for each level

**Advantage**: Reveals the value of individual features, not just overall price tolerance. Essential for designing pricing tiers.

**Limitation**: Complex to set up and analyze. Requires 300+ respondents for statistical significance. Use a tool (Conjointly, SurveyMonkey, Qualtrics) rather than building from scratch.

### When to Use Each Method

| Method | Stage | Sample Size | Complexity | Output |
|--------|-------|-------------|------------|--------|
| Van Westendorp | Early exploration | 100+ | Low | Price range |
| Gabor-Granger | Price finalization | 200+ | Medium | Revenue-maximizing price |
| Conjoint | Tier/bundle design | 300+ | High | Feature valuations, tier design |

---

## Output Format

When executing this skill, deliver:

1. **Churn Diagnosis** — segmented by type, lifecycle stage, and root cause
2. **Engagement Score Design** — key actions, weights, thresholds, response playbook
3. **Retention Strategy** — specific interventions mapped to diagnosed problems
4. **Habit Formation Assessment** — Hooked model analysis with design recommendations
5. **Retention Benchmarks** — calibrated to the product type with gap analysis
6. **Pricing Recommendation** — experiment design and/or analysis if pricing is a factor

## Anti-Patterns

- **Treating all churn as one problem.** Involuntary churn needs dunning. Activation churn needs onboarding. Competitive churn needs product improvement. Diagnosing the type comes first.
- **Optimizing retention before fixing activation.** If 80% of users never reach the aha moment, fixing retention for the 20% who did is optimizing the wrong thing.
- **Using discounts to retain.** Discounts attract price-sensitive users and train all users to negotiate. Fix the value proposition instead.
- **Measuring retention with the wrong metric.** DAU/MAU for a product used weekly is misleading. Match the metric to the natural usage frequency.
- **Reactivation campaigns without segmentation.** "Come back!" emails to users who left because of a bug, users who left because of price, and users who left because they no longer need the product should be three different campaigns.
- **Ignoring involuntary churn.** Failed payments cause 20-40% of all churn in subscription businesses. Smart retry logic and dunning emails recover 30-50% of these.

---

## References

- Nir Eyal, *Hooked* — habit formation framework
- Andrew Chen, *The Cold Start Problem* — network effects and retention
- Casey Winters, Reforge — retention frameworks and engagement scoring
- Patrick Campbell, ProfitWell — pricing research methodologies
- Lenny Rachitsky — retention benchmarks and aha moment methodology
