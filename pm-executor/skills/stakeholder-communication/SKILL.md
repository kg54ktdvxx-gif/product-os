---
name: stakeholder-communication
description: "Stakeholder mapping with Power x Interest grid, meeting transcript synthesis, executive update templates, and product sunset/deprecation communication. Includes communication frequency and channel guidance by stakeholder type, how to deliver bad news, and how to write a compelling 'why' for buy-in."
---

# Stakeholder Communication

## Part 1: Stakeholder Mapping

### The Power x Interest Grid

Every stakeholder has two attributes:
- **Power**: Their ability to influence decisions, resources, budget, or outcomes
- **Interest**: How much the project directly affects them or how engaged they want to be

Map each stakeholder into one of four quadrants:

```
                    HIGH INTEREST
                         |
    KEEP SATISFIED       |      MANAGE CLOSELY
    (High Power,         |      (High Power,
     Low Interest)       |       High Interest)
                         |
   ----------------------+----------------------
                         |
    MONITOR              |      KEEP INFORMED
    (Low Power,          |      (Low Power,
     Low Interest)       |       High Interest)
                         |
                    LOW INTEREST
```

### Communication Strategy by Quadrant

**Manage Closely (High Power, High Interest)**
- Frequency: Weekly or bi-weekly 1:1s
- Channel: Face-to-face or video call, with written follow-up
- Approach: Involve in decisions early. Seek input before announcing. No surprises.
- Risk if neglected: They block the project because they feel uninformed or disrespected.

**Keep Satisfied (High Power, Low Interest)**
- Frequency: Monthly or milestone-based updates
- Channel: Brief email or executive summary (1 paragraph)
- Approach: Proactive escalation of critical issues only. Concise, outcome-focused.
- Risk if neglected: They suddenly pay attention at the worst moment and derail progress.

**Keep Informed (Low Power, High Interest)**
- Frequency: Weekly status updates, demo invitations
- Channel: Team channels (Slack, email newsletter), sprint demos
- Approach: Regular, lightweight updates. Invite to demos. Gather feedback.
- Risk if neglected: They feel excluded and become vocal detractors internally.

**Monitor (Low Power, Low Interest)**
- Frequency: Major milestones only
- Channel: Broad announcements, all-hands, release notes
- Approach: Minimal investment. Available if they come to you.
- Risk if neglected: Minimal, but keep them on the broadcast list.

### Identifying Stakeholders You Missed

Always check these groups -- they are commonly forgotten:
- **Customer Support**: They will handle the fallout. Brief them early.
- **Documentation team**: They need lead time to update help docs.
- **Sales enablement**: They need to know what to sell and what not to promise.
- **Legal/Compliance**: Especially for features involving data, payments, or international users.
- **Adjacent teams**: Teams whose features interact with yours.
- **On-call engineers**: They will debug issues at 2 AM. Make sure they know about the change.

### Stakeholder Stance Assessment

Beyond Power and Interest, assess each stakeholder's stance:
- **Supportive**: Actively championing the project
- **Neutral**: No strong opinion, will go along
- **Resistant**: Has concerns or objections

For resistant stakeholders, document:
- What their concern is (specifically)
- Whether the concern is valid (be honest)
- What would change their stance
- Who has influence over them

### Stakeholder Map Output Format

```
## Stakeholder Map: [Initiative]

### Grid
| Stakeholder | Role | Power | Interest | Quadrant | Stance |
|------------|------|-------|----------|----------|--------|

### Communication Plan
| Stakeholder | Channel | Frequency | Key Message | Owner | Next Touchpoint |
|------------|---------|-----------|-------------|-------|----------------|

### Potential Conflicts
| Stakeholders | Conflict | Mitigation Strategy |
|-------------|---------|-------------------|

### RACI Matrix
| Decision Area | Responsible | Accountable | Consulted | Informed |
|--------------|-------------|-------------|-----------|----------|

### Escalation Path
[Who to go to when decisions are blocked, in order]
```

---

## Part 2: Meeting Transcript Synthesis

### Extraction Priority

When processing a meeting transcript, extract in this order of importance:

