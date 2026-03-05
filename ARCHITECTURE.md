# Product OS: Architecture

## How It Actually Works

Product OS is a **layered prompt composition system**. There are no separate agent processes, no microservices, no inter-process communication. When a user invokes a command:

1. The coordinator skill loads into context
2. It classifies the request and identifies which specialist skills to apply
3. The specialist's agent definition + relevant knowledge skills inform the response
4. The output is self-evaluated against domain-specific quality criteria
5. Context files in `.product-os/context/` are updated
6. Confidence scoring footer is appended

"Routing to the Strategist" means applying the strategist's skill definitions and quality criteria. This is explicit — the system never uses theatrical agent-spawning language.

---

## System Architecture

```
                    USER
                      |
                 [/command or natural language]
                      |
                      v
            +-------------------+
            |     PM BRAIN      |  Single entry point
            |   (coordinator)   |  Routes, decomposes, orchestrates,
            |                   |  guards quality, manages context
            |  10 slash commands |
            +--------+----------+
                     |
                     | [applies specialist skills]
                     |
        +------------+------------+------------+------------+
        |            |            |            |            |
   STRATEGIST   DISCOVERER   EXECUTOR      GROWTH      ANALYST
   (direction)  (evidence)   (shipping)   (traction)  (measurement)
        |            |            |            |            |
        +------------+------------+------------+------------+
                                 |
                    +-------------------------+
                    |     CONTEXT LAYER        |
                    |  .product-os/context/    |
                    |  (12 persistent files)   |
                    +-------------------------+
```

---

## Plugin Structure

Product OS is distributed as a single Claude Code plugin. One install, everything included.

```
product-os/                              # Marketplace root
  .claude-plugin/marketplace.json        # Registry — lists the single plugin
  CLAUDE.md                              # System instructions (10 rules)
  ARCHITECTURE.md                        # This document
  README.md                              # User-facing documentation
  validate_plugins.py                    # Structural validation

  pm-brain/                              # Single plugin — all commands + all skills
    .claude-plugin/plugin.json
    commands/
      think.md                           # Strategic reasoning
      status.md                          # Cross-context synthesis
      brief.md                           # Initialize product context
      plan.md                            # Decompose into agent tasks
      update.md                          # Intake new information
      strategy.md                        # → Strategist skills
      discover.md                        # → Discoverer skills
      build.md                           # → Executor skills
      launch.md                          # → Growth skills
      measure.md                         # → Analyst skills
      log.md                             # Record outcomes, extract learnings
    skills/
      # Brain (3 skills)
      coordinator/SKILL.md               # Brain agent definition
      context-manager/SKILL.md           # Context layer management
      getting-started/SKILL.md           # First-run onboarding

      # Strategist (6 skills)
      strategist/SKILL.md               # Agent definition
      product-strategy/SKILL.md         # Vision, strategy canvas, positioning
      competitive-analysis/SKILL.md     # Porter's, PESTLE, SWOT, Ansoff
      business-models/SKILL.md          # BMC, Lean Canvas, monetization
      market-assessment/SKILL.md        # Sizing, segments, journey maps
      positioning/SKILL.md              # April Dunford, value prop, pricing

      # Discoverer (6 skills)
      discoverer/SKILL.md               # Agent definition
      discovery-cycle/SKILL.md          # Brainstorming (new + existing products)
      assumption-testing/SKILL.md       # Identify, prioritize, validate
      opportunity-mapping/SKILL.md      # OST, metrics dashboard
      user-research/SKILL.md            # Interview scripts, synthesis
      feature-prioritization/SKILL.md   # RICE, WSJF, MoSCoW, ICE + requests

      # Executor (8 skills)
      executor/SKILL.md                 # Agent definition
      prd/SKILL.md                      # Auto-populated from context
      okrs-roadmap/SKILL.md             # OKRs + 9 prioritization frameworks
      sprint-delivery/SKILL.md          # Sprint, retro, release, pre-mortem
      stakeholder-communication/SKILL.md # Stakeholder map, exec updates, sunset
      technical-specs/SKILL.md          # RFC + ADR templates
      backlog-items/SKILL.md            # User stories, job stories, WWA
      ai-product-management/SKILL.md    # AI-native PM practices

      # Growth (6 skills)
      growth/SKILL.md                   # Agent definition
      gtm-strategy/SKILL.md            # GTM, beachhead, ICP, motions
      growth-engines/SKILL.md           # Growth loops, NSM, PLG playbook
      battlecards/SKILL.md              # Competitive battlecards
      launch-readiness/SKILL.md         # 8-dimension launch checklist
      retention/SKILL.md                # Churn, engagement, pricing experiments

      # Analyst (5 skills)
      analyst/SKILL.md                  # Agent definition
      metrics-definition/SKILL.md       # NSM, dashboards, precision protocol
      sql-analytics/SKILL.md            # SQL generation, cohort analysis
      experiment-design/SKILL.md        # A/B tests, pre-registration
      instrumentation/SKILL.md          # Event taxonomy, tracking plans
```

