---
name: launch
description: "Full launch planning workflow — from context gathering through beachhead selection, GTM strategy, competitive battlecards, growth loop design, launch readiness checklist, and compiled launch plan with next steps."
argument-hint: "<product or feature to launch>"
---

# /launch -- Full Launch Planning

Build a complete launch plan from first principles. This command orchestrates the full Growth agent toolkit: GTM strategy, competitive intelligence, growth loop design, and launch readiness verification.

## Invocation

```
/launch AI-powered proposal writer for consulting firms
/launch New enterprise tier for our project management tool
/launch Mobile app for existing web product — launching on iOS
/launch [attach strategy.md, personas.md, or product brief]
```

## Workflow

### Step 1: Read Context Files

Read all available context files to understand the product, market, and strategic direction:

- `strategy.md` — Product strategy, vision, and strategic bets
- `personas.md` — User and buyer personas with JTBD
- `competitive-landscape.md` — Competitor analysis, positioning gaps, market dynamics
- `metrics.md` — Current metrics, targets, and measurement frameworks
- `product-brief.md` — Product description, features, value proposition

**If files are missing, flag with explicit warnings**:

| Missing File | Warning | Impact |
|-------------|---------|--------|
| `strategy.md` | "No strategy document found. GTM recommendations will be based on product brief and user input only." | Cannot validate GTM alignment with broader strategy |
| `personas.md` | "No personas defined. Will need to define ICP from scratch — this adds risk." | ICP definition will be based on assumptions, not research |
| `competitive-landscape.md` | "No competitive data available. Will use WebSearch for competitive research — results may be incomplete." | Battlecard will rely on public information only |
| `metrics.md` | "No metrics baseline. Cannot set data-informed targets — will use industry benchmarks." | Success metrics will be generic, not calibrated to current performance |
| `product-brief.md` | "No product brief found. Cannot proceed without understanding the product. Please describe the product." | BLOCKS — cannot proceed without product understanding |

**Do not skip this step.** Missing context produces generic plans. Flag what is missing so the user can decide whether to proceed or fill gaps first.

### Step 2: Understand the Launch

Ask clarifying questions (if not already answered by context files or user input):

- **What are you launching?** New product, new feature, new tier, market expansion, geographic expansion?
- **What stage?** Pre-launch planning (weeks/months out), imminent launch (days), or post-launch optimization?
- **Starting from zero or existing base?** Do you have existing customers, a waitlist, beta users?
- **Timeline?** Hard deadline (event, competitive pressure) or flexible?
- **Budget and team?** What resources can be allocated to launch?
- **GTM motion?** Already decided (PLG, sales-led), or need to determine?

### Step 3: Define Beachhead Segment and ICP

Apply the `gtm-strategy` skill:

1. **List 3-5 candidate segments** based on product brief and persona data
2. **Score each** on the four beachhead criteria (burning pain, willingness to pay, winnability, referral potential)
3. **Select the beachhead** with justification
4. **Define the ICP** within the beachhead: demographics, behaviors, JTBD, pain points, disqualification criteria
5. **Validate** the beachhead is specific enough to find 10 real people in it

**Output**: Beachhead segment selection with scoring + detailed ICP

### Step 4: Create GTM Strategy

Apply the `gtm-strategy` skill:

1. **Select GTM motion**: PLG, sales-led, community-led, or hybrid — with rationale based on ASP, complexity, and buyer type
2. **Choose 2-4 channels**: Ranked by expected CAC with justification
3. **Craft positioning**: Positioning statement that differentiates from actual competitors (reference `competitive-landscape.md`)
4. **Develop messaging**: By stakeholder (end user, manager, executive, IT/security)
5. **Define success metrics**: Launch (30-day), growth (90-day), and steady-state targets

**Output**: GTM strategy document with motion, channels, positioning, messaging, and metrics

### Step 5: Build Competitive Battlecard

Apply the `battlecards` skill:

1. **Identify top 1-3 competitors** that the target segment is most likely to evaluate
2. **Use WebSearch** to research current product, pricing, positioning, and recent changes for each
3. **Build battlecard** for the primary competitor: overview, comparison table, win themes, objection handling, landmines, pricing comparison
4. **Include customer proof points** if available from context files

**Output**: Sales-ready battlecard for the primary competitor (offer to create additional battlecards as next step)

### Step 6: Design Growth Loops

Apply the `growth-engines` skill:

1. **Evaluate all four loop types** (viral, content, paid, sales) for fit with this product and segment
2. **Design the primary growth loop** with quantitative estimates: loop coefficient, cycle time, expected impact over 6 months
3. **Design a secondary loop** if applicable
4. **Define the North Star Metric** with input metrics and validation against 7 criteria

**Output**: Primary and secondary growth loops with quantitative model + North Star Metric framework

### Step 7: Run Launch Readiness Checklist

Apply the `launch-readiness` skill:

1. **Assess all 8 dimensions**: Product, Marketing, Sales, Support, Engineering, Legal, Analytics, Operations
2. **Score each** as Ready / At Risk / Not Ready
3. **Flag must-haves** that are incomplete
4. **Provide a launch/delay recommendation** based on the assessment
5. **Create rollback triggers** with specific thresholds

**Output**: Readiness assessment with dimension scores + launch day playbook + rollback triggers

### Step 8: Compile Launch Plan

Compile all outputs into a single, structured launch plan:

```markdown
# Launch Plan: [Product/Feature]

**Date**: [target launch date]
**Type**: [new product / feature / tier / market expansion]
**Status**: [Ready / At Risk / Not Ready]
**DRI**: [to be assigned]

---

## Executive Summary
[3-5 sentence summary: what we are launching, for whom, through what motion, with what definition of success]

## Beachhead Segment
**Who**: [specific segment]
**Why them first**: [criteria-based rationale]
**Size**: [TAM/SAM/SOM]

## Ideal Customer Profile
| Attribute | Definition |
|-----------|-----------|
| Company size | [range] |
| Industry | [specific] |
| Decision maker | [title/role] |
| Key JTBD | [job] |
| Current solution | [what they use today] |
| Qualification signal | [how to identify them] |
| Disqualification | [who is NOT a fit] |

## GTM Strategy
**Motion**: [PLG / Sales-Led / Community-Led / Hybrid]
**Rationale**: [why this motion for this segment]

### Positioning
For [who] who [need], [product] is [category] that [benefit].
Unlike [alternative], [product] [differentiator].

### Messaging by Stakeholder
| Audience | Message | Proof Point |
|----------|---------|------------|

### Channel Strategy
| Channel | Tactic | Expected CAC | Timeline | Priority |
|---------|--------|-------------|----------|----------|

## Competitive Battlecard: [Competitor]
[Summary battlecard — full version attached separately]

## Growth Strategy
### North Star Metric
**Metric**: [name]
**Definition**: [formula]
**Target**: [goal]

### Primary Growth Loop
**Type**: [viral / content / paid / sales]
**Mechanism**: [step-by-step]
**Loop coefficient**: [estimate]
**Cycle time**: [estimate]

### Secondary Growth Loop
[same format]

## Launch Readiness
| Dimension | Status | Key Risks |
|-----------|--------|-----------|
| Product | [Ready/At Risk/Not Ready] | [specific items] |
| Marketing | ... | ... |
| Sales | ... | ... |
| Support | ... | ... |
| Engineering | ... | ... |
| Legal | ... | ... |
| Analytics | ... | ... |
| Operations | ... | ... |

**Overall Assessment**: [Ready to launch / Launch with mitigations / Delay]

## Launch Timeline
| Phase | Timing | Actions | Owner |
|-------|--------|---------|-------|
| Pre-launch | [dates] | [list] | [who] |
| Launch week | [dates] | [list] | [who] |
| Post-launch | [dates] | [list] | [who] |

## Success Metrics
| Metric | 7-day target | 30-day target | 90-day target |
|--------|-------------|-------------|-------------|

## Rollback Triggers
| Trigger | Threshold | Action |
|---------|-----------|--------|

## Risks and Mitigations
| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|-----------|

## Post-Launch Review Schedule
- **Day 1 review**: [date] — signups, activation, critical bugs, sentiment
- **Week 1 review**: [date] — retention, channel attribution, support patterns
- **Month 1 review**: [date] — full metrics review, lessons learned, scaling decision
```

### Step 9: Offer Next Steps

After delivering the launch plan, offer concrete follow-up actions:

1. **Metrics setup**: "Want me to design the metrics dashboard and define tracking requirements?"
2. **Pricing experiment**: "Should I design a Van Westendorp or Gabor-Granger pricing experiment to validate the price point?"
3. **Retention strategy**: "Want me to design the retention and engagement strategy for post-launch?"
4. **Additional battlecards**: "Should I create battlecards for the other [N] competitors?"
5. **Marketing content**: "Want me to draft the launch blog post, email sequence, or landing page copy?"
6. **Growth experiments**: "Should I design the first 5 growth experiments to run in the first 30 days?"

---

## Execution Notes

- **Do not skip Step 1 (context reading).** A launch plan without context is generic advice. Context makes it specific and actionable.
- **Flag missing prerequisites loudly.** Do not silently work around missing personas or competitive data — tell the user what is missing and what risk it creates.
- **Use WebSearch for competitive intelligence.** Do not rely on stale context files for competitor pricing, recent launches, or market dynamics. Always verify with current data.
- **Be opinionated.** Recommend one beachhead, one primary loop, one primary channel. Do not present 5 options and ask the user to choose without a recommendation.
- **Connect everything to the persona.** Every channel, message, and tactic should trace back to a specific persona behavior or need. If it does not connect, cut it.
- **Define failure.** A launch plan without rollback triggers is wishful thinking. Every success metric needs a "below this threshold, we pause and reassess" counterpart.
- **The plan is a living document.** It should be updated at each post-launch review. The day-1 plan is a hypothesis — the month-1 plan is informed by data.
