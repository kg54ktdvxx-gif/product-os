---
name: experiment-design
description: "Design, size, and analyze A/B tests and experiments with statistical rigor. Covers frequentist and Bayesian approaches, sample size calculation with actual formulas, sequential testing, pre-registration templates, guardrail metrics, and post-experiment analysis checklists. Includes common experiment mistakes and decision frameworks."
---

# Experiment Design & A/B Test Analysis

Design experiments that produce trustworthy results. Analyze A/B tests with statistical rigor. Make ship/extend/kill decisions with explicit reasoning and stated assumptions.

## When to Experiment (and When Not To)

### Experiment When:
- You have a clear, measurable hypothesis
- The change is reversible
- You have enough traffic to reach statistical significance in a reasonable time
- The downside risk of the variant is acceptable
- You genuinely don't know which option is better

### Don't Experiment When:
- The change is obviously correct (fixing a broken flow, legal compliance)
- You don't have enough traffic (< 1,000 users/week in the target flow)
- The metric you care about takes months to observe (e.g., annual renewal)
- The change affects a tiny population (< 100 users) — just ship and monitor
- You're testing cosmetic changes that won't move business metrics

## Hypothesis Formulation

A good hypothesis is **falsifiable**, **specific**, and **connected to a metric**.

### Template
```
We believe that [change]
for [user segment]
will cause [expected effect on primary metric]
because [reasoning based on evidence].

We will know this is true when we observe [specific metric change]
within [timeframe].

We will know this is false when we observe [specific metric NOT changing or degrading]
after [minimum observation period].
```

### Example
```
We believe that adding a progress bar to the onboarding flow
for new free-tier users
will increase onboarding completion rate by at least 10% relative
because user research showed 40% of drop-offs cited "not knowing how many steps remain."

We will know this is true when onboarding completion rate increases from 62% to >= 68.2%
within 3 weeks (at current signup volume).

We will know this is false when completion rate shows < 5% relative improvement
after 4 weeks of testing with >= 4,000 users per variant.
```

## Sample Size Calculation

### The Formula (Binary/Proportion Metrics)

For comparing two proportions (e.g., conversion rates):

```
n = (Z_{alpha/2} + Z_{beta})^2 * (p1*(1-p1) + p2*(1-p2)) / (p1 - p2)^2
```

Where:
- `n` = required sample size **per group**
- `Z_{alpha/2}` = z-score for significance level (1.96 for alpha=0.05 two-tailed)
- `Z_{beta}` = z-score for power (0.84 for 80% power, 1.28 for 90% power)
- `p1` = baseline conversion rate (control)
- `p2` = expected conversion rate (variant) = p1 * (1 + MDE)
- `MDE` = minimum detectable effect (relative)

### The Formula (Continuous Metrics)

For comparing two means (e.g., revenue per user, session duration):

```
n = (Z_{alpha/2} + Z_{beta})^2 * 2 * sigma^2 / delta^2
```

Where:
- `sigma` = standard deviation of the metric
- `delta` = minimum detectable absolute difference in means

**Simplified rule of thumb** (80% power, alpha=0.05):
```
n per group = 16 * sigma^2 / delta^2
```

### Worked Example

**Scenario**: Current checkout conversion is 4.2%. We want to detect a 10% relative improvement (to 4.62%). Alpha = 0.05 (two-tailed), Power = 80%.

```
p1 = 0.042 (baseline)
p2 = 0.042 * 1.10 = 0.0462 (target)
Z_{alpha/2} = 1.96
Z_{beta} = 0.84

n = (1.96 + 0.84)^2 * (0.042*0.958 + 0.0462*0.9538) / (0.042 - 0.0462)^2
n = (2.80)^2 * (0.04024 + 0.04407) / (0.0042)^2
n = 7.84 * 0.08431 / 0.00001764
n = 0.6610 / 0.00001764
n = 37,472 per group
```

**Total sample needed**: ~75,000 (37,500 per group).

