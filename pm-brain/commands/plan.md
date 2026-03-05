---
name: plan
description: Decompose a complex outcome into a sequenced plan of agent tasks — the Coordinator designs the workflow
argument-hint: "<desired outcome>"
---

# /plan — Decompose & Sequence

Break a complex outcome into ordered agent tasks. The Coordinator analyzes the request, checks existing context, identifies gaps, and produces a sequenced execution plan.

## Invocation

```
/plan Take our meeting transcription idea from concept to launch
/plan Build a competitive response to [competitor's new feature]
/plan Get ready for our Series A fundraise
/plan          # asks what outcome you want
```

## Workflow

### Step 1: Understand the Outcome

Clarify what "done" looks like. Restate the outcome as a concrete deliverable or state:
- "Done = PRD approved, engineering estimates complete, launch plan written"
- "Done = competitive battlecard updated, positioning adjusted, comms drafted"

### Step 2: Check Context

Read all context files. Assess:
- What already exists that this plan can build on?
- What's missing that must be created first?
- What's stale that needs refreshing?

### Step 3: Design the Plan

Present a numbered sequence of agent tasks:

```markdown
## Plan: [Outcome]

**Starting context**: [What exists]
**Missing prerequisites**: [What needs to be created first]
**Estimated depth**: [Light (15 min) | Medium (30 min) | Deep (60 min)]

### Steps

1. **[Agent]**: [Task description]
   - Input: [What context/files this step uses]
   - Output: [What this step produces]
   - Updates: [Which context files get updated]

2. **[Agent]**: [Task description] — depends on Step 1
   - Input: [...]
   - Output: [...]
   - Updates: [...]

[Continue for all steps]

### Parallel opportunities
- Steps X and Y can run simultaneously
- Step Z must wait for both to complete

### Decision points
- After Step N: User reviews [output] and decides [what]
- After Step M: If [condition], skip Step P
```

### Step 4: Present the Plan with Exact Commands

Present the plan. Each step should include the exact command the user will run:

```
Step 1: Run `/discover [topic]`
  → This produces personas + assumptions. Review before continuing.

Step 2: Run `/strategy`
  → Builds on discovery output. Review positioning before continuing.

Step 3: Run `/build [feature]`
  → Auto-populates PRD from Steps 1-2. Review PRD before sprint planning.
```

Ask: "Ready to start with Step 1, or want to adjust the scope?"

**Important**: `/plan` produces a plan — the user executes each step as a separate command. This is deliberate: each step benefits from user review and course-correction before the next step builds on it. Don't try to produce all outputs in one response.

## Notes

- Plans should be concrete — name the exact commands, outputs, and context files
- Include decision points where the user reviews before continuing
- Identify steps that can run in parallel vs must be sequential
- If the outcome is simple enough for one command, say so and route directly
- Don't plan more than 7 steps. If it's bigger, break it into phases.
- Log the plan to activity-log.md so future sessions know the roadmap
