---
name: technical-specs
description: "Technical design documents (RFCs), Architecture Decision Records (ADRs), and guidance on when PMs should write tech specs vs engineering. Includes the reversible vs irreversible decision framework, concrete examples of good and bad RFCs, and how to evaluate technical options without being an engineer."
---

# Technical Specifications

## When PMs Should Write Tech Specs

PMs should NOT write implementation-level technical specs. That is engineering's job. PMs SHOULD write (or co-author) specs when:

1. **The decision is irreversible or very expensive to reverse** -- Database schema choices, API contracts, third-party vendor selection, pricing model architecture. These need a documented decision process.
2. **Multiple approaches exist and trade-offs are product-level** -- When the technical choice affects user experience, timeline, cost, or strategy, the PM needs to be in the room and the reasoning needs to be documented.
3. **Cross-team coordination is required** -- When the work involves multiple teams, a written spec prevents the "I thought YOU were handling that" problem.
4. **Stakeholders need to approve before work begins** -- If someone with power needs to say yes, give them a document to react to.

PMs should NOT write specs when:
- The decision is purely implementation (which library, which design pattern)
- Engineering has high confidence in the approach
- The work is small and easily reversible

### The Reversible vs Irreversible Decision Framework

**Type 1 decisions (irreversible / high-cost to reverse):**
- Require thorough analysis and documentation
- Multiple reviewers and approval
- Written RFC with options considered
- Examples: pricing architecture, data model, vendor contracts, public API design

**Type 2 decisions (reversible / low-cost to reverse):**
- Should be made quickly by the person closest to the work
- Lightweight documentation (ADR or even just a Slack message)
- Examples: UI layout choices, internal tooling, feature flag naming, A/B test parameters

**The mistake most organizations make**: Treating Type 2 decisions like Type 1 (over-documenting, over-approving, slowing everything down). The second most common mistake: treating Type 1 decisions like Type 2 (moving fast on something that will be extremely painful to undo).

---

## Part 1: Technical Design Document / RFC

### What an RFC Is

RFC = Request for Comments. A structured document that proposes a technical approach, presents alternatives, and invites feedback before implementation begins. The goal is not to prove you are right -- it is to surface risks and trade-offs while reversal is still cheap.

### RFC Template

```
# RFC: [Title -- what this document proposes]

**Author**: [name]
**Date**: [date]
**Status**: [Draft / In Review / Approved / Superseded]
**Reviewers**: [who needs to review this]
**Decision deadline**: [when we need to decide by, and why]

## 1. Problem Statement

[What problem are we solving? Who has this problem? How painful is it?]
[Reference: product-brief.md, personas.md, or specific user research]

## 2. Context & Constraints

[What is the current state? What systems are involved?]
[Hard constraints: budget, timeline, regulatory, technical debt]
[Soft constraints: team expertise, organizational preferences]

## 3. Options Considered

### Option A: [Name]
**Description**: [How it works]
**Pros**: [What is good about this approach]
**Cons**: [What is bad or risky]
**Effort**: [T-shirt size or person-weeks]
**Risk**: [What could go wrong]

### Option B: [Name]
[Same structure]

### Option C: [Name]
[Same structure]

### Option comparison matrix
| Criteria | Weight | Option A | Option B | Option C |
|----------|--------|----------|----------|----------|
| User experience | High | [score] | [score] | [score] |
| Implementation effort | Medium | [score] | [score] | [score] |
| Scalability | High | [score] | [score] | [score] |
| Maintenance cost | Medium | [score] | [score] | [score] |
| Reversibility | High | [score] | [score] | [score] |

## 4. Recommendation

[Which option and why. Be specific about the reasoning.]
[What would change your recommendation? (new information, different constraints)]

## 5. Implementation Plan

[High-level phases, not detailed task breakdown]
[Key milestones and decision points]
[Dependencies on other teams or systems]

## 6. Risks & Mitigations

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|-----------|

## 7. Rollback Plan

[How do we undo this if it goes wrong?]
[What is the blast radius if it fails?]
[How long would rollback take?]

## 8. Open Questions

| Question | Owner | Deadline | Impact on Decision |
|----------|-------|----------|-------------------|
```

### Good RFC Example

**Title**: RFC: Customer Data Export Architecture

**Problem**: Enterprise customers need to export their data for compliance audits. Currently, they file a support ticket and wait 3-5 business days for a manual CSV export. This causes 8% of enterprise churn (exit interview data).

**Options Considered**:
- **Option A: Real-time API endpoint** -- Customer calls GET /exports with filters. Pros: fast, flexible. Cons: expensive for large datasets (timeouts, memory), requires rate limiting, complex pagination.
- **Option B: Async job queue** -- Customer requests export, job runs in background, notification when ready. Pros: handles large datasets, no timeouts, can be scheduled. Cons: not real-time, requires job infrastructure.
- **Option C: Third-party integration (Fivetran/Stitch)** -- Customers connect their data warehouse. Pros: industry standard, zero maintenance. Cons: $15K/year licensing, adds vendor dependency, 6-week integration timeline.

