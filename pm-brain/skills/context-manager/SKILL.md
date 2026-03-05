---
name: context-manager
description: "Manages the persistent product context layer — initializes, reads, updates, and validates the 10 context files in .product-os/context/ within the user's project directory. Handles file creation, freshness checks, selective loading, ownership enforcement, and conflict resolution."
---

# Context Manager

You manage the persistent product context layer — 10 files that form the shared memory of the PM agent system. Every agent reads from these files. Each file has a single owning agent that writes to it.

## Critical: File Location

Context files live in the **user's project directory**, NOT the plugin install directory:

```
[project root]/
  .product-os/
    context/
      product-brief.md
      strategy.md
      personas.md
      competitive-landscape.md
      opportunity-tree.md
      assumptions.md
      metrics.md
      decisions.md
      roadmap.md
      outcomes.md
```

When any command runs, check for `.product-os/context/product-brief.md` relative to the current working directory. If it doesn't exist, trigger the getting-started skill.

## Context Files

| File | Purpose | Owner |
|------|---------|-------|
| product-brief.md | Foundation: what, who, why, stage, constraints | Brain (coordinator) |
| strategy.md | Strategic choices: vision, positioning, tradeoffs | Strategist |
| personas.md | Target users with evidence | Discoverer |
| competitive-landscape.md | Competitors with real data | Strategist |
| opportunity-tree.md | Opportunities, solutions, experiments | Discoverer |
| assumptions.md | What we believe but haven't proven | Discoverer |
| metrics.md | How we measure success | Analyst |
| decisions.md | What we decided and why | Brain (coordinator) |
| roadmap.md | What we're building and when | Executor |
| outcomes.md | What actually happened (feedback loop) | Brain (coordinator) |

## File Header (required on every file)

```markdown
<!-- owner: [agent-name] | updated: [YYYY-MM-DD] | status: [empty|draft|active|stale] -->
```

Status definitions:
- **empty**: File exists but has no content beyond the header
- **draft**: Initial content written, not yet validated or reviewed
- **active**: Content is current and has been reviewed or validated
- **stale**: Content is >2 weeks old and may not reflect current reality

## Selective Context Loading

Do NOT load all 10 files on every request. Load selectively based on the task:

| Task Domain | Always Load | Load If Available | Skip |
|------------|------------|-------------------|------|
| Strategy | product-brief.md | personas.md, metrics.md, competitive-landscape.md | roadmap.md, opportunity-tree.md |
| Discovery | product-brief.md | strategy.md, assumptions.md, metrics.md | competitive-landscape.md, roadmap.md |
| Execution | product-brief.md | strategy.md, personas.md, metrics.md, assumptions.md | competitive-landscape.md |
| Growth | product-brief.md | strategy.md, personas.md, competitive-landscape.md | opportunity-tree.md, assumptions.md |
| Analytics | product-brief.md | strategy.md, assumptions.md | personas.md, competitive-landscape.md |
| Status/Think | product-brief.md | ALL (scan headers only for staleness, load full content selectively) | — |

**product-brief.md is always loaded.** It's the foundation and should be kept concise (under 500 words).

## Multi-Modal Input Handling

Context files can reference external artifacts. Use these conventions:

```markdown
**Screenshot**: [description] — see attached image
**File**: [filename.csv] — uploaded by user on [date]
**URL**: [url] — competitor pricing page, fetched [date]
**Recording**: [description] — transcript in user-research/[filename].md
```

When users provide images (competitor screenshots, whiteboard photos, Figma exports), PDFs, CSVs, or URLs:
1. Analyze the content directly (Claude can read images and PDFs)
2. Extract relevant information into the appropriate context file
3. Reference the original artifact for traceability

## File Schemas

### product-brief.md

```markdown
<!-- owner: coordinator | updated: YYYY-MM-DD | status: draft -->

# Product Brief: [Product Name]

## What
[1-2 paragraphs: what the product does, core mechanism]

## Who
[Primary target users — brief description, link to personas.md for detail]

## Why
[The problem, why it matters, why now]

## Stage
[Idea | Discovery | Building | Live | Scaling]

## Constraints
- Team: [size, skills]
- Timeline: [any deadlines or urgency]
- Budget: [if relevant]
- Technical: [platform, stack, dependencies]
- Regulatory: [if relevant]

## Open Questions
- [Questions that need answering]
```

### strategy.md

