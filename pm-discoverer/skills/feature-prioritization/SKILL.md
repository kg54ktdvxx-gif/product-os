---
name: feature-prioritization
description: "Feature prioritization with 9 frameworks (Opportunity Score, ICE, RICE, MoSCoW, Kano, WSJF, Buy-a-Feature, Story Mapping, Cost of Delay), feature request analysis, scoring formulas, bias detection, and stakeholder management."
---

# Feature Prioritization: Frameworks, Formulas, and Discipline

Prioritization is the hardest part of product management because it requires saying no. A ranked list without visible methodology is just one person's opinion. The Discoverer ensures that every prioritization decision shows its work — the framework used, the scores assigned, the formula applied, and the reasoning behind subjective inputs.

## The Nine Frameworks

### 1. Opportunity Score (Dan Olsen)

**When to use**: Evaluating customer PROBLEMS (opportunities), not solutions. Best for deciding which problem space to invest in.

**Formula**:
```
Opportunity Score = Importance x (1 - Satisfaction)
```

- **Importance**: How important is this need to users? (0 to 1)
- **Satisfaction**: How well is this need currently met by existing solutions? (0 to 1)

**Data sources**: Customer interviews, surveys (Likert scale normalized to 0-1), support ticket frequency.

**Interpretation**:
| Importance | Satisfaction | Opportunity Score | Action |
|-----------|-------------|------------------|--------|
| High (0.8+) | Low (0.2-) | High (0.64+) | Best opportunity — invest here |
| High (0.8+) | High (0.8+) | Low (0.16) | Table stakes — maintain, don't differentiate |
| Low (0.2-) | Low (0.2-) | Low (0.16) | Don't bother — users don't care |
| Low (0.2-) | High (0.8+) | Near 0 (0.04) | Over-served — reduce investment |

**Strong example**:
"Opportunity: 'Finding relevant content quickly.' Importance: 0.9 (mentioned unprompted by 11/15 interviewees, ranked #1 in survey). Satisfaction: 0.25 (current search returns irrelevant results 60% of the time per analytics). Opportunity Score: 0.9 x 0.75 = 0.675."

**Weak example**:
"Opportunity: 'Better search.' Importance: High. Satisfaction: Low. Score: High."
(No numbers. No evidence. No methodology. This is just labeling.)

### 2. ICE (Impact, Confidence, Ease)

**When to use**: Quick scoring of individual initiatives when you need a fast, rough ranking. Good for weekly triage, not for major strategic decisions.

**Formula**:
```
ICE Score = Impact x Confidence x Ease
```

All three dimensions scored 1-10.

- **Impact**: How much will this move the target metric? (1 = negligible, 10 = transformative)
- **Confidence**: How confident are you in the impact estimate? (1 = pure guess, 10 = validated by data)
- **Ease**: How easy is it to implement? (1 = multi-quarter effort, 10 = ship this week)

**Why confidence matters**: Impact x Ease alone rewards big, easy ideas — but if the impact estimate is a guess, the score is meaningless. Confidence penalizes wishful thinking.

**Example**:
| Feature | Impact | Confidence | Ease | ICE Score |
|---------|--------|-----------|------|-----------|
| Automated digest email | 7 | 8 | 9 | 504 |
| AI recommendations | 9 | 3 | 4 | 108 |
| Dark mode | 4 | 7 | 8 | 224 |

The AI recommendations have the highest raw impact, but low confidence and low ease make them a poor bet compared to the digest email.

### 3. RICE (Reach, Impact, Confidence, Effort)

**When to use**: When you have quantitative reach data (user counts, traffic numbers) and need a more rigorous version of ICE. Standard at larger companies (Intercom originated this).

**Formula**:
```
RICE Score = (Reach x Impact x Confidence) / Effort
```

- **Reach**: How many users will this affect in a quarter? (absolute number)
- **Impact**: How much will each affected user benefit? (0.25 = minimal, 0.5 = low, 1 = medium, 2 = high, 3 = massive)
- **Confidence**: How confident in the estimates? (100% = high, 80% = medium, 50% = low)
- **Effort**: Person-months of work required (engineering + design + QA)

