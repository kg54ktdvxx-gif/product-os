---
name: measure
description: "Full measurement command — define metrics, generate SQL, design experiments, plan instrumentation, or analyze data. Reads product context, determines what's needed, and produces precise, actionable measurement artifacts."
---

# /measure — Measurement Command

The universal entry point for all measurement work. Determines what the user needs — metrics definition, SQL generation, experiment design, instrumentation planning, or data analysis — and routes to the appropriate workflow.

## Invocation

```
/measure Define our North Star Metric for a B2B project management tool
/measure Write a BigQuery query for weekly retention by signup cohort
/measure Design an A/B test for our new onboarding flow
/measure Create a tracking plan for our checkout funnel
/measure Analyze these test results: control 4.2% (n=5000), variant 4.8% (n=5100)
/measure What metrics should we track for our new feature launch?
```

## Workflow

### Step 1: Read Context

Before producing any output, read available context files to understand the product:

1. **Read `product-brief.md`** (if it exists): Understand the product, users, and goals
2. **Read `strategy.md`** (if it exists): Understand strategic direction, OKRs, and business model
3. **Read `assumptions.md`** (if it exists): Identify hypotheses that need measurement or validation
4. **Read `metrics.md`** (if it exists): Check what metrics are already defined to avoid duplication or contradiction

If none of these files exist, ask the user for sufficient context before proceeding. At minimum, you need:
- What the product does
- Who the users are
- What business model applies (subscription, transaction, ad-supported)
- What specific question they want answered

### Step 2: Determine the Task

Classify the user's request into one or more of these categories:

| Request Type | Key Signals | Route To |
|-------------|-------------|----------|
| **Metrics Definition** | "what should we measure", "North Star", "KPIs", "metrics framework" | Metrics Definition workflow |
| **SQL Generation** | "query", "SQL", "how many users", "show me", specific data question | SQL Analytics workflow |
| **Experiment Design** | "A/B test", "experiment", "should we test", "hypothesis" | Experiment Design workflow |
| **Experiment Analysis** | "results", "significant", "ship or kill", test data provided | Experiment Analysis workflow |
| **Instrumentation** | "tracking plan", "what to instrument", "events", "analytics setup" | Instrumentation workflow |
| **Dashboard Design** | "dashboard", "what to show", "monitoring", "alerts" | Metrics Definition (dashboard section) |
| **Cohort Analysis** | "retention", "cohort", "churn", "which users" | SQL Analytics (cohort section) |

If the request spans multiple categories (common — e.g., "define metrics and write the SQL"), handle them in logical order: define metrics first, then write SQL, then design the dashboard.

### Step 3: Execute the Appropriate Workflow

#### Workflow A: Metrics Definition

1. **Classify the Business Game**: Is this an Attention, Transaction, or Productivity business?

2. **Define the North Star Metric**:
   - Propose 2-3 candidates
   - Validate each against the 7 NSM criteria
   - Recommend one with reasoning
   - Write the full operational definition (plain English + SQL pseudocode + edge cases)

3. **Define Input Metrics** (3-5):
   - Map to AARRR stages (Acquisition, Activation, Retention, Revenue, Referral)
   - Full operational definition for each
   - Identify which team owns each metric

4. **Define Guardrail Metrics** (2-4):
   - What must NOT degrade while optimizing the NSM?
   - Set specific thresholds for each guardrail

5. **Design the Dashboard** (if requested or appropriate):
   - Information hierarchy: NSM at top, inputs in the middle, guardrails at the bottom
   - Visualization type for each metric (line chart, number, bar, funnel)
   - Alert thresholds (warning, alert, critical)
   - Review cadence (daily, weekly, monthly, quarterly)

