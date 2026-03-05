---
name: strategy
description: Run a full product strategy workflow — competitive analysis, strategy canvas, positioning, and documentation
argument-hint: "<product or strategic question>"
---

# /strategy Command

Run a complete product strategy workflow. Follows the strategist skill's operating protocol (context loading, quality evaluation, context updates). Steps below define what to produce.

## Invocation

```
/strategy [product name or description]
```

## Workflow

### Step 1: Context Assessment

Present what's KNOWN (with sources), ASSUMED (with confidence), and UNKNOWN (with impact). Ask: "Are these assumptions correct? Should I proceed, or do you have context to share?"

### Step 2: Competitive Analysis

If competitive data is thin or outdated, use WebSearch (or ask the user if unavailable) to gather top 3-5 competitor pricing, features, positioning, recent moves, and customer sentiment. Write to `competitive-landscape.md`.

### Step 3: Strategy Canvas

Build the 9-section canvas from `product-strategy/SKILL.md`: Vision, Market Segments, Relative Costs, Value Proposition, Trade-offs, Key Metrics, Growth, Capabilities, Can't/Won't. Apply Playing to Win as a coherence check.

### Step 4: Positioning

Run the Dunford exercise from `positioning/SKILL.md`. Write positioning statement. Apply the "could this describe any competitor?" test.

### Step 5: Document

Write to `strategy.md`. Include: Strategic Narrative, Vision, Where to Play / NOT Play, How to Win, Value Prop, Positioning, Metrics, Growth, Competitive Position, Trade-offs, Defensibility, Assumptions & Gaps, Next Actions.
