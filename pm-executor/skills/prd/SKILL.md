---
name: prd
description: "Create a comprehensive Product Requirements Document grounded in existing context files. 8-section template with auto-population from personas, strategy, metrics, and assumptions. Includes AI PRD considerations, one-pager alternative, and concrete good/bad examples."
---

# Product Requirements Document (PRD)

## Purpose

Create a comprehensive PRD that serves as the authoritative specification for a product or feature initiative. The Executor's PRD is distinguished from generic PRDs by one principle: every section is auto-populated from existing context files, not written from scratch.

## The Auto-Population Protocol

This is the most important section. Before writing any PRD section, check the corresponding context file:

| PRD Section | Primary Source | Secondary Source | If Missing |
|-------------|---------------|-----------------|------------|
| Background & Context | `product-brief.md` | `strategy.md` | Flag: "No product brief found. Background is based on user-provided description only." |
| Market Segments | `personas.md` | `market-research.md` | Flag: "No validated personas. Segments are hypothetical." |
| Value Propositions | `strategy.md` (value prop section) | `product-brief.md` | Flag: "No strategy doc. Value props are assumed." |
| Objective & Key Results | `metrics.md` | `strategy.md` (goals) | Flag: "No metrics baseline. Targets are estimated." |
| Assumptions | `assumptions.md` | Interview notes | Flag: "No assumption tracking. All assumptions in this PRD are unvalidated." |
| Competitive Context | `strategy.md` (competitive section) | `market-research.md` | Flag: "No competitive analysis available." |

**Rule**: If you reference a persona, metric, or strategic position that does not exist in the context files, you MUST flag it with a `[UNVALIDATED]` tag.

## The 8-Section PRD Template

### Section 1: Executive Summary (2-3 sentences)

What is this document about? For whom? Why now?

**Good example:**
> This PRD defines a self-serve billing portal for our SMB segment (see personas.md: "Sarah the Startup Founder"). Current billing changes require support tickets (avg 2.3 days resolution), causing 12% of billing-related churn (metrics.md: churn-by-cause). The portal will allow customers to upgrade, downgrade, and manage payment methods without support intervention.

**Bad example:**
> This PRD is about building a billing portal. Users want to manage their billing. It will improve the user experience.

The bad example has no specifics, no persona reference, no metric, and no "why now."

### Section 2: Contacts

| Role | Name | Responsibility |
|------|------|---------------|
| Product Manager | [Name] | PRD owner, scope decisions |
| Engineering Lead | [Name] | Technical feasibility, estimates |
| Design Lead | [Name] | UX, prototypes |
| Stakeholder | [Name] | Approval, business context |

### Section 3: Background & Context

Pull from `product-brief.md` and `strategy.md`. Answer:
- What is this initiative about?
- Why now? What changed? (Market shift, customer pain threshold, competitive move, new capability)
- What has been tried before? What did we learn?
- How does this connect to product strategy?

**Anti-pattern**: Writing background from scratch when `product-brief.md` exists. If the brief covers this ground, reference it and add only what is new.

### Section 4: Objective & Key Results

Pull baseline metrics from `metrics.md`. Objectives should be SMART.

**Good OKR in a PRD:**
> **Objective**: Eliminate billing-related support burden for SMB customers
> - KR1: Reduce billing support tickets from 340/month to <50/month within 90 days of launch
> - KR2: Self-serve billing adoption rate >70% of SMB accounts within 60 days
> - KR3: Billing-related churn drops from 12% to <5% within one quarter

**Bad OKR in a PRD:**
> **Objective**: Improve billing experience
> - KR1: Launch billing portal
> - KR2: Get good feedback
> - KR3: Reduce churn

The bad version has no numbers, no timelines, and KR1 is an output (launching) not an outcome (impact).

### Section 5: Market Segments

Pull directly from `personas.md`. Do not invent new personas for the PRD. If the feature targets a segment not yet in `personas.md`, flag it:

> **[CONTEXT GAP]**: This feature targets enterprise IT administrators. No validated persona exists for this segment in `personas.md`. Recommend: create and validate this persona before committing to this PRD scope.

For each segment, specify:
- Which persona from `personas.md`
- Their relevant jobs-to-be-done
- Current workaround and pain level
- Size of segment (from `market-research.md` if available)

### Section 6: Value Propositions

Pull from `strategy.md` value proposition section. For each target segment:
- What customer jobs/needs does this address?
- What gains does the customer get?
- What pains does this eliminate?
- How does this compare to competitor solutions? (reference `strategy.md` competitive section)

Use the Value Curve framework when comparing to competitors: which factors do we raise, reduce, eliminate, or create?

### Section 7: Solution

#### 7.1 User Flows & Prototypes
Link to designs. If no designs exist, describe the flow in words with clear decision points.

#### 7.2 Key Features (prioritized)

**P0 -- Must Have (launch blockers):**