**Example**:
| Feature | Reach (/qtr) | Impact | Confidence | Effort (pm) | RICE |
|---------|-------------|--------|-----------|-------------|------|
| Onboarding redesign | 5000 | 2 | 80% | 3 | 2667 |
| Bulk export | 800 | 1 | 90% | 1 | 720 |
| Dashboard v2 | 3000 | 1 | 50% | 6 | 250 |

**Strong example**:
"Onboarding redesign: Reach = 5000 new signups/quarter (from analytics). Impact = 2 (high — we expect to double activation rate based on prototype test results). Confidence = 80% (prototype tested with 5 users, 4/5 completed activation; survey of 200 users confirms pain point). Effort = 3 person-months (designer + 2 engineers, scoped by tech lead). RICE = (5000 x 2 x 0.8) / 3 = 2667."

### 4. MoSCoW (Must Have, Should Have, Could Have, Won't Have)

**When to use**: Scope negotiation for a specific release or MVP. Not for long-term prioritization — it's a classification, not a ranking.

- **Must Have**: Without this, the release is pointless. Literally cannot ship without it.
- **Should Have**: Important but not fatal if missing. Could ship without, but it would hurt.
- **Could Have**: Nice to have. Include only if time permits.
- **Won't Have (this time)**: Explicitly out of scope. Saying this out loud prevents scope creep.

**The trap**: Everything becomes "Must Have." Counter this by asking: "If we shipped without this feature and it failed, would THIS be the reason?" If no, it's not Must Have.

**Strong MoSCoW**:
- Must: User can create an account and complete the core workflow
- Should: User can invite team members
- Could: User can customize their dashboard layout
- Won't: AI-powered recommendations (future release)

**Weak MoSCoW**:
- Must: Everything the stakeholder asked for
- Should: (empty)
- Could: (empty)
- Won't: (empty)
(This is just a feature list with a "Must" label.)

### 5. Kano Model

**When to use**: Understanding user expectations and satisfaction dynamics. Identifies features that delight vs. features that are table stakes.

**Categories**:
- **Must-Be (Basic)**: Users don't notice when present, but are angry when absent. Example: login works, data is saved, pages load.
- **One-Dimensional (Performance)**: Satisfaction increases linearly with implementation quality. Example: faster load times, more storage, better search accuracy.
- **Attractive (Delighters)**: Users don't expect them, but are thrilled when present. Example: unexpected shortcut that saves time, a delightful animation, proactive alerts.
- **Indifferent**: Users don't care either way. Example: changing the settings icon from a gear to a wrench.
- **Reverse**: Some users actively dislike it. Example: forced social sharing, gamification badges for professional tools.

**The Kano survey method**: For each feature, ask two questions:
1. "How would you feel if this feature were present?" (I'd like it / I expect it / Neutral / I can live with it / I'd dislike it)
2. "How would you feel if this feature were absent?" (same options)

Cross-reference the answers in the Kano evaluation table to classify.

**Strategic implication**: Must-Be features are cost of entry — you must have them but can't differentiate on them. Invest the minimum. Attractive features are your competitive advantage — invest disproportionately. One-Dimensional features are the battleground — win on quality.

### 6. WSJF (Weighted Shortest Job First)

**When to use**: When you need to optimize for flow and throughput, common in SAFe and Lean environments. Prioritizes high-value, time-sensitive, small work items.

**Formula**:
```
WSJF = Cost of Delay / Job Duration
```

Where **Cost of Delay** = User/Business Value + Time Criticality + Risk Reduction/Opportunity Enablement

All components scored on a relative Fibonacci scale (1, 2, 3, 5, 8, 13, 21).

**Example**:
| Feature | User Value | Time Criticality | Risk Reduction | CoD | Duration | WSJF |
|---------|-----------|-----------------|---------------|-----|----------|------|
| Security patch | 3 | 21 | 13 | 37 | 2 | 18.5 |
| New onboarding | 13 | 5 | 8 | 26 | 8 | 3.25 |
| Dark mode | 5 | 1 | 1 | 7 | 3 | 2.33 |

The security patch has the highest WSJF because of extreme time criticality and risk reduction, even though user value is low.

### 7. Buy-a-Feature

