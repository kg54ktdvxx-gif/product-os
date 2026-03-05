---
name: launch-readiness
description: "Launch readiness checklist across 8 dimensions (Product, Marketing, Sales, Support, Engineering, Legal, Analytics, Operations), launch day playbook, post-launch review templates, and guidance on launch-and-iterate vs delay-until-ready decisions."
---

# Launch Readiness

## Overview

Launch readiness is the systematic verification that your product, team, and infrastructure are prepared for the moment customers start using what you built. It is the difference between a launch that builds momentum and a launch that creates a support crisis.

This skill covers three phases: the pre-launch checklist (are you ready?), the launch day playbook (what happens hour-by-hour?), and the post-launch review (did it work, and what do you do next?).

## When to Use

- 2-4 weeks before a planned product launch
- Before a major feature release to existing customers
- Before opening a product to a new market segment
- When deciding whether to launch now or delay
- After a botched launch, to prevent recurrence

---

## Part 1: The 8-Dimension Launch Readiness Checklist

Each dimension is scored as Ready (all must-haves met), At Risk (some must-haves incomplete), or Not Ready (critical must-haves missing). A launch with ANY dimension at "Not Ready" should be delayed. A launch with "At Risk" dimensions can proceed with mitigation plans.

### Dimension 1: Product

The product must deliver the core value promise reliably for the target segment.

| Item | Must Have | Good to Have | Status |
|------|----------|-------------|--------|
| Core user flow works end-to-end | YES | - | [ ] |
| Performance meets SLA (page load < 2s, API < 500ms) | YES | - | [ ] |
| Works on target browsers/devices/OS versions | YES | - | [ ] |
| Data migration / import path tested (if replacing existing tool) | YES (if applicable) | - | [ ] |
| Known bugs documented with severity and workarounds | - | YES | [ ] |
| Edge cases handled gracefully (error messages, empty states) | - | YES | [ ] |
| Accessibility basics (keyboard nav, screen reader, contrast) | - | YES (MUST for enterprise) | [ ] |
| Onboarding flow tested with 5+ external users | YES | - | [ ] |
| Free trial / freemium experience is complete | YES (if PLG) | - | [ ] |

**Common oversight**: Testing only the happy path. Run through the product as a hostile user: wrong inputs, back button, expired session, slow connection, mobile browser.

### Dimension 2: Marketing

Marketing assets must be ready to drive awareness and convert interest into signups.

| Item | Must Have | Good to Have | Status |
|------|----------|-------------|--------|
| Positioning statement finalized and approved | YES | - | [ ] |
| Website / landing page live with clear CTA | YES | - | [ ] |
| Launch blog post / announcement drafted | YES | - | [ ] |
| Social media posts scheduled (LinkedIn, X/Twitter, relevant platforms) | - | YES | [ ] |
| Email to existing customers / waitlist drafted | YES (if applicable) | - | [ ] |
| Press / analyst briefings scheduled | - | YES (for major launches) | [ ] |
| Product Hunt / launch platform submission prepared | - | YES (for PLG products) | [ ] |
| Case study or beta customer quote available | - | YES | [ ] |
| SEO: target pages indexed, meta tags, schema markup | - | YES | [ ] |
| Paid campaigns configured and approved | - | YES (if paid is a launch channel) | [ ] |

**Common oversight**: Landing page CTA goes to a signup flow that is not ready. Test the FULL path from ad/post to signup to activation.

### Dimension 3: Sales

Sales team must be equipped to handle inbound interest and proactive outreach.

| Item | Must Have | Good to Have | Status |
|------|----------|-------------|--------|
| Pricing finalized and published (or prepared for sales quotes) | YES | - | [ ] |
| Sales team trained on product (demo, value prop, ICP) | YES | - | [ ] |
| Competitive battlecards available for top 3 competitors | YES | - | [ ] |
| Demo environment stable and populated with realistic data | YES | - | [ ] |
| CRM updated with new product/SKU, lead routing configured | YES | - | [ ] |
| Sales deck / one-pager available | - | YES | [ ] |
| Objection handling guide distributed | - | YES | [ ] |
| Quota / compensation plan updated for new product | - | YES | [ ] |