At 1,000 users/day through the flow with a 50/50 split: ~75 days. That's too long. Options:
1. Accept a larger MDE (20% relative -> ~9,400 per group -> ~19 days)
2. Increase power to detect the 10% effect by running longer
3. Question whether this test is worth running at this traffic level

### Quick Reference Lookup Table

Sample sizes per group for common scenarios (alpha=0.05 two-tailed, 80% power):

| Baseline Rate | 5% Relative MDE | 10% Relative MDE | 20% Relative MDE | 50% Relative MDE |
|---------------|-----------------|-------------------|-------------------|-------------------|
| 1% | 3,150,000 | 788,000 | 197,000 | 31,600 |
| 2% | 1,545,000 | 386,000 | 96,600 | 15,500 |
| 5% | 590,000 | 147,600 | 36,900 | 5,920 |
| 10% | 277,400 | 69,400 | 17,400 | 2,780 |
| 20% | 123,400 | 30,900 | 7,720 | 1,240 |
| 50% | 30,700 | 7,680 | 1,920 | 308 |

**Reading the table**: If your baseline conversion is 5% and you want to detect a 10% relative improvement (from 5.0% to 5.5%), you need ~147,600 users per group (~295,200 total).

### Duration Calculation

```
Duration (days) = (2 * n_per_group) / (daily_eligible_users * allocation_percentage)
```

**Minimum duration**: Always run for at least 1-2 full business cycles (7-14 days) regardless of sample size, to capture day-of-week effects.

**Maximum recommended duration**: 90 days. Beyond this, external factors (seasonality, product changes, user population shifts) make results unreliable.

## Frequentist Analysis

### The Standard Approach (Z-Test for Proportions)

```
z = (p_variant - p_control) / sqrt(p_pooled * (1 - p_pooled) * (1/n_control + 1/n_variant))

where p_pooled = (x_control + x_variant) / (n_control + n_variant)
```

