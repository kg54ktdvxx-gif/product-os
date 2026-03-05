# Product OS: AI-Native Product Management Operating System

> 6 coordinated agents, 35+ skills, 10 commands, persistent product context. From idea to launch to growth — with quality gates, real data, and a feedback loop that learns.

## Start Here

```
/brief My product idea                   # Initialize product context (2 min)
/status                                   # See what's defined vs missing
/think Should we build X or Y?            # Strategic reasoning
```

Then go deeper:

```
/discover                                 # Validate assumptions, build opportunity tree
/strategy                                 # Competitive analysis, positioning, strategy canvas
/build                                    # PRD, user stories, sprint plan
/launch                                   # GTM strategy, battlecards, launch plan
/measure                                  # Metrics, experiments, SQL, dashboards
```

Or orchestrate:

```
/plan Take our idea from concept to launch    # Multi-agent workflow
/update Our competitor just raised $50M       # Intake new context
```

## How It Works

Product OS is a **layered prompt composition system**. One model, layered instructions:

1. **You type a command** (or describe what you need)
2. **The Brain (coordinator)** classifies your request and loads relevant context
3. **Specialist skills** provide frameworks, quality criteria, and anti-patterns
4. **Quality gates** check output for specificity, consistency, and honesty
5. **Context files** get updated so knowledge compounds across sessions

No theatrical agent spawning. No 20-minute onboarding. Ask a question, get a rigorous answer.

## The 6 Agents

### Brain (pm-brain)
The coordinator. Routes all requests, manages context, enforces quality. All 10 commands live here.

### Strategist (pm-strategist)
Product strategy, competitive analysis (with web research), market assessment, business models, pricing, positioning.

### Discoverer (pm-discoverer)
User research synthesis, assumption testing, opportunity mapping, experiment design, feature prioritization.

### Executor (pm-executor)
PRDs (auto-populated from context), OKRs, roadmaps, sprints, user stories, stakeholder communication, technical specs, AI product management.

### Growth (pm-growth)
GTM strategy, launch planning, growth loops, positioning, battlecards, product-led growth, retention strategy.

### Analyst (pm-analyst)
Metrics definition (with SQL precision), A/B test analysis, cohort analysis, experiment design, analytics instrumentation.

## The Context Layer

10 persistent files in `.product-os/context/` that compound knowledge across sessions:

```
.product-os/context/
  product-brief.md          # Brain — the foundation
  strategy.md               # Strategist — strategic choices
  personas.md               # Discoverer — target users with evidence
  competitive-landscape.md  # Strategist — competitors with data
  opportunity-tree.md       # Discoverer — opportunities and experiments
  assumptions.md            # Discoverer — what we believe but haven't proven
  metrics.md                # Analyst — how we measure success
  decisions.md              # Brain — what we decided and why
  roadmap.md                # Executor — what we're building
  outcomes.md               # Brain — what actually happened (feedback loop)
```

Context is created automatically when you run `/brief`. Agents update their owned files as work happens. You never explain your product from scratch twice.

## Quality System

Every output gets:

1. **Domain-specific quality criteria** — each specialist checks 5-7 criteria before returning
2. **Anti-generic guardrail** — output must contain actual product name, real competitors, specific numbers
3. **Assumption flagging** — every claim is evidence-backed or explicitly marked `[ASSUMED]`
4. **Confidence scoring** — every substantive output includes a confidence assessment footer

```
---
Output Assessment
- Confidence: Medium — no validated personas, user segments are hypothetical
- Evidence-backed claims: 6 of 9
- Assumptions made: target market size, willingness to pay, competitor pricing
- Context files used: product-brief.md, competitive-landscape.md
- Gaps that would improve this: personas.md, metrics.md
```

## Multi-Modal Input

Share what you have — don't just describe it:

- **Screenshots** of competitor UIs, pricing pages, whiteboard sketches
- **PDFs** of research reports, analyst decks, contracts
- **CSVs** of survey data, analytics exports, feature request lists
- **URLs** for competitor sites (fetched with WebSearch/WebFetch)
- **Transcripts** of user interviews, meeting recordings

## MCP Integration

When connected, agents use real data instead of asking you to copy-paste:

| MCP Server | What It Enables |
|-----------|----------------|
| Jira / Linear | Sprint data, tickets, roadmap items |
| Amplitude / Mixpanel | Real metrics, funnels, cohort data |
| Slack | Customer feedback, support conversations |
| Figma | Design specs, prototypes, user flows |
| GitHub | Issues, PRs, technical decisions |

## Installation

### Claude Code (recommended)

Add the marketplace and install all plugins:

```
/plugin marketplace add kg54ktdvxx-gif/product-os
```

Then install the plugins:

```
/plugin install pm-brain@product-os
/plugin install pm-strategist@product-os
/plugin install pm-discoverer@product-os
/plugin install pm-executor@product-os
/plugin install pm-growth@product-os
/plugin install pm-analyst@product-os
```

Or install just the brain (gets all 10 commands):

```
/plugin install pm-brain@product-os
```

> **Note**: The brain has the commands; specialist plugins add deeper skill context. For the full system, install all 6.

### Local Development

```bash
git clone https://github.com/kg54ktdvxx-gif/product-os.git
/plugin marketplace add ./product-os
```

### Other AI Assistants

The `skills/*/SKILL.md` files follow the universal skill format:

```bash
# Copy all skills for Gemini CLI
for plugin in pm-*/; do
  cp -r "$plugin/skills/"* ~/.gemini/skills/ 2>/dev/null
done
```

## What's Different from pm-skills

| | pm-skills (v1) | Product OS (v2) |
|--|---------------|----------------|
| Architecture | 8 silos, 65 flat prompts | 6 agents + brain, shared context |
| Entry point | Remember which plugin has which command | Single brain, 10 commands |
| State | Stateless (start fresh every time) | 10 persistent context files |
| Output quality | Variable (40-222 lines per skill) | Consistent (all 100-460 lines, quality gates) |
| Self-evaluation | None | Per-agent criteria + confidence scoring |
| Tools | None | WebSearch, file I/O, MCP integrations |
| Multi-modal | Text only | Images, PDFs, CSVs, URLs |
| Feedback loop | None | outcomes.md tracks what actually happened |
| AI PM skills | None | Dedicated AI product management skill |
| Specificity | Often generic templates | Anti-generic guardrail enforced |

## Credits

Frameworks from Teresa Torres, Marty Cagan, Alberto Savoia, Dan Olsen, Roger L. Martin, April Dunford, Sean Ellis, and others. Original skill foundations from [Pawel Huryn's PM Skills](https://github.com/phuryn/pm-skills).

## License

MIT
