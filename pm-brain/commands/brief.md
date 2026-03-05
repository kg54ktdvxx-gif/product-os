---
name: brief
description: Initialize or update the product brief — the foundation context that all agents reference
argument-hint: "<product name or description>"
---

# /brief — Product Brief

Create or update product-brief.md — the foundation file that all agents read on every request.

## Invocation

```
/brief AI-powered golf swing analyzer for iOS
/brief                # asks about the product
/brief update         # update existing brief with new info
```

## Workflow

### Step 1: Gather Context (conversational, not a form)

If creating new: Ask these questions naturally, not as a numbered list. Adapt based on what the user already provided in their initial message.

1. **What does it do?** (core mechanism, not feature list)
2. **Who is it for?** (specific user, not "everyone")
3. **Why does it matter?** (the problem, and why now)
4. **What stage is it?** (idea / discovery / building / live / scaling)
5. **What are the constraints?** (team, timeline, budget, technical)

If the user provided a detailed description in $ARGUMENTS, extract answers from it and confirm rather than re-asking.

If updating: Read existing product-brief.md, ask what changed, update relevant sections.

### Step 2: Write product-brief.md

Follow the schema from the context-manager skill. Keep it to one page.

### Step 3: Initialize Empty Context Files

Create the remaining 11 context files with headers and empty status (including activity-log.md and learnings.md). Don't force the user to fill them — agents will populate them as work happens.

### Step 4: Suggest Kickoff Sequence

Don't just suggest one command — give a concrete 3-step sequence to warm up the context layer:

- **Idea/Discovery**:
  ```
  1. /discover — build personas, surface assumptions, design experiments (20 min)
  2. /strategy — draft positioning using brief + discovery output (15 min)
  3. /status — see what's grounded and what still needs validation
  ```
- **Building**:
  ```
  1. /strategy — capture your competitive positioning (15 min)
  2. /build — PRD grounded in strategy context (20 min)
  3. /measure — define success metrics before you ship
  ```
- **Live/Scaling**:
  ```
  1. /status — assess what context exists and what's stale
  2. /measure — define or review metrics framework
  3. /launch or /strategy — based on what /status surfaces
  ```

End with: "After these 3 steps your context layer is warm enough for any command to produce grounded output. Run [first command] now?"

## Notes

- This should take 2-3 minutes, not 20. The brief is a starting point, not a thesis.
- Don't ask for information the user clearly doesn't have yet. If they say "it's just an idea," don't ask for team size and budget.
- The brief will be refined as other agents do their work — personas get sharper after discovery, constraints get clearer after technical specs.
