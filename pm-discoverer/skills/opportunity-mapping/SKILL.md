---
name: opportunity-mapping
description: "Opportunity Solution Tree (Teresa Torres) with detailed level-by-level guidance, Opportunity Score formula, and metrics dashboard design. Covers OST principles, weak/strong opportunity framing, and maintaining the tree as a living document."
---

# Opportunity Mapping: Opportunity Solution Trees and Metrics

## Part 1: The Opportunity Solution Tree (OST)

The Opportunity Solution Tree (Teresa Torres, *Continuous Discovery Habits*) is the structural backbone of product discovery. It prevents the most common product failure mode: jumping from a vague goal to a specific solution without understanding the problem space.

### Why the OST Exists

Most product teams operate in one of two dysfunctional modes:
1. **Feature factory**: Stakeholders request features, the team builds them, nobody checks if they moved a metric. The backlog is a wish list, not a strategy.
2. **Metric-obsessed without structure**: The team knows the target metric but brainstorms solutions randomly. They build whatever sounds best in the meeting, with no systematic exploration of the opportunity space.

The OST fixes both by creating an explicit, visible structure: Outcome -> Opportunities -> Solutions -> Experiments. Every solution traces back to an opportunity (customer problem), and every opportunity traces back to a measurable outcome.

### The Four Levels

#### Level 1: Desired Outcome (The Top)

A single, measurable business or product outcome the team is pursuing. This comes from your strategy, OKRs, or product brief — the Discoverer does not invent it, but validates that it's the right one.

**Rules**:
- ONE outcome per tree. Multiple outcomes = multiple trees. A tree trying to serve two masters serves neither.
- Must be measurable with a specific metric and target: "Increase 30-day retention from 34% to 45%"
- Must be a leading indicator of business success (not a lagging vanity metric)
- Must be within the team's sphere of influence

**Strong outcomes**:
- "Increase 7-day activation rate from 22% to 35%"
- "Reduce time-to-first-value from 4.2 days to <1 day"
- "Increase monthly active paid users from 8,200 to 12,000"

**Weak outcomes**:
- "Make the product better" (not measurable)
- "Increase revenue" (too broad, not within one team's control)
- "Launch the new dashboard" (this is an output, not an outcome)
- "Improve NPS" (lagging indicator, hard to action directly)

#### Level 2: Opportunities (Customer Problems)

Opportunities are customer needs, pain points, or desires discovered through research. They are expressed from the customer's perspective and describe PROBLEMS, never solutions.

**Rules**:
- Frame from the customer's point of view: "I struggle to..." / "I can't find..." / "I waste time on..."
- Must connect to the outcome: this opportunity, if addressed, would move the metric
- Should be discovered through evidence (interviews, analytics, support tickets), not assumed
- Aim for 3-7 opportunities per tree — fewer means you haven't explored enough, more means you haven't prioritized
- Group related opportunities under parent opportunities for complex problem spaces

**Strong opportunity framing**:
- "I can't figure out which features are relevant to me during onboarding, so I give up before finding value"
- "I spend 2+ hours every Monday compiling status updates from three different tools"
- "When I'm on mobile, I can't complete the approval workflow, so it waits until I'm back at my desk"
- "I don't trust the recommendations because I can't see how they were generated"

**Weak opportunity framing** (and why):
- "We need better search" — This is a solution dressed as an opportunity. The opportunity is: "I can't find what I need when I'm in a hurry and end up giving up or asking a colleague."
- "Users want a mobile app" — This is a solution. The opportunity is: "I need to complete critical tasks when I'm away from my desk, and the current web experience is unusable on my phone."
- "Improve the dashboard" — Vague and solution-oriented. What problem does the current dashboard create? "I can't quickly answer 'how is my project doing?' without clicking through 6 screens."
- "Add API access" — Solution. The opportunity is: "I need to connect this tool to my existing workflow, and manual copy-paste introduces errors and wastes 30 minutes per day."

**The reframing test**: If an "opportunity" can be directly implemented by engineering, it's a solution. Real opportunities require creative problem-solving — there should be multiple possible solutions.

#### Level 3: Solutions (Possible Approaches)

For each prioritized opportunity, generate multiple possible solutions. Never commit to the first idea.

**Rules**:
- At least 3 solutions per opportunity before evaluating. The "compare and contrast" principle prevents premature commitment.
- Solutions should vary in approach, not just scope. "Small dashboard" vs. "big dashboard" is one solution at two sizes, not two solutions.
- The Product Trio (PM + Designer + Engineer) should ideate together. "Best ideas often come from engineers" who see technical possibilities invisible to PMs and designers.
- Rate each solution on Desirability x Viability x Feasibility before selecting

**Example**:
Opportunity: "I can't figure out which features are relevant to me during onboarding"
- Solution A: Personalized onboarding flow based on stated role during signup
- Solution B: Interactive "feature tour" triggered by first use, with skip-ahead
- Solution C: AI-powered "suggested next action" based on similar users' first-week behavior
- Solution D: Simplified default view that hides advanced features until requested

These are genuinely different approaches. Evaluating them reveals different assumptions (A assumes users will self-identify accurately, B assumes users want guided tours, C assumes we have enough behavioral data, D assumes a simpler interface increases discovery).

#### Level 4: Experiments (Validation)

For each promising solution, design fast, cheap tests to validate the riskiest assumption. See the discovery-cycle skill for experiment design details.

**Rules**:
- Test the riskiest assumption, not the easiest one
- Each experiment has a hypothesis, method, metric, success threshold, and decision framework
- Run the cheapest experiment that answers the question
- Pre-commit to decision criteria before seeing results

### Prioritizing Opportunities: The Opportunity Score

**Opportunity Score** (Dan Olsen, *The Lean Product Playbook*):

```
Opportunity Score = Importance x (1 - Satisfaction)
```

Where:
- **Importance**: How important is this need to the user? (0 to 1, normalized)
- **Satisfaction**: How well is this need currently met? (0 to 1, normalized)

**Interpretation**:
- High Importance + Low Satisfaction = Best opportunity (users care a lot and current solutions are bad)
- High Importance + High Satisfaction = Table stakes (must have, but no competitive advantage — users are already well served)
- Low Importance + Low Satisfaction = Don't bother (users don't care enough even though solutions are bad)
- Low Importance + High Satisfaction = Over-served (stop investing here)