**Common oversight**: Sales team has not actually USED the product. Every rep should complete the onboarding flow themselves before launch.

### Dimension 4: Support

Support team must be prepared for the surge of questions, bug reports, and confusion that follows every launch.

| Item | Must Have | Good to Have | Status |
|------|----------|-------------|--------|
| Documentation / help center articles published | YES | - | [ ] |
| FAQ covering top 10 anticipated questions | YES | - | [ ] |
| Support team trained on product and known issues | YES | - | [ ] |
| Escalation path defined (support → engineering → on-call) | YES | - | [ ] |
| Support ticketing system configured for new product | YES | - | [ ] |
| Canned responses for common scenarios drafted | - | YES | [ ] |
| Self-serve troubleshooting guides available | - | YES | [ ] |
| Support capacity plan for launch week (extra staff?) | - | YES | [ ] |

**Common oversight**: Documentation written by engineers, not tested by non-technical users. Have someone outside the team follow the docs to complete a task.

### Dimension 5: Engineering

Infrastructure must be ready for launch traffic, and the team must be prepared to respond to incidents.

| Item | Must Have | Good to Have | Status |
|------|----------|-------------|--------|
| Load testing completed at 2-3x expected launch traffic | YES | - | [ ] |
| Monitoring and alerting configured (uptime, error rate, latency) | YES | - | [ ] |
| Rollback plan documented and tested | YES | - | [ ] |
| On-call rotation set for launch week | YES | - | [ ] |
| Feature flags in place for gradual rollout | - | YES | [ ] |
| Database backups verified and restore tested | YES | - | [ ] |
| CDN / caching configured for static assets | - | YES | [ ] |
| Rate limiting in place to prevent abuse | - | YES | [ ] |
| Incident communication plan (status page, internal Slack channel) | YES | - | [ ] |

**Common oversight**: Rollback plan exists but has never been tested. Run a rollback drill before launch.

### Dimension 6: Legal

Legal requirements must be met before customers start using the product and providing data.

| Item | Must Have | Good to Have | Status |
|------|----------|-------------|--------|
| Terms of Service published and linked from signup flow | YES | - | [ ] |
| Privacy Policy updated to cover new product/data usage | YES | - | [ ] |
| Cookie consent / tracking opt-in compliant with GDPR, CCPA | YES | - | [ ] |
| Data Processing Agreement available (for B2B) | YES (if B2B) | - | [ ] |
| IP / trademark search complete for product name | YES | - | [ ] |
| Export compliance verified (if selling internationally) | - | YES | [ ] |
| Accessibility compliance (ADA, WCAG) assessed | - | YES | [ ] |

**Common oversight**: Privacy policy references the old product/data practices but does not cover new data collection in the launched feature.

### Dimension 7: Analytics

You must be able to measure whether the launch succeeded. If you cannot measure it, you cannot learn from it.

| Item | Must Have | Good to Have | Status |
|------|----------|-------------|--------|
| Success metrics defined with specific targets | YES | - | [ ] |
| Tracking instrumented for signup, activation, and conversion events | YES | - | [ ] |
| Attribution tracking configured (UTM, referral source) | YES | - | [ ] |
| Dashboard live showing real-time launch metrics | YES | - | [ ] |
| A/B testing infrastructure ready (if running experiments) | - | YES | [ ] |
| Funnel visualization configured (signup → activation → conversion) | - | YES | [ ] |
| Cohort analysis capability for retention tracking | - | YES | [ ] |
| Alerting on anomalous metrics (crash rate, error rate) | YES | - | [ ] |

**Common oversight**: Tracking is instrumented in staging but not verified in production. Always verify events are firing correctly in the production environment before launch.

### Dimension 8: Operations

Back-office processes must work for the first paying customer.

