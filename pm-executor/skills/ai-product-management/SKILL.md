---
name: ai-product-management
description: >
  A comprehensive skill for product managers building AI-powered features in 2026.
  Covers AI feature evaluation, writing AI-specific PRDs, LLM product decisions
  (RAG vs fine-tuning vs prompt engineering), human-in-the-loop design, AI safety
  and bias, AI UX patterns, and AI product metrics. Includes decision matrices,
  concrete examples, anti-patterns, and actionable frameworks.
---

# AI Product Management

This skill covers the unique product management challenges of building AI-powered features. Traditional PM skills (user research, prioritization, spec writing) still apply — this skill covers the **delta**: what changes when the feature relies on a model instead of deterministic code.

---

## 1. AI Feature Evaluation

### When to Use AI vs Rule-Based vs Manual

Not every problem needs AI. The most expensive mistake a PM can make is reaching for a model when a simple rule or a human process would do.

**Use rule-based when:**
- The logic can be expressed as explicit conditions (e.g., "flag orders over $10,000 for review")
- Requirements are stable and well-understood
- You need 100% predictability and auditability
- The input space is bounded and enumerable

**Use AI/ML when:**
- The pattern is too complex for rules (e.g., "detect fraudulent transactions" across hundreds of signals)
- You have sufficient labeled data to train or evaluate
- Approximate answers are acceptable
- The problem involves perception (vision, language, audio)

**Keep it manual when:**
- Volume is low (fewer than 100 decisions per day)
- Stakes are extremely high and context-dependent (e.g., crisis communications)
- You lack training data and cannot generate it affordably
- The task requires empathy, judgment, or relationship context that no model captures

### Decision Matrix

Before greenlighting an AI feature, score these dimensions:

| Dimension | Low (favors rules/manual) | High (favors AI) |
|---|---|---|
| **Pattern complexity** | Few variables, clear thresholds | Hundreds of signals, fuzzy boundaries |
| **Data availability** | < 1K labeled examples | 10K+ labeled examples, or strong foundation model |
| **Accuracy requirement** | Must be 100% correct | 90%+ acceptable with fallback |
| **Latency tolerance** | < 50ms hard requirement | Seconds acceptable, or async is fine |
| **Cost budget** | < $0.001 per decision | $0.01–$1.00 per decision acceptable |
| **Explainability need** | Must justify every decision (regulatory) | Directional explanation sufficient |
| **Maintenance budget** | No dedicated ML team | Team can monitor, retrain, iterate |

If you score "Low" on 4+ dimensions, do not use AI. Build a rule engine or keep it manual.

### The "AI Tax"

Every AI feature carries ongoing costs that traditional features do not:

- **Training data**: Collection, cleaning, labeling, versioning. Budget $2–$10 per labeled example for human annotation. For LLM features, prompt tuning and evaluation sets cost engineer time, not labeling money — but the cost is real.
- **Model maintenance**: Models degrade as the world changes. Plan for quarterly retraining or continuous fine-tuning at minimum.
- **Drift monitoring**: You need infrastructure to detect when model performance degrades in production. This is not optional — it is a launch requirement.
- **Edge case handling**: AI features produce novel failure modes that rule-based features do not. Budget 30% of post-launch engineering time for edge case triage.
- **Compute costs**: Inference is not free. A single LLM call can cost $0.01–$0.50. At scale, this dominates your cost structure.
- **Evaluation infrastructure**: You need offline eval suites, online A/B testing, human evaluation protocols. This is a permanent line item.

**Weak evaluation**: "We should use AI for this — it would be really cool."
**Strong evaluation**: "Rule-based classification handles 70% of cases at 99% accuracy. AI would cover the remaining 30% (estimated 12K cases/month) at 85%+ accuracy. The AI tax is ~$4K/month in compute plus 0.5 FTE for monitoring. The 30% currently requires 2 FTEs of manual review. Net savings: 1.5 FTEs minus $4K/month."

---

## 2. Writing AI Product Specs

An AI PRD needs everything a traditional PRD needs, plus six additional sections that most PMs skip.

### What an AI PRD Requires Beyond a Traditional PRD

#### 2a. Model Selection Criteria

State the tradeoffs explicitly. Every model decision is a four-way tradeoff:

| Factor | Question to Answer |
|---|---|
| **Accuracy** | What is the minimum acceptable performance? On what benchmark? |
| **Latency** | What is the p50 and p99 latency budget? Streaming or batch? |
| **Cost** | What is the maximum cost per inference? Per user per month? |
| **Privacy** | Can data leave the device? Leave the region? Be logged? |