**Data sources for scoring**:
- Importance: Interview frequency, survey rankings, support ticket volume, competitive feature comparison
- Satisfaction: NPS sub-scores, task completion rates, time-on-task, support ticket severity, churn correlation

**Example scoring**:

| Opportunity | Importance (0-1) | Satisfaction (0-1) | Score |
|-------------|-----------------|-------------------|-------|
| Can't find what I need quickly | 0.9 | 0.3 | 0.63 |
| Status updates take too long | 0.7 | 0.2 | 0.56 |
| Mobile approval workflow broken | 0.8 | 0.4 | 0.48 |
| Want prettier reports | 0.3 | 0.5 | 0.15 |

Rank by score. Focus on the top 2-3.

### Maintaining the OST as a Living Document

The OST is not a workshop artifact. If it was created in a meeting and never updated, it's wall decoration.

**Weekly updates**:
- Add new opportunities discovered through interviews, analytics, or support tickets
- Update opportunity scores as new evidence arrives
- Move experiments through their lifecycle (planned -> running -> complete)
- Prune solutions that have been invalidated by experiments

**Monthly reviews**:
- Is the desired outcome still correct? (Strategy may have shifted)
- Are the top opportunities still the right ones? (New evidence may have reshuffled priorities)
- Are there whole branches of the tree that haven't been explored?
- Are there branches with completed experiments that need decisions?

**Quarterly reassessment**:
- Does the tree need a new desired outcome? (OKRs change quarterly)
- Archive completed/invalidated branches into a "learnings" document
- Share the tree with stakeholders for alignment and feedback

### OST Visualization Format

```
OUTCOME: Increase 30-day retention from 34% to 45%
|
+-- OPPORTUNITY: "I can't find value in my first session" [Score: 0.63]
|   |
|   +-- Solution: Personalized onboarding flow
|   |   +-- Experiment: Prototype test with 5 users [COMPLETE: 4/5 found value]
|   |   +-- Experiment: A/B test personalized vs generic [PLANNED]
|   |
|   +-- Solution: AI-suggested first actions
|   |   +-- Experiment: Fake door test [RUNNING: 3.2% CTR after 1 week]
|   |
|   +-- Solution: Simplified default view
|       +-- Experiment: Competitor analysis [COMPLETE: 3/5 competitors use this]
|
+-- OPPORTUNITY: "Status updates take too long" [Score: 0.56]
|   |
|   +-- Solution: Automated weekly digest
|   +-- Solution: Inline status comments
|   +-- Solution: Slack integration for async updates
|
+-- OPPORTUNITY: "Mobile workflow is blocked" [Score: 0.48]
    |
    +-- Solution: Responsive web redesign
    +-- Solution: Native mobile app (approval flow only)
    +-- Solution: Email-based approval (reply to approve)
```

### OST Anti-Patterns

1. **Feature trees masquerading as opportunity trees**: Every "opportunity" is actually a feature request. This is just a backlog with extra steps.
2. **One solution per opportunity**: If you only generated one solution, you didn't explore the space. You're anchored on the first idea.
3. **No experiments**: Solutions without experiments are commitments without evidence. You're waterfall with post-it notes.
4. **Stale trees**: Created 3 months ago, never updated. The market has moved but the tree hasn't.
5. **Multiple outcomes**: A tree with 3 outcomes is 3 trees badly merged. Split them.
6. **No prioritization**: All opportunities treated equally. Without scoring, the team defaults to working on whatever the loudest stakeholder wants.

---

## Part 2: Metrics Dashboard Design

The metrics dashboard is the quantitative backbone of opportunity mapping. Without metrics, opportunities are anecdotes. Without dashboards, metrics are ignored.

### The Metrics Hierarchy