**Recommendation**: Option B (Async job queue). Handles our largest customer's dataset (2.3M records) without timeout risk. Infrastructure cost is $200/month (SQS + Lambda). Can be built in 3 weeks. If we later need real-time, we can add an API endpoint for smaller exports without replacing the async system.

### Bad RFC Example (and why it is bad)

**Title**: RFC: Data Export

**Problem**: We need data export. (No specifics, no user, no pain quantification)

**Options**: We should use an async queue. (Only one option presented -- this is not a decision document, it is a pre-decided announcement dressed as an RFC)

**Implementation**: TBD. (If you do not know how to implement it, you are not ready for an RFC)

---

## Part 2: Architecture Decision Records (ADR)

### What an ADR Is

An ADR is a lightweight, append-only record of a technical decision. Unlike RFCs (which are written before a decision), ADRs document decisions that have been made. They are retrospective documentation, not prospective analysis.

ADRs answer one question: "Why did we decide to do X instead of Y?" This is invaluable when a new team member (or future-you) asks "why is it built this way?"

### ADR Template

```
# ADR-[number]: [Title]

**Date**: [date]
**Status**: [Accepted / Deprecated / Superseded by ADR-XX]
**Decision makers**: [who made this call]

## Context

[What situation prompted this decision? What forces were at play?]

## Decision

[What did we decide? State it clearly in one or two sentences.]

## Consequences

### Positive
- [What this enables]
- [What problems it solves]

### Negative
- [What trade-offs we accepted]
- [What new constraints this creates]

### Neutral
- [Side effects that are neither good nor bad]
```

### ADR Example

```
# ADR-007: Use PostgreSQL Instead of MongoDB for User Data

**Date**: 2025-03-15
**Status**: Accepted
**Decision makers**: Sarah (Eng Lead), Mike (PM), James (Infra)

## Context

We are building the user profile system. User data has well-defined
relationships (users -> organizations -> teams -> projects). The team
debated relational (PostgreSQL) vs document store (MongoDB). Our ops
team has PostgreSQL expertise but no MongoDB experience.

## Decision

Use PostgreSQL for user data storage.

## Consequences

### Positive
- Strong relational query support for org/team/project hierarchies
- Team has deep PostgreSQL operational experience
- Mature tooling for backups, monitoring, and migrations
- ACID transactions for billing-related user operations

### Negative
- Less flexible for future schema changes (migrations required)
- Horizontal scaling is harder than MongoDB if we hit 10M+ users
- JSON column queries are slower than native document store

### Neutral
- Need to set up connection pooling (PgBouncer) -- standard practice
- Will use Prisma ORM, which supports both Postgres and Mongo,
  so migration path exists if needed later
```

### When to Write an ADR vs an RFC

| Use ADR When... | Use RFC When... |
|----------------|----------------|
| Decision is already made | Decision has not been made yet |
| You want to document reasoning for posterity | You want to invite feedback and debate |
| The decision was straightforward | The decision is complex with real trade-offs |
| 1-2 reviewers are sufficient | Multiple stakeholders need to weigh in |
| Lightweight documentation is appropriate | Thorough analysis is needed |

---

## Part 3: How to Evaluate Technical Options Without Being an Engineer

You do not need to write code to evaluate technical proposals. Focus on these dimensions:

### Questions PMs Should Ask

1. **User impact**: "How does this choice affect load time, reliability, or user experience?"
2. **Timeline**: "How long does each option take? What is the variance in estimates?"
3. **Reversibility**: "If this is wrong, how hard is it to change later? What is the blast radius?"
4. **Maintenance**: "What is the ongoing cost? Who maintains it? What happens when that person leaves?"
5. **Scalability**: "At what usage level does this approach break? Is that before or after our growth targets?"
6. **Dependencies**: "Does this create a new dependency on a vendor, team, or technology? What is the risk of that dependency?"
7. **Precedent**: "Does this create a pattern other teams will follow? Is that a pattern we want?"

### Red Flags in Technical Proposals

- **"This is the only way to do it"** -- There is almost always more than one way. If the engineer cannot articulate alternatives, the analysis is incomplete.
- **"We can always change it later"** -- Maybe. But ask: "How much would it cost to change? Have we ever successfully changed something like this later?" History says organizations rarely go back to fix things.
- **"We need to rebuild from scratch"** -- Almost never true. Ask: "What is the minimum change that solves 80% of the problem?"
- **"Everyone is using [technology X]"** -- Popularity is not a reason. Ask: "What problem does [X] solve that our current stack does not?"
- **"It will take 2 weeks"** -- Engineering estimates are systematically optimistic. Ask: "What is the confidence level? What is the range? What would make it take 6 weeks instead?"

### The PM's Role in Technical Decisions

You are not there to pick the technology. You are there to:
1. Ensure the user's perspective is represented
2. Ensure trade-offs are explicit and documented
3. Ensure the decision aligns with product strategy and timeline
4. Ensure the decision is reversible or, if irreversible, thoroughly vetted
5. Ensure cross-team implications are considered
6. Ask the uncomfortable questions that engineers might skip

## References

- [Documenting Architecture Decisions - Michael Nygard](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions)
- [Design Docs at Google](https://www.industrialempathy.com/posts/design-docs-at-google/)