**When to use**: Stakeholder alignment and negotiation. Good for resolving "everything is priority 1" deadlocks. Not a rigorous framework — a facilitation technique.

**Method**:
1. List features with price tags proportional to effort (e.g., "Security patch = $100, New dashboard = $500")
2. Give each stakeholder a budget (e.g., $1000)
3. They "buy" the features they care about most
4. Features nobody buys get deprioritized with visible consensus

**Why it works**: Forces trade-offs. When everything costs something, stakeholders can't say "do all of it." They must reveal their real priorities by spending scarce currency.

### 8. Story Mapping (Jeff Patton)

**When to use**: Planning releases for a product with multiple user journeys. Good for MVP scoping and release planning.

**Method**:
1. Map the user journey left to right (backbone): Account Creation -> Setup -> Daily Use -> Admin
2. Under each step, list features top to bottom in priority order
3. Draw a horizontal line to define the MVP: everything above the line ships first

**Advantage**: Ensures the MVP is a complete (if thin) user journey, not a pile of unrelated features.

### 9. Cost of Delay

**When to use**: When timing matters — features with expiring value, competitive windows, or contractual deadlines.

**Types of Cost of Delay**:
- **Standard**: Linear — every week of delay costs the same amount (lost revenue per week)
- **Urgent**: Exponential — the longer you wait, the worse it gets (security vulnerability, compliance deadline)
- **Fixed Date**: Binary — if you miss the date, the value drops to zero (seasonal campaign, conference launch, contractual commitment)
- **Intangible**: Hard to quantify but real (competitive response, talent retention, brand reputation)

**Formula**:
```
Priority = Cost of Delay / Duration
```

This is the same principle as WSJF — do the most valuable, most time-sensitive, smallest work first.

---

## Choosing the Right Framework

| Situation | Best Framework(s) |
|-----------|-----------------|
| "Which customer PROBLEM should we solve?" | Opportunity Score |
| "Quick ranking of 10 features" | ICE |
| "Rigorous ranking with user data" | RICE |
| "Scoping an MVP release" | MoSCoW + Story Mapping |
| "Understanding user expectations" | Kano |
| "Optimizing development throughput" | WSJF |
| "Stakeholder alignment meeting" | Buy-a-Feature |
| "Time-sensitive decisions" | Cost of Delay |
| "Feature request triage" | Opportunity Score + RICE |

You can (and should) combine frameworks. Use Opportunity Score to identify the right problem, then RICE to prioritize the solutions within that problem space.

---

## Feature Request Analysis

Feature requests are raw material, not a roadmap. The Discoverer's job is to process them into insights.

### Step 1: Extract the Need Behind the Request

Every feature request is a solution proposed by a user who has a problem. Your job is to find the problem.

| Request (What they said) | Need (What they meant) |
|--------------------------|----------------------|
| "Add dark mode" | "Reduce eye strain during long sessions" |
| "We need an API" | "I need to connect this to my existing workflow to eliminate manual steps" |
| "Make it faster" | "The current load time breaks my concentration and costs me 10 minutes/day" |
| "Add bulk editing" | "I have 200 items to update and doing them one by one takes 3 hours" |
| "Can you add Slack integration?" | "I need to stay in my primary workspace, not switch contexts" |

### Step 2: Categorize by Theme

Group requests by the underlying need, not by the proposed solution:
- "Add Slack integration" + "Add email notifications" + "Add webhook support" = **Theme: Keep me informed without context-switching**
- "Bulk edit" + "CSV import" + "Template system" = **Theme: Reduce repetitive manual work**

### Step 3: Quantify Signal Strength