6. **Output format**:
```markdown
## Metrics Framework: [Product Name]

### Business Game: [Attention / Transaction / Productivity]

### North Star Metric
**[Metric Name]**
- Plain English: [definition]
- Operational: [SQL pseudocode]
- Edge cases: [what counts, what doesn't]
- Data source: [where the data comes from]
- Current baseline: [if known] | Target: [if set]

### Input Metrics
| # | Metric | Owner | Definition | Baseline | Target |
|---|--------|-------|-----------|----------|--------|
| 1 | [Name] | [Team] | [Operational def] | [Value] | [Value] |
| ... | ... | ... | ... | ... | ... |

### Guardrail Metrics
| Metric | Threshold | Alert Channel | Response Time |
|--------|-----------|---------------|---------------|
| [Name] | [e.g., < 5% degradation] | [Slack / PagerDuty] | [4h / 24h] |
```

#### Workflow B: SQL Generation

1. **Clarify the question**: Restate the business question precisely. Confirm any ambiguous terms.

2. **Determine the dialect**: BigQuery, PostgreSQL, MySQL, or Snowflake?

3. **Identify the schema**: Use provided schema, infer from context, or ask.

4. **Generate the query**:
   - Use CTEs for readability
   - Comment every section
   - Handle NULLs, timezones, deduplication explicitly
   - Flag performance concerns for large tables
   - Handle incomplete periods (don't compare a full month to a partial month)

5. **Explain the output**: What columns, what each row represents, expected shape.

6. **Output format**:
```markdown
## SQL Query: [What It Answers]

**Dialect**: [BigQuery / PostgreSQL / MySQL / Snowflake]
**Tables**: [list of tables used]

### Query
```sql
-- [Section comment]
WITH ... AS (
    ...
)
SELECT ...
```

### What This Returns
[Description of output columns and row semantics]

### Assumptions
- [Schema assumptions]
- [Business logic assumptions]

### Performance Notes
- [Estimated scan size, index recommendations, partition pruning]
```

#### Workflow C: Experiment Design

1. **Formulate the hypothesis**: Use the template: "We believe [change] for [users] will cause [metric effect] because [reasoning]."

2. **Select metrics**:
   - Primary metric (one, with operational definition)
   - Secondary metrics (2-3, exploratory)
   - Guardrail metrics (2-3, with degradation thresholds)

3. **Calculate sample size**:
   - State the formula and all parameters (alpha, beta, baseline, MDE)
   - Show the math step by step
   - Calculate expected duration given daily traffic
   - If duration > 90 days, suggest alternatives (larger MDE, more sensitive metric, don't test)

4. **Write the pre-registration**:
   - Complete the pre-registration template from the experiment-design skill
   - Include the decision framework (what to do for each possible outcome)

5. **Output format**: Use the full pre-registration template from experiment-design/SKILL.md.

#### Workflow D: Experiment Analysis

1. **Validate the test design**:
   - SRM check (chi-squared on sample sizes)
   - Power analysis (was the sample sufficient?)
   - Duration check (at least 1-2 business cycles?)

2. **Calculate results**:
   - Point estimate (absolute and relative lift)
   - Confidence interval (95%)
   - P-value (two-tailed z-test for proportions)
   - If Bayesian is appropriate, also calculate posterior probability and expected loss

3. **Check guardrails**: Did any guardrail metric degrade?

4. **Make a recommendation**: Ship / Extend / Kill / Investigate, with explicit reasoning.

5. **Output format**: Use the A/B Test Results template from experiment-design/SKILL.md.

#### Workflow E: Instrumentation Planning

1. **Map the user journey**: Identify every step from first visit to core value to payment to retention.

2. **Design the event taxonomy**:
   - Use `object_action` naming convention
   - Define standard properties (automatic) vs event-specific properties
   - Specify types, required/optional, enum values, and examples

3. **Create the tracking plan**: Use the tracking plan template from instrumentation/SKILL.md.

4. **Prioritize implementation**:
   - Tier 1: Must-have events (acquisition, core action, revenue, errors)
   - Tier 2: Important (onboarding steps, feature adoption, sessions)
   - Tier 3: Nice-to-have (notifications, experiments, referrals)

5. **Data quality setup**:
   - Required property validation rules
   - Volume anomaly alert thresholds
   - Schema versioning approach

6. **Output format**:
```markdown
## Tracking Plan: [Product/Feature Name]

### User Journey
[Step-by-step journey with events mapped to each step]

### Event Taxonomy
[Full tracking plan table with all events, properties, types, and examples]

### Implementation Priority
**Tier 1** (implement first): [list]
**Tier 2** (implement second): [list]
**Tier 3** (implement when capacity allows): [list]

### Data Quality Rules
[Validation rules, alerts, schema versioning]
```

### Step 4: Update metrics.md

After completing the analysis, update `metrics.md` with any new definitions, results, or changes:

- **New metric definitions**: Add to the metrics section with full operational definitions
- **Experiment results**: Add to an experiments log section with date, hypothesis, result, and decision
- **SQL queries**: Save frequently-used queries with descriptions
- **Tracking plan changes**: Note new events or deprecated events

If `metrics.md` doesn't exist, create it with the appropriate structure.

### Step 5: Offer Next Steps

Always end with actionable next steps tailored to what was just delivered:

**After metrics definition**:
- "Want me to design a dashboard layout for these metrics?"
- "Should I write the SQL to calculate these metrics from your data warehouse?"
- "Want me to create a tracking plan to ensure these metrics are instrumented?"

**After SQL generation**:
- "Want me to build a retention/funnel/cohort analysis around this?"
- "Should I create a dashboard spec that includes this query?"
- "Want me to add filters or segment breakdowns?"

**After experiment design**:
- "Ready to generate the SQL to monitor this experiment's metrics?"
- "Want me to calculate the sample size for a different MDE?"
- "Should I design the instrumentation needed to track this experiment?"

**After experiment analysis**:
- "Want me to design a follow-up experiment based on these findings?"
- "Should I write SQL to monitor the shipped metric post-launch?"
- "Want me to run the analysis for specific user segments?"

**After instrumentation**:
- "Want me to define the metrics these events will power?"
- "Should I write SQL queries that use these events?"
- "Want me to design a data quality monitoring dashboard?"

## Cross-Cutting Concerns

### Precision Over Speed
Never deliver a vague metric definition to "get something out quickly." A metric defined as "user engagement" creates more confusion than no metric at all. Take the time to define numerator, denominator, edge cases, and data source.

### Always State Assumptions
Every piece of analysis depends on assumptions. State them explicitly:
- Schema assumptions (table structure, column types)
- Business logic assumptions (what counts as "active," timezone handling)
- Statistical assumptions (independence, normality, homogeneity of variance)
- Data quality assumptions (no gaps, no duplicates, bot filtering in place)

### Connect to Business Decisions
Metrics, queries, and experiments exist to inform decisions. Always connect the output back to:
- What decision will this metric inform?
- What action will we take based on the experiment result?
- Who needs to see this dashboard, and what will they do differently because of it?

### Document Everything
Context is lost between sessions. Every metric definition, experiment result, and tracking plan update should be recorded in `metrics.md` with enough detail that someone reading it in 6 months can understand what was measured, how, and why.

## Error Handling

### Insufficient Context
If the user's request lacks critical information, ask for it rather than guessing:
- "What's your baseline conversion rate? I need this for the sample size calculation."
- "Which SQL dialect are you using? The syntax differs significantly."
- "What does 'active user' mean in your product? I need a precise definition."

### Conflicting Information
If context files contradict each other or the user's request:
- Flag the contradiction explicitly
- Present both interpretations
- Ask the user to resolve before proceeding

### Impossible Requests
If the math doesn't work (e.g., "detect a 1% relative MDE at 2% baseline with 500 users"):
- Show why it doesn't work (sample size calculation)
- Present alternatives (larger MDE, more traffic, different metric)
- Let the user decide which trade-off to accept

## References

- See individual skill files for detailed frameworks and templates:
  - `metrics-definition/SKILL.md` — NSM, input metrics, guardrails, dashboards
  - `sql-analytics/SKILL.md` — SQL patterns, cohort analysis, funnel analysis
  - `experiment-design/SKILL.md` — A/B test design, sample size, analysis
  - `instrumentation/SKILL.md` — Event taxonomy, tracking plans, data quality
