---
name: discovery-cycle
description: "Full discovery cycle knowledge: ideation with quality evaluation, assumption mapping, and experiment design for both existing and new products. Covers multi-perspective ideation, XYZ hypotheses, pretotyping, A/B tests, fake doors, and concierge MVPs."
---

# Discovery Cycle: Ideation, Assumption Mapping, and Experiment Design

The discovery cycle moves from divergent thinking (ideation) through critical analysis (assumption mapping) to focused validation (experiment design). This is not a waterfall — it is a loop. Failed experiments feed back into ideation. Validated assumptions unlock new opportunities. The cycle never ends for a living product.

## Part 1: Ideation

### Multi-Perspective Ideation

Generate ideas from three perspectives to avoid the tunnel vision of a single role:

**Product Manager Lens**: Business value, strategic alignment, market positioning, revenue potential, competitive differentiation. Asks: "Does this move the needle on our outcome? Is there a business model behind it?"

**Designer Lens**: User experience, usability, delight, accessibility, emotional impact, behavior change. Asks: "Does this reduce friction? Does it create a moment of delight? Will users actually adopt this behavior?"

**Engineer Lens**: Technical possibilities, data leverage, platform capabilities, scalable architecture, automation potential. Asks: "What can we build that wasn't possible before? What data do we have that we're not using? What can we automate that users do manually?"

### Ideation for Existing Products (Continuous Discovery)

Ground ideas in observed user behavior, not speculation. Sources:
- Usage analytics: Where do users drop off? What features are underused? What do power users do differently?
- Support tickets: What problems repeat weekly? What workarounds have users invented?
- Interview insights: What Jobs to Be Done are underserved?
- Competitor moves: What are competitors doing that our users are asking about?

**Process**:
1. Define the opportunity space (from the Opportunity Solution Tree)
2. Generate 5 ideas per perspective (15 total)
3. Evaluate each idea on the Idea Quality Scorecard (below)
4. Rank the top 5 with explicit rationale
5. Identify the riskiest assumption behind each top idea

### Ideation for New Products (Initial Discovery)

Focus on core value delivery and speed to validate. Don't ideate features — ideate value propositions.

**Process**:
1. Articulate the core problem and target user
2. Generate 5 ideas per perspective (15 total)
3. Weight heavily toward: core value delivery, speed to validate, differentiation potential
4. Rank the top 5
5. For each, identify the leap-of-faith assumption

### The Idea Quality Scorecard

Rate every idea on these five dimensions (1-5 scale):

| Dimension | 1 (Poor) | 3 (Adequate) | 5 (Excellent) |
|-----------|----------|---------------|----------------|
| **Desirability** | No evidence users want this | Some signals (requests, complaints) | Strong pull (users built workarounds, pay for alternatives) |
| **Viability** | No business model, cannibalizes existing revenue | Unclear monetization but doesn't hurt | Clear revenue path or strategic value |
| **Feasibility** | Requires technology that doesn't exist | Possible but significant R&D | Can build with existing stack in weeks |
| **Differentiation** | Competitors already do this well | Competitors do this, but poorly | No competitor offers this; defensible |
| **Evidence Base** | Pure speculation | Anecdotal (a few users mentioned it) | Quantitative (data, surveys, multiple interviews) |

**Composite Score** = (D + V + F + Diff + E) / 5

Ideas scoring below 2.5 should be challenged. Ideas scoring above 4.0 are rare — verify the scores aren't inflated by optimism bias.

### What Makes a Good Idea vs. a Bad Idea

**Strong Idea Example**:
"Automated weekly progress digest email. Based on 8/15 interviewed project managers saying they spend 2+ hours every Monday compiling status updates manually. Uses data we already collect. Low effort (2-week build), high retention signal (solves a recurring pain)."
- Grounded in evidence (8/15 interviews)
- Solves a recurring, time-consuming pain
- Uses existing data (feasible)
- Clear behavior signal (2+ hours/week = strong pain)

**Weak Idea Example**:
"Add AI to the dashboard. AI is trending and our competitors are doing it. Users would probably find it useful."
- No specific user problem identified
- "AI" is a technology, not a solution
- "Probably find it useful" = no evidence
- Competitor-driven, not user-driven

### Idea Generation Anti-Patterns

- **Solution-first thinking**: "Let's add a chatbot" before understanding what problem it solves
- **Technology-driven ideation**: "We should use ML because we have data" — ML is a tool, not a value proposition
- **Copycat features**: "Competitor X launched this, so we should too" — without evidence your users need it
- **Pet features**: Ideas championed by a senior stakeholder with no user evidence (handle diplomatically but flag the risk)
- **Kitchen sink**: Generating 50 ideas without evaluating any — quantity without quality evaluation is brainstorming theater

---

## Part 2: Assumption Mapping

