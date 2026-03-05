---
name: user-research
description: "Interview script creation with JTBD probing, Mom Test principles, transcript synthesis, cross-interview persona extraction, and weekly research synthesis cadence. Covers the full research loop from preparation through analysis to action."
---

# User Research: Interviews, Synthesis, and Continuous Learning

User research is not a phase. It is a weekly practice. The team that stops talking to users starts building for imaginary people. The Discoverer ensures research happens, is synthesized properly, and feeds directly into the opportunity tree and assumption tracker.

## Part 1: Interview Preparation

### Research Objectives First

Before writing a single question, answer these three meta-questions:
1. **What decisions will this research inform?** ("Whether to build feature X" / "How to design the onboarding flow" / "Whether to expand to market segment Y")
2. **What do we already know and what's missing?** (Check assumptions.md — are we testing a specific assumption, or exploring an unknown space?)
3. **Who should we talk to?** (Not "users" — which segment, which behavior pattern, which lifecycle stage?)

If you can't answer #1, you're not ready to do research. Undirected research is a fishing expedition — sometimes necessary, but know that's what you're doing.

### The Mom Test (Rob Fitzpatrick)

The core principle: **Ask about their life, not your idea.** Every question should be about the past (what they did), not the future (what they would do).

**The Mom Test rules**:
1. Talk about **their life**, not your idea
2. Ask about **specifics in the past**, not generics or hypotheticals
3. **Talk less, listen more** — aim for 80/20 split (them talking 80%)
4. **Never pitch** during the interview — the moment you pitch, the data is contaminated
5. Look for **strong emotions** — they signal real pain or genuine delight
6. **Compliments are noise** — "That sounds cool!" tells you absolutely nothing about whether they'll use or pay for it

### Bad Questions vs. Good Questions

**"Would you use a feature that does X?"**
Bad. Everyone says yes to hypotheticals. They're being polite, not honest.
Good alternative: "How do you currently handle X? Walk me through the last time."

**"Do you think this is a good idea?"**
Bad. You're asking for their opinion about your idea. They'll say yes to avoid conflict.
Good alternative: "Tell me about the last time you faced [the problem this idea solves]. What happened?"

**"How much would you pay for this?"**
Bad. Stated willingness to pay has almost zero correlation with actual willingness to pay.
Good alternative: "What do you currently spend (in time or money) to solve this problem? Have you tried any paid solutions?"

**"Would this save you time?"**
Bad. Leading question — implies the answer is yes.
Good alternative: "How long does this typically take you? What steps are involved?"

**"What features would you want in a product like this?"**
Bad. You're asking users to design the product. Users describe solutions to yesterday's problems.
Good alternative: "What's the hardest part of your workflow right now? What have you tried to fix it?"

**"On a scale of 1-10, how important is X to you?"**
Bad. Abstract numerical ratings are unreliable and unactionable.
Good alternative: "Where does X rank in your daily priorities? What do you do before X? What gets skipped when you're busy?"

### Interview Script Structure

#### Opening (2-3 minutes)
Purpose: Establish trust, set expectations, get permission.

"Thanks for taking the time to talk with me. I'm [name] from [company]. We're trying to learn more about [topic area] — I'm here to learn from your experience, not sell anything. There are absolutely no right or wrong answers. If anything I ask doesn't make sense, just say so. Is it okay if I [record / take notes]? This will take about [X] minutes."

#### Warm-Up: Context and Background (5 minutes)
Purpose: Build rapport, understand their world, calibrate your follow-up questions.

- "Tell me about your role. What does a typical week look like?"
- "How long have you been doing [activity]?"
- "Who else is involved in [activity]? Who depends on you, and who do you depend on?"

#### Core Exploration: Jobs to Be Done (15-20 minutes)
Purpose: Understand what they're trying to accomplish, how they do it today, and where it breaks down.

**Current situation and behavior** (always past tense, always specific):
- "Walk me through the last time you [did the thing we're exploring]. Start from the very beginning."
- "What tools did you use? Were there other people involved?"
- "How long did it take from start to finish?"
- "Was that typical, or was this time unusual?"

