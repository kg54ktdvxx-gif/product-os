---
name: discover
description: "Run a discovery cycle — assumption mapping, experiment design, and validation planning. Scope adapts to the question."
argument-hint: "<product or feature idea>"
---

# /discover — Discovery Cycle

Run a structured product discovery process. Follows the discoverer skill's operating protocol (context loading, quality evaluation, context updates). Steps below define what to produce.

## Invocation

```
/discover Smart notification system for our project management tool
/discover                    # interactive mode
```

## Scope Detection

Match output depth to the request:

- **Narrow question** ("Should we add dark mode?"): Identify 3-5 assumptions, design 1-2 experiments, done. ~500 words.
- **Feature exploration** ("Smart notifications"): Brainstorm ideas, map assumptions, design experiments. ~1,000 words.
- **Full discovery cycle** ("New product idea" or `--deep`): All steps below. ~2,000 words.

Default to focused. Go deep only when asked or when the scope demands it.

## Workflow

### Step 1: Determine Stage

- **Existing product**: Real users, real data. Use 4 core risk categories. Design A/B tests, fake doors.
- **New product**: No validated demand. Use 8 extended risk categories. Focus on desirability. Design pretotype experiments.

### Step 2: Check What We Already Know

Review `assumptions.md`: what's validated, invalidated, untested? Brief summary: "[X] validated, [Y] invalidated, [Z] untested. Biggest gaps: [list]."

### Step 3: Brainstorm & Score (if scope warrants)

Generate ideas from PM/Designer/Engineer perspectives. Score each on Desirability, Viability, Feasibility, Differentiation, Evidence Base. Present top ideas ranked by composite.

### Step 4: Map Assumptions

For selected ideas, extract assumptions with: Category, Impact (1-5), Evidence Level (None→Validated), Priority Score. Identify leap-of-faith assumptions (Impact ≥ 4, Evidence = None/Anecdotal).

### Step 5: Design Experiments

For each high-priority assumption:
- Hypothesis (specific, falsifiable)
- Method (cheapest viable: data analysis → fake door → prototype → A/B)
- Success threshold (specific number)
- Decision framework (if X → proceed, if Y → investigate, if Z → kill)
- Effort and timeline

Sequence: cheapest first, dependency order, leap-of-faith first.

### Step 6: Update Context

Write to: `personas.md` (if refined), `opportunity-tree.md` (new branches), `assumptions.md` (new entries with status).
