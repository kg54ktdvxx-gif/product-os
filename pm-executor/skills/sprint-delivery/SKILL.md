---
name: sprint-delivery
description: "Full sprint lifecycle: planning with capacity estimation, retrospectives with structured facilitation, release notes, pre-mortem risk analysis (Tigers/Paper Tigers/Elephants), test scenario generation, and dummy dataset creation. Includes concrete examples and anti-patterns for each phase."
---

# Sprint Delivery Lifecycle

## Part 1: Sprint Planning

### Capacity Estimation

Capacity is not "how many people we have." It is:

```
Available capacity = Team members
                     x Available days (minus PTO, holidays, on-call)
                     x Productive hours per day (typically 5-6, not 8)
                     x Historical velocity factor (from last 3 sprints)
                     - Buffer (15-20% for bugs, interrupts, meetings)
```

**Example:**
- 4 engineers, 2-week sprint (10 working days)
- Engineer A: full availability (10 days)
- Engineer B: 2 days PTO (8 days)
- Engineer C: on-call for 3 days (7 effective days)
- Engineer D: full availability (10 days)
- Total: 35 available days x 6 productive hours = 210 hours
- Historical velocity: 75% of estimated hours actually spent on sprint work
- Effective capacity: 210 x 0.75 = 157.5 hours
- Buffer (20%): 126 hours of committable work

**Anti-pattern: Planning at 100% capacity.** Teams that plan at full capacity always miss. Always. The 20% buffer is not slack -- it is reality.

### Story Selection

1. Pull from the prioritized backlog (highest priority first)
2. Verify each story meets Definition of Ready:
   - Acceptance criteria are written and testable
   - Estimate exists (story points or hours)
   - No unresolved blockers
   - Design is available (if UI work)
3. Flag stories that need refinement before committing
4. Stop adding stories when capacity is reached
5. Balance: include at least one quick win alongside larger items

### Sprint Goal

**Good sprint goal:**
> "Customers can self-serve all billing changes without contacting support"

**Bad sprint goal:**
> "Complete stories 1-7 from the backlog"

The good goal describes value delivery. The bad goal describes task completion. If you complete stories 1-7 but billing self-serve does not work end-to-end, is the sprint successful? No.

### Dependency Mapping

For each story, identify:
- Does it depend on another story in this sprint?
- Does it depend on work by another team?
- Does it block other stories?
- What is the critical path (longest chain of dependencies)?

Flag external dependencies explicitly with owner and expected delivery date. If a dependency is unconfirmed, treat it as a risk.

### How to Handle Scope Changes Mid-Sprint

When new work arrives mid-sprint:
1. Ask: "Is this more important than what we already committed to?"
2. If yes: remove an equivalent-effort item from the sprint. Never add without removing.
3. If no: add it to the backlog for next sprint.
4. If unclear: escalate to the product owner for a priority call.

Never silently absorb scope. It erodes sprint predictability and burns out the team.

### Sprint Plan Output Format

```
## Sprint Plan: [Sprint Name/Number]

**Duration**: [dates]
**Sprint Goal**: [one sentence describing value delivery]
**Team**: [members and availability]

### Capacity
| Member | Available Days | Capacity (hrs) | Notes |
|--------|--------------|----------------|-------|

**Total capacity**: [X] hours
**Committed**: [Y] hours ([Z]% of capacity)
**Buffer**: [remaining] hours

### Committed Stories
| # | Story | Points/Hours | Owner | Dependencies | Risk |
|---|-------|-------------|-------|-------------|------|

### Risks
| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|-----------|

### Definition of Done
- [ ] Code reviewed and approved
- [ ] Tests passing (unit + integration)
- [ ] Deployed to staging
- [ ] QA approved
- [ ] Documentation updated (if applicable)
- [ ] Acceptance criteria verified
```

---

## Part 2: Sprint Retrospective

### The Three Formats

**Format A -- Start / Stop / Continue** (fastest, best for experienced teams):
- **Start**: What should we begin doing?
- **Stop**: What should we stop doing?
- **Continue**: What is working well?