| Item | Must Have | Good to Have | Status |
|------|----------|-------------|--------|
| Billing system configured and tested (create, upgrade, cancel) | YES (if paid) | - | [ ] |
| Provisioning flow tested (signup → account creation → first use) | YES | - | [ ] |
| Invoice generation and receipt emails working | YES (if paid) | - | [ ] |
| Cancellation and refund process defined | YES (if paid) | - | [ ] |
| Onboarding email sequence configured and tested | - | YES | [ ] |
| Welcome email sent on signup with clear next steps | YES | - | [ ] |
| Account deletion / data export available (GDPR right to erasure) | YES (for EU customers) | - | [ ] |

**Common oversight**: Testing the purchase flow but not the cancellation flow. A customer who cannot cancel will file a chargeback and leave a negative review.

---

## Part 2: Launch Day Playbook

### Pre-Launch (T-24 hours)

| Time | Action | Owner |
|------|--------|-------|
| T-24h | Final go/no-go meeting with all dimension owners | Launch DRI |
| T-24h | Verify all "Must Have" items are green | Each dimension owner |
| T-12h | Pre-stage marketing content (blog post, social, emails in draft) | Marketing |
| T-12h | Engineering on-call confirmed and monitoring dashboards open | Engineering |
| T-6h | Final smoke test of signup → activation → (purchase) flow in production | Product / QA |
| T-2h | War room channel created (Slack, Teams) with all stakeholders | Launch DRI |
| T-1h | Status page verified working | Engineering |

### Launch Hour

| Time | Action | Owner |
|------|--------|-------|
| T+0 | Publish blog post / press release | Marketing |
| T+0 | Send launch email to waitlist / customers | Marketing |
| T+5min | Post to social media channels | Marketing |
| T+5min | Submit to Product Hunt / HackerNews (if planned) | Growth |
| T+15min | First metrics check: site up, signups flowing, no errors spiking | Engineering |
| T+30min | First support queue check: any unexpected issues? | Support |
| T+1h | Metrics snapshot shared in war room | Analytics |
| T+2h | Second metrics review: activation rate, error rate, support volume | Product |

### Launch Day (T+2h to T+24h)

| Cadence | Action | Owner |
|---------|--------|-------|
| Every 2 hours | Metrics update in war room channel | Analytics |
| Every 2 hours | Support queue review — emerging patterns? | Support |
| As needed | Bug triage — severity assessment, hotfix vs next release | Engineering |
| T+8h | End-of-day summary: signups, activation, issues, sentiment | Launch DRI |
| T+24h | Day 1 review meeting | All |

### Rollback Triggers

Define these BEFORE launch. If any trigger is hit, pause and assess:

| Trigger | Threshold | Action |
|---------|-----------|--------|
| Error rate | > 5% of requests for 15+ minutes | Pause marketing, investigate |
| Downtime | > 10 minutes continuous | Activate rollback plan |
| Data loss / corruption | Any confirmed instance | Immediate rollback |
| Support volume | > 3x baseline within 2 hours | Pause launch marketing, triage |
| Security incident | Any confirmed breach | Immediate rollback, incident response |
| Activation rate | < 50% of target after day 1 | Review onboarding flow, do not scale marketing |

---

## Part 3: Post-Launch Reviews

### Day 1 Review (T+24h)

| Question | Answer |
|----------|--------|
| How many signups? vs target? | |
| What is the activation rate? | |
| What are the top 3 support issues? | |
| Any critical bugs or incidents? | |
| What is the sentiment? (social, support, NPS) | |
| Are we on track to hit day 7 targets? | |
| Decision: continue, adjust, or pause? | |

### Week 1 Review (T+7 days)

| Question | Answer |
|----------|--------|
| Signups: total and daily trend (growing, flat, declining?) | |
| Activation rate: improving, stable, or declining? | |
| Day 1 and Day 7 retention: | |
| Channel attribution: which channels drove quality signups? | |
| Support: have common issues been resolved? | |
| Competitive response: any competitor reactions? | |
| What surprised us? What did we get wrong? | |
| Adjustments for week 2: | |

### Month 1 Review (T+30 days)