### Key Structural Decisions

1. **Single plugin, everything included.** Users run two commands: add the marketplace, install the plugin. All 34 skills and 11 commands come in one package.

2. **Skills, not knowledge.** Each specialist's domain files are structured as `skills/[skill-name]/SKILL.md` following the Claude Code plugin format. The agent definition file (e.g., `strategist/SKILL.md`) acts as the orchestrator for that domain's skills.

3. **No bundled context.** Context files live in the user's project directory (`.product-os/context/`), never in the plugin directory. This ensures context persists across plugin updates and is project-specific.

---

## The Context Layer

### Location

Context files live in the **user's project directory**, not the plugin install directory:

```
[user's project]/
  .product-os/
    context/
      product-brief.md          # Brain owns — the foundation
      strategy.md               # Strategist owns
      personas.md               # Discoverer owns
      competitive-landscape.md  # Strategist owns
      opportunity-tree.md       # Discoverer owns
      assumptions.md            # Discoverer owns
      metrics.md                # Analyst owns
      decisions.md              # Brain owns — decision log
      roadmap.md                # Executor owns
      outcomes.md               # Brain owns — feedback loop
      activity-log.md           # Brain owns — session history
      learnings.md              # Brain owns — compound knowledge
```

### Ownership Model

| File | Owner | Reads | Updated When |
|------|-------|-------|-------------|
| product-brief.md | Brain | All agents | User provides product context |
| strategy.md | Strategist | Executor, Growth, Brain | Strategy work completed |
| personas.md | Discoverer | Strategist, Executor, Growth | Research synthesized |
| competitive-landscape.md | Strategist | Growth, Brain | Competitive analysis run |
| opportunity-tree.md | Discoverer | Executor, Brain | Discovery work completed |
| assumptions.md | Discoverer | All agents | Assumptions identified or tested |
| metrics.md | Analyst | All agents | Metrics defined or updated |
| decisions.md | Brain | All agents | Significant decision made |
| roadmap.md | Executor | Brain, Growth | Planning completed |
| outcomes.md | Brain | All agents | Results logged (feedback loop) |
| activity-log.md | Brain | All agents (last 3) | End of every command |
| learnings.md | Brain | All agents | Insight proven by evidence |

### Selective Loading

Memory files are loaded for ALL domains. Domain-specific files load selectively.

**Always loaded (all domains)**:
- `product-brief.md` — full content
- `learnings.md` — full content (compound knowledge)
- `activity-log.md` — last 3 entries (session memory, anti-duplication)
- `decisions.md` — last 5 entries (recent decisions)
- `outcomes.md` — last 5 entries (feedback loop)

**Domain-specific**:

| Task Domain | Load If Available | Skip |
|------------|-------------------|------|
| Strategy | personas.md, metrics.md, competitive-landscape.md | roadmap.md, opportunity-tree.md |
| Discovery | strategy.md, assumptions.md, metrics.md | competitive-landscape.md, roadmap.md |
| Execution | strategy.md, personas.md, metrics.md, assumptions.md | competitive-landscape.md |
| Growth | strategy.md, personas.md, competitive-landscape.md, assumptions.md | opportunity-tree.md |
| Analytics | strategy.md, assumptions.md | personas.md, competitive-landscape.md |
| Status | ALL (scan headers only, load full content selectively) | — |

### File Headers