1. **Decisions made** -- The most valuable output. What was agreed? By whom? With what conditions?
2. **Action items** -- Who does what by when? An action item without an owner is not an action item.
3. **Open questions** -- What was discussed but NOT decided? Who needs to resolve it?
4. **Key context** -- Background information that attendees shared that is relevant to the project.
5. **Disagreements** -- Where did participants disagree? What was the resolution (or lack thereof)?

### Distinguishing "Discussed" from "Decided"

This is the most common error in meeting notes. Many topics are explored without reaching a conclusion. Be precise:
- "The team discussed moving to weekly releases" (no decision)
- "The team decided to move to weekly releases starting Sprint 12" (decision)
- "The team discussed moving to weekly releases; Sarah will evaluate CI/CD readiness by Friday" (discussion + action item, but no decision yet)

### Meeting Summary Output Format

```
## Meeting Summary

**Date**: [date]
**Participants**: [names and roles]
**Meeting type**: [standup / planning / review / 1:1 / stakeholder / all-hands]
**Topic**: [primary subject]

### TL;DR (30-second version)
[3-5 sentences covering the most important outcomes]

### Decisions Made
1. **[Decision]** -- [context and rationale]

### Action Items
| # | Action | Owner | Deadline | Status |
|---|--------|-------|----------|--------|

### Discussion Highlights
**[Topic 1]**: [key points, perspectives, conclusion]
**[Topic 2]**: [key points, perspectives, conclusion]

### Open Questions
- [Question] -- needs input from [person/team] by [date]

### Next Steps
- [What happens next]
- Next meeting: [date/cadence]
```

---

## Part 3: Executive Updates (NEW)

### Weekly Executive Update Template

This is the update that goes to your VP/CPO/CEO. It should take them 60 seconds to read.

```
## Weekly Product Update -- [Date]

### Metrics Snapshot
| Metric | This Week | Last Week | Trend | Target |
|--------|----------|-----------|-------|--------|

### Progress Against OKRs
| Objective | Status | Key Update |
|-----------|--------|-----------|
| [Obj 1] | [On Track / At Risk / Blocked] | [One sentence] |

### Shipped This Week
- [Feature/fix -- one sentence impact]

### Blockers & Asks
| Blocker | Impact | Ask | Decision Needed By |
|---------|--------|-----|-------------------|

### Decisions Needed
| Decision | Options | Recommendation | Deadline |
|----------|---------|---------------|----------|

### Next Week Focus
- [Priority 1]
- [Priority 2]
```

### Monthly Executive Update Template

More strategic, less tactical. Suitable for board-level or quarterly business reviews.

```
## Monthly Product Report -- [Month Year]

### Executive Summary
[3-5 sentences: what happened, what it means, what is next]

### OKR Scorecard
| Objective | KR1 | KR2 | KR3 | Overall | Notes |
|-----------|-----|-----|-----|---------|-------|

### Key Wins
1. [Win + quantified impact]
2. [Win + quantified impact]

### Key Risks
1. [Risk + mitigation status]
2. [Risk + mitigation status]

### Customer/Market Signal
[Notable customer feedback, churn patterns, competitive moves]

### Resource & Budget
| Area | Planned | Actual | Variance | Notes |
|------|---------|--------|----------|-------|

### Strategic Asks
[What you need from leadership -- budget, headcount, priority calls]

### 90-Day Outlook
[What is coming and why it matters]
```

---

## Part 4: Product Sunset / Deprecation Communication (NEW)

### When to Use This

When you are shutting down a product, feature, API version, or integration. This is one of the hardest communications a PM does because you are telling customers something they do not want to hear.

### The Sunset Communication Framework

**Step 1: Internal Alignment (Before External)**
- Align with leadership on the decision and rationale
- Brief support, sales, and customer success teams BEFORE customers hear
- Prepare FAQ for customer-facing teams
- Identify high-risk customers (heavy users of the feature being sunset)

**Step 2: Customer Impact Analysis**

| Segment | # Affected | Usage Level | Migration Path | Risk Level |
|---------|-----------|-------------|---------------|-----------|
| [Segment 1] | [count] | [Heavy/Medium/Light] | [Where they go] | [High/Medium/Low] |

**Step 3: Timeline**

