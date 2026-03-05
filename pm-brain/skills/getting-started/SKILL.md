---
name: getting-started
description: "Auto-loads on first PM-related interaction when no product context exists. Guides the user through initializing their product context and explains available commands. Detects missing .product-os/context/ directory and offers setup."
---

# Getting Started with Product OS

This skill auto-loads when a user asks a PM-related question but no product context exists yet.

## Detection

Check for the existence of `.product-os/context/product-brief.md` in the current working directory.

- **If it exists**: Skip this skill. The user has context. Route to the appropriate agent.
- **If it doesn't exist**: This is a first-time user or a new project. Guide them through setup.

## First Interaction

When no product context is detected, introduce the system briefly and offer to initialize:

```
I'm your PM operating system — 5 specialist agents coordinated by a central brain,
with persistent product context that compounds across sessions.

I don't see a product context for this project yet. Let's set one up:

Tell me about your product in a sentence or two, and I'll initialize everything.
Or type /brief to start the guided setup.

Once context exists, you can use:
  /think    — reason through a product question
  /discover — validate assumptions and map opportunities
  /strategy — competitive analysis, positioning, strategy canvas
  /build    — PRD, user stories, sprint planning
  /launch   — GTM strategy, battlecards, launch plan
  /measure  — metrics, experiments, SQL, dashboards
  /status   — see what's defined vs missing
```

## Quick Setup (if user provides product description directly)

If the user describes their product without using `/brief`, extract what you can and initialize:

1. Create `.product-os/context/` directory
2. Write `product-brief.md` from what they provided
3. Create remaining 9 context files with empty headers
4. Confirm what was created and suggest first actions based on product stage

## Setup Principles

- **Take less than 2 minutes.** Don't ask 20 questions. Extract what you can from what they said, create the brief, and start working.
- **Don't block on missing info.** If they said "it's an AI writing assistant" and nothing else, that's enough to start. The brief will get refined as agents do their work.
- **Suggest the right first command** based on what they told you:
  - Vague idea → `/discover` (validate before building)
  - Clear idea, no validation → `/discover` (test assumptions)
  - Validated idea, need direction → `/strategy`
  - Know what to build → `/build`
  - Product exists, need growth → `/launch` or `/measure`
  - Just exploring → `/think`

## Context Directory Structure

When initializing, create:

```
.product-os/
  context/
    product-brief.md          # Populated from user input
    strategy.md               # Empty (strategist will fill)
    personas.md               # Empty (discoverer will fill)
    competitive-landscape.md  # Empty (strategist will fill)
    opportunity-tree.md       # Empty (discoverer will fill)
    assumptions.md            # Empty (discoverer will fill)
    metrics.md                # Empty (analyst will fill)
    decisions.md              # Empty (brain logs decisions here)
    roadmap.md                # Empty (executor will fill)
    outcomes.md               # Empty (tracks what actually happened)
```

## Returning Users

If product context exists but is stale (>30 days since any update), mention it:

```
Welcome back. Your product context was last updated [date].
Type /status to see what's current and what needs refreshing.
```

## Notes

- This skill should feel like a helpful onboarding, not a gate. Never block the user from doing work.
- If the user asks a specific PM question without context (e.g., "help me write a PRD"), do both: answer their question AND mention that setting up context would make future work better.
- Never force the user through the full setup if they just want to ask a quick question.