Every context file has a metadata header:

```markdown
<!-- owner: [agent-name] | updated: [YYYY-MM-DD] | status: [empty|draft|active|stale] -->
```

### Freshness & Proactive Alerts

The coordinator monitors context health:
- Files with `status: stale` or updated >14 days ago are flagged
- Assumptions past their planned test date are surfaced
- Decisions >30 days old without logged outcomes trigger a reminder
- Product stage mismatches (e.g., stage says "Idea" but user is writing PRDs) are noted

---

## Quality System

### Per-Agent Self-Evaluation

Every specialist agent has 5-7 domain-specific quality criteria checked before output is returned. Examples:

- **Strategist**: Evidence-backed claims, clear choices, explicit tradeoffs, specific competitive data, measurable winning, product-specific
- **Discoverer**: Evidence-based personas, categorized assumptions, measurable experiments, outcome-connected OST, scored prioritization, DxVxF evaluation
- **Executor**: Context grounding, measurable key results, INVEST compliance, testable acceptance criteria, strategic linkage, explicit scope, assumption transparency
- **Growth**: Segment specificity, channels ranked by CAC, quantitative growth loops, evidence-cited battlecards, launch rollback triggers, competitive positioning, JTBD-tied recommendations
- **Analyst**: Precise operational definitions, valid SQL, stated statistical assumptions, reproducible cohorts, dashboard hierarchy, consistent event taxonomy

### Universal Quality Checks (Coordinator)

```
CHECK 1: Specificity
  Contains the product's actual name? (not "[Product]")
  References real competitors by name? (where relevant)
  Metrics have numbers or ranges? (not "improve engagement")
  Recommendations are actionable this week?
  → FAIL: Iterate. Make specific using product-brief.md context.

CHECK 2: Consistency
  Contradicts existing context files?
  → FAIL: Flag contradiction to user. Never silently resolve.

CHECK 3: Completeness
  Actionable without additional work? (single tasks)
  Next step has everything it needs? (workflow steps)
  → FAIL: Identify what's missing. Fill from context or ask.

CHECK 4: Honesty
  Assumptions marked as assumptions?
  Evidence-based claims cite evidence?
  → FAIL: Annotate assumptions. Add [UNVALIDATED] or [ASSUMED] tags.
```

### Confidence Scoring Footer

Every substantive output includes:

```markdown
---
**Output Assessment**
- Confidence: [High|Medium|Low] — [one-line reasoning]
- Evidence-backed claims: [X of Y]
- Assumptions made: [count, list if <5]
- Context used: [files referenced]
- Gaps that would improve this: [specific missing context]
```

This is mandatory. No exceptions.

---

## Commands

All 11 commands live in pm-brain. Specialist plugins have no commands.

| Command | Routes To | What It Does |
|---------|----------|-------------|
| `/think [question]` | Brain + relevant agents | Strategic reasoning about a question or decision |
| `/status` | Brain | Synthesize product state across all context files |
| `/brief [product]` | Brain | Initialize or update product brief |
| `/plan [outcome]` | Brain | Decompose complex outcome into sequenced tasks |
| `/update [info]` | Brain → relevant agents | Intake new information into context layer |
| `/strategy [topic]` | Strategist skills | Competitive analysis, positioning, strategy canvas |
| `/discover [topic]` | Discoverer skills | Discovery cycle: ideation, assumptions, experiments |
| `/build [feature]` | Executor skills | PRD, user stories, sprint planning |
| `/launch [product]` | Growth skills | GTM strategy, battlecards, launch plan |
| `/measure [question]` | Analyst skills | Metrics, experiments, SQL, dashboards |
| `/log [outcome]` | Brain | Record outcome, extract learning, close feedback loop |

---

## Cross-Agent Workflows

### Idea to Launch (`/plan Take idea to launch`)