**Format B -- 4Ls** (best for nuanced reflection):
- **Liked**: What did the team enjoy?
- **Learned**: What new knowledge was gained?
- **Lacked**: What was missing?
- **Longed For**: What do we wish we had?

**Format C -- Sailboat** (best for visual thinkers):
- **Wind** (propels us): What is driving us forward?
- **Anchor** (holds us back): What is slowing us down?
- **Rocks** (risks): What dangers lie ahead?
- **Island** (goal): Where are we trying to get?

### Retrospective Anti-Patterns

1. **The blame game** -- Retros that focus on WHO did wrong instead of WHAT went wrong. Fix: use "we" language, focus on systems not individuals.
2. **No action items** -- Retros that generate discussion but no commitments. Fix: limit to 2-3 specific, owned, deadlined action items.
3. **Same issues every sprint** -- If "communication" appears in every retro, the action items are not working. Fix: review previous retro actions at the START of each retro. Were they completed? Did they help?
4. **Only negative** -- Retros that skip celebrating wins. Fix: always start with "what went well" and spend real time on it.
5. **Too many action items** -- 10 action items means 0 action items. Fix: maximum 3, prioritized by impact.
6. **Attendance theater** -- Everyone attends but no one speaks honestly. Fix: anonymous input collection before the retro, then discuss themes.

### Retro Output Format

```
## Sprint [X] Retrospective -- [Date]

### Sprint Performance
- Goal: [Achieved / Partially / Missed]
- Committed: [X pts] | Completed: [Y pts] | Velocity: [Z]%

### Previous Retro Actions (accountability check)
| Action | Owner | Status | Impact |
|--------|-------|--------|--------|

### Key Themes
1. [Theme] -- [summary with evidence]
2. [Theme] -- [summary with evidence]

### Action Items (MAX 3)
| # | Action | Owner | Deadline | Success Metric |
|---|--------|-------|----------|---------------|

### Wins Worth Celebrating
- [Win 1]
- [Win 2]
```

---

## Part 3: Release Notes

### Transformation Principle

Technical change --> User benefit. Always.

**Before (technical):** "Implemented Redis caching layer for dashboard API endpoints"
**After (user-facing):** "Dashboards now load up to 3x faster, so you spend less time waiting and more time analyzing."

**Before (technical):** "Fixed race condition in concurrent checkout flow"
**After (user-facing):** "Fixed an issue where some orders could fail during high-traffic periods."

### Release Notes Structure

```
# [Product Name] -- [Version / Date]

## Highlights
[1-2 sentence summary of the most impactful change]

## New Features
- **[Feature name]**: [What it does and why it matters to YOU, the user]

## Improvements
- **[Area]**: [What got better and how it helps]

## Bug Fixes
- Fixed [issue description in user terms]

## Breaking Changes (if any)
- **Action required**: [Exactly what users need to do]

## Coming Soon
[Optional teaser for next release]
```

### Tone by Product Type

- **B2B SaaS**: Professional, benefit-focused, include migration details
- **Consumer app**: Friendly, short, emoji-appropriate
- **Developer API**: Technical, precise, include code samples for breaking changes
- **Enterprise**: Formal, compliance-aware, include security patch details

---

## Part 4: Pre-Mortem Risk Analysis

### The Framework: Tigers, Paper Tigers, Elephants

Imagine the product launched two weeks ago and FAILED. What went wrong?

**Tigers** -- Real risks that could cause failure. Based on evidence, past experience, or clear logic.

Classify by urgency:
- **Launch-blocking**: Must be solved before launch. No exceptions.
- **Fast-follow**: Must be solved within 30 days post-launch.
- **Track**: Monitor post-launch. Act if it becomes real.

**Paper Tigers** -- Concerns that feel scary but are overblown. Worth documenting to prevent stakeholder anxiety, but not worth significant investment.

**Elephants** -- Risks the team knows about but avoids discussing. Often political, organizational, or uncomfortable. These are the HIGHEST-VALUE output of a pre-mortem because they surface what no one else will say.

### Pre-Mortem Risk Categories

Ensure you cover all categories:
- **Technical**: Performance, scalability, integration, data integrity
- **User**: Adoption, usability, unmet expectations, migration friction
- **Business**: Revenue impact, competitive response, market timing, cannibalization
- **Operational**: Support load, documentation, training, monitoring
- **Dependencies**: Third-party services, cross-team handoffs, regulatory approval

