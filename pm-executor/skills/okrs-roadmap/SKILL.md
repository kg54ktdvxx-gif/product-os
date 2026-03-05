---
name: okrs-roadmap
description: "OKR creation with company-to-team alignment, outcome-focused roadmap transformation (Now/Next/Later), and 9 prioritization frameworks with formulas. Includes OKR anti-patterns, scoring methodology, quarterly review protocol, and audience-specific roadmap communication."
---

# OKRs, Roadmaps, and Prioritization

## Part 1: OKR Creation

### What OKRs Are (and Are Not)

**OKRs** (Objectives and Key Results) bridge vision and execution:
- **Objective**: Qualitative, inspirational, time-bound. Describes WHERE you want to go. Typically quarterly.
- **Key Results**: Quantitative, measurable. Describe HOW you will know you got there. Typically 3 per objective.

**OKRs, KPIs, and NSM are interconnected -- not alternatives:**
- **Key Results** always refer to quantitative metrics, some of which might be KPIs.
- **KPIs** = a few key quantitative metrics tracked over a longer period. Can be used as Key Results, or you can set Key Results for a KPI's input metrics.
- **North Star Metric** = a single, customer-centric KPI that is a leading indicator of business success.

### How to Write Good OKRs

**Step 1: Start with Company Objectives**
What is the company trying to achieve this quarter? Team OKRs must ladder up to company OKRs. If there are no company OKRs, derive from product strategy or business goals.

**Step 2: Identify Team Impact Areas**
What are the 3-5 areas where this team can most influence company objectives? These become candidate objectives.

**Step 3: Write Objectives**
- Qualitative and inspiring ("Delight new users with an effortless onboarding experience")
- Time-bound (quarterly by default)
- Ambitious but achievable (60-70% confidence of hitting all KRs)
- Maximum 3 objectives per team per quarter. More = less focus.

**Step 4: Write Key Results**
For each objective, define exactly 3 Key Results that are:
- Measurable with data, not judgment
- Outcome-oriented, not output-oriented
- Have baselines and targets
- Have clear owners

**Good KR example:**
> KR: Increase 7-day activation rate from 23% to 40%
> Baseline: 23% (last quarter average from metrics.md)
> Target: 40%
> Owner: Growth team

**Bad KR examples (and why):**
- "Launch onboarding redesign" -- this is an OUTPUT, not an outcome. What if you launch it and activation does not improve?
- "Improve retention" -- unmeasurable. Improve by how much? From what baseline? Over what period?
- "Ship 5 features" -- incentivizes shipping junk. Quantity of features has zero correlation with customer value.
- "Increase NPS" -- from what? To what? By when?
- "Run 3 experiments" -- activity metric. Running experiments that all fail does not count as success.

### OKR Scoring Methodology

At the end of each period, score each KR from 0.0 to 1.0:

| Score | Interpretation |
|-------|---------------|
| 0.0-0.3 | Significant miss. Investigate root cause. Was the target wrong or was execution flawed? |
| 0.4-0.6 | Progress made but fell short. Identify what blocked full achievement. |
| 0.7-0.9 | Well-calibrated stretch goal. THIS IS THE TARGET ZONE. If you consistently score 1.0, your targets are not ambitious enough. |
| 1.0 | Either nailed it perfectly or the target was sandbagged. Review ambition level. |

**Quarterly Review Protocol:**
1. Score each KR with data (not judgment)
2. Score the Objective as the average of its KRs
3. For each KR scored below 0.4: write a brief root cause analysis
4. For each KR scored 1.0: ask whether the target was truly ambitious
5. Identify learnings that should influence next quarter's OKRs
6. Archive with date and context for future reference

### Check-in Cadence

- **Weekly**: Traffic-light status update on each KR (green/yellow/red) with one sentence of context
- **Mid-quarter**: Deep review. Are targets still relevant? Has context changed? Adjust if the world changed, not because hitting the target is hard.
- **End of quarter**: Full scoring, retrospective, and input into next quarter planning