```
Phase 1: Foundation (Brain)
  → Initialize product-brief.md, identify context gaps

Phase 2: Discovery (Discoverer skills)
  → Build personas, map opportunities, identify assumptions
  → Writes: personas.md, opportunity-tree.md, assumptions.md

Phase 3: Strategy (Strategist skills)
  → Define positioning, competitive angle, strategy canvas
  → Writes: strategy.md, competitive-landscape.md

Phase 4: Definition (Executor skills)
  → PRD (auto-populated from context), user stories, OKRs
  → Writes: roadmap.md

Phase 5: Go-to-Market (Growth skills)
  → GTM strategy, battlecards, launch plan

Phase 6: Measurement (Analyst skills)
  → North Star metric, tracking plan, experiment design
  → Writes: metrics.md

Phase 7: Synthesis (Brain)
  → Compile outputs, identify remaining gaps, next actions
  → Writes: decisions.md
```

### Competitive Response (`/update Competitor just launched X`)

```
Phase 1: Intelligence (Strategist) → WebSearch, update competitive-landscape.md
Phase 2: Assessment (Brain + Strategist) → Impact on positioning, response options
Phase 3: Implications → Route to affected agents (Growth for battlecards, Executor for roadmap)
Phase 4: Decision (Brain) → Present options, record in decisions.md
```

### Weekly Cadence (`/status`)

```
1. Read all 10 context file headers
2. Load full content selectively
3. Produce: state summary, context health, critical gaps, stale files, open questions, top 3 actions
```

---

## Multi-Modal Input

All agents accept and analyze non-text input:

| Input Type | Handling |
|-----------|---------|
| Screenshots | Analyze visually — competitor UIs, pricing pages, whiteboard sketches |
| PDFs | Read and extract — research reports, analyst decks, contracts |
| CSVs | Analyze data — survey results, analytics exports, feature requests |
| URLs | WebFetch — competitor sites, pricing pages, job postings |
| Transcripts | Synthesize — interview recordings, meeting notes |
| Figma links | Reference in PRDs and user stories |

---

## MCP Integration

When MCP servers are connected, agents use real data instead of asking users to copy-paste:

| MCP Server | What It Enables | Which Agents Benefit |
|-----------|----------------|---------------------|
| Jira / Linear | Tickets, sprint data, roadmap items | Executor |
| Amplitude / Mixpanel | Real metrics, funnel data, cohort analysis | Analyst |
| Slack | Customer feedback, support conversations | Discoverer |
| Figma | Design specs, prototypes, user flows | Executor |
| GitHub | Issues, PRs, technical decisions | Executor |
| Google Sheets | Survey data, prioritization matrices | Multiple |
| Database | Direct SQL execution | Analyst |

---

## Design Principles

1. **Agents own domains, not documents.** A Strategist doesn't "write a strategy doc." It maintains strategic clarity — which sometimes means a document, sometimes a one-line answer, sometimes "you're asking the wrong question."

2. **Context is shared, ownership is clear.** Every persistent file has one agent that writes it. All agents can read all files. The Brain resolves conflicts.

3. **Quality gates, not quality hopes.** Every agent evaluates its own output against explicit criteria before returning. If it can't meet the bar, it says what's missing.

4. **Warnings, not blocking.** For single tasks, produce with prominent warnings when context is missing. For workflows, flag gaps and let the user decide.

5. **Honest about mechanism.** This is prompt composition, not agent spawning. Never waste tokens on theatrical language.

6. **Specific, not generic.** Output must contain actual product names, real competitors, specific numbers. The "could this describe any product?" test must fail.

7. **Feedback loop.** outcomes.md tracks what actually happened after decisions, enabling the system to learn across sessions.

---

## What Changed from pm-skills (v1)

| Aspect | pm-skills (v1) | Product OS (v2) |
|--------|---------------|-----------------|
| Architecture | 8 silos, 65 flat prompts | 6 agents + brain, shared context |
| Entry point | Remember which plugin has which command | Single brain, 11 commands |
| State | Stateless (start fresh every time) | 12 persistent context files + session memory |
| Output quality | Variable (40-222 lines per skill) | Consistent (100-460 lines, quality gates) |
| Self-evaluation | None | Per-agent criteria + confidence scoring |
| Tools | None | WebSearch, file I/O, MCP integrations |
| Multi-modal | Text only | Images, PDFs, CSVs, URLs |
| Feedback loop | None | outcomes.md tracks what actually happened |
| AI PM skills | None | Dedicated AI product management skill |
| Specificity | Often generic templates | Anti-generic guardrail enforced |
