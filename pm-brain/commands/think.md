---
name: think
description: Strategic reasoning about a product question — the Coordinator and relevant specialist agents think through it together
argument-hint: "<question or decision to think through>"
---

# /think — Strategic Reasoning

Think deeply about a product question, decision, or tradeoff. The Coordinator reads product context, identifies which specialist perspectives are relevant, and produces structured reasoning.

## Invocation

```
/think Should we build an API or focus on the consumer app?
/think What's our real competitive advantage?
/think Is this feature worth building given our current stage?
/think             # asks what you're thinking about
```

## Workflow

### Step 1: Understand the Question

Read product-brief.md and any relevant context files. Determine:
- What type of question is this? (strategic, tactical, prioritization, risk, positioning)
- What context exists that informs it?
- What context is missing that would change the answer?

If no product-brief.md exists, ask 2-3 questions to establish enough context to reason usefully.

### Step 2: Frame the Decision

Structure the question:
- **What we're deciding**: Restate clearly
- **Why it matters**: What depends on this decision
- **Constraints**: Time, resources, information, dependencies
- **What we know**: Evidence from context files
- **What we don't know**: Gaps that affect the answer

### Step 3: Reason Through It

Apply relevant specialist perspectives:
- **Strategist lens**: Market position, competitive dynamics, long-term defensibility
- **Discoverer lens**: User evidence, validated vs assumed, risk of building the wrong thing
- **Executor lens**: Feasibility, effort, opportunity cost, team capacity
- **Growth lens**: Acquisition impact, retention impact, market timing
- **Analyst lens**: What the data says (or would say if we had it)

For each perspective, state:
- The recommendation from that angle
- The key assumption behind it
- What would change the recommendation

### Step 4: Synthesize

Produce a clear recommendation:

```markdown
## Thinking: [Question]

### Context
[What we know and what we don't]

### Options
| Option | Upside | Downside | Key Assumption |
|--------|--------|----------|----------------|
| A | ... | ... | ... |
| B | ... | ... | ... |

### Recommendation
[Clear recommendation with reasoning]

### What Could Change This
- If [condition], then [alternative] would be better
- We need to learn [X] before we can be confident

### Suggested Next Step
[One specific action to take]
```

### Step 5: Log (if the user decides)

If the user makes a decision based on this thinking, log it in decisions.md.

## Notes

- This is the "thinking partner" command — it reasons, it doesn't produce artifacts
- Keep output concise. One page max, not a 10-page analysis
- If the answer is obvious, say so. Don't manufacture complexity
- If there isn't enough context to reason well, say what's missing and offer to gather it
- Never hide behind "it depends" — take a position, state the assumptions, let the user decide