```markdown
<!-- owner: strategist | updated: YYYY-MM-DD | status: draft -->

# Strategy: [Product Name]

## Vision
[What we aspire to achieve — inspiring, specific, time-bounded]

## Where We Play
[Target segments defined by problems/JTBD, not demographics]

## How We Win
[Our competitive advantage — what we do differently]

## Tradeoffs
[What we explicitly choose NOT to do and why]

## Cost Position
[Low-cost vs premium value vs hybrid — with reasoning]

## Growth Model
[PLG vs sales-led vs hybrid — primary acquisition channels]

## Defensibility
[Network effects, switching costs, IP, data moats, brand]

## Key Hypotheses
- Hypothesis 1: [statement] — Status: [untested|testing|validated|invalidated]

## Open Questions
- [Strategic questions requiring more data or decisions]
```

### personas.md

```markdown
<!-- owner: discoverer | updated: YYYY-MM-DD | status: draft -->

# Personas: [Product Name]

## Persona 1: [Name — descriptive label]

**Evidence base**: [N interviews, survey data, analytics, etc.]

**Jobs to Be Done**:
- Primary: [When I..., I want to..., so I can...]

**Pain Points**:
1. [Specific pain with evidence/quote]

**Current Solutions**: [What they use today and why it falls short]

**Satisfaction Level**: [1-10 with current solutions, with reasoning]

**Key Behaviors**: [How they work, what tools they use, frequency]

**Constraints**: [Budget, authority, technical skill, time]

## Open Questions
- [What we still need to learn about our users]
```

### competitive-landscape.md

```markdown
<!-- owner: strategist | updated: YYYY-MM-DD | status: draft -->

# Competitive Landscape: [Product Name]

## Market Category
[How we define the competitive space]

## Direct Competitors

### [Competitor 1 Name]
- **What they do**: [1-2 sentences]
- **Pricing**: [Specific tiers and prices]
- **Strengths**: [With evidence]
- **Weaknesses**: [With evidence]
- **Recent moves**: [Funding, launches, hires, pivots]
- **Our differentiation**: [Why we win against them]

## Indirect Competitors / Substitutes
[What else solves the same problem — including "do nothing"]

## Market Dynamics
- **Trends**: [What's changing]
- **Barriers to entry**: [What makes it hard for new entrants]
- **Key success factors**: [What winners have in common]

## Open Questions
- [What we need to learn about the competitive landscape]
```

### opportunity-tree.md

```markdown
<!-- owner: discoverer | updated: YYYY-MM-DD | status: draft -->

# Opportunity Solution Tree: [Product Name]

## Desired Outcome
[Single measurable outcome this tree targets]

## Opportunities

### Opportunity 1: [Customer-framed problem]
- **Evidence**: [Research supporting this]
- **Opportunity Score**: [Importance x (1 - Satisfaction)]
- **Priority**: [High|Medium|Low]

#### Solutions
1. [Solution A] — Status: [idea|testing|validated|invalidated|shipped]

#### Experiments
| Solution | Experiment | Hypothesis | Success Criteria | Status | Result |
|----------|-----------|-----------|-----------------|--------|--------|

## Open Questions
- [Discovery questions to explore next]
```

### assumptions.md

```markdown
<!-- owner: discoverer | updated: YYYY-MM-DD | status: draft -->

# Assumptions Tracker: [Product Name]

## Critical Assumptions (High Impact x High Uncertainty)

| # | Assumption | Category | Impact | Evidence Level | Status | Test Method | Result |
|---|-----------|----------|--------|---------------|--------|------------|--------|
| 1 | [Statement] | Value/Usability/Viability/Feasibility | H/M/L | None/Weak/Moderate/Strong | untested/testing/validated/invalidated | [How] | [If tested] |

## Validated Assumptions
[Moved here when confirmed with evidence]

## Invalidated Assumptions
[Moved here when disproven — include what we learned and what changed]

## Open Questions
- [What assumptions haven't we even identified yet?]
```

### metrics.md

```markdown
<!-- owner: analyst | updated: YYYY-MM-DD | status: draft -->

# Metrics Framework: [Product Name]

## North Star Metric
- **Metric**: [Name]
- **Definition**: [Precise operational definition]
- **SQL**: `[Pseudocode or actual query]`
- **Current value**: [If known]
- **Target**: [Goal with timeframe]
- **Business game**: [Attention|Transaction|Productivity]

## Input Metrics
| Metric | Definition | Current | Target | Owner |
|--------|-----------|---------|--------|-------|

## Guardrail Metrics
| Metric | Definition | Floor | Alert Threshold |
|--------|-----------|-------|----------------|

## Tracking Plan
| Event | When Fired | Properties | Status |
|-------|-----------|------------|--------|

## Open Questions
- [Measurement gaps or definition ambiguities]
```

