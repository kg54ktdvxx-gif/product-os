---
name: discover
description: "Run a full discovery cycle — from context review through ideation, assumption mapping, and experiment design to a complete discovery plan with updated context files."
argument-hint: "<product or feature idea>"
---

# /discover -- Full Discovery Cycle

Run a structured product discovery process that moves from understanding through divergent thinking to focused validation. This command produces a complete discovery plan and updates all relevant context files.

## Invocation

```
/discover Smart notification system for our project management tool
/discover New product: AI writing assistant for non-native speakers
/discover                    # interactive mode — asks what you're discovering
```

## Workflow

### Step 1: Read Context and Determine Product Stage

**Read context files**:
- `product-brief.md` — product vision, target users, problem statement
- `strategy.md` — strategic bets, competitive positioning, constraints
- `metrics.md` — North Star metric, current performance data
- `personas.md` — existing user personas (if any)
- `opportunity-tree.md` — existing opportunity mapping (if any)
- `assumptions.md` — previously identified and tracked assumptions (if any)

**Determine product stage**:
- **Existing product (continuous discovery)**: Real users, real data, established product. Use 4 core risk categories. Ground ideas in observed behavior. Design A/B tests, fake doors, prototypes.
- **New product (initial discovery)**: No validated demand. Use 8 extended risk categories. Focus on desirability first. Design pretotype experiments, XYZ hypotheses.

If the stage is unclear, ask: "Is this for an existing product with real users, or a new product concept that hasn't been validated yet?"

### Step 2: Check Existing Knowledge

Review `assumptions.md` to understand what's already known:
- What assumptions have been tested and validated?
- What assumptions have been tested and invalidated?
- What assumptions are currently being tested?
- What assumptions have been identified but not yet tested?

Present a brief summary: "Here's what we know and don't know. [X] assumptions validated, [Y] invalidated, [Z] untested. The biggest knowledge gaps are: [list]."

If `assumptions.md` doesn't exist, note: "No assumption tracking found. We're starting from scratch — extra rigor needed."

### Step 3: Brainstorm Ideas with Quality Evaluation

Generate ideas from three perspectives (PM, Designer, Engineer). For each idea, evaluate on the Idea Quality Scorecard:

| Dimension | Score (1-5) |
|-----------|-------------|
| Desirability | [evidence-based rating] |
| Viability | [business model assessment] |
| Feasibility | [technical assessment] |
| Differentiation | [competitive assessment] |
| Evidence Base | [quality of supporting evidence] |
| **Composite** | **[average]** |

Present the top 10 ideas ranked by composite score.

**Checkpoint**: "Here are 10 ideas with quality scores. Which ones should we stress-test? Pick 3-5 to carry forward, or I'll take the top 5 by score."

### Step 4: Map Assumptions with Risk x Evidence Ratings

For each selected idea, extract assumptions across risk categories and rate each:

| Assumption | Category | Impact (1-5) | Evidence Level | Priority Score |
|-----------|----------|-------------|----------------|---------------|
| [assumption] | [Value/Usability/Viability/Feasibility/...] | [1-5] | [None/Anecdotal/Qualitative/Quantitative/Validated] | [Impact x Uncertainty] |

Evidence Level mapping to Uncertainty score:
- None = 5
- Anecdotal = 4
- Qualitative = 3
- Quantitative = 2
- Validated = 1

### Step 5: Prioritize and Identify Leap-of-Faith Assumptions

Plot assumptions on the Impact x Uncertainty matrix:

```
EXPERIMENT (test first)  |  INVESTIGATE (gather info)
High Impact, High Uncert.|  Low Impact, High Uncert.
-------------------------+-------------------------
PROCEED (move forward)   |  DEFER (revisit later)
High Impact, Low Uncert. |  Low Impact, Low Uncert.
```

Identify leap-of-faith assumptions: Impact >= 4 AND Evidence Level = None or Anecdotal.

**Checkpoint**: "Here are the riskiest assumptions. The leap-of-faith assumptions are: [list]. Which feel most critical to validate first?"

### Step 6: Design Experiments with Decision Frameworks

For each high-priority assumption, design an experiment:

```
ASSUMPTION: [specific, falsifiable hypothesis]
EXPERIMENT: [method — fake door, prototype, A/B test, landing page, etc.]
METRIC: [what to measure]
SUCCESS THRESHOLD: [specific number]
DECISION FRAMEWORK:
  If [metric] > [threshold A]: PROCEED to [next step]
  If [metric] between [threshold B] and [threshold A]: INVESTIGATE with [method]
  If [metric] < [threshold B]: KILL or PIVOT to [alternative]
EFFORT: [T-shirt size + person-days]
TIMELINE: [start date -> end date]
DEPENDENCIES: [what needs to be true for this experiment to run]
```

Sequence experiments by:
1. Cheapest first (data analysis before fake doors before prototypes before A/B tests)
2. Dependency order (if Experiment B depends on Experiment A's result, A runs first)
3. Leap-of-faith first (test the most dangerous assumption before investing in less risky ones)

### Step 7: Compile Discovery Plan

```
## Discovery Plan: [Topic]

**Date**: [today]
**Product Stage**: [existing / new]
**Discovery Question**: [the core question we're trying to answer]

### Context Summary
[Brief summary of product brief, strategy, existing knowledge]

### Ideas Explored
| Rank | Idea | Composite Score | Top Strength | Top Risk |
|------|------|----------------|--------------|---------|

### Selected Ideas for Validation
[3-5 ideas with rationale for selection]

### Critical Assumptions
| # | Assumption | Category | Impact | Evidence | Priority | Quadrant |
|---|-----------|----------|--------|----------|----------|----------|

### Leap-of-Faith Assumptions
[The 1-3 assumptions that, if wrong, invalidate the entire direction]

### Validation Experiments
| # | Tests Assumption | Method | Success Criteria | Decision Framework | Effort | Timeline |
|---|-----------------|--------|-----------------|-------------------|--------|----------|

### Experiment Details
[For each experiment: full description, setup steps, measurement plan, decision criteria]

### Discovery Timeline
Week 1: [experiments and activities]
Week 2: [experiments and activities]
Week 3: [analysis, synthesis, and decision]

### Decision Framework
- If Experiment 1 succeeds AND Experiment 2 succeeds -> proceed to [PRD / prototype / MVP]
- If Experiment 1 succeeds AND Experiment 2 fails -> [pivot approach, keep opportunity]
- If Experiment 1 fails -> [kill direction, explore alternative opportunities]

### Risks and Mitigations
[What could go wrong with the discovery process itself?]
```

### Step 8: Update Context Files

Update the following files based on the discovery plan:

**personas.md**: Add or refine personas based on any new understanding of users from this discovery cycle.

**opportunity-tree.md**: Add new opportunities identified during ideation. Update scores. Add solutions and planned experiments under the appropriate opportunities.

**assumptions.md**: Add all newly identified assumptions to the tracker with their current status (Identified, Prioritized, or Planned for Testing). Update any previously tracked assumptions that were informed by this discovery cycle.

### Step 9: Offer Next Steps

Based on the discovery plan, suggest concrete next actions routed to the appropriate agent or activity:

- "Run the planned experiments" -> Discoverer (self)
- "Prepare interview scripts to supplement Experiment #2" -> `/interview prep [topic]`
- "Draft a PRD for the top idea (after validation)" -> Executor agent
- "Update the product strategy to reflect these findings" -> Strategist agent
- "Set up metrics to track experiment outcomes" -> `/setup-metrics [topic]`
- "Triage the feature requests that informed this analysis" -> `/triage-requests`
- "Prioritize the validated features for the roadmap" -> `/prioritize [features]`

## Quality Checklist (Before Delivering)

- [ ] Every idea has a composite quality score, not just a ranking
- [ ] Every assumption has a risk category, impact score, and evidence level
- [ ] Every experiment has a specific success threshold and decision framework
- [ ] The opportunity tree connects to a measurable outcome
- [ ] No features disguised as opportunities
- [ ] No user claims without evidence sources
- [ ] The discovery plan has a timeline and explicit decision criteria
- [ ] Context files are updated

## Notes

- This is a 20-40 minute structured workflow. Let the user know upfront.
- At each checkpoint, the user can redirect, skip, or go deeper.
- If the user has research data (interviews, analytics, survey results), extract insights before brainstorming.
- The discovery plan should be a living document — offer to update it as experiments complete.
- For new products, emphasize desirability validation before feasibility.
- For existing products, always check if analytics can answer the question before designing a new experiment.
- The Discoverer's bias should be toward "we don't know enough" rather than "this looks good enough."
