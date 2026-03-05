---
name: measure
description: "Define metrics, generate SQL, design experiments, plan instrumentation, or analyze data."
---

# /measure — Measurement Command

Universal entry point for measurement work. Follows the analyst skill's operating protocol. Routes to the right workflow based on the request.

## Invocation

```
/measure Define our North Star Metric
/measure Write a BigQuery query for weekly retention by signup cohort
/measure Design an A/B test for our new onboarding flow
/measure Create a tracking plan for our checkout funnel
/measure Analyze these results: control 4.2% (n=5000), variant 4.8% (n=5100)
```

## Route Detection

| Request Type | Key Signals | Workflow |
|-------------|-------------|----------|
| Metrics Definition | "what to measure", "North Star", "KPIs" | Define NSM + inputs + guardrails + dashboard |
| SQL Generation | "query", "SQL", "how many users" | Generate commented SQL with edge case handling |
| Experiment Design | "A/B test", "experiment", "hypothesis" | Pre-registration with sample size + decision framework |
| Experiment Analysis | "results", "significant", test data provided | Validate design → calculate → check guardrails → recommend |
| Instrumentation | "tracking plan", "events", "analytics setup" | Event taxonomy + tracking plan + implementation priority |
| Cohort Analysis | "retention", "cohort", "churn" | Retention table + patterns + root cause hypotheses |

If the request spans multiple types, handle in logical order: define metrics → write SQL → design dashboard.

## Workflow Details

### Metrics Definition
1. Classify business game (Attention/Transaction/Productivity)
2. Propose 2-3 NSM candidates, validate against 7 criteria, recommend one
3. Full operational definition for NSM + 3-5 input metrics + 2-4 guardrails
4. Dashboard hierarchy if requested (NSM top, inputs middle, guardrails bottom)

### SQL Generation
1. Restate the business question precisely
2. Determine dialect (BigQuery/PostgreSQL/MySQL/Snowflake)
3. Generate with CTEs, comments, NULL/timezone/dedup handling
4. Explain output shape and performance notes

### Experiment Design
1. Formulate hypothesis: "We believe [change] for [users] will cause [metric effect] because [reasoning]"
2. Select primary + secondary + guardrail metrics
3. Calculate sample size (show formula, all parameters, expected duration)
4. Write pre-registration with decision framework

### Experiment Analysis
1. Validate: SRM check, power analysis, duration check
2. Calculate: point estimate, CI, p-value (+ Bayesian if appropriate)
3. Check guardrails
4. Recommend: Ship / Extend / Kill / Investigate

### Instrumentation
1. Map user journey → events
2. `object_action` naming, typed properties, required/optional flags
3. Prioritize: Tier 1 (must-have) → Tier 2 → Tier 3
4. Data quality rules and alert thresholds