### decisions.md

```markdown
<!-- owner: coordinator | updated: YYYY-MM-DD | status: active -->

# Decision Log: [Product Name]

Append-only. Most recent first.

### [YYYY-MM-DD] [Short title]
**Context**: [What prompted this]
**Options**: [Alternatives considered]
**Decision**: [What was decided]
**Rationale**: [Why]
**Implications**: [What changes — files to update, work to do]
```

### roadmap.md

```markdown
<!-- owner: executor | updated: YYYY-MM-DD | status: draft -->

# Roadmap: [Product Name]

## Current Quarter: [Q_ YYYY]

### Now (committed, in progress)
| Item | Outcome | Status | Link |
|------|---------|--------|------|

### Next (planned, high confidence)
| Item | Outcome | Depends On | Est. Effort |
|------|---------|-----------|-------------|

### Later (exploring, lower confidence)
| Item | Outcome | Open Questions |
|------|---------|---------------|

## Not Doing (explicit tradeoffs)
- [Thing we chose not to build and why]

## Open Questions
- [Roadmap decisions pending more data or stakeholder input]
```

### outcomes.md (NEW — the feedback loop)

```markdown
<!-- owner: coordinator | updated: YYYY-MM-DD | status: active -->

# Outcomes Log: [Product Name]

Track what actually happened after decisions, launches, and experiments. This is the feedback loop that makes the system learn.

Append-only. Most recent first.

### [YYYY-MM-DD] [Short title]
**What we did**: [Decision or action taken — link to decisions.md entry]
**What we expected**: [Predicted outcome with metrics]
**What actually happened**: [Observed outcome with data]
**Delta**: [Better/worse/different than expected, by how much]
**What we learned**: [Insight that should inform future work]
**Context updates needed**: [Which files should be updated based on this learning]
```

## MCP Integration Points

When available, these MCP servers enhance context management:

| MCP Server | What It Enables | Which Agents Benefit |
|-----------|----------------|---------------------|
| **Jira / Linear** | Pull tickets, sprint data, roadmap items | Executor (roadmap.md, sprint planning) |
| **Amplitude / Mixpanel** | Pull real metrics, funnel data, cohort analysis | Analyst (metrics.md, experiment analysis) |
| **Slack** | Pull user feedback, support conversations, team discussions | Discoverer (research synthesis) |
| **Figma** | Pull design specs, user flows, prototypes | Executor (PRD references) |
| **GitHub** | Pull issues, PRs, technical decisions | Executor (technical specs, ADRs) |
| **Google Sheets** | Pull survey data, prioritization matrices, OKR trackers | Multiple agents |
| **Notion / Confluence** | Pull existing docs, wikis, meeting notes | Multiple agents |

If an MCP server is connected, agents should use it to pull real data rather than asking the user to copy-paste. Reference the data source in context files for traceability.

## Operations

### Initialize Context

When a user starts with a new product:
1. Create `.product-os/context/` directory in the current working directory
2. Write product-brief.md from user input (keep it under 500 words)
3. Create remaining 9 files with empty status headers
4. Don't force the user to populate everything — agents fill files organically

### Update Context

When an agent produces output that should update a context file:
1. Check that the agent owns the file (or is the Brain updating product-brief.md, decisions.md, or outcomes.md)
2. Preserve existing content that is still valid
3. Update the header: new date, appropriate status
4. Add new content in the correct section
5. Move invalidated content to appropriate sections

### Freshness Check

When running `/status` or before any major workflow:
1. Read all 10 file headers (headers only — not full content)
2. Flag any file with status "stale" or updated >14 days ago
3. Flag any file with status "empty" that would improve current work
4. Recommend specific actions to refresh stale context

### Proactive Alerts

When any context file is loaded and the coordinator notices:
- A file is stale (>14 days): mention it briefly ("Note: competitive-landscape.md hasn't been updated in 3 weeks")
- An assumption should have been tested by now (assumptions.md has items older than their planned test date): flag it
- A decision was made >30 days ago with no outcome logged: suggest adding to outcomes.md
- The product stage in product-brief.md doesn't match the work being done (e.g., stage says "Idea" but user is writing PRDs): suggest updating

### Conflict Resolution

If agents produce contradictory information:
1. Do NOT silently resolve — present both to the user
2. Explain the contradiction clearly
3. Ask the user to decide
4. Log the decision in decisions.md
5. Update the relevant context file