**North Star Metric**: The single metric that best captures core value delivery to users. Not revenue (that's a business outcome). Not DAU (that's engagement, not value). The North Star measures how much value users are receiving.

Examples by product type:
- **Marketplace**: Transactions completed per week
- **SaaS tool**: Tasks completed per active user per week
- **Social platform**: Content pieces consumed per session
- **Subscription media**: Hours of content consumed per subscriber per month

**4 criteria for a good metric** (Ben Yoskovitz, *Lean Analytics*):
1. **Understandable**: Creates a common language across the team
2. **Comparative**: Measured over time (trend), not as a snapshot
3. **Ratio or Rate**: More revealing than absolute numbers (e.g., conversion rate vs. total signups)
4. **Behavior-changing**: If it moves, you change what you're doing. "If a metric won't change how you behave, it's a bad metric."

**Input Metrics (3-5)**: The levers that directly drive the North Star. Each input metric should be:
- Directly actionable by a specific team or initiative
- Causally linked to the North Star (not just correlated)
- MECE (mutually exclusive, collectively exhaustive) in explaining North Star movement

**Health Metrics**: Guardrails that ensure the product remains healthy while you optimize inputs:
- Error rates, latency (P50, P95, P99)
- Support ticket volume and resolution time
- NPS, CSAT
- Churn rate (leading indicator: engagement drop-off)

**Counter-Metrics**: Metrics that catch optimization gone wrong:
- If North Star is DAU, counter-metric is session quality (prevent empty opens)
- If North Star is transactions, counter-metric is refund rate (prevent low-quality transactions)
- If North Star is activation rate, counter-metric is Day-30 retention (prevent shallow activation)

**Vanity vs. Actionable Metrics**:
- **Vanity**: Total registered users (only goes up, never changes behavior)
- **Actionable**: Weekly active users as % of registered (goes up AND down, triggers investigation)

**Leading vs. Lagging Indicators**:
- **Lagging**: Revenue (tells you what happened, too late to change)
- **Leading**: Feature adoption in first week (predicts 30-day retention, early enough to intervene)

### Dashboard Layout

```
+-----------------------------------------------------+
|  NORTH STAR: [Metric] -- [Current Value]             |
|  Trend: [sparkline, period-over-period change]       |
+--------------------------+---------------------------+
|  Input Metric 1          |  Input Metric 2           |
|  [Value, trend, target]  |  [Value, trend, target]   |
+--------------------------+---------------------------+
|  Input Metric 3          |  Input Metric 4           |
|  [Value, trend, target]  |  [Value, trend, target]   |
+--------------------------+---------------------------+
|  HEALTH: [Error Rate] [Latency P95] [NPS] [Churn]   |
+-----------------------------------------------------+
|  COUNTER: [Counter-metric 1] [Counter-metric 2]     |
+-----------------------------------------------------+
|  BUSINESS: [MRR] [CAC] [LTV] [LTV:CAC ratio]        |
+-----------------------------------------------------+
```

### Alert Thresholds

For each metric, define three zones:

| Zone | Meaning | Action |
|------|---------|--------|
| **Green** | Within expected range | Continue monitoring |
| **Yellow** | Outside normal range | Investigate within 24 hours — check for data issues, seasonal effects, or real degradation |
| **Red** | Critical deviation | Escalate immediately — page the on-call PM and engineering lead |

**Setting thresholds**:
- Use 2 standard deviations from rolling 4-week average for Yellow
- Use 3 standard deviations for Red
- For new metrics without history, set thresholds based on business impact: "At what value does this metric indicate a real problem?"

### Review Cadence

- **Daily**: Glance at health metrics and North Star (automated alerts for deviations)
- **Weekly**: Review input metric trends in team standup. Ask: "Are inputs moving as expected? If not, why?"
- **Monthly**: Deep dive — are inputs actually driving the North Star? Check causal assumptions. Review experiment impact.
- **Quarterly**: Reassess the entire metrics framework. Are we measuring the right things? Has the strategy changed? Do we need new input metrics?

### Metrics Anti-Patterns

1. **Vanity dashboards**: All numbers go up and to the right, but none are actionable
2. **Too many metrics**: If you track 30 metrics, you track none. 8-12 is the practical maximum for a team to actively monitor.
3. **No North Star**: Multiple "key metrics" with no hierarchy — nobody knows what to optimize
4. **Missing counter-metrics**: You'll Goodhart's-Law yourself into optimizing the wrong thing
5. **Snapshot reporting**: "We have 50,000 users" tells you nothing without trend, cohort, and segment breakdowns
6. **Metrics without owners**: If nobody is responsible for moving a metric, it won't move (or its movement will go unnoticed)

### Connecting Metrics to Opportunities

The metrics dashboard and the Opportunity Solution Tree should reference each other:
- Each input metric should map to one or more opportunities in the OST
- Each opportunity should have at least one metric that would move if the opportunity were addressed
- Experiment success criteria should reference specific metrics on the dashboard

This creates a closed loop: the team discovers opportunities, builds solutions, runs experiments, and measures impact — all traceable through a single connected structure.