Every idea is a bundle of assumptions. Before building anything, unbundle the assumptions and identify which ones are most dangerous (high impact if wrong, low evidence they're right).

### From Ideas to Assumptions

For each top idea, extract assumptions across risk categories:

**Value**: "Users will want this enough to [use it / pay for it / switch to it]"
**Usability**: "Users will figure out how to [complete the core task] without [training / support / documentation]"
**Viability**: "The business can [monetize / support / scale] this without [excessive cost / legal risk / brand damage]"
**Feasibility**: "The team can build this with [existing technology / current skills / available time]"

For new products, add:
**Go-to-Market**: "We can reach [target users] through [channel] at [cost]"
**Strategy**: "The market will [remain favorable / not be disrupted] during [timeframe]"
**Ethics**: "This product will not [harm users / create perverse incentives / violate privacy norms]"
**Team**: "The team has [the skills / the motivation / the stability] to execute"

### Assumption Quality Test

A well-formed assumption is:
1. **Specific**: Names the user segment, the behavior, and the threshold
2. **Falsifiable**: You can imagine evidence that would prove it wrong
3. **Consequential**: If wrong, it changes what you build or whether you build at all

**Strong assumption**: "At least 30% of free-tier users who hit the 5-project limit will upgrade to the paid plan within 7 days."
**Weak assumption**: "Users will see value in the premium tier."

### The Assumption Spectrum

Assumptions exist on a spectrum from untested to validated:

```
UNTESTED -> ANECDOTAL -> QUALITATIVE -> QUANTITATIVE -> VALIDATED
   (no       (a few       (interview     (A/B test,      (shipped,
  evidence)   mentions)    themes,        survey with     measured
                           patterns)      n>100)          at scale)
```

Track where each assumption sits. The goal is to move high-risk assumptions rightward on this spectrum as cheaply as possible.

---

## Part 3: Experiment Design

### Experiment Design for Existing Products

You have real users, real traffic, and real data. Use that advantage.

**Experiment Types (ordered by effort, low to high)**:

1. **Data Analysis** (hours): Query existing analytics to test the assumption. "Do users who [behavior X] retain better?" This is free and immediate — always check data first.

2. **Fake Door Test** (days): Add a button/link for the feature that doesn't exist yet. Measure click-through rate. "If >5% of users click 'Export to PDF', there's demand."

3. **Survey with Behavioral Anchoring** (days): Survey users who exhibited a specific behavior. "You used feature X 12 times last week — what were you trying to accomplish?" Never ask "Would you use feature Y?" — ask about behavior, not intent.

4. **Prototype Usability Test** (1-2 weeks): Build a clickable prototype (Figma, etc.) and watch 5 users try to complete a task. Measure task completion rate and time. 5 users find ~85% of usability issues (Nielsen).

5. **A/B Test** (2-4 weeks): Ship a minimal version to a percentage of users. Measure the target metric. Requires statistical significance planning: sample size, runtime, minimum detectable effect.

6. **Wizard of Oz** (1-4 weeks): The feature appears automated to users but is manually operated behind the scenes. Tests value without building the technology. Good for AI/ML features.

7. **Concierge** (2-4 weeks): Manually deliver the service to a small group of users. Measures value delivered and willingness to continue. Good for service-oriented features.

### Experiment Design for New Products (Pretotyping)

You have no users, no traffic, no data. You need to generate your own signal cheaply.

**The Pretotyping Methodology** (Alberto Savoia, "The Right It"):

Core principle: "Make sure you are building The Right It before you build It right." Most new products fail not because they were built badly, but because they were the wrong thing to build.

**XYZ Hypothesis Format**:
"At least **X%** of **Y** (target market) will **Z** (measurable action) within **S** (specific timeframe)."

Example: "At least 10% of freelance designers who visit the landing page will sign up for the waitlist within 30 days of the campaign launch."

**Key principle: Skin in the Game (SITG)**. Opinions are cheap. Only count signals where the user commits something real — time, money, reputation, or effort. A waitlist signup is weak SITG. A pre-order with a credit card is strong SITG.

**Your Own Data (YODA) vs. Others' Data (ODP)**: Market reports, competitor revenue, and industry benchmarks are ODP — they tell you about someone else's product in someone else's context. Only your own experiments (YODA) tell you about YOUR product for YOUR users. "The market for your idea does not care about the market for someone else's idea."

**Pretotype Experiment Types**:

1. **Landing Page Test** (days): Build a landing page describing the value proposition. Drive traffic via ads ($200-500). Measure: signup rate, time on page, scroll depth. Success: >8% signup rate.

2. **Explainer Video** (days): Create a 60-90 second video showing the concept. Measure: completion rate, CTA click-through. Success: >50% completion, >5% CTA click.

3. **Email/Ad Campaign** (days): Test messaging and positioning through targeted ads. Measure: CTR, CPC, signup cost. Compare multiple value propositions head-to-head.

4. **Pre-Order / Waitlist** (1-2 weeks): Test willingness to pay. Waitlist = weak signal. Pre-order with payment info = strong signal. "Would you buy this?" means nothing. "Here's the buy button" means everything.

5. **Concierge MVP** (2-4 weeks): Manually deliver the service to 5-10 users. Measure: repeat usage, willingness to pay, NPS. This is the strongest signal — you're delivering real value and measuring real reactions.

6. **The Mechanical Turk** (1-2 weeks): Present an automated-looking interface but fulfill requests manually. Tests whether users want the outcome without building the automation.

7. **The Pinocchio** (1-2 weeks): Build a non-functional version (the "wooden puppet") and see if users try to use it. Measures demand before building functionality.

### What Makes a Good Experiment vs. a Bad Experiment

**Strong Experiment**:
```
Assumption: Enterprise users will pay $50/mo for automated compliance reports.
Experiment: Fake door test — add "Compliance Reports (Beta)" button to enterprise dashboard.
Metric: Click-through rate over 2 weeks.
Sample: ~2000 enterprise users (current base).
Success criteria: >8% CTR -> proceed to prototype.
                  3-8% CTR -> run 5 follow-up interviews with clickers.
                  <3% CTR -> kill the idea.
Decision owner: Product lead.
Timeline: 2 weeks setup + 2 weeks measurement.
```

**Weak Experiment**:
```
Assumption: Users want compliance reports.
Experiment: Ask users in a survey if they'd use compliance reports.
Metric: % who say yes.
Problem: Opinion-based. "Would you use X?" always gets inflated yes responses.
         No skin in the game. No behavioral measurement. No decision criteria.
```

### Experiment Sequencing

Run experiments in order of cheapest-to-most-expensive:
1. **Can we find evidence in existing data?** (free)
2. **Can we test demand with a fake door or landing page?** (days, <$500)
3. **Can we test usability with a prototype?** (1-2 weeks)
4. **Can we test value with a concierge/Wizard of Oz?** (2-4 weeks)
5. **Can we test at scale with an A/B test?** (2-4 weeks, requires traffic)

Never run an expensive experiment when a cheap one would answer the same question. Never run an experiment without decision criteria agreed upon in advance.

### The Experiment Tracker

Maintain a living tracker:

```
| # | Assumption | Experiment | Status | Start | End | Result | Decision |
|---|-----------|-----------|--------|-------|-----|--------|----------|
| 1 | Value: 30% upgrade | Fake door on limit screen | Complete | Jan 5 | Jan 19 | 4.2% CTR | Interview clickers |
| 2 | Usability: <2min onboard | Prototype test, n=5 | Running | Jan 20 | Feb 3 | - | - |
| 3 | GTM: $15 CAC via Google | Ad campaign, $500 budget | Planned | Feb 10 | Feb 24 | - | - |
```

### Common Experiment Pitfalls

- **No baseline**: You can't measure improvement without knowing where you started
- **Too many variables**: Test one assumption per experiment. If you change three things, you learn nothing.
- **Premature optimization**: Don't A/B test button colors before you've validated that anyone wants the feature
- **Ignoring negative results**: A failed experiment is a successful learning. The failure is running the experiment and then building the feature anyway.
- **Confirmation bias in interpretation**: Pre-commit to decision criteria BEFORE seeing results. If you set the threshold after, you'll rationalize any outcome.
- **Insufficient sample size**: 10 clicks on a fake door is noise, not signal. Plan for statistical power.
- **Testing opinions, not behavior**: "Would you use this?" is not an experiment. "Did you click this?" is.

---

## Tying It All Together: The Discovery Loop

```
IDEATE (diverge) -> EVALUATE (scorecard) -> MAP ASSUMPTIONS (risk)
                                                    |
                                                    v
                                          PRIORITIZE (impact x uncertainty)
                                                    |
                                                    v
                                          EXPERIMENT (validate cheaply)
                                                    |
                                            +-------+-------+
                                            |               |
                                         VALIDATED       INVALIDATED
                                            |               |
                                            v               v
                                      BUILD / SHIP     PIVOT / KILL
                                                       -> back to IDEATE
```

Discovery is not a phase. It is a continuous practice that runs in parallel with delivery. The team should be discovering next quarter's work while delivering this quarter's.

### Cadence for Continuous Discovery

- **Weekly**: Review experiment results, update assumption tracker, conduct 1-2 user interviews
- **Biweekly**: Update the Opportunity Solution Tree with new evidence
- **Monthly**: Review personas for accuracy, update prioritization scores
- **Quarterly**: Reassess the opportunity space, retire validated assumptions, identify new risks
