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

Create the remaining 9 context files with headers and empty status. Don't force the user to fill them — agents will populate them as work happens.

### Step 4: Suggest First Actions

Based on the product stage:
- **Idea**: "Start with `/discover` to validate assumptions and build an opportunity tree"
- **Discovery**: "Start with `/discover` or provide research data for synthesis"
- **Building**: "Start with `/build` for PRD or `/measure` to define metrics"
- **Live**: "Start with `/status` to assess gaps, or `/measure` to review metrics"
- **Scaling**: "Start with `/launch` for growth strategy or `/strategy` for competitive positioning"

## Notes

- This should take 2-3 minutes, not 20. The brief is a starting point, not a thesis.
- Don't ask for information the user clearly doesn't have yet. If they say "it's just an idea," don't ask for team size and budget.
- The brief will be refined as other agents do their work — personas get sharper after discovery, constraints get clearer after technical specs.