### Pre-Mortem Output Format

```
## Pre-Mortem: [Feature/Launch]

### Risk Summary
- Tigers: [count] ([launch-blocking], [fast-follow], [track])
- Paper Tigers: [count]
- Elephants: [count]

### Launch-Blocking Tigers
| # | Risk | Likelihood | Impact | Mitigation | Owner | Deadline |
|---|------|-----------|--------|-----------|-------|----------|

### Fast-Follow Tigers
| # | Risk | Planned Response | Owner | Timeline |
|---|------|-----------------|-------|----------|

### Paper Tigers
| # | Concern | Why It Is Manageable | Would Become Real Tiger If... |
|---|---------|---------------------|------------------------------|

### Elephants in the Room
| # | Unspoken Risk | Why It Matters | Suggested Discussion Starter |
|---|--------------|---------------|------------------------------|

### Go/No-Go Checklist
- [ ] All launch-blocking Tigers mitigated
- [ ] Fast-follow plan documented and assigned
- [ ] Monitoring in place for Track Tigers
- [ ] Rollback plan defined and tested
- [ ] Support team briefed and trained
```

---

## Part 5: Test Scenarios

### Scenario Types

For each user story or requirement, generate:
1. **Happy path**: The expected flow works correctly
2. **Edge cases**: Boundary conditions, unusual inputs, concurrent operations
3. **Error scenarios**: Invalid inputs, system failures, network issues
4. **Security scenarios**: Auth, permissions, data access, injection
5. **Performance scenarios**: Load, timeout, large datasets
6. **Accessibility scenarios**: Screen reader, keyboard navigation, color contrast

### Test Scenario Template

```
**Scenario**: [Clear, descriptive name]
**Tests**: [Which story/requirement]
**Preconditions**: [System state, data setup, user permissions]
**User role**: [Specific persona, not "user"]

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | [User does X] | [System responds with Y] |
| 2 | [User does X] | [System responds with Y] |

**Postconditions**: [System state after completion]
**Priority**: [Critical / High / Medium / Low]
```

### Good vs Bad Acceptance Criteria in Tests

**Bad**: "Search works correctly" -- What does "correctly" mean? A QA engineer cannot execute this.

**Good**: "Search returns results within 200ms for queries up to 100 characters, displays top 20 results sorted by relevance, shows 'no results found' message with spelling suggestions when no matches exist, and handles special characters without error."

---

## Part 6: Dummy Dataset Generation

### When You Need Test Data

- Development: Realistic data for building UI and testing logic
- QA: Specific data patterns to exercise edge cases
- Demos: Data that tells a compelling story
- Load testing: Large volumes with realistic distribution

### Output Formats

- **CSV**: Flat tabular, works everywhere
- **JSON**: Nested structure, good for APIs
- **SQL INSERT**: Directly executable on databases
- **Python script**: Reproducible generator for custom needs

### Realism Checklist

- Names look real (not "User1", "Test User")
- Emails use realistic domains (gmail, company.com -- not test@test.com)
- Dates are chronological and realistic
- Numeric distributions match real patterns (not uniform random)
- Relationships are consistent (an order references an existing customer)
- Cardinality is realistic (1000 users do not have 1000 unique cities)

### Example Specification

```
Dataset: Customer Feedback
Rows: 500
Columns: feedback_id, customer_name, email, date, rating (1-5), category, text
Constraints:
  - Rating distribution: 40% 5-star, 30% 4-star, 20% 3-star, 10% 1-2 star
  - Bug reports only with ratings 1-3
  - Feature requests only with ratings 3-5
  - Dates within last 90 days, weighted toward recent
Format: CSV + Python generator script
```

## References

- [Product Owner vs Product Manager](https://www.productcompass.pm/p/product-manager-vs-product-owner)
- [How Meta Uses Pre-Mortems](https://www.productcompass.pm/p/how-to-run-pre-mortem-template)
- [How to Manage Risks as a PM](https://www.productcompass.pm/p/how-to-manage-risks-as-a-product-manager)