**Pain points and frustrations** (observe, don't lead):
- "What was the hardest part about that?"
- "If you could wave a magic wand and change one thing about this process, what would it be?"
- "What have you tried to make this easier? What happened when you tried that?"
- "Have you looked for other solutions? What did you find? Why did you stick with / switch from them?"

**Desired outcomes** (their words, not yours):
- "What does 'good' look like for you here?"
- "How would you know if this was working well?"
- "What would change in your day/week if this problem were solved?"

**Willingness to pay / priority** (skin in the game signals):
- "How much time do you spend on this per week?"
- "Have you ever paid for a tool to help with this? How much?"
- "If a tool existed that solved this perfectly, what would it be worth to you in terms of time saved?"
- "What would you give up to have this solved?"

#### Probing Techniques

Use these when you hit an interesting thread. The goal is to go deeper, not wider:

- **"Tell me more about that."** — The universal opener. Works on any topic.
- **"Why?" (asked gently, 2-3 times)** — Gets to root causes. "Why did you choose that approach?" -> "Why was speed important?" -> "Why couldn't you wait for the normal process?"
- **"Can you give me a specific example?"** — Moves from opinions ("it's frustrating") to facts ("last Tuesday I spent 45 minutes trying to find the report").
- **"What happened next?"** — Follows the story to find unexpected consequences.
- **"How did that make you feel?"** — Captures emotional intensity. Strong emotions = real pain or delight.
- **"You mentioned [X]. Say more about that."** — Demonstrates you're listening and opens up details they assumed you wouldn't be interested in.

#### Wrap-Up (3-5 minutes)
Purpose: Capture anything missed, get referrals, close gracefully.

- "Is there anything I should have asked but didn't?"
- "Is there anything else about [topic] that you think is important for us to understand?"
- "Who else should I talk to about this? Anyone who has a really different perspective?"
- "Thank you for your time. Here's what happens next: [next steps]."

### Note-Taking Template

```
## Interview Notes
Participant: [Name or ID]
Segment: [User type / persona]
Date: [Date]
Duration: [X minutes]
Interviewer: [Name]

### Context
- Role: [their role and responsibilities]
- Experience: [how long they've been doing the relevant activity]
- Current tools: [what they use today]

### Jobs to Be Done
- Primary: [When I..., I want to..., so I can...]
- Secondary: [additional jobs]

### Current Workflow
[Step-by-step description of how they do the thing today]

### Pain Points
| Pain | Severity (1-5) | Frequency | Quote |
|------|----------------|-----------|-------|
| [pain] | [severity] | [daily/weekly/monthly] | "[exact quote]" |

### Satisfaction Signals
| What Works | Why | Quote |
|-----------|-----|-------|
| [thing that works] | [why it works for them] | "[exact quote]" |

### Key Quotes
> "[verbatim quote]" — context: [what prompted this]

### Surprise Findings
- [Anything unexpected or that contradicts team assumptions]

### Assumptions Tested
| Assumption | Result | Evidence |
|-----------|--------|----------|
| [assumption from tracker] | Supported / Challenged / Unclear | [what they said/did] |

### Follow-Up Actions
- [ ] [Next step from this interview]
```

### Red Flags During Interviews

Watch for signals that the data is unreliable:
- **Excessive agreement**: They say yes to everything. They're being polite, not honest. Try asking about negatives: "What's the worst part?"
- **Future promises**: "I would definitely use that!" — Stated intent != behavior. Redirect to past: "Have you tried anything like that before?"
- **Vague answers**: "It's generally fine, I guess." — Push for specifics: "Can you walk me through a specific time?"
- **Performing for the camera**: They give "smart" answers instead of honest ones. Make it safe: "A lot of people struggle with this — what's been your experience?"
- **Solution pitching**: They start designing the feature for you. Redirect: "That's an interesting idea — let me step back and understand the problem first."

---

## Part 2: Interview Synthesis

### Single Interview Summary

After each interview, synthesize within 24 hours while the memory is fresh. Use the output template:

```
## Interview Summary: [Participant ID / Segment]

**Date**: [date]
**Participant**: [role, segment, experience level — anonymized if needed]
**Duration**: [X minutes]
**Interviewer**: [name]

### Key Insights (top 3-5)
1. **[Insight]** — [supporting evidence/quote]
2. **[Insight]** — [supporting evidence/quote]

### Jobs to Be Done
- **Primary JTBD**: When I [situation], I want to [motivation], so I can [desired outcome].
- **Related JTBDs**: [additional jobs discovered]

### Current Workflow
[How they solve the problem today, step by step]

### Pain Points
| Pain Point | Severity | Frequency | Quote |
|-----------|----------|-----------|-------|
| [pain] | [1-5] | [how often] | "[exact quote]" |

### What Works Today
| Current Solution | Why It Works | Quote |
|-----------------|-------------|-------|
| [tool/process] | [reason] | "[quote]" |

### Notable Quotes
> "[quote]" — on [topic]

### Assumptions Validated / Challenged
| Assumption | Status | Evidence |
|-----------|--------|----------|
| [from tracker] | Validated / Challenged / Inconclusive | [evidence] |

### Surprises
- [Anything unexpected]

### Action Items
- [ ] [Follow-up from this interview]
```

### Cross-Interview Synthesis (After 5+ Interviews)

After collecting multiple interviews, synthesize across them to extract patterns:

**Step 1: Pattern Identification**
- What themes appear across 3+ interviews?
- What pain points are universal vs. segment-specific?
- What JTBDs are shared? Which are unique?
- Where do interviewees agree? Where do they contradict each other?

**Step 2: Evidence Weighting**
- A theme mentioned by 8/10 interviewees is strong signal
- A theme mentioned by 2/10 could be a niche segment or an outlier — note it but don't over-index
- Behavioral evidence (what they DO) outweighs stated preferences (what they SAY they want)

**Step 3: Persona Extraction**
Group interviewees by behavior patterns, NOT demographics:

**Strong persona basis**:
- "Power users who use the product >5x/week and have built custom workflows"
- "Reluctant adopters who use the product because their company mandates it but resist learning new features"
- "Decision-makers who evaluate the product but rarely use it day-to-day"

**Weak persona basis**:
- "25-34 year old urban professionals" (demographics don't predict behavior)
- "Tech-savvy millennials" (lazy generalization)
- "Enterprise users" (too broad — the CTO and the intern are both "enterprise users")

**Step 4: Opportunity Theme Extraction**
Map interview themes to opportunities for the OST:
- Each opportunity should be supported by evidence from multiple interviews
- Include the evidence count: "7/12 interviewees mentioned difficulty finding relevant content"
- Quote the strongest expressions of each opportunity

**Step 5: Update Context Files**
- Update `personas.md` with new or refined persona definitions
- Update `opportunity-tree.md` with newly discovered or validated opportunities
- Update `assumptions.md` with assumptions that were validated or challenged

---

## Part 3: Continuous Research Synthesis

### The Weekly Research Habit

Research is not a project. It is a recurring practice. The Discoverer maintains a weekly cadence:

**Weekly inputs to monitor**:
1. **Support tickets**: What problems are users reporting? What workarounds are they asking about? Categorize by theme and count frequency.
2. **NPS/CSAT responses**: Read the open-text comments, not just the scores. Scores tell you there's a problem; comments tell you what it is.
3. **Feature requests**: What are users asking for? More importantly, what problem is behind each request? (See feature-prioritization skill)
4. **Usage analytics**: What changed this week? Any significant drops in feature usage? New patterns in user flows?
5. **Churned user feedback**: Why did they leave? Exit surveys, cancellation reasons, support interactions before churn.
6. **Sales call notes**: What objections come up? What features do prospects ask about? What competitors are mentioned?
7. **App store reviews / social mentions**: What are users saying publicly?

**Weekly synthesis output**:
A brief document (1 page) summarizing:
- Top 3 themes from this week's signals
- Any new opportunities surfaced
- Any assumptions challenged
- Recommended actions (interview deeper, update OST, run experiment)

### The Research Repository

Maintain a structured archive of all research:

```
/research
  /interviews
    /2024-Q3
      interview-001-power-user.md
      interview-002-new-user.md
      synthesis-q3-round-1.md
  /support-analysis
    weekly-2024-01-15.md
    weekly-2024-01-22.md
  /surveys
    onboarding-survey-2024-01.md
  /analytics
    retention-cohort-analysis-2024-01.md
```

### Research Rigor Checklist

Before treating any research finding as "validated," check:
- [ ] Sample size is sufficient (5+ interviews for qualitative themes, 30+ responses for survey data, n>100 for quantitative significance)
- [ ] Behavioral evidence supports stated preferences (they didn't just say they'd use it — they showed you evidence of the problem)
- [ ] Multiple segments are represented (or the finding is explicitly segment-specific)
- [ ] The research questions were open-ended, not leading
- [ ] Contradicting evidence has been examined, not dismissed
- [ ] The finding is specific enough to be actionable (not "users want it to be better")
- [ ] The finding has been cross-referenced with quantitative data where possible

### Research Ethics

- Always get consent for recording
- Anonymize participants in shared documents
- Never share raw interview data outside the immediate team without consent
- Be transparent about the purpose of the research
- Compensate participants appropriately for their time
- If a participant reveals a critical issue during the interview (safety concern, urgent bug), act on it immediately — don't wait for the synthesis
