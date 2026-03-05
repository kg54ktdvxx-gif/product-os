---
name: strategy
description: Run a full product strategy workflow — competitive analysis, strategy canvas, positioning, and documentation
argument-hint: "<product or strategic question>"
---

# /strategy Command

Run a complete product strategy workflow. This command chains the strategist's skills into a structured, evidence-based strategy deliverable.

## Workflow

### Step 1: Read Context & Identify Gaps

Read all available context files:
- `product-brief.md` — product description, problem, users
- `personas.md` — user personas and segments
- `metrics.md` — current performance data
- `strategy.md` — any existing strategy (to update, not overwrite)
- `competitive-landscape.md` — any existing competitive intel

Create an inventory of what's KNOWN (with sources), what's ASSUMED (with confidence), and what's UNKNOWN (with impact). Present this to the user before proceeding.

```
## Context Assessment

### Known (grounded in data)
- [fact] — source: [file or data point]

### Assumed (needs validation)
- [assumption] — confidence: H/M/L — impact if wrong: [consequence]

### Unknown (gaps to fill)
- [gap] — impact: [how it affects strategy quality]
```

Ask the user: "Are these assumptions correct? Should I proceed with competitive research, or do you have additional context to share?"

### Step 2: Competitive Analysis (with WebSearch)

If competitive data is thin or outdated, use WebSearch to gather:
- Top 3-5 competitor pricing, features, and positioning
- Recent funding, hiring, and product announcements
- Customer reviews and sentiment from G2, Capterra, Reddit
- Market size data and industry benchmarks

Produce a competitive landscape summary using the framework from `skills/competitive-analysis/SKILL.md`. Write findings to `competitive-landscape.md`.

### Step 3: Build Product Strategy Canvas

Using the 9-section canvas from `skills/product-strategy/SKILL.md`:

1. **Vision**: Draft 2-3 options, recommend one with rationale
2. **Market Segments**: Define 2-3 segments by JTBD, select first segment with justification
3. **Relative Costs**: Position on cost-value spectrum
4. **Value Proposition**: Use 6-part JTBD template for primary segment (from `skills/positioning/SKILL.md`)
5. **Trade-offs**: List what you will NOT do (minimum 3 meaningful trade-offs)
6. **Key Metrics**: North Star + OMTM + 2-3 input metrics
7. **Growth**: PLG/SLG, channels, unit economics
8. **Capabilities**: Build/buy/partner decisions
9. **Can't/Won't**: Honest defensibility assessment

Apply the Playing to Win cascade as a coherence check: Does Where to Play match How to Win? Do Capabilities support the strategy? Are Management Systems in place?

### Step 4: Define Positioning & Value Proposition

Using frameworks from `skills/positioning/SKILL.md`:

1. Run the Dunford positioning exercise (competitive alternatives -> unique attributes -> value -> target customer -> market category)
2. Write the value proposition using the 6-part JTBD template
3. Draft a positioning statement
4. Apply the "could this describe any competitor?" test — revise if it fails
5. If pricing is relevant, outline initial pricing strategy with competitive context

### Step 5: Document in strategy.md

Write the complete strategy to `strategy.md` with these sections:

```markdown
# Product Strategy: [Product Name]
_Last updated: [date]_

## Strategic Narrative (Why Now)
[What changed in the world that creates this opportunity]

## Vision
[Vision statement + rationale]

## Where to Play / Where NOT to Play
[Segments, geographies, channels — with explicit exclusions]

## How to Win
[Theory of competitive advantage — cost leadership, differentiation, or focus]

## Value Proposition
[6-part JTBD value proposition for primary segment]

## Positioning Statement
[Dunford-format positioning statement]

## Key Metrics
[North Star, OMTM, input metrics]

## Growth Strategy
[Channels, motion, unit economics]

## Competitive Position
[Key competitors, our differentiation, competitive dynamics]

## Trade-offs
[What we will NOT do, and what that costs us]

## Defensibility
[Honest assessment of moats and barriers]

## Assumptions & Gaps
[Table of assumptions with confidence and validation plan]

## Next Actions
[Specific, actionable next steps]
```

### Step 6: Self-Evaluate

Before presenting, check all 6 quality criteria from the strategist agent definition:
1. Every claim evidence-backed or flagged as assumption?
2. Clear choices — where to play AND where NOT to play?
3. Explicit tradeoffs with stated costs?
4. Competitive data is specific and cited?
5. Measurable definition of winning?
6. Output is specific to THIS product?

Revise anything that fails.

### Step 7: Suggest Next Steps

Based on the strategy, recommend 2-3 specific next actions. Common handoffs:

- **If user assumptions need validation**: "Interview 5-8 [segment] customers to test assumption #[N] about [topic]. Use The Mom Test methodology — ask about their behavior, not whether they'd use your product."
- **If strategy is solid, product needs definition**: "Hand off to the Discovery agent to run user research, then the Executor to define specific requirements."
- **If positioning and pricing are ready**: "Hand off to the Growth agent to build launch plan, messaging, and channel strategy."
- **If market data is thin**: "Run a deeper market assessment using the market-assessment skill with focused WebSearch on [specific data gaps]."
- **If competitive landscape is shifting**: "Set up monthly competitive monitoring on [specific competitors] — track pricing changes, feature releases, and hiring patterns."

## Usage

```
/strategy [product name or description]
```

If no product description is provided, look for `product-brief.md` in the workspace. If neither exists, ask the user to describe the product, target market, and current state before proceeding.