| Question | Answer |
|----------|--------|
| Total signups and conversion rate to paid (if applicable) | |
| Retention curve: day 1, 7, 14, 30 | |
| CAC by channel: which channels are efficient? | |
| NPS / CSAT from launch cohort | |
| Feature usage: what are users actually using vs what we expected? | |
| Revenue (if applicable): vs target | |
| Lessons learned for next launch | |
| Decision: scale, iterate, or pivot? | |

---

## Part 4: Launch-and-Iterate vs Delay-Until-Ready

This is a judgment call, but here are the decision factors:

### Launch and Iterate When:
- Core value proposition works (users who complete onboarding are retained)
- Missing features are nice-to-haves, not must-haves for the beachhead segment
- Competitive pressure — a competitor is about to launch something similar
- You have a small, forgiving beachhead (early adopters who will tolerate rough edges)
- You can ship fixes daily (no app store review cycles, no enterprise deployment windows)
- The primary risk is "we built the wrong thing" — which only real users can answer

### Delay Until Ready When:
- Core user flow has known bugs that prevent activation
- Security or data integrity issues are unresolved
- Legal requirements (privacy policy, compliance) are not met
- The target segment is NOT forgiving (enterprise buyers, regulated industries)
- A failed launch will burn the segment — you only get one chance with this audience
- Fix cycle time is slow (App Store review, enterprise release cycles)
- Support team is not trained and cannot handle launch volume

### Launch Failure Examples

**Failure: Healthcare.gov (2013)**
- What happened: Launched to 250 million potential users without load testing at scale
- Root cause: Engineering dimension failed — no load testing, no rollback plan, no gradual rollout
- Lesson: For high-stakes launches, use feature flags and gradual rollout. Never go from 0 to full traffic.

**Failure: Google Wave (2009)**
- What happened: Launched with massive hype but no clear use case or onboarding
- Root cause: Product dimension failed — users did not understand what to do after signup
- Lesson: If your activation rate in beta is below 20%, do not scale marketing. Fix activation first.

**Failure: Quibi (2020)**
- What happened: $1.75B invested, launched with massive marketing budget, shut down in 6 months
- Root cause: GTM strategy failed — no beachhead segment, no clear differentiation from YouTube/TikTok, pricing did not match value
- Lesson: Marketing spend cannot compensate for missing product-market fit. Launch small, validate, then scale.

**Success: Notion (2016-2019)**
- What happened: Launched quietly, iterated for 3 years, found PMF with small teams and power users before scaling
- What they did right: Small beachhead (power users, template creators), PLG motion, community-led growth, iterated on product before investing in marketing
- Lesson: A slow, deliberate launch that finds PMF beats a big-bang launch that does not.

---

## Output Format

When executing this skill, deliver:

1. **Readiness Assessment** — all 8 dimensions scored as Ready / At Risk / Not Ready with specific items flagged
2. **Launch Day Playbook** — hour-by-hour plan customized to the product and team
3. **Rollback Triggers** — defined thresholds and actions
4. **Post-Launch Review Schedule** — day 1, week 1, month 1 templates pre-filled with the launch's success metrics
5. **Launch / Delay Recommendation** — clear recommendation with reasoning based on the readiness assessment

## Anti-Patterns

- **"We will fix it after launch"** — Acceptable for nice-to-haves. Not acceptable for core flow bugs, security issues, or legal requirements.
- **Checklist completed by one person** — Each dimension should be verified by its owner (engineering verifies engineering, marketing verifies marketing). A PM checking all 8 dimensions creates false confidence.
- **No rollback plan** — If you cannot undo the launch, you are betting the company on a single deployment. Always have a rollback plan, always test it.
- **Launch without analytics** — If you cannot measure success, you cannot learn. Instrumenting analytics AFTER launch means you miss the most important data (the launch cohort).
- **Big-bang launch without soft launch** — For most products, launch to a small cohort first (beta, waitlist, friends and family), verify the experience, then open broadly. Exceptions: products where network effects require critical mass on day 1.