#### 2b. Training Data Requirements

Specify:
- **Volume**: Minimum viable dataset size (typically 1K–10K examples for fine-tuning, 50–200 for few-shot evaluation)
- **Quality**: Labeling guidelines, inter-annotator agreement targets (aim for Cohen's kappa > 0.8)
- **Representativeness**: Demographic, geographic, linguistic, and edge-case coverage requirements
- **Labeling process**: Who labels? What tool? What is the review/QA process?
- **Data freshness**: How often does training data need to be updated?

#### 2c. Evaluation Metrics

Do not ship an AI feature without defining success metrics **before** building it.

- **Classification tasks**: Precision, recall, F1-score. State which matters more — false positives or false negatives — and why.
- **Generation tasks**: BLEU/ROUGE for automated eval, but always pair with human evaluation. Define the human eval protocol: how many evaluators, what rubric, what is the passing score.
- **Retrieval tasks (RAG)**: Recall@K, MRR, answer correctness (human-judged), faithfulness (does the answer match the source?).
- **Set a floor**: "We will not launch if precision drops below 85% on the holdout set."

#### 2d. Edge Case Taxonomy

Enumerate what happens when the model is wrong. Categories:

- **Silent failures**: Model returns a confident but wrong answer. User trusts it. This is the most dangerous category.
- **Refusals**: Model declines to answer when it should. Frustrating but safe.
- **Hallucinations**: Model invents information. Critical for any factual use case.
- **Bias failures**: Model performs differently across demographic groups.
- **Adversarial inputs**: Users deliberately trying to break or jailbreak the feature.

For each category, specify the detection method and the mitigation.

#### 2e. Confidence Thresholds and Fallback Behavior

Define three tiers:

| Confidence | Action | Example |
|---|---|---|
| High (> 0.9) | Auto-apply result | Auto-categorize expense report |
| Medium (0.6–0.9) | Show result with option to override | Suggest category, user confirms |
| Low (< 0.6) | Fall back to manual/rule-based | Route to human reviewer |

The thresholds are not fixed — calibrate them on your evaluation set so that "high confidence" actually means high accuracy (aim for 95%+ precision in the auto-apply tier).

#### 2f. Privacy and Data Handling

- Does training data contain PII? If yes, what is the anonymization strategy?
- Is inference on-device or cloud? On-device eliminates data transmission risk but limits model size.
- Are user inputs logged for model improvement? Is there opt-out?
- What is the data retention policy for inference logs?
- Does the feature comply with GDPR Article 22 (automated decision-making)?

### Concrete Example: Strong vs Weak AI Feature Spec

**Weak spec:**
> "We will use AI to summarize customer support tickets. The model should be accurate and fast. We will use GPT-4o or similar."

**Strong spec:**
> **Feature**: Auto-summarize support tickets on close, saving agents ~2 minutes per ticket.
>
> **Model**: Claude Sonnet (estimated $0.008/ticket at avg 2K input tokens). On-device not required — tickets are already cloud-stored. Latency budget: < 5s p99.
>
> **Evaluation**: Human eval on 200 ticket sample. Rubric: factual accuracy (binary), completeness (1–5 scale), conciseness (1–5 scale). Launch gate: 95% factual accuracy, 4.0+ avg completeness, 3.5+ avg conciseness.
>
> **Training data**: No fine-tuning at launch. 50-example prompt engineering eval set, stratified across 5 ticket categories. Expand to 200 examples within 30 days.
>
> **Edge cases**: (1) Multi-language tickets — launch in English only, detect language and skip summarization for others. (2) Tickets with sensitive data (health, financial) — apply PII redaction before summarization. (3) Very short tickets (< 50 words) — skip summarization, display original.
>
> **Confidence/fallback**: No confidence score available for generation. Instead, use length ratio heuristic: if summary is > 80% of original length, flag for review. If summarization API is down, display "Summary unavailable" — do not block ticket closure.
>
> **Privacy**: Inputs are logged for 90 days for quality monitoring. Users can delete via data export. No PII in prompts beyond what is already in the ticket (which is governed by existing data policy).
>
> **Metrics**: Primary: agent time-to-close (A/B test). Secondary: summary edit rate (proxy for quality). Guardrail: escalation rate must not increase.

---

## 3. LLM-Specific Product Decisions

### RAG vs Fine-Tuning vs Prompt Engineering

This is the most common architectural decision for LLM features in 2026. Here is when to use each:

#### Prompt Engineering

**Use when:** You are shipping fast, iterating on behavior, volume is low-to-moderate (< 10K requests/day), and the task is within the base model's capabilities.

- Fastest to ship (hours to days)
- Easiest to iterate (change the prompt, not the model)
- Most expensive per-request (full context window every time)
- Least consistent (sensitive to phrasing, model updates)

**Best for**: Internal tools, v1 of customer-facing features, tasks where you are still learning what "good" looks like.

#### RAG (Retrieval-Augmented Generation)

**Use when:** You need current or proprietary data, you want to cite sources, you do not want to retrain models, or the knowledge base changes frequently.

- Medium effort to ship (need a retrieval pipeline: embedding, indexing, search)
- Answers are grounded in source documents (reduces hallucination)
- You can update knowledge without retraining (just re-index)
- Latency is higher (retrieval + generation)
- Quality depends heavily on retrieval quality — garbage in, garbage out

**Best for**: Customer support (search knowledge base), documentation Q&A, enterprise search, any feature where "I need the model to know about OUR data" is the requirement.

**Critical RAG decisions**:
- Chunk size: 256–512 tokens is a good starting point. Too small loses context; too large dilutes relevance.
- Retrieval count: 3–5 chunks is typical. More chunks = more context but higher cost and potential confusion.
- Reranking: A reranker (cross-encoder) between retrieval and generation significantly improves relevance. Budget the latency (~100ms).
- Hybrid search: Combine vector similarity with keyword search (BM25). Neither alone is sufficient.

#### Fine-Tuning

**Use when:** You need consistent style/format, domain-specific behavior that prompting cannot achieve, or you need cost optimization at scale (shorter prompts post-tuning).

- Highest upfront effort (need training data, training infrastructure, evaluation)
- Most consistent outputs (behavior is baked into weights)
- Cheapest per-request at scale (smaller model, shorter prompts)
- Hardest to update (retrain for every behavior change)
- Risk of catastrophic forgetting (model loses general capabilities)

**Best for**: Structured extraction at scale, domain-specific classification, consistent tone/format across millions of requests, replacing a larger model with a fine-tuned smaller one.

**Decision flowchart:**
1. Can a good prompt + examples solve it? → Start with prompt engineering.
2. Does the model need access to proprietary/current data? → Add RAG.
3. Is prompt engineering working but too expensive or inconsistent at scale? → Consider fine-tuning.
4. Do you need both proprietary data AND consistent behavior? → Fine-tuned model + RAG.

### Cost / Latency / Quality Triangle

You get to optimize for two. The third suffers.

| Priority | What You Sacrifice | Example |
|---|---|---|
| Quality + Speed | Cost | Use the largest model with streaming, cache nothing |
| Quality + Cost | Speed | Use batch APIs, queue requests, process async |
| Speed + Cost | Quality | Use the smallest model, aggressive caching, short prompts |

### Model Tier Selection

Most providers offer three tiers. Here is when to use each (using Anthropic's lineup as reference):

| Tier | When to Use | Cost/1M tokens (approx) |
|---|---|---|
| **Opus-class** | Complex reasoning, multi-step analysis, code generation, tasks where errors are expensive | $15–75 |
| **Sonnet-class** | Balanced — most production features, summarization, classification, chat | $3–15 |
| **Haiku-class** | High-volume, low-complexity: tagging, routing, extraction, filtering | $0.25–1 |

**Common pattern**: Use Haiku for classification/routing, then Sonnet or Opus for the actual task. This "model cascade" cuts costs 50–80% with minimal quality loss.

### Caching Strategies

- **Prompt caching** (provider-level): Reuse cached prefixes for system prompts and few-shot examples. Reduces cost by 80–90% on the cached portion. Available from Anthropic, OpenAI, and others.
- **Semantic caching**: Hash the intent of the request, not the literal text. If a similar question was asked recently, return the cached answer. Use embedding similarity with a threshold (typically 0.95+).
- **Result caching**: Cache the final output keyed on input. Simple but effective for deterministic-ish queries. Set a TTL based on how fast the underlying data changes.

### Token Economics

Estimate cost per request:
1. **Input tokens**: System prompt + user input + RAG context. Measure on 100 real examples.
2. **Output tokens**: Measure average output length. Output tokens cost 3–5x more than input.
3. **Multiply by volume**: Daily requests x cost per request x 30 = monthly cost.
4. **Add overhead**: Failed requests (retries), evaluation runs, development/testing usage. Typically 20–40% on top.

### Streaming vs Batch

- **Streaming**: User sees tokens as they are generated. Reduces perceived latency. Best for chat, writing, any interactive feature. Adds complexity (partial state handling, error mid-stream).
- **Batch**: Wait for complete response. Simpler to implement. Best for background processing, classification, extraction, anything non-interactive. Often cheaper (batch API discounts).

---

## 4. Human-in-the-Loop Design

### When to Require Human Review

- **High stakes**: Medical, legal, financial decisions. Hiring/firing. Content that could cause harm.
- **Low confidence**: Model output below the auto-approve threshold (see Section 2e).
- **Learning phase**: First 30 days of a new model deployment. Use human review to build an evaluation dataset.
- **Novel inputs**: Inputs that are far from the training distribution (detected via embedding distance or input classifiers).

### Confidence Threshold Calibration

Do not guess thresholds. Calibrate them:

1. Run the model on your evaluation set.
2. For each confidence threshold (0.5, 0.6, 0.7, 0.8, 0.9), measure precision.
3. Set auto-approve at the threshold where precision >= your target (e.g., 95%).
4. Set reject at the threshold where recall is unacceptably low (e.g., < 60%).
5. Everything in between goes to human review.

Re-calibrate monthly or after any model update.

### Feedback Loops

User corrections are the highest-quality training signal you will ever get.

- **Explicit feedback**: Thumbs up/down, "this is wrong" button, correction interface.
- **Implicit feedback**: Did the user edit the AI output? Did they use the suggestion? Did they undo it?
- **Closing the loop**: Periodically retrain or update prompts based on collected feedback. Track feedback volume — a sudden spike in "wrong" signals indicates drift.

### Graceful Degradation

Every AI feature needs an answer to: "What happens when the model is unavailable?"

| Strategy | When to Use |
|---|---|
| **Cache last-known-good** | Recommendations, classifications that change slowly |
| **Fall back to rules** | When you have a simpler but functional rule-based system |
| **Show nothing** | When a wrong answer is worse than no answer (medical, legal) |
| **Queue for later** | Background processing, non-urgent tasks |
| **Degrade to manual** | Route to human operator |

Never show a loading spinner indefinitely. Set a timeout (5–15s for interactive, 60s for background) and trigger the fallback.

### The "Centaur" Model

The most effective AI features make humans better, not replace them. Design for **human + AI > either alone**:

- AI drafts, human reviews and edits (writing, code review, support responses)
- AI surfaces relevant information, human makes the decision (medical diagnosis, fraud investigation)
- AI handles volume, human handles exceptions (content moderation, application review)
- AI monitors continuously, human is alerted for anomalies (infrastructure, security)

---

## 5. AI Safety and Bias

### Bias Sources

Bias is not a single problem. It enters at every stage:

1. **Training data**: Historical data reflects historical inequities. A hiring model trained on past decisions will replicate past discrimination.
2. **Labeling**: Annotator demographics and guidelines affect labels. Three annotators from the same background will systematically miss certain edge cases.
3. **Feature selection**: Proxy variables (zip code, name, school) can encode protected attributes.
4. **Evaluation criteria**: If your test set is not representative, you will not detect bias until production.
5. **Feedback loops**: If the model is wrong for a subgroup and that subgroup stops using the feature, you lose their feedback data, and the model gets worse for them.

### Fairness Metrics

Pick the right metric for your use case (they are mutually exclusive in most cases):

- **Demographic parity**: Equal positive prediction rates across groups. Use for: marketing, recommendations.
- **Equalized odds**: Equal true positive AND false positive rates across groups. Use for: lending, hiring.
- **Calibration**: When the model says 80% confidence, it is correct 80% of the time for ALL groups. Use for: risk scoring, medical diagnosis.

### Red Teaming

Before launching any user-facing AI feature, conduct adversarial testing:

1. **Recruit diverse testers** — not just engineers. Include people from different backgrounds, skill levels, and adversarial mindsets.
2. **Test for**: Jailbreaks, prompt injection, PII extraction, hate speech generation, confidently wrong outputs, demographic bias.
3. **Document every failure** and classify severity (launch-blocking vs known limitation vs acceptable risk).
4. **Set a launch gate**: "Zero P0 red team findings unmitigated. All P1 findings documented with monitoring in place."

### Content Safety

For generative features:

- **Input filters**: Block known-harmful prompts before they reach the model.
- **Output filters**: Scan generated content for harmful material before showing to users.
- **Rate limiting**: Prevent abuse by throttling unusual usage patterns.
- **Monitoring**: Sample and review production outputs. Automated classifiers catch the obvious cases; human review catches the subtle ones.

### Transparency

- Disclose AI involvement when the output could be mistaken for human work.
- Provide a way for users to report AI errors.
- Document known limitations publicly, not just internally.
- For high-stakes decisions, provide the reasoning or evidence the model used.

---

## 6. AI UX Patterns

### Confidence Indicators

**Show confidence when:**
- The user is an expert who can interpret it (data analysts, doctors, developers)
- The feature is in a learning phase and you want to set expectations
- Decisions have high stakes and the user needs to calibrate trust

**Hide confidence when:**
- The user is not technical and numbers would cause confusion
- Confidence is not well-calibrated (showing "95% confident" when true accuracy is 70% is worse than showing nothing)
- The feature should feel seamless (autocomplete, spell check)

### Explanation and Attribution

- **RAG features**: Always cite sources. Link to the original document. Let users verify.
- **Classification features**: Show the top contributing factors ("flagged because: unusual amount, new recipient, foreign IP").
- **Generation features**: Distinguish AI-generated content from human-written content. Use visual cues (different background, label, icon).

### User Correction Mechanisms

Every AI output should have a correction path:

- **Thumbs up/down**: Minimum viable feedback. Low friction, low information.
- **Edit-in-place**: User modifies the AI output directly. Captures exactly what was wrong.
- **"This is wrong" + category**: "Incorrect fact," "missing information," "wrong tone," "offensive content."
- **Ignore**: Track when users see but do not use AI suggestions. This is implicit negative feedback.

### Progressive Disclosure

1. Show the AI result (one line, one label, one suggestion).
2. On click/tap, show supporting evidence or reasoning.
3. On further interaction, show alternative results, confidence, or raw data.

Do not dump the full model output on the user. Surface the answer first, the evidence second.

### Setting Expectations

- Use "AI-generated" or "AI-suggested" labels on all AI outputs in v1. Remove them only after the feature has earned user trust (measured by low correction rates over 90+ days).
- Include accuracy disclaimers for high-stakes features: "This suggestion is for informational purposes. Please verify before acting."
- Never claim the AI is "always right" or "never wrong" in any user-facing copy.

### The Uncanny Valley of AI Accuracy

At 80% accuracy, users know to double-check everything. They treat the AI as a draft or starting point. This is a healthy interaction pattern.

At 95% accuracy, users start trusting the AI completely. The 5% error rate becomes invisible — users stop checking, and the errors that slip through cause real damage (because nobody caught them).

**This means 95% accuracy can be MORE dangerous than 80% accuracy for certain use cases.** The countermeasure: design the UX so that even at high accuracy, the user still engages with the output (e.g., require a confirmation click, highlight the least-confident parts, ask a verification question).

---

## 7. AI Product Metrics

### Model Metrics vs Product Metrics

Model accuracy is necessary but not sufficient. A model with 98% accuracy that takes 10 seconds to respond will be abandoned by users.

| Model Metric | Corresponding Product Metric |
|---|---|
| Accuracy / F1 | User correction rate, escalation rate |
| Latency (p50, p99) | Time-to-value, task completion time |
| Token usage | Cost per user per month |
| Hallucination rate | Trust score (survey), support tickets about wrong answers |
| Bias metrics | Demographic usage parity, satisfaction parity |

**Track both.** A model improvement that increases F1 by 2% but doubles latency is probably a net negative for the product.

### Online vs Offline Evaluation

- **Offline (lab)**: Run on holdout set. Fast, repeatable, cheap. But does not capture real-world distribution, user behavior, or system effects.
- **Online (production)**: A/B test with real users. Captures everything offline misses. But slower, more expensive, and confounded by external factors.

**Launch sequence**: Offline eval to gate launch (must pass minimum thresholds) → staged rollout with online metrics → full launch.

### A/B Testing AI Features

AI A/B tests have unique challenges:

- **Non-determinism**: Same input, different output. Use fixed seeds or treat variance as a feature (measure it).
- **Cold start**: Personalized models need data from the user. New users in the treatment group may have a worse experience initially.
- **Novelty effect**: Users engage more with new AI features simply because they are new. Wait 2+ weeks before reading results.
- **Interference**: If users in the control group hear about the AI feature from treatment users, the control is contaminated. Use cluster randomization if this is a risk.

### Measuring AI ROI

| Metric | How to Measure |
|---|---|
| **Time saved** | Task completion time: control vs treatment |
| **Error reduction** | Manual review catch rate, customer complaints, rework rate |
| **User satisfaction** | NPS/CSAT delta, feature adoption rate, retention impact |
| **Cost per query** | Total infrastructure cost / total queries (include all components: retrieval, generation, caching, monitoring) |
| **Cost avoided** | Headcount that would be needed without the feature (be honest — this number is usually lower than the pitch deck claims) |

### Drift Detection

Models degrade. The world changes, user behavior shifts, data distributions evolve.

**Monitor these signals:**
- **Prediction distribution shift**: If the model suddenly classifies 40% of inputs as category A when the historical rate is 25%, something changed.
- **Confidence distribution shift**: If average confidence drops, the model is seeing unfamiliar inputs.
- **Feedback signal shift**: If user correction rate increases, the model is getting worse.
- **Input distribution shift**: If the embedding distribution of production inputs diverges from training data (measured by KL divergence or similar), retrain.

**Set alerts, not dashboards.** A dashboard that nobody checks is worthless. Alert when any metric crosses a threshold.

---

## Anti-Patterns

### 1. "Let's Add AI To It"
Adding AI without a clear user problem to solve. The question is never "can we use AI here?" — it is "what user problem are we solving, and is AI the best tool for it?" If you cannot articulate the user problem in one sentence without the word "AI," you do not have a product — you have a technology demo.

### 2. Shipping Without Fallback
Every AI feature will fail. Network outages, model errors, adversarial inputs, rate limits. If your feature has no fallback behavior, your users have no recourse. Define the fallback before writing any model code.

### 3. Accuracy as the Only Metric
A model with 99% accuracy, 8-second latency, $0.50 per request, and demographic bias is not a good model. Evaluate accuracy AND latency AND cost AND fairness AND user satisfaction. Optimize for the portfolio, not a single number.

### 4. Fine-Tuning When Prompt Engineering Would Suffice
Fine-tuning is expensive, slow, and hard to iterate. If you have not exhausted prompt engineering (system prompts, few-shot examples, chain-of-thought, structured output), you are not ready to fine-tune. The bar for fine-tuning should be: "We have tried prompt engineering, it works but costs too much at our volume or is not consistent enough for our use case."

### 5. Not Monitoring Post-Launch
The model that passed evaluation last month may be failing today. User behavior changes, data distributions shift, the world moves on. If you are not monitoring model performance weekly, you are flying blind. Set up automated alerts on key metrics from day one.

### 6. Treating AI as "Set and Forget"
AI features require ongoing investment: retraining, prompt iteration, evaluation set expansion, drift monitoring, edge case handling, cost optimization. Budget for this. If your roadmap has "Launch AI Feature" as a single line item with no follow-up work, the feature will degrade within months.

### 7. Ignoring the Cost Curve
LLM costs drop roughly 10x every 18 months (as of 2026). A feature that is too expensive today may be viable in six months. Conversely, a feature that is affordable today at 1K requests/day may be ruinous at 100K requests/day. Model your cost at 10x and 100x current volume before committing.

### 8. Skipping Human Evaluation
Automated metrics (BLEU, ROUGE, F1) are proxies. They correlate with quality but do not measure it. If you have not had humans evaluate your AI feature's output, you do not know if it is good. Budget for human evaluation at launch and quarterly thereafter.

---

## Quick Reference: AI Feature Launch Checklist

- [ ] User problem clearly defined (without the word "AI")
- [ ] AI vs rule-based vs manual decision documented with evidence
- [ ] Model selection criteria specified (accuracy, latency, cost, privacy)
- [ ] Evaluation set built (minimum 200 examples, stratified)
- [ ] Offline evaluation passes minimum thresholds
- [ ] Edge case taxonomy documented with mitigations
- [ ] Confidence thresholds calibrated on evaluation set
- [ ] Fallback behavior implemented and tested
- [ ] Human-in-the-loop flow designed for low-confidence outputs
- [ ] Bias evaluation completed across relevant demographic groups
- [ ] Red team testing completed, all P0 findings mitigated
- [ ] Privacy review completed (PII handling, data retention, consent)
- [ ] Cost model validated at 10x projected volume
- [ ] Monitoring and alerting configured (drift, feedback, latency, cost)
- [ ] AI disclosure / transparency copy reviewed
- [ ] User correction mechanism implemented
- [ ] Post-launch review scheduled (30 days)
