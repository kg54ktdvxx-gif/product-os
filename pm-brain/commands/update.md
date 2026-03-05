---
description: Intake new information into the product context layer — research, decisions, competitive intel, or feedback
argument-hint: "<new information or context>"
---

# /update — Context Intake

Feed new information into the product context layer. The Coordinator classifies it, updates the right files, and flags downstream implications.

## Invocation

```
/update Our main competitor just raised $50M and launched an AI feature
/update [paste interview transcript]
/update We decided to go PLG instead of sales-led
/update Here's our latest NPS data [attach file]
```

## Workflow

### Step 1: Classify

What type of information is this?
- **Competitive intel** → update competitive-landscape.md (Strategist)
- **User research** → update personas.md, assumptions.md, opportunity-tree.md (Discoverer)
- **Decision** → log in decisions.md (Coordinator)
- **Metrics/data** → update metrics.md (Analyst)
- **Strategy change** → update strategy.md (Strategist)
- **Roadmap change** → update roadmap.md (Executor)
- **General context** → update product-brief.md (Coordinator)

### Step 2: Update Files

Route to the owning agent to update the appropriate context file(s). Preserve existing content — add, don't overwrite.

### Step 3: Flag Implications

After updating, check for downstream effects:

```markdown
## Updated
- [File]: [What changed]

## Implications
- [Agent]: [What this means for their domain]
  Example: "Strategist: Competitor's AI feature may require repositioning"
  Example: "Growth: Battlecard needs updating with new competitor pricing"
  Example: "Discoverer: Assumption #3 about [X] is now invalidated"

## Suggested Actions
1. [Specific action to take in response]
```

## Notes

- For large data (transcripts, CSVs, survey results), route to the appropriate specialist agent for analysis first, then update context with the synthesized findings
- For decisions, always log in decisions.md with the full format (context, options, decision, rationale, implications)
- If the update contradicts existing context, flag the contradiction — don't silently overwrite
