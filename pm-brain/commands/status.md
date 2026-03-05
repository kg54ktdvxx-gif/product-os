---
description: Synthesize current product state across all context files — what's defined, what's missing, what's stale, and what to do next
argument-hint: ""
---

# /status — Product State Synthesis

Read all 9 context files and produce a one-page state-of-the-product summary with prioritized next actions.

## Invocation

```
/status
/status strategy       # focus on strategic context
/status gaps           # focus on what's missing
```

## Workflow

### Step 1: Read All Context Files

Read every file in the context/ directory. For each, note:
- Exists? (yes/no)
- Status from header (empty/draft/active/stale)
- Last updated date
- Completeness (are key sections filled in? are there open questions?)

### Step 2: Synthesize

Produce:

```markdown
## Product State: [Product Name]
**As of**: [today's date]
**Stage**: [from product-brief.md]

### Context Health
| File | Status | Updated | Completeness |
|------|--------|---------|-------------|
| product-brief.md | active | Mar 5 | Full |
| strategy.md | draft | Mar 3 | Partial — missing defensibility |
| personas.md | empty | — | Not started |
| ... | ... | ... | ... |

### What's Defined
- [Key strategic choices that have been made]
- [Personas or user understanding that exists]
- [Metrics that are tracked]

### What's Missing (impact-ranked)
1. [Most impactful gap] — "No validated personas. Every downstream decision (PRD, GTM, positioning) is based on assumptions."
2. [Second gap]
3. [Third gap]

### Open Questions (across all files)
- [Aggregated from Open Questions sections of all context files]

### Stale Context
- [Files updated >14 days ago that may not reflect reality]

### Top 3 Actions This Week
1. [Specific, actionable — names the agent and command to use]
2. [...]
3. [...]
```

### Step 3: Offer Actions

For each recommended action, offer to execute it immediately:
"Want me to run discovery to build personas? That's the highest-impact gap right now."

## Notes

- This should be fast — a scan and synthesis, not deep analysis
- If context/ is empty, say so and offer `/brief` to start
- Focus on what's BLOCKING progress, not a comprehensive audit
- The goal is: after reading this, the PM knows exactly what to do next
