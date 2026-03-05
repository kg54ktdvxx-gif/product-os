---
name: backlog-items
description: "Three backlog item formats -- User Stories (3 C's + INVEST), Job Stories (JTBD), and WWA (Why-What-Acceptance) -- with concrete weak/strong examples, acceptance criteria guidance, story splitting techniques, and anti-pattern detection."
---

# Backlog Items: User Stories, Job Stories, and WWA

## When to Use Which Format

| Format | Best When | Team Type | Focus |
|--------|----------|-----------|-------|
| **User Stories** | Role matters. Different users have different needs for the same feature. | Most teams (default choice) | WHO wants WHAT and WHY |
| **Job Stories** | Context/situation matters more than role. JTBD-oriented teams. | Discovery-heavy teams | WHEN someone needs WHAT to achieve WHAT |
| **WWA** | Strategic alignment matters. Leadership wants to see business context in every backlog item. | Cross-functional teams | WHY this matters, WHAT we build, HOW we verify |

**Default recommendation**: Start with User Stories. Switch to Job Stories if the team finds that "As a [role]" is always the same person and the SITUATION is what varies. Switch to WWA if stakeholders keep asking "but WHY are we building this?"

---

## Part 1: User Stories

### The 3 C's Framework

1. **Card**: A brief title and one-line description. Fits on a sticky note. This is a REMINDER of a conversation, not a specification.
2. **Conversation**: The discussion between PM, designer, and engineers that fleshes out intent, constraints, and edge cases. This happens LIVE, not in writing.
3. **Confirmation**: The acceptance criteria that define "done." Written, testable, unambiguous.

### The INVEST Criteria

Every user story must be:

- **I**ndependent: Can be developed, tested, and deployed without requiring another story to be done first. If Story B depends on Story A, they are not independent.
- **N**egotiable: The implementation approach is open to discussion. The story describes the WHAT and WHY, not the HOW.
- **V**aluable: Delivers value to a user or the business ON ITS OWN. If a story is only valuable as part of a larger group, it is too small or poorly defined.
- **E**stimable: The team can estimate the effort. If they cannot, the story needs refinement (break it down or do a spike first).
- **S**mall: Can be completed within one sprint. If it cannot, split it.
- **T**estable: There is a clear way to verify that the story is done. If you cannot write a test for it, the acceptance criteria are too vague.

### User Story Template

```
**Title**: [Short, descriptive name]

**Description**: As a [specific persona from personas.md],
I want to [capability/action],
so that [benefit/outcome].

**Design**: [Link to Figma/mockups]

**Acceptance Criteria**:
1. [Testable criterion]
2. [Testable criterion]
3. [Testable criterion]
4. [Edge case handling]

**Priority**: P0/P1/P2
**Estimate**: [S/M/L or story points]
**Dependencies**: [none or list]
```

### Weak vs Strong User Stories

**WEAK**: "As a user, I want to search so that I can find things."

Problems with this story:
- "As a user" -- which user? The admin? The customer? The free-tier user? Each has different search needs.
- "search" -- search what? Products? Documentation? Other users? Order history?
- "find things" -- what things? How fast? How many results?

This story is so vague that five engineers would build five different features.

**STRONG**: "As a returning customer with 50+ past orders (personas.md: 'Power Buyer Patricia'), I want to search my order history by product name so that I can quickly reorder items I have bought before."

Why this is better:
- Specific persona with context (50+ orders = need for search)
- Specific scope (order history, not products or docs)
- Specific search parameter (product name)
- Clear outcome (reorder)
- An engineer can estimate this. A designer can wireframe it. QA can test it.

**WEAK**: "As a user, I want notifications so I can stay updated."

**STRONG**: "As a project manager ('PM Priya' from personas.md) managing 5+ active projects, I want to receive a daily digest email at 9 AM summarizing tasks that are overdue or due today across all my projects, so that I can prioritize my morning without opening the app."

### Weak vs Strong Acceptance Criteria

**WEAK**: "Search works correctly."

A QA engineer reading this has no idea what to test. What does "correctly" mean? Fast? Relevant? Handles typos?

**STRONG**:
1. Search returns results within 200ms for queries up to 100 characters
2. Results are sorted by most recent order date (newest first)
3. Search matches against product name and SKU (not description)
4. Partial matches are supported (searching "head" matches "headphones")
5. When no results are found, the page displays "No orders found for '[query]'" with a link to browse all orders
6. Special characters in the query do not cause errors (they are stripped)
7. Search works with 0, 1, and 1000+ results without pagination breaking

**WEAK**: "Notifications are sent on time."

**STRONG**:
1. Digest email is sent between 8:55 AM and 9:05 AM in the user's local timezone
2. Email contains all tasks due today and all tasks overdue (across all active projects)
3. Tasks are grouped by project, sorted by due date (overdue first)
4. Each task shows: title, project name, due date, assignee
5. If the user has no overdue or due-today tasks, no email is sent (not an empty email)
6. Email renders correctly in Gmail, Outlook, and Apple Mail (tested)
7. Unsubscribe link is present and functional

---

## Part 2: Job Stories

### The Format

```
When [situation/context],
I want to [motivation/action],
so I can [expected outcome].
```

Job stories focus on the SITUATION that triggers the need, not the user's role. This is useful when the same person has different needs in different contexts.

### Job Story Template

```
**Title**: [Outcome or result]

**Description**: When [specific situation],
I want to [motivation],
so I can [outcome].

**Design**: [Link to mockups]

**Acceptance Criteria**:
1. [Situation is properly recognized]
2. [System enables the desired action]
3. [Outcome is achieved]
4. [Edge cases handled]
```