| Milestone | Date | What Happens |
|-----------|------|-------------|
| Announcement | T | Deprecation notice sent. Feature still fully functional. |
| Migration support begins | T + 2 weeks | Migration tools/docs available. Proactive outreach to heavy users. |
| New signups disabled | T + 1 month | Existing users continue. No new users can adopt. |
| Feature read-only | T + 2 months | Data accessible but no new actions. |
| Full shutdown | T + 3 months | Feature removed. Data export deadline. |

Minimum timeline: 90 days for any feature with active users. Shorter timelines require VP+ approval and a very good reason.

**Step 4: The Communication Itself**

Structure:
1. **What is changing** (clear, no hedging)
2. **Why** (honest reason -- cost, usage, strategic direction)
3. **When** (specific dates for each milestone)
4. **What you need to do** (specific migration steps)
5. **How we will help** (support, migration tools, data export)
6. **What happens to your data** (retention, export, deletion timeline)

**Good sunset communication:**
> Starting March 1, we are retiring the Legacy Reports feature. Over the past year, 92% of report usage has shifted to our new Analytics Dashboard, which offers real-time data and custom views that Legacy Reports cannot support. Here is what this means for you:
> - **Now through Feb 28**: Legacy Reports works normally. Export any reports you want to keep.
> - **March 1-31**: Legacy Reports becomes read-only. You can view and export but not create new reports.
> - **April 1**: Legacy Reports is removed. All data will have been migrated to Analytics Dashboard.
> Need help migrating? [Link to migration guide] or contact support@company.com.

**Bad sunset communication:**
> We are sunsetting Legacy Reports to focus on our next-generation analytics platform. Please transition at your earliest convenience.

The bad version has no dates, no "why" the customer should care, no migration help, and "earliest convenience" is meaninglessly vague.

---

## Part 5: How to Deliver Bad News

### The Framework

Bad news includes: project delays, scope cuts, budget overruns, pivot decisions, feature kills, missed targets.

**Structure:**
1. **State the news directly** -- Do not bury the lead. "We are going to miss the Q2 launch date by 3 weeks."
2. **Explain why** -- Root cause, not excuses. "The payment integration took longer than estimated because [specific reason]."
3. **State the impact** -- What does this mean for the business? For customers? For the team?
4. **Present the plan** -- What are you doing about it? Options if there are trade-offs.
5. **Ask for what you need** -- Decision, resources, cover, patience.

**Anti-patterns in delivering bad news:**
- **The slow reveal**: Dripping bad news over multiple updates instead of ripping the bandage off. Stakeholders lose trust faster when they feel information was withheld.
- **The blame shift**: "Engineering missed the estimate." Even if true, the PM owns the outcome. Say "We underestimated the integration complexity."
- **The sugarcoat**: "We are slightly behind schedule" when you are 4 weeks late. Precision builds trust; euphemism destroys it.
- **The no-plan delivery**: Sharing bad news without a recovery plan. Always come with options.

---

## Part 6: Writing a Compelling "Why" for Buy-In

### When You Need Buy-In

- Proposing a new initiative that requires resources
- Recommending a pivot or strategic change
- Asking for headcount or budget
- Killing a feature that a stakeholder championed

### The Structure

1. **Start with the problem, not the solution** -- "Enterprise customers are churning at 2x the rate of SMB, and exit interviews point to onboarding friction" not "We should build SSO."
2. **Quantify the stakes** -- "This churn costs us $400K/quarter in lost ARR" not "This is a big problem."
3. **Show you have considered alternatives** -- "We evaluated three options: SSO, guided onboarding, and dedicated CSM. Here is why we recommend SSO."
4. **Connect to things they already care about** -- Reference their OKRs, the board deck, or the company strategy. "This directly addresses the board's concern about enterprise logo retention."
5. **Make the ask specific** -- "We need 2 engineers for 6 weeks and design support for 2 weeks" not "We need some resources."
6. **Name the trade-off** -- "If we do this, we delay the analytics redesign by one sprint. Here is why that trade-off is worth it."

## References

- [The Product Frameworks Compendium](https://www.productcompass.pm/p/the-product-frameworks-compendium)
- [Team Topologies](https://www.productcompass.pm/p/team-topologies-a-handbook-to-set)