### Counter-Metrics

For every KR, identify a counter-metric that prevents gaming:
- KR: "Increase activation rate to 40%" --> Counter: "Without decreasing 30-day retention below 65%"
- KR: "Reduce support tickets by 50%" --> Counter: "Without decreasing CSAT below 4.0"
- KR: "Increase page load speed by 2x" --> Counter: "Without removing core functionality"

---

## Part 2: Outcome-Focused Roadmaps

### Why Output Roadmaps Fail

Output roadmaps ("Q1: Build SSO, Q2: Redesign dashboard, Q3: Add API v2") fail because:
- They create false precision about timelines
- They lock teams into solutions before problems are validated
- They communicate WHAT without WHY
- They make it impossible to reprioritize without "breaking promises"

### The Transformation Process

For each item on a feature roadmap, ask: "So what?" until you reach a real outcome.

**Example chain:**
- "Build SSO" --> So what? --> "Enterprise customers can log in easier" --> So what? --> "Faster enterprise onboarding" --> So what? --> "**Reduce enterprise time-to-value from 14 days to 3 days**"

That last answer is your outcome statement.

**Outcome statement format:**
> Enable [customer segment] to [desired outcome] so that [business impact]
> Success metric: [specific, measurable target]

### Now / Next / Later Format

The recommended roadmap format for most audiences:

**Now (Current Quarter)** -- High confidence, actively being worked on
- Outcome statements with success metrics
- Specific initiatives mapped to outcomes
- Status tracking (on track / at risk / blocked)

**Next (Next Quarter)** -- Medium confidence, scoped but not committed
- Outcome statements with success metrics
- Candidate initiatives (may change)
- Dependencies and prerequisites

**Later (Future)** -- Low confidence, directional only
- Outcome statements only (no specific solutions)
- Strategic themes they support
- What needs to be true before we commit

### Roadmap Communication by Audience

Different audiences need different roadmap presentations:

| Audience | Format | Detail Level | Update Frequency |
|----------|--------|-------------|-----------------|
| Board / Executives | Outcome-only, strategic themes | High-level, 3-5 items | Quarterly |
| Engineering | Outcomes + initiatives + dependencies | Detailed, sequenced | Sprint-level |
| Sales / Customer Success | Outcomes + rough timing + customer impact | Medium, benefit-focused | Monthly |
| Customers | Themes + directional timing | Vague on dates, strong on intent | Quarterly or less |
| Marketing | Outcomes + messaging angles + launch dates | Medium, story-focused | Monthly |

**Rule**: Never share the engineering-detail roadmap with customers. Never share the customer-facing roadmap with engineers. Same strategy, different translations.

---

## Part 3: Prioritization Frameworks

### When to Use Which Framework

| Situation | Recommended Framework |
|-----------|---------------------|
| Prioritizing customer problems | **Opportunity Score** |
| Quick triage of many ideas | **ICE** |
| Rigorous prioritization at scale | **RICE** |
| Requirements scoping for a release | **MoSCoW** |
| Understanding customer expectations | **Kano Model** |
| Complex decisions with many factors | **Weighted Decision Matrix** |
| Prioritizing based on economic value | **WSJF** (Weighted Shortest Job First) |
| Getting stakeholder buy-in on priorities | **Buy-a-Feature** |
| Visualizing the user journey and gaps | **Story Mapping** |

### Core Principle

Never allow customers to design solutions. Prioritize PROBLEMS (opportunities), not features.

### Framework 1: Opportunity Score (Recommended)

From Dan Olsen, *The Lean Product Playbook*.

Survey customers on **Importance** and **Satisfaction** for each need (normalize to 0-1 scale):

- **Current value** = Importance x Satisfaction
- **Opportunity Score** = Importance x (1 - Satisfaction)
- **Customer value created** = Importance x (S2 - S1), where S1 = satisfaction before, S2 = after