### Weak vs Strong Job Stories

**WEAK**: "When I use the app, I want to see my data, so I can make decisions."

Problems: "use the app" is not a situation. "see my data" is vague. "make decisions" is generic.

**STRONG**: "When I am preparing for my Monday morning team standup and need to report on last week's progress, I want to see a summary of completed tasks grouped by team member with time spent, so I can give an accurate update without manually counting tickets."

Why this is better:
- Specific situation (Monday morning, preparing for standup)
- Specific trigger (need to report progress)
- Specific data need (completed tasks, by team member, with time)
- Specific outcome (accurate update without manual work)

**WEAK**: "When I want to pay, I want to pay easily, so I can be done."

**STRONG**: "When I have found the item I want to buy and I am in a rush (lunch break, commuting), I want to complete checkout with a single tap using my saved payment method, so I can finish the purchase in under 10 seconds without re-entering card details."

---

## Part 3: WWA (Why-What-Acceptance)

### The Format

```
**Why**: [Strategic context -- connects to business/team objectives]
**What**: [Short description of the deliverable, with design link]
**Acceptance Criteria**: [Observable, testable outcomes]
```

WWA is best when the team needs to understand the strategic reason for every item in the backlog. It prevents the "we are just building what the PM told us" dynamic.

### WWA Template

```
**Title**: [What will be delivered]

**Why**: [1-2 sentences connecting to strategy.md or team OKRs.
This is not "because the user wants it" -- it is "because this
supports our Q2 objective of reducing churn by 15%."]

**What**: [Short description + design link. 1-2 paragraphs MAX.
This is a reminder of discussion, not a detailed spec.]

**Acceptance Criteria**:
- [Observable outcome 1]
- [Observable outcome 2]
- [Observable outcome 3]
- [Observable outcome 4]
```

### Weak vs Strong WWA

**WEAK**:
- Why: "Users want this feature."
- What: "Build a dashboard."
- Acceptance: "Dashboard works."

**STRONG**:
- Why: "Our Q2 OKR is to reduce time-to-insight by 30% (metrics.md baseline: 12 minutes). Customer interviews reveal that operators spend 40% of their dashboard time switching between tabs to correlate metrics. A unified view directly supports KR2."
- What: "Single-pane dashboard that displays system health, active alerts, and recent deployments on one screen. Designs in [Figma link]. Discussed in sprint planning on Jan 15 -- team agreed on a WebSocket approach for real-time updates."
- Acceptance:
  - Dashboard loads in under 2 seconds with 6 months of data
  - System health, alerts, and deployments are visible without scrolling on a 1080p display
  - Alerts update in real-time (within 5 seconds of trigger)
  - User can filter by service, severity, and time range
  - Dashboard state persists across sessions (filters, layout)

---

## Part 4: Story Splitting Techniques

When a story is too large (cannot be completed in one sprint), split it using one of these techniques:

### The Hamburger Method

Think of a story as a hamburger: the bun is the UI (top) and database (bottom), the patty is the business logic. Split by making the simplest possible hamburger first, then adding toppings:

1. **Bare minimum**: Simplest happy path, no edge cases, minimal UI
2. **Add validations**: Error handling, input validation
3. **Add edge cases**: Empty states, boundary conditions
4. **Add polish**: Animations, advanced UI, performance optimization

### Split by User Type
- Story for admin users
- Story for regular users
- Story for guest/anonymous users

### Split by Operation (CRUD)
- Story for Create
- Story for Read/View
- Story for Update/Edit
- Story for Delete

### Split by Data Variation
- Story for single item
- Story for bulk/multiple items
- Story for empty state

### Split by Platform
- Story for web
- Story for mobile
- Story for API

### Anti-Pattern: Developer Stories

**BAD**: "As a developer, I want to refactor the database schema so that the code is cleaner."

This is a TASK, not a story. It delivers no user value on its own. Refactoring is valid work, but frame it as:

**BETTER**: "As a [persona], I want my dashboard to load in under 2 seconds (currently 8 seconds) so I can monitor systems without waiting."

Technical work (including refactoring) should be justified by the user outcome it enables. If a refactor does not enable any user outcome, question whether it is worth doing right now.

**Exception**: Platform/infrastructure work that enables future velocity. Frame as: "This technical investment enables us to ship [next 3 features] 40% faster. Without it, each feature takes an additional sprint due to [specific technical debt]."

---

## Part 5: Estimation Guidelines

### T-Shirt Sizing

| Size | Effort | Description |
|------|--------|-------------|
| **S** | < 1 day | Well-understood, no unknowns, minimal testing |
| **M** | 1-3 days | Clear scope, some edge cases, standard testing |
| **L** | 3-5 days | Multiple components, integration points, thorough testing |
| **XL** | 1-2 weeks | Complex, cross-cutting, needs spike or should be split |

If an estimate is **XL**, it should almost always be split into smaller stories.

### When Estimation Is Impossible

If the team cannot estimate a story, it means one of:
1. The scope is unclear --> refine the story (add detail, narrow scope)
2. The technology is unknown --> create a SPIKE story (time-boxed investigation, output = estimate for the real story)
3. The story is too large --> split it using the techniques above

Never force an estimate. A confident wrong estimate is worse than admitting uncertainty.

## References

- [How to Write User Stories: The Ultimate Guide](https://www.productcompass.pm/p/how-to-write-user-stories)
- [Jobs-to-be-Done Masterclass](https://www.productcompass.pm/p/jobs-to-be-done-masterclass-with)
