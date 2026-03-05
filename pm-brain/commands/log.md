---
name: log
description: "Log an outcome, result, or learning. Fast way to close the feedback loop."
argument-hint: "<what happened>"
---

# /log — Outcome Logging

Quick way to record what actually happened after a decision, launch, or experiment. Closes the feedback loop that makes Product OS learn across sessions.

## Invocation

```
/log Our conversion went up 12% after the pricing change
/log The Product Hunt launch got 500 signups but only 3% activated
/log We killed the notification feature — users didn't engage
/log                     # interactive — asks what happened
```

## Workflow

### Step 1: Identify What This Is About

Check `decisions.md` and `activity-log.md`. Does this outcome relate to a logged decision or recent work? If so, link them.

### Step 2: Log the Outcome

Write to `outcomes.md`:
- What we did (link to decision if applicable)
- What we expected
- What actually happened (with numbers)
- Delta (better/worse/different, by how much)
- What we learned

### Step 3: Extract Learnings

If this outcome reveals a proven insight, add it to `learnings.md`. Only add insights backed by evidence — not speculation.

Examples:
- "Product Hunt drives signups but <5% activate" → learnings.md under "About Our Product"
- "SMB customers are 3x more price-sensitive than enterprise" → learnings.md under "About Our Users"

### Step 4: Flag Implications

Check if this outcome invalidates any assumptions in `assumptions.md` or contradicts any strategy in `strategy.md`. Flag for the user.

## Notes

- This should take 1-2 minutes. Don't over-document.
- If the user provides numbers, use them. If not, ask for specifics — "what was the actual number?"
- The goal is to close the loop: decision → outcome → learning → better future decisions.
