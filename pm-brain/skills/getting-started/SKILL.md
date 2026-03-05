---
name: getting-started
description: "Auto-loads on first interaction when no product context exists. Introduces Product OS, explains what it does and how to use it, then guides setup. Detects missing .product-os/context/ directory."
---

# Getting Started with Product OS

This skill auto-loads when a user runs any command but no product context exists yet.

## Detection

Check for `.product-os/context/product-brief.md` in the current working directory.

- **If it exists**: Skip this skill. Route to the appropriate agent.
- **If it doesn't exist**: First-time user or new project. Show the welcome message.

## Welcome Message

When no product context is detected, introduce Product OS:

```
Welcome to Product OS — an AI-native product management operating system.

Here's what you just installed:

  6 specialist agents     Strategist, Discoverer, Executor, Growth, Analyst
                          — coordinated by a central Brain
  34 skills               Deep PM frameworks, not generic templates
  11 commands             Everything from ideation to launch to measurement
  Persistent memory       12 files that remember your product across sessions
                          — strategy informs PRDs, discovery validates assumptions,
                            metrics track what actually happened, learnings compound
  Quality gates           Every output is self-evaluated with confidence scoring

How it works:
  1. You describe your product (or run /brief)
  2. I create a persistent context layer in .product-os/context/
  3. Every command reads and builds on that context
  4. Knowledge compounds — you never explain your product from scratch twice

Commands:
  /brief [product]      — Start here. Initialize your product context
  /think [question]     — Reason through a product question or decision
  /discover [topic]     — Validate assumptions, map opportunities, design experiments
  /strategy [topic]     — Competitive analysis, positioning, strategy canvas
  /build [feature]      — PRD, user stories, sprint planning
  /launch [product]     — GTM strategy, battlecards, launch plan
  /measure [question]   — Metrics, A/B tests, SQL, dashboards
  /status               — See what's defined, what's missing, what's stale
  /plan [outcome]       — Decompose a big goal into sequenced agent tasks
  /update [info]        — Feed new information into the context layer
  /log [outcome]        — Record what happened, extract learnings

Ready? Tell me about your product in a sentence or two, or type /brief to start.
```

## Quick Setup (if user provides product description directly)

If the user describes their product without using `/brief`, extract what you can and initialize:

1. Create `.product-os/context/` directory
2. Write `product-brief.md` from what they provided
3. Create remaining 11 context files with empty headers
4. Confirm what was created and suggest first actions based on product stage

## Setup Principles

- **Take less than 2 minutes.** Don't ask 20 questions. Extract what you can, create the brief, start working.
- **Don't block on missing info.** If they said "it's an AI writing assistant" and nothing else, that's enough. The brief gets refined as agents do their work.
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
    activity-log.md           # Empty (session history — auto-updated)
    learnings.md              # Empty (compound insights — grows over time)
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