| # | Feature | User Story | Acceptance Criteria |
|---|---------|-----------|-------------------|
| 1 | [Feature] | As [persona from personas.md], I want... | [Testable criteria] |

**P1 -- Should Have (fast-follow):**
[Same format]

**P2 -- Nice to Have (future consideration):**
[Same format]

#### 7.3 Technical Considerations
Only include if relevant. Architecture choices, API design, data model implications. For significant technical decisions, reference the technical-specs skill to produce a separate RFC.

#### 7.4 Assumptions
Pull from `assumptions.md` and add PRD-specific assumptions. For each assumption, state:
- The assumption itself
- Whether it is validated or unvalidated
- What happens if it is wrong (impact on this PRD)
- How to validate it (if unvalidated)

**Example:**
> ASSUMPTION: SMB customers will prefer self-serve billing over calling support. STATUS: Unvalidated. IMPACT: If wrong, adoption will be low and billing support tickets will not decrease. VALIDATION: Include opt-in survey in first 30 days; track self-serve vs support ticket ratio.

#### 7.5 Non-Goals (Explicit Scope Exclusions)
What are we NOT building? And why?

**Good non-goal:**
> We will NOT support multi-currency billing in V1. Reason: Only 8% of SMB customers are international (metrics.md), and multi-currency adds 3 weeks to the timeline. Will revisit in V2 if international SMB segment grows.

**Bad non-goal:**
> We are not doing multi-currency right now.

The bad version does not explain WHY or WHEN it might be reconsidered.

### Section 8: Release & Timeline

- Relative timeframes, not exact dates. "4-6 weeks after engineering kick-off" not "March 15."
- Phase 1 vs Phase 2 scope. What goes in the first version? What is deferred?
- Dependencies on other teams or systems.
- Rollback plan if launch goes badly.

## The One-Pager PRD Alternative

For smaller features or rapid iteration, use a condensed format:

```
# [Feature Name] -- One-Pager PRD

**Problem**: [1-2 sentences -- what is broken and for whom]
**Persona**: [from personas.md]
**Metric to move**: [from metrics.md]
**Proposed solution**: [2-3 sentences]
**Success criteria**: [2-3 measurable outcomes]
**Non-goals**: [what we are NOT doing]
**Open questions**: [what we do not know yet]
**Effort estimate**: [T-shirt size: S/M/L/XL]
```

Use the one-pager when: the feature is <2 weeks of engineering, the scope is well-understood, and there are fewer than 3 stakeholders.

## AI PRD Template Considerations

When the PRD involves AI/ML features, add these sections (inspired by Miqdad Jaffer's AI PRD Template):

### Evaluation Metrics
- What offline metrics define model quality? (precision, recall, F1, BLEU, etc.)
- What online metrics define user-perceived quality? (task completion rate, user satisfaction, error rate)
- What is the minimum acceptable performance threshold for launch?

### Safety & Guardrails
- What harmful outputs could the model produce?
- What guardrails exist? (content filtering, output validation, human review)
- What is the escalation path when guardrails fail?

### Human-in-the-Loop
- Where does a human review AI output before it reaches the user?
- What is the feedback loop for improving model quality?
- Can users correct or override AI decisions?

### Edge Cases & Failure Modes
- What happens when the model is uncertain?
- What is the fallback experience when AI is unavailable?
- How do we handle adversarial inputs?

### Bias & Fairness
- What populations could be disproportionately affected?
- How do we measure and monitor fairness?
- What data biases exist in the training set?

### Data Requirements
- What data does the model need? Where does it come from?
- What are the privacy implications? (PII, consent, retention)
- What is the data pipeline for retraining?

## Common PRD Failures

These are the patterns that make PRDs useless. Avoid them:

1. **Too long** -- A 30-page PRD that nobody reads is worse than a 3-page PRD everyone references. Cut ruthlessly.
2. **No success metrics** -- If you cannot define what success looks like, you are not ready to write a PRD.
3. **Solution before problem** -- The PRD jumps to features without establishing who has the problem and how painful it is.
4. **Scope creep through ambiguity** -- "We might also want to..." and "potentially including..." create implied scope that engineering will discover mid-sprint.
5. **No non-goals** -- Without explicit exclusions, every stakeholder assumes their pet feature is in scope.
6. **Disconnected from strategy** -- The PRD does not reference the product strategy, making it impossible to evaluate whether this feature is worth building vs. the 50 other things on the backlog.
7. **Vanity metrics** -- "Increase page views" without connecting to business outcomes. Page views of what? Leading to what action? Driving what revenue?
8. **Missing assumptions** -- Every PRD has assumptions. The ones that are not stated are the most dangerous because nobody validates them.

## References

- [How to Write a Product Requirements Document? The Best PRD Template.](https://www.productcompass.pm/p/prd-template)
- [A Proven AI PRD Template by Miqdad Jaffer (Product Lead @ OpenAI)](https://www.productcompass.pm/p/ai-prd-template)
