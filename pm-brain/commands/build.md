---
name: build
description: "PRD from context, user stories, effort estimates, sprint-ready backlog, roadmap update."
---

# /build — Product Build Pipeline

Turn a feature or initiative into a sprint-ready backlog. Follows the executor skill's operating protocol (context loading, quality evaluation, context updates). Steps below define what to produce.

## Invocation

```
/build Self-serve billing portal for SMB customers
/build Reduce enterprise onboarding time from 14 days to 3 days
```

## Scope Detection

- **Bug fix**: Skip PRD → stories + test scenarios only
- **Enhancement**: One-pager PRD → stories → estimates
- **New feature**: Full PRD → stories → estimates → sprint backlog
- **Experiment**: Lightweight PRD with success/failure criteria → minimal stories

Default to the lightest scope that fits. If unclear, ask.

## Workflow

### Step 1: Context Gaps

Read all context files. For each missing file, flag impact:
```
WARNING: personas.md MISSING — user segments are hypothetical.
WARNING: metrics.md MISSING — success metrics have no baseline.
```

### Step 2: Auto-Populate PRD

Pull every section from context files (prd skill). Do NOT reinvent context that exists. Flag unvalidated sections with `[UNVALIDATED]`.

If >3 high-impact unvalidated assumptions: recommend a validation sprint before committing engineering.

### Step 3: User Stories

Decompose PRD into 5-15 stories. Use specific personas (not "As a user"). 3-5 testable acceptance criteria each. Prioritize: P0 (must-have), P1 (fast-follow), P2 (nice-to-have). INVEST check on each.

### Step 4: Estimates & Dependencies

T-shirt sizes (S/M/L/XL). Dependency graph. Critical path identified. Risk levels.

### Step 5: Sprint Backlog

Organize into recommended Sprint 1 scope (P0 stories that fit capacity) + Sprint 2+ candidates + backlog. Include sprint goal as one sentence.

### Step 6: Update Roadmap

Add initiative to `roadmap.md` as an OUTCOME (not a feature name). Note trade-offs if this displaces existing items.
