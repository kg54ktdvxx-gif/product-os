---
name: assumption-testing
description: "Assumption identification across risk categories, impact-uncertainty prioritization, leap-of-faith detection, and continuous tracking. Covers existing products (4 risks) and new products (8+ risks), with devil's advocate techniques and the assumption lifecycle."
---

# Assumption Testing: Identification, Prioritization, and Tracking

Every product decision rests on assumptions. Most teams treat assumptions as things they'll "validate later." The Discoverer treats them as the primary unit of work. An untested assumption is a landmine — it will not announce itself before it detonates.

## Part 1: Assumption Identification

### The Four Core Risk Categories (Teresa Torres)

These apply to every product, existing or new:

**1. Value Risk** — Will users want this?
- Will it solve a real, important problem?
- Is the problem frequent enough to justify a product?
- Will users choose this over their current solution?
- Will they keep using it after the novelty wears off?
- Will they pay for it (or will they only use it if it's free)?

**2. Usability Risk** — Will users figure it out?
- Can they complete the core task without help?
- Is the learning curve acceptable for the target audience?
- Will it fit into their existing workflow or require behavior change?
- Are there accessibility barriers?
- Does it increase cognitive load beyond the value it delivers?

**3. Viability Risk** — Does the business case work?
- Can we monetize it sustainably?
- Can marketing, sales, and support handle it?
- Does it comply with regulations (GDPR, SOX, HIPAA, etc.)?
- Does it cannibalize existing revenue?
- Can we scale it without costs growing faster than revenue?

**4. Feasibility Risk** — Can we build it?
- Can it be built with existing technology and skills?
- Are there integration dependencies with third parties?
- Can it perform at the required scale and latency?
- What's the maintenance burden?
- Are there data requirements we can't meet?

### Extended Risk Categories for New Products

New products face risks that existing products have already navigated (or at least confronted). Add these four:

**5. Go-to-Market Risk** — Can we reach users?
- Do we have access to the target audience?
- What channels will work? At what cost?
- Is the messaging clear enough to convert cold traffic?
- Is this the right time to launch (market timing)?
- Can we compete for attention against established players?

**6. Strategy Risk** — Are we solving the right problem?
- Are we targeting the right market segment?
- Can competitors copy this easily? Is it defensible?
- Have we considered PESTEL factors (Political, Economic, Social, Technological, Environmental, Legal)?
- Is the market big enough to justify the investment?
- Could a platform shift (regulatory, technological) make this irrelevant?

**7. Ethics Risk** — Should we do this at all?
- Could this harm users (addiction, privacy violation, discrimination)?
- Are we creating perverse incentives?
- What happens if this is misused?
- Are there vulnerable populations disproportionately affected?
- Would we be comfortable if a journalist wrote about how this works?

**8. Team Risk** — Can this team execute?
- Do we have the right skills?
- Is the team stable enough to see this through?
- Do we have the right tools and infrastructure?
- Is there organizational alignment (or will politics kill it)?
- Is the team motivated by this problem or just assigned to it?

**9. Legal/Regulatory Risk** (sometimes separated from Viability)
- Are there pending regulations that could affect this?
- Do we need legal review before launch?
- Are there IP/patent concerns?
- What jurisdiction-specific rules apply?

### The Devil's Advocate Technique

For each idea, adopt three adversarial perspectives:

**The Skeptical User**: "I've been burned by products that promise this. Why should I believe yours is different? I won't switch unless the improvement is 10x, not 2x. I don't have time to learn a new tool."

**The Hostile Competitor**: "We can build this faster, cheaper, and distribute it to our existing 10M users. What's stopping us? We can copy the valuable parts and bundle them for free."

**The Ruthless CFO**: "Show me the unit economics. What's the CAC? What's the LTV? When does this break even? What happens to our margins at 10x scale? What are we NOT building by building this?"

### Common Hidden Assumptions PMs Miss

These are the assumptions that nobody writes down because they seem "obvious" — and they're often the ones that kill products:

1. **"Users will discover this feature"** — Most users never explore past the main screen. Discovery requires active promotion, not just existence.

2. **"Users will understand the value from the description"** — Your value prop is clear to you because you've lived with it for months. To a new user, it's often incomprehensible jargon.

3. **"This market is big enough"** — TAM slides are fiction. The serviceable obtainable market (SOM) is what matters, and it's usually 1-5% of what the TAM slide says.

4. **"Users will migrate their data"** — Data migration is the #1 switching cost. If users have years of data in a competitor, "just export and import" is a fantasy.

5. **"Our team can build this in [timeline]"** — Engineering estimates are optimistic by 2-3x on average. This is not cynicism; it's base rate data from decades of software projects.

6. **"The current behavior will continue"** — Markets shift. A competitor could launch tomorrow. A regulation could change next quarter. "Steady state" is an assumption.

7. **"Users who say they want this will actually use it"** — The gap between stated preference and revealed preference is enormous. "I would definitely use that!" translates to actual usage about 20% of the time.

8. **"One size fits all"** — Different user segments have different needs, different willingness to pay, and different definitions of "good enough." A feature that delights power users might overwhelm beginners.

9. **"The technical approach will work at production scale"** — Prototypes run on clean data with low traffic. Production runs on messy data with unpredictable load spikes.

10. **"Users will tell us when something is wrong"** — Most users don't complain; they leave. For every support ticket, there are 10-100 users who silently churned.

### Turning Vague Concerns into Testable Hypotheses

When someone says something vague, apply this formula:

**Vague concern**: "I'm worried users won't adopt this."

**Step 1 — Specify the user**: Which users? New users? Power users? Enterprise admins? Free tier?

**Step 2 — Specify the behavior**: What does "adopt" mean? First use? Daily use? Use instead of the alternative? Pay for it?

**Step 3 — Specify the threshold**: What level of adoption would make this a success? What level would make it a failure?

**Step 4 — Specify the timeframe**: By when? First week? First month? First quarter?

**Testable hypothesis**: "We believe that at least 25% of new free-tier users will complete the onboarding flow and use the core feature at least 3 times in their first 7 days."

---

## Part 2: Assumption Prioritization

### The Impact x Uncertainty Matrix

Plot every assumption on two dimensions:

**Impact** (1-5): If this assumption is wrong, how badly does it hurt?
- 1: Minor inconvenience, easy to course-correct
- 3: Significant rework, delayed timeline, missed target
- 5: Product failure, total pivot required, existential risk

**Uncertainty** (1-5): How little evidence do we have?
- 1: Quantitatively validated (A/B test, production data at scale)
- 2: Qualitatively validated (consistent theme across 10+ interviews)
- 3: Anecdotally supported (a few data points, some interviews)
- 4: Educated guess (industry experience, analogies)
- 5: Complete unknown (no data, no precedent, pure speculation)

**Priority Score** = Impact x Uncertainty

### The Four Quadrants

```
                    HIGH UNCERTAINTY
                         |
          EXPERIMENT     |     INVESTIGATE
         (High Impact    |    (Low Impact
          High Uncert.)  |     High Uncert.)
                         |
   HIGH ----------------+---------------- LOW
   IMPACT               |                IMPACT
                         |
          PROCEED        |      DEFER
         (High Impact    |    (Low Impact
          Low Uncert.)   |     Low Uncert.)
                         |
                    LOW UNCERTAINTY
```

**EXPERIMENT (top-left)**: These are your leap-of-faith assumptions. They are high impact AND high uncertainty. If you're wrong, the product fails, and you have little evidence either way. Test these first, cheaply, before committing resources.

**PROCEED (bottom-left)**: High impact but well-evidenced. You're probably right, and it matters. Move forward with confidence, but monitor for disconfirming signals.

**INVESTIGATE (top-right)**: Low impact but you don't know much. Gather information passively — don't invest in formal experiments, but stay alert. These sometimes migrate to high-impact as you learn more.

**DEFER (bottom-right)**: Low impact and well-understood. Ignore for now. Revisit only if the landscape changes.

### Identifying Leap-of-Faith Assumptions

A leap-of-faith assumption (term from Eric Ries, Lean Startup) is one where:
1. If it's wrong, everything collapses (Impact = 5)
2. You have no direct evidence it's right (Uncertainty >= 4)
3. The team is proceeding as if it's true

Every product has at least one. Common examples:
- "Users will pay for this" (for a product with no revenue yet)
- "We can acquire users for less than $X" (for a product with no marketing data)
- "Users will switch from [incumbent]" (for a product challenging an established player)
- "The technology can deliver [performance threshold] at scale" (for a technically novel product)

If you can't identify the leap-of-faith assumption, you haven't thought hard enough.

### Prioritization Biases to Watch For

**Optimism bias**: "We're confident this will work" — based on what evidence? Confidence without evidence is delusion.

**Anchoring**: The first assumption discussed gets rated as highest priority regardless of actual risk. Randomize the order.

**Availability bias**: The assumption related to the most recent meeting or loudest stakeholder gets priority. Use the matrix, not memory.

**IKEA effect**: Assumptions behind ideas the team already invested in get rated as "low risk" to justify continuing. Be honest about sunk costs.

**Groupthink**: If everyone agrees an assumption is safe, ask: "What would change our minds?" If nobody can answer, the assumption hasn't been examined.

---

## Part 3: Continuous Assumption Tracking

### The Assumption Lifecycle

Assumptions are not a one-time exercise. They are a living inventory that evolves as the product evolves.

```
IDENTIFIED -> PRIORITIZED -> TESTING -> VALIDATED -> MONITORED
                                    \-> INVALIDATED -> PIVOT/KILL
```

### The Assumption Tracker Format

Maintain a living document with this structure:

```
## Assumption Tracker: [Product/Feature]
Last updated: [date]

### Active Testing
| ID | Assumption | Category | Impact | Uncertainty | Experiment | Status | Due Date |
|----|-----------|----------|--------|-------------|-----------|--------|----------|
| A1 | 30% of free users upgrade at limit | Value | 5 | 4 | Fake door test | Running | Feb 15 |
| A2 | Users complete onboarding in <2min | Usability | 4 | 3 | Prototype test (n=5) | Planned | Mar 1 |

### Validated (with evidence)
| ID | Assumption | Evidence | Date Validated | Confidence |
|----|-----------|---------|---------------|-----------|
| A5 | Users want export to PDF | 8.2% fake door CTR (n=3400) | Jan 19 | High |

### Invalidated (with evidence and response)
| ID | Assumption | Evidence | Date Invalidated | Response |
|----|-----------|---------|-----------------|----------|
| A3 | Users will self-serve setup | 1/5 completed unassisted | Jan 25 | Adding setup wizard |

### Deferred (low priority, revisit quarterly)
| ID | Assumption | Category | Last Reviewed |
|----|-----------|----------|--------------|
| A8 | Mobile usage will exceed desktop | Strategy | Jan Q1 |
```

### Assumption Review Cadence

- **Weekly**: Update active experiments. Move completed experiments to Validated/Invalidated. Identify any new assumptions surfaced by interviews, analytics, or team discussions.
- **Monthly**: Review the full tracker. Are priorities still correct? Have any deferred assumptions become more important? Are there stale assumptions that need fresh testing?
- **Quarterly**: Comprehensive review. Archive old assumptions. Re-prioritize the entire list against updated strategy and metrics.

### Signals That Trigger New Assumptions

Stay alert for moments that introduce new, unexamined assumptions:
- **Strategy change**: New OKRs, pivot, market expansion
- **Competitive move**: A competitor launches something that changes the game
- **User behavior shift**: Unexpected usage pattern in analytics
- **Technology change**: New platform capability, API deprecation, regulation
- **Team change**: Key engineer leaves, new designer joins with different perspective
- **Negative experiment result**: Every invalidated assumption cascades into new questions

### Cross-Team Assumption Visibility

Assumptions are not private to the product team. Engineering has feasibility assumptions. Marketing has GTM assumptions. Sales has pricing assumptions. Finance has unit economics assumptions.

The Discoverer's job is to surface and consolidate assumptions across functions, not just within the product trio. A product assumption validated by user research can still fail if the engineering feasibility assumption underneath it is wrong.

### Templates for Different Contexts

**For a feature launch (existing product)**:
Focus on Value + Usability. The business model exists; the question is whether this feature adds enough value and whether users can use it.

**For a new pricing model (existing product)**:
Focus on Value + Viability. Can we charge more? Will users accept the new model? What happens to churn?

**For a new product**:
Focus on Value + Go-to-Market. Does anyone want this? Can we reach them? Everything else is secondary until you have users.

**For a platform migration (existing product)**:
Focus on Feasibility + Value preservation. Can we rebuild without losing functionality? Will users notice (and tolerate) the differences?