| Signal | Weight | Rationale |
|--------|--------|-----------|
| Number of unique requestors | High | More people = broader need |
| Revenue at risk (churning customers asking for it) | Very High | Direct business impact |
| Request frequency (same user asks repeatedly) | Medium | Indicates strong pain for individuals |
| Strategic fit with current goals | High | Alignment multiplier |
| Competitive gap (competitors have it, we don't) | Medium | Context-dependent — don't copy blindly |
| Effort to implement | Inverse | Small effort + high signal = quick win |

### Step 4: Assess Strategic Fit

For each theme, evaluate:
- Does it serve the target persona? (or a different, potentially lower-value segment?)
- Does it move the North Star metric?
- Does it align with the current quarter's objectives?
- Is it a must-have for an upcoming deal or expansion?

### Step 5: Output the Analysis

```
## Feature Request Analysis: [Date Range]

### Summary
- Requests analyzed: [N]
- Themes identified: [N]
- Sources: [Support tickets, sales calls, surveys, etc.]

### Theme Ranking
| Rank | Theme | Requests | Segments | Strategic Fit | Recommended Action |
|------|-------|----------|----------|--------------|-------------------|
| 1 | Reduce manual work | 34 | SMB, Enterprise | High | Scope MVP for Q2 |
| 2 | Stay informed | 21 | All | Medium | Experiment: fake door |
| 3 | Better reporting | 15 | Enterprise | High | Interview 5 enterprise users |
| 4 | Dark mode | 12 | All | Low | Defer — cosmetic, not strategic |

### Notable Patterns
- [Key insight about what users are really saying]
- [Segment-specific pattern]
- [Gap between what users ask for and underlying need]

### Requests to Decline (with rationale)
- [Request] — [Why it doesn't fit: wrong segment, conflicts with strategy, too costly for value]
```

---

## Common Prioritization Biases

### 1. HiPPO (Highest Paid Person's Opinion)
The CEO says "build X" and it becomes priority 1 regardless of evidence. Counter: present the framework scores publicly. "Here's how X scored against our criteria. Here's the data."

### 2. Recency Bias
The feature mentioned in today's meeting gets priority over the one discussed last month. Counter: use the framework consistently across all candidates, regardless of when they were proposed.

### 3. Sunk Cost Fallacy
"We already started building X, so we should finish it" — even if evidence now suggests X is wrong. Counter: evaluate every feature against the same criteria, regardless of investment to date.

### 4. Squeaky Wheel Bias
The loudest customer or most persistent stakeholder gets their feature. Counter: weight by number of affected users, not volume of complaints from individuals.

### 5. Everything is High Priority
When asked to prioritize, stakeholders rate everything as "critical." Counter: force-rank (ordinal, not rating). "You must order these 1-10. No ties allowed."

### 6. Confidence Inflation
Teams rate their confidence in an idea higher than warranted because they want to build it. Counter: require evidence for confidence ratings. "You scored confidence 9/10 — what data supports that?"

### 7. Effort Underestimation
Features seem easier than they are because engineering complexity is invisible to PMs. Counter: require engineering lead sign-off on effort estimates. Add 50% as a standard buffer.

---

## Prioritization Meeting Template

```
## Prioritization Session: [Date]

### Attendees: [PM, Design Lead, Eng Lead, ...]
### Framework: [RICE / ICE / etc.]
### Scope: [Features for Q2 / Requests from last month / etc.]

### Pre-Work
Each attendee independently scores each feature before the meeting.
Bring your scores. We'll calibrate in the session.

### Agenda (60 min)
1. (5 min) Align on outcome and constraints
2. (10 min) Present individual scores, flag divergences
3. (30 min) Calibrate — discuss items where scores diverge by >2 points
4. (10 min) Final ranking — agree on top 5
5. (5 min) Assign next steps for top 5

### Rules
- Show the math. No "I just feel this is important."
- Evidence trumps opinion.
- Engineering gets veto on effort scores.
- Force-rank the output. No ties.

### Output
| Rank | Feature | [Criterion 1] | [Criterion 2] | ... | Score | Owner | Next Step |
```

---

## The Trap of "Everything is High Priority"

When everything is high priority, nothing is. The Discoverer's response:

1. **Force ordinal ranking**: "You can't have five P0s. Rank them 1-5."
2. **Apply a capacity constraint**: "We have 3 engineers for 6 weeks. What ships?" This makes trade-offs visceral.
3. **Use the framework**: "Here are the RICE scores. The data says this is the order. What data-based argument would change it?"
4. **Name what you're NOT doing**: Every Yes implies a No. Make the No explicit: "If we build X, we are choosing not to build Y and Z this quarter. Is the team comfortable with that?"
5. **Time-box the debate**: "We have 30 minutes to rank these. If we can't agree, the framework score wins."
