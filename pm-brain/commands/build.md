---
name: build
description: "Full build command: reads all context, auto-populates a PRD from validated context, flags gaps, breaks into user stories, estimates effort, produces a sprint-ready backlog, and updates the roadmap."
---

# /build -- Full Product Build Pipeline

Turn a feature idea, problem statement, or strategic initiative into a sprint-ready backlog in one pass. This command orchestrates the full Executor pipeline: context reading, PRD creation, story decomposition, effort estimation, and roadmap update.

## Invocation

```
/build Self-serve billing portal for SMB customers
/build Reduce enterprise onboarding time from 14 days to 3 days
/build [upload a brief, research doc, or strategy deck]
/build We keep losing deals to [competitor] because we lack [capability]
```

## Full Pipeline

### Step 1: Read ALL Context Files

Before producing anything, read every available context file in this order:

1. `product-brief.md` -- the foundation (what the product is, who it serves)
2. `strategy.md` -- competitive positioning, strategic bets, value propositions
3. `personas.md` -- validated user personas with jobs-to-be-done
4. `metrics.md` -- current metrics, baselines, targets, KPIs, North Star Metric
5. `assumptions.md` -- validated and unvalidated assumptions
6. `roadmap.md` -- current roadmap (to check for conflicts and alignment)
7. `competitive-landscape.md` -- competitive intelligence, market dynamics
8. `opportunity-tree.md` -- discovery state, opportunities, solutions

For each file that exists, extract relevant information for the build. For each file that does NOT exist, note it as a context gap:

```
## Context Gaps Detected

WARNING: The following context files are missing. This build is
operating with incomplete information.

- personas.md -- MISSING. User segments in this build are hypothetical.
  Recommended: run user interviews before committing engineering resources.
- metrics.md -- MISSING. Success metrics have no baseline. Targets are
  estimated, not data-driven.
- assumptions.md -- MISSING. All assumptions in this build are unvalidated.
```

### Step 2: Determine What Is Being Built

Classify the request:

| Type | Characteristics | Build Approach |
|------|----------------|---------------|
| **New feature** | Does not exist today. Adds new capability. | Full PRD + stories + estimation |
| **Enhancement** | Improves existing feature. | One-pager PRD + stories + estimation |
| **Technical debt** | No direct user impact. Enables future velocity. | Technical spec + stories + justification |
| **Bug fix** | Something is broken. | Skip PRD. Go straight to stories + test scenarios. |
| **Experiment** | Validating a hypothesis. | Lightweight PRD with success/failure criteria + minimal stories |

If the request is ambiguous, ask the user to clarify before proceeding.

### Step 3: Auto-Populate PRD from Context

Apply the **prd** skill with auto-population:

For each PRD section, pull from the corresponding context file (see the auto-population protocol in the prd skill). Do NOT reinvent information that already exists in context files.

**Critical checks:**
- Does the Background section reference `product-brief.md` and `strategy.md`?
- Does Market Segments reference specific personas from `personas.md`?
- Do success metrics have baselines from `metrics.md`?
- Are assumptions tagged as validated or unvalidated from `assumptions.md`?
- Is competitive context referenced from `strategy.md`?

If any section relies on information that is NOT in a context file, add a prominent warning:

> **[UNVALIDATED]**: This section assumes that SMB customers prefer self-serve
> over phone support. No validated data supports this assumption. Recommend:
> survey 50 SMB customers before committing to this scope.

### Step 4: Flag Unvalidated Assumptions

Compile a list of every assumption in the PRD. For each:

| # | Assumption | Source | Status | Impact If Wrong | Validation Method |
|---|-----------|--------|--------|----------------|------------------|
| 1 | SMB prefers self-serve billing | PM intuition | UNVALIDATED | Low adoption, wasted build | Survey 50 SMB customers |
| 2 | Average billing change takes 2.3 days via support | support-data.csv | VALIDATED | N/A | Already confirmed |
| 3 | Payment processor supports plan changes via API | Vendor docs | PARTIALLY VALIDATED | Cannot build -- blocker | Test API in sandbox |

**Rule**: If there are more than 3 unvalidated assumptions that are high-impact, recommend running a validation sprint BEFORE the build sprint. Building on unvalidated assumptions is how teams waste months of engineering time.

### Step 5: Break Into User Stories with Acceptance Criteria

Apply the **backlog-items** skill:

1. Decompose the PRD into 5-15 independent user stories
2. Use the persona from `personas.md` in each story (not "As a user")
3. Write 3-5 testable acceptance criteria per story
4. Prioritize: P0 (must have for launch), P1 (should have, fast-follow), P2 (nice to have)
5. Flag stories that need design input, technical spikes, or external dependencies

**Quality check on each story:**
- Does it pass INVEST? (Independent, Negotiable, Valuable, Estimable, Small, Testable)
- Could a QA engineer write a test from the acceptance criteria alone?
- Does it reference a specific persona?
- Is it small enough for one sprint?

### Step 6: Estimate Effort and Identify Dependencies

For each story, provide:
- **T-shirt size**: S (< 1 day), M (1-3 days), L (3-5 days), XL (split this)
- **Dependencies**: Other stories, other teams, external services
- **Risk level**: Low (well-understood), Medium (some unknowns), High (needs spike)

Create a dependency graph:
```
Story 1 (no deps) ──> Story 4 (depends on 1)
Story 2 (no deps) ──> Story 5 (depends on 2 + 3)
Story 3 (no deps) ──┘
Story 6 (no deps, independent)
```

Identify the critical path (longest chain of dependencies).

### Step 7: Produce Sprint-Ready Backlog

Organize stories into a sprint-ready format:

```
## Sprint-Ready Backlog: [Feature Name]

### Summary
- Total stories: [count]
- P0 stories: [count] ([total effort])
- P1 stories: [count] ([total effort])
- P2 stories: [count] ([total effort])
- Stories needing design: [count]
- Stories needing spikes: [count]
- External dependencies: [count]

### Recommended Sprint 1 Scope
[Select P0 stories that fit within team capacity, respecting dependencies]

| # | Story | Size | Owner | Deps | Risk |
|---|-------|------|-------|------|------|

Sprint goal: "[One sentence describing the value delivered in Sprint 1]"

### Sprint 2+ Candidates
[Remaining P0 and P1 stories]

### Backlog (P2 / Future)
[P2 stories and deferred scope]

### Spike Stories (Do First)
[Technical investigations needed before estimation is possible]

### Open Questions
| Question | Blocks | Owner | Deadline |
|----------|--------|-------|----------|
```

### Step 8: Update roadmap.md

If the build changes scope, priorities, or timeline:
- Add the new initiative to `roadmap.md` under the appropriate time horizon (Now/Next/Later)
- Write it as an OUTCOME, not a feature ("Reduce billing support tickets by 85%" not "Build billing portal")
- Include the success metric from the PRD
- Note dependencies and confidence level
- If this displaces something currently on the roadmap, flag the trade-off explicitly

### Step 9: Offer Next Steps

After producing the build output, suggest 2-3 logical next actions:

```
## Recommended Next Steps

1. **Run a pre-mortem** on the PRD before committing engineering.
   [3 unvalidated assumptions detected -- risk of building the wrong thing]

2. **Create a technical design doc** for the payment processor integration.
   [This is a Type 1 decision -- irreversible vendor choice]

3. **Generate test scenarios** for the P0 stories.
   [QA can start writing tests while engineering starts Sprint 1]

4. **Draft a stakeholder update** for the sales team.
   [This feature changes what sales can promise to prospects]

5. **Create a metrics dashboard** to track the success criteria.
   [Baseline measurement should start NOW, before the feature ships]
```

## Quality Checklist (Self-Evaluation)

Before presenting the build output, verify:

- [ ] Every PRD section references a context file (or flags its absence)
- [ ] No user story starts with "As a user" -- all reference specific personas
- [ ] All acceptance criteria are testable by QA without interpretation
- [ ] Success metrics have baselines (or flag that baselines are missing)
- [ ] Assumptions are explicitly listed with validation status
- [ ] Non-goals are stated (what is OUT of scope)
- [ ] Stories pass INVEST criteria
- [ ] Estimates are provided for all stories
- [ ] Dependencies are mapped
- [ ] Critical path is identified
- [ ] roadmap.md is updated (or flagged for update)
- [ ] At least one unvalidated assumption is called out for investigation

## Notes

- The build command is the Executor's primary workflow. It is the full pipeline from idea to sprint-ready backlog.
- If the input is too vague to build ("we should improve onboarding"), ask clarifying questions before proceeding. Do not guess.
- If context files are missing, produce the build with warnings rather than refusing. A grounded-but-gapped build is better than no build.
- If the feature is too large (15+ stories), recommend phasing and build only Phase 1.
- The build output should be saved as a markdown file: `BUILD-[feature-name].md`
- Always end with next steps. The build is not the end -- it is the beginning of execution.