**Interpret**:
- Calculate the p-value from the z-statistic
- If p < alpha (typically 0.05): reject the null hypothesis (there IS a statistically significant difference)
- If p >= alpha: fail to reject the null (we cannot conclude there's a difference)
- Always report the confidence interval, not just the p-value

### Confidence Interval for the Difference

```
CI = (p_variant - p_control) +/- Z_{alpha/2} * sqrt(p_variant*(1-p_variant)/n_variant + p_control*(1-p_control)/n_control)
```

**How to read it**: "We are 95% confident the true difference in conversion rates is between [lower bound] and [upper bound]."

- If the CI excludes 0: statistically significant
- If the CI is entirely positive: variant is better
- If the CI is entirely negative: control is better
- Width of CI tells you precision — a wide CI means you need more data

### Practical vs Statistical Significance

A result can be:
- **Statistically significant but not practically significant**: p=0.03, but the lift is +0.1%. The effect is real but too small to matter.
- **Practically significant but not statistically significant**: The lift is +8%, but p=0.12 because the sample is too small. Extend the test.
- **Both**: The ideal outcome. Ship with confidence.
- **Neither**: Stop the test. The effect, if it exists, is too small to detect or matter.

## Bayesian Analysis

### When to Use Bayesian vs Frequentist

| Situation | Recommended Approach | Why |
|-----------|---------------------|-----|
| Standard A/B test with fixed sample | Frequentist | Well-understood, widely accepted |
| Continuous monitoring / early stopping | Bayesian | No peeking problem |
| Multiple variants (A/B/C/D) | Bayesian | Better handling of multiplicity |
| Low traffic / small sample | Bayesian | Can incorporate prior information |
| Stakeholders want "probability of being better" | Bayesian | More intuitive interpretation |
| Regulatory / high-stakes decisions | Frequentist | More established in formal contexts |

### Bayesian Key Concepts

**Prior**: Your belief about the conversion rate before seeing data. Use a Beta(1,1) prior (uniform) if you have no prior knowledge. Use Beta(alpha, beta) fitted to historical data if you do.

**Posterior**: Updated belief after seeing data. For conversion rates with a Beta prior:
```
Posterior = Beta(alpha + successes, beta + failures)
```

**Probability of Being Better**:
```
P(variant > control) = proportion of posterior samples where variant > control
```

If P(variant > control) > 0.95, ship it. If P < 0.05, revert. Between 0.05 and 0.95, need more data.

**Expected Loss**: The expected cost of choosing the wrong variant. If expected loss < your "threshold of caring," ship the leading variant regardless of certainty.

**Credible Interval**: The Bayesian equivalent of a confidence interval. "There is a 95% probability the true conversion rate is between [lower] and [upper]." (Note: this is what people THINK confidence intervals mean, but only credible intervals actually mean this.)

## Sequential Testing

### The Peeking Problem

In frequentist testing, checking results multiple times inflates the false positive rate:
- Check once at the end: 5% false positive rate (as designed)
- Check every day for 30 days: up to 25-30% false positive rate

**You are not just "looking at the data." Every peek is a statistical test.**

### Solutions to the Peeking Problem

#### 1. Group Sequential Boundaries (O'Brien-Fleming)
Pre-specify interim analysis points (e.g., at 25%, 50%, 75%, 100% of target sample). Use adjusted significance thresholds at each look:

| Information Fraction | O'Brien-Fleming Boundary (alpha per look) |
|---------------------|-------------------------------------------|
| 25% | 0.0001 (essentially impossible to stop early) |
| 50% | 0.0054 |
| 75% | 0.0184 |
| 100% | 0.0412 |

Overall alpha is preserved at 0.05 across all looks.

#### 2. Always-Valid P-Values (mSPRT)
Use a mixture sequential probability ratio test. These p-values are valid at ANY stopping time — you can check as often as you want.

Trade-off: mSPRT requires ~30% more sample than fixed-horizon tests for the same power.

#### 3. Bayesian (No Peeking Problem)
Bayesian analysis doesn't have a peeking problem because there's no null hypothesis to falsely reject. You can check posterior probabilities as often as you want. The cost is that Bayesian analysis requires specifying a prior.

## Pre-Registration Template

Complete this BEFORE launching the experiment. This prevents post-hoc rationalization.

```markdown
## Experiment Pre-Registration

### Experiment Name: [Name]
### Date: [Date]
### Owner: [PM Name]

### 1. Hypothesis
[State the hypothesis using the template above]

### 2. Variants
- **Control**: [Current experience — describe precisely]
- **Variant A**: [Changed experience — describe precisely]
- **Variant B** (if applicable): [Second variant]

### 3. Primary Metric
- **Name**: [Precise operational definition]
- **Baseline**: [Current value with date range]
- **MDE**: [Minimum detectable effect, relative %]
- **Direction**: [One-tailed (expect improvement only) or two-tailed]

### 4. Secondary Metrics
| Metric | Baseline | Expected Direction |
|--------|----------|-------------------|
| [Name] | [Value]  | [Up/Down/Neutral] |

### 5. Guardrail Metrics
| Metric | Acceptable Range | Rationale |
|--------|-----------------|-----------|
| [Name] | [e.g., < 5% degradation] | [Why this matters] |

### 6. Sample Size & Duration
- **Required sample per group**: [N] (alpha=[X], power=[X]%, MDE=[X]%)
- **Daily eligible users**: [N]
- **Traffic allocation**: [X]% per variant
- **Expected duration**: [N days]
- **Minimum duration**: [N days] (to capture weekly cycles)
- **Maximum duration**: [N days]

### 7. Randomization
- **Unit**: [User / Session / Device / Organization]
- **Stratification**: [None / By plan tier / By country / etc.]
- **Exclusions**: [Internal users, bots, users in other experiments]

### 8. Decision Framework
| Outcome | Action |
|---------|--------|
| p < 0.05 AND guardrails hold | **Ship** — roll out to 100% |
| p < 0.05 BUT guardrail degrades > threshold | **Investigate** — understand trade-off, present to leadership |
| p > 0.05, positive trend, < 75% of target sample | **Extend** — continue to full sample |
| p > 0.05 at full sample | **Kill** — revert to control, document learnings |
| p < 0.05, NEGATIVE direction | **Revert immediately** — analyze what went wrong |

### 9. Analysis Plan
- **Primary analysis**: [Frequentist z-test / Bayesian / etc.]
- **Segment analysis**: [Segments to check: new vs returning, mobile vs desktop, plan tier]
- **Pre-specified interactions**: [Any known interactions with other experiments]
```

## Common Experiment Mistakes

### 1. Peeking Without Correction
**The mistake**: Checking results daily and stopping when p < 0.05.
**Why it's wrong**: At 5% daily check rate over 30 days, your true false positive rate is ~25%.
**The fix**: Use sequential testing boundaries, Bayesian analysis, or commit to a fixed sample size and don't look until you reach it.

### 2. Underpowered Tests
**The mistake**: Running a test with 500 users per group to detect a 3% relative lift in a 2% baseline metric.
**Why it's wrong**: You'd need ~1.5M per group. With 500, you have <1% chance of detecting a real effect. "No significant result" doesn't mean "no effect" — it means your test was too small to see it.
**The fix**: Run the sample size calculation BEFORE launching. If you can't get enough traffic, either accept a larger MDE, find a more sensitive metric, or don't run the test.

### 3. Novelty Effects
**The mistake**: Shipping a variant after a 1-week test showed +15% engagement.
**Why it's wrong**: Users interact with new things more because they're new. The "Hawthorne effect" fades after 2-4 weeks.
**The fix**: Run for at least 2-4 weeks. Check if the lift is decreasing over time (plot daily lift). For major UX changes, consider a holdback group you can measure after 30+ days.

### 4. Sample Ratio Mismatch (SRM)
**The mistake**: Ignoring that your 50/50 split actually produced 52/48.
**Why it's wrong**: SRM indicates a systematic bias in assignment. Your results are contaminated — the difference might be caused by the bias, not the treatment.
**The fix**: Always check the chi-squared test for SRM before analyzing results. If `chi2 > 3.84` (p < 0.05) for a 2-variant test, your experiment has a fundamental problem. Stop and fix the randomization.

**SRM Check**:
```
Expected: n_control = n_variant = N/2
chi2 = (n_control - N/2)^2 / (N/2) + (n_variant - N/2)^2 / (N/2)
If chi2 > 3.84: SRM detected, results are untrustworthy
```

### 5. Interaction Effects Between Simultaneous Experiments
**The mistake**: Running experiment A (new checkout flow) and experiment B (new pricing display) on overlapping populations without accounting for interactions.
**Why it's wrong**: If A improves conversion by 5% and B improves conversion by 3%, the combined effect might be 2% (negative interaction) or 10% (positive interaction). You can't know unless you measure.
**The fix**: Either exclude users in one experiment from the other (reduces traffic), or run a factorial design (A x B → 4 groups: control-control, A-control, control-B, A-B) and test for interaction.

### 6. Wrong Randomization Unit
**The mistake**: Randomizing by session for a test that affects the user experience across sessions (e.g., new navigation).
**Why it's wrong**: A user might see the variant in one session and control in the next. This contaminates both groups.
**The fix**: Match the randomization unit to the scope of the change. User-level for persistent UX changes. Session-level only for within-session changes. Organization-level for B2B features that affect teams.

### 7. Multiple Comparisons Without Correction
**The mistake**: Testing 10 metrics and declaring victory when one of them is significant at p < 0.05.
**Why it's wrong**: With 10 metrics at alpha=0.05, there's a 40% chance at least one is significant by chance.
**The fix**: Apply Bonferroni correction (alpha/n = 0.05/10 = 0.005 per metric) or designate ONE primary metric before the test starts. Secondary metrics are exploratory — they generate hypotheses for the next test.

### 8. Survivorship Bias in Metric Calculation
**The mistake**: Calculating "average revenue per user" only for users who made a purchase.
**Why it's wrong**: If the variant causes fewer users to purchase but those who do spend more, "revenue per purchaser" goes up while total revenue goes down.
**The fix**: Always calculate metrics over the full randomized population, not just the subset who performed the action.

## Post-Experiment Analysis Checklist

Run this checklist after every experiment, before making a ship/kill decision:

### Validity Checks
- [ ] **SRM check**: Is the sample ratio within expected bounds? (chi-squared test)
- [ ] **Duration check**: Did the test run for at least 1-2 full business cycles?
- [ ] **Sample size check**: Did we reach the pre-registered sample size?
- [ ] **External events**: Were there any confounding events during the test? (outages, marketing campaigns, holidays, press coverage)

### Primary Analysis
- [ ] **Primary metric**: What is the point estimate, confidence interval, and p-value?
- [ ] **Practical significance**: Is the effect large enough to matter for the business?
- [ ] **Guardrail check**: Did any guardrail metric degrade beyond the pre-stated threshold?

### Segment Analysis
- [ ] **New vs returning users**: Did the treatment affect new and returning users differently?
- [ ] **Mobile vs desktop**: Platform-specific effects?
- [ ] **Plan tier / user segment**: Did high-value users respond differently than low-value users?
- [ ] **Geographic**: Any regional differences?

Note: Segment analysis is EXPLORATORY. A significant segment result generates a hypothesis for the next test — it does not prove the treatment works differently for that segment (multiple comparisons problem).

### Long-Term Considerations
- [ ] **Novelty effect check**: Is the daily lift stable, increasing, or decreasing over the test period?
- [ ] **Learning effects**: Could users get better at using the variant over time (increasing lift)?
- [ ] **Network effects**: Could widespread rollout change the effect? (e.g., a referral feature tested on 5% of users won't show its full network effect)
- [ ] **Downstream metrics**: Will this change affect metrics that take weeks or months to observe? (retention, LTV, churn)

### Documentation
- [ ] **Results documented**: In metrics.md or experiment log with full methodology
- [ ] **Decision recorded**: Ship / Kill / Extend, with reasoning
- [ ] **Learnings captured**: What did we learn about user behavior, even if we don't ship?
- [ ] **Follow-up experiments**: What new hypotheses did this test generate?

## A/B Test Results Template

```markdown
## A/B Test Results: [Test Name]

**Hypothesis**: [What we expected]
**Duration**: [X days] | **Sample**: [N control / M variant]
**Pre-registration**: [Link to pre-registration document]

### Results Summary
| Metric | Control | Variant | Absolute Diff | Relative Lift | 95% CI | p-value | Sig? |
|--------|---------|---------|---------------|---------------|--------|---------|------|
| [Primary] | X% | Y% | +Z pp | +W% | [L%, U%] | 0.0XX | Y/N |
| [Secondary] | ... | ... | ... | ... | ... | ... | ... |
| [Guardrail] | ... | ... | ... | ... | ... | ... | ... |

### Validity Checks
- **SRM**: [Pass/Fail] (chi2=[X], p=[Y])
- **Power**: [Sufficiently powered / Underpowered] ([N] needed, [M] observed)
- **Duration**: [X days] ([Sufficient / Insufficient])

### Decision: [SHIP / EXTEND / KILL / INVESTIGATE]

**Reasoning**: [Why this decision, connecting statistical results to business impact]

### Business Impact Estimate
If shipped to 100%:
- [Primary metric]: expected [change] per [period]
- Revenue impact: [estimate with confidence interval]

### Learnings
1. [What we learned about user behavior]
2. [Surprising findings from segment analysis]

### Follow-Up
- [ ] [Next experiment to run]
- [ ] [Monitoring plan post-ship]
```

## References

- [A/B Testing 101 + Examples](https://www.productcompass.pm/p/ab-testing-101-for-pms)
- [Testing Product Ideas: The Ultimate Validation Experiments Library](https://www.productcompass.pm/p/the-ultimate-experiments-library)
- [Are You Tracking the Right Metrics?](https://www.productcompass.pm/p/are-you-tracking-the-right-metrics)
- Kohavi, Tang, Xu — *Trustworthy Online Controlled Experiments* (the bible of A/B testing)
- Georgiev — *Statistical Methods in Online A/B Testing*