High Importance + Low Satisfaction = highest Opportunity Score = best opportunities. Plot on an Importance vs Satisfaction chart -- upper-left quadrant is the sweet spot.

### Framework 2: ICE

- **I** (Impact) = Opportunity Score x Number of Customers affected
- **C** (Confidence) = How confident are we? (1-10)
- **E** (Ease) = How easy to implement? (1-10)
- **Score** = I x C x E

Best for: Quick prioritization when you need to move fast and have reasonable intuition about impact.

### Framework 3: RICE

- **R** (Reach) = Number of customers affected per quarter
- **I** (Impact) = Value per customer (0.25 = minimal, 0.5 = low, 1 = medium, 2 = high, 3 = massive)
- **C** (Confidence) = How confident? (100% = high, 80% = medium, 50% = low)
- **E** (Effort) = Person-months of work
- **Score** = (R x I x C) / E

Best for: Larger teams that need more granularity than ICE. The explicit Effort denominator penalizes big bets appropriately.

### Framework 4: MoSCoW

- **Must have**: Without this, the release is not viable
- **Should have**: Important but the release works without it
- **Could have**: Desirable, included only if time permits
- **Won't have (this time)**: Explicitly excluded from this release

Best for: Scoping a specific release. Caution: project management origin; does not inherently connect to customer value.

### Framework 5: Kano Model

Categorizes features by customer reaction:
- **Must-be**: Expected. Absence causes dissatisfaction; presence does not delight. (e.g., login works)
- **Performance**: More is better. Linear relationship with satisfaction. (e.g., page load speed)
- **Attractive**: Unexpected. Absence is fine; presence delights. (e.g., personalized recommendations)
- **Indifferent**: Customer does not care either way.
- **Reverse**: Customer actively does NOT want this.

Best for: Understanding expectations, not prioritizing. Use Kano to inform which features go into which MoSCoW category.

### Framework 6: WSJF (Weighted Shortest Job First)

From SAFe. Prioritizes based on economic value of doing something sooner rather than later.

- **Cost of Delay** = User Value + Time Criticality + Risk Reduction
- **WSJF** = Cost of Delay / Job Duration

Best for: When sequence matters more than absolute priority. Answers: "What should we do FIRST?"

### Framework 7: Buy-a-Feature

Give stakeholders a fixed budget of fake money. They "buy" features from a menu. Features are priced based on estimated effort. Stakeholders must pool money for expensive features, forcing negotiation and revealing true priorities.

Best for: Getting buy-in from non-technical stakeholders. Makes trade-offs visceral.

### Framework 8: Story Mapping

Lay out the user journey horizontally (activities and tasks). Slice vertically for releases. The top row is the "walking skeleton" (minimum viable flow). Each row below adds richness.

Best for: Visualizing what a phased release looks like from the user's perspective.

### Framework 9: Cost of Delay

Quantifies the economic impact of NOT doing something. Three profiles:
- **Standard**: Linear value loss over time (most features)
- **Urgent**: Exponential value loss (regulatory deadlines, competitive response)
- **Fixed date**: Cliff-edge value loss (seasonal, event-driven)

Best for: Making the case for urgency. "Every week we delay this costs us $X in churn."

## References

- [Product Vision vs Strategy vs Objectives vs Roadmap](https://www.productcompass.pm/p/product-vision-strategy-goals-and)
- [OKRs 101 + Advanced Techniques](https://www.productcompass.pm/p/okrs-101-advanced-techniques)
- [Business Outcomes vs Product Outcomes vs Customer Outcomes](https://www.productcompass.pm/p/business-outcomes-vs-product-outcomes)
- [The Product Frameworks Compendium](https://www.productcompass.pm/p/the-product-frameworks-compendium)
- [Kano Model: How to Delight Customers](https://www.productcompass.pm/p/kano-model-how-to-delight-your-customers)
- [From Strategy to Objectives Masterclass](https://www.productcompass.pm/p/product-vision-strategy-objectives-course)
