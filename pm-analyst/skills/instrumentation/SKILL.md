---
name: instrumentation
description: "Design event taxonomies, tracking plans, and data quality audits for product analytics. Covers naming conventions, property specifications, common instrumentation failures, and platform-specific guidance for Segment, Amplitude, Mixpanel, and warehouse-native patterns."
---

# Analytics Instrumentation

Design instrumentation that produces trustworthy data. A tracking plan is the contract between product and engineering about what gets measured, how, and why. Bad instrumentation is worse than no instrumentation — it creates false confidence.

## The Cost of Bad Instrumentation

Every analytics question that can't be answered because of missing or malformed data represents:
- A decision made on gut feel instead of evidence
- An A/B test that can't be analyzed properly
- A retention curve with gaps that hide the real story
- A dashboard metric that says one thing and means another

**Get instrumentation right once and every downstream analysis benefits. Get it wrong and every downstream analysis is compromised.**

## Event Taxonomy Design

### Naming Convention: `object_action`

Every event name follows the pattern: `[object]_[action]`

The **object** is the thing being acted upon. The **action** is what happened to it.

| Object | Action | Event Name | Trigger |
|--------|--------|------------|---------|
| page | viewed | `page_viewed` | Page fully renders (DOMContentLoaded + above-fold content visible) |
| button | clicked | `button_clicked` | User taps/clicks a button (not programmatic triggers) |
| form | submitted | `form_submitted` | Form passes client-side validation and submit request fires |
| order | completed | `order_completed` | Payment processor confirms charge (not "submit clicked") |
| feature | activated | `feature_activated` | User performs the core action of a feature for the first time |
| subscription | started | `subscription_started` | Billing system confirms new subscription creation |
| subscription | cancelled | `subscription_cancelled` | Cancellation confirmed (not "cancel button clicked") |
| search | performed | `search_performed` | Search query submitted (not each keystroke) |
| onboarding | completed | `onboarding_completed` | User finishes the last onboarding step |
| error | occurred | `error_occurred` | Application error caught (client or server) |

### Naming Rules

1. **Always `snake_case`**: `page_viewed`, not `pageViewed`, `PageViewed`, or `Page Viewed`
2. **Past tense for actions**: `order_completed`, not `order_complete` or `completing_order`
3. **Object first**: `page_viewed`, not `viewed_page` — this groups related events alphabetically
4. **Be specific**: `checkout_button_clicked`, not `button_clicked` (unless you use a `button_name` property)
5. **No abbreviations**: `subscription_cancelled`, not `sub_cancelled`
6. **No platform prefixes**: `page_viewed`, not `ios_page_viewed` — platform goes in a property

### Event Categories

Group events into these categories for organizational clarity:

| Category | Purpose | Examples |
|----------|---------|---------|
| **Lifecycle** | User state changes | `account_created`, `subscription_started`, `account_deleted` |
| **Navigation** | Movement through the product | `page_viewed`, `tab_switched`, `deep_link_opened` |
| **Engagement** | Core product interactions | `content_created`, `message_sent`, `item_favorited` |
| **Commerce** | Revenue-related actions | `cart_updated`, `checkout_started`, `order_completed` |
| **System** | Technical events | `error_occurred`, `notification_received`, `app_backgrounded` |

## Standard Properties

### Properties Every Event Must Have

These are set automatically by the analytics SDK — individual events should NOT set them manually:

| Property | Type | Description | Example |
|----------|------|-------------|---------|
| `user_id` | string | Authenticated user identifier (null if anonymous) | `"usr_abc123"` |
| `anonymous_id` | string | Device/browser identifier for pre-auth tracking | `"a8f3e2b1-..."` |
| `session_id` | string | Session identifier (new after 30 min inactivity) | `"sess_xyz789"` |
| `timestamp` | ISO 8601 | When the event occurred (client clock) | `"2026-03-05T14:30:00Z"` |
| `received_at` | ISO 8601 | When the server received the event | `"2026-03-05T14:30:01Z"` |
| `platform` | string enum | `"ios"`, `"android"`, `"web"`, `"api"` | `"ios"` |
| `app_version` | string | Semantic version of the application | `"2.4.1"` |
| `os_version` | string | Operating system version | `"iOS 19.0"` |
| `device_type` | string | Device category | `"iPhone"`, `"iPad"`, `"desktop"` |
| `locale` | string | User's locale setting | `"en-US"` |

### Property Naming Rules

1. **Always `snake_case`**: `page_name`, not `pageName`
2. **Explicit types**: Document whether `user_id` is a string, integer, or UUID — and never mix types
3. **Consistent units**: If `duration` is in seconds in one event, it must be in seconds in ALL events. Document the unit in the property description.
4. **Enums over free text**: `plan_type: "pro"` not `plan_type: "Pro Plan"` or `plan_type: "professional"`. Define the enum values in the tracking plan.
5. **Required vs optional**: Mark every property. Missing required properties should trigger a data quality alert.
6. **No PII in event properties**: No email addresses, phone numbers, full names, IP addresses. Use hashed or tokenized identifiers.

## Tracking Plan Template

The tracking plan is the canonical reference for all instrumented events. It lives in a spreadsheet or structured document that both product and engineering reference.

### Format

| Event Name | Category | Trigger Description | Property | Type | Required | Enum Values | Example | Status |
|------------|----------|---------------------|----------|------|----------|-------------|---------|--------|
| `page_viewed` | Navigation | Page fully renders (DOMContentLoaded + above-fold visible) | `page_name` | string | Yes | - | `"dashboard"` | Live |
| | | | `page_url` | string | Yes | - | `"/app/dashboard"` | Live |
| | | | `referrer` | string | No | - | `"/app/settings"` | Live |
| | | | `time_on_previous_page_sec` | float | No | - | `12.4` | Live |
| `button_clicked` | Engagement | User taps/clicks a UI button | `button_name` | string | Yes | - | `"upgrade_cta"` | Live |
| | | | `button_location` | string | Yes | - | `"header"`, `"modal"` | Live |
| | | | `page_name` | string | Yes | - | `"pricing"` | Live |
| `order_completed` | Commerce | Payment processor confirms charge | `order_id` | string | Yes | - | `"ord_abc123"` | Live |
| | | | `total_amount_cents` | integer | Yes | - | `4999` | Live |
| | | | `currency` | string | Yes | ISO 4217 | `"USD"` | Live |
| | | | `item_count` | integer | Yes | - | `3` | Live |
| | | | `payment_method` | string | Yes | `"card"`, `"paypal"`, `"apple_pay"` | `"card"` | Live |
| `error_occurred` | System | Application error caught | `error_code` | string | Yes | - | `"PAYMENT_DECLINED"` | Live |
| | | | `error_message` | string | Yes | - | `"Card was declined"` | Live |
| | | | `error_source` | string | Yes | `"client"`, `"server"`, `"third_party"` | `"server"` | Live |
| | | | `page_name` | string | No | - | `"checkout"` | Live |

### Status Values

| Status | Meaning |
|--------|---------|
| **Planned** | In the tracking plan, not yet implemented |
| **In Development** | Engineering is implementing |
| **In QA** | Implemented, being validated |
| **Live** | In production, data flowing |
| **Deprecated** | Scheduled for removal, do not use in new analyses |
| **Removed** | No longer firing, historical data still available |

## Data Quality Checklist

Run this checklist when auditing existing instrumentation or validating a new tracking plan.

### Coverage
- [ ] **Are all key user actions instrumented?** Map the user journey and verify every meaningful step has an event.
- [ ] **Is there a "heartbeat" or "last seen" event?** Without this, DAU calculations rely on action events, which undercount passive users.
- [ ] **Are error events instrumented with error codes and context?** Generic "error occurred" without a code or page context is useless.
- [ ] **Are both success and failure paths instrumented?** Don't just track `checkout_completed` — also track `checkout_abandoned` and `checkout_failed`.
- [ ] **Are onboarding steps individually tracked?** Not just "started" and "completed" — each step, so you can find the drop-off point.

### Consistency
- [ ] **Are event names consistent?** No `page_view` AND `pageView` AND `PageViewed`. Pick one convention and enforce it.
- [ ] **Are property types consistent?** Is `user_id` always a string, or sometimes an integer? Is `amount` in cents or dollars? Is `duration` in seconds or milliseconds?
- [ ] **Are enum values consistent?** Is it `"ios"` or `"iOS"` or `"apple"`? Define the canonical values.
- [ ] **Is the timezone documented?** Event timestamps in UTC? User-local? Server-local? If mixed, you have a problem.

### Accuracy
- [ ] **Do events fire at the right moment?** `page_viewed` on DOMContentLoaded, not on link click. `order_completed` on payment confirmation, not on submit button click.
- [ ] **Do events fire exactly once per action?** A `button_clicked` that fires on every re-render is not a button click — it's noise. Check for debouncing.
- [ ] **Are bot and internal users excluded?** Or at least flaggable. If your DAU includes your QA team's 500 daily sessions, it's inflated.
- [ ] **Is the identity graph working?** Can you connect anonymous browsing to authenticated sessions? Can you merge cross-device activity for the same user?

### Completeness
- [ ] **Are required properties always present?** Query for NULL values in required fields. If > 1% of events are missing a required property, something is broken.
- [ ] **Are event volumes reasonable?** A sudden 10x spike in `page_viewed` events might mean a re-render bug, not 10x traffic.
- [ ] **Are there gaps in the data?** Missing hours or days in event volume charts indicate instrumentation outages.

## What to Instrument First: The 80/20

If you're starting from scratch or have limited engineering bandwidth, prioritize these events in order:

### Tier 1: Must-Have (covers 80% of analysis needs)
1. `account_created` — acquisition funnel entry
2. `page_viewed` (with `page_name`) — basic navigation and engagement
3. `[core_action]_completed` — whatever your product's core value action is (message sent, design exported, workout logged, etc.)
4. `subscription_started` / `order_completed` — revenue events
5. `error_occurred` — product health

### Tier 2: Important (enables cohort and funnel analysis)
6. `onboarding_step_completed` (with `step_name` and `step_number`) — activation analysis
7. `feature_activated` (with `feature_name`) — feature adoption
8. `session_started` / `session_ended` — session-level analysis
9. `subscription_cancelled` — churn analysis
10. `search_performed` (with `query` and `results_count`) — search quality

### Tier 3: Nice-to-Have (enables advanced analysis)
11. `notification_sent` / `notification_opened` — notification effectiveness
12. `experiment_viewed` (with `experiment_name`, `variant`) — A/B test tracking
13. `invite_sent` / `invite_accepted` — referral analysis
14. `feedback_submitted` — qualitative signal
15. `app_backgrounded` / `app_foregrounded` — mobile engagement depth

## Common Instrumentation Failures

### 1. Events That Fire on Page Load, Not User Action

**The failure**: `button_clicked` fires when the page renders because the analytics call is in the component's mount lifecycle, not in the click handler.

**The symptom**: Button click rate is 100%. Every page view produces a button click event.

**The fix**: Attach analytics calls to user-initiated event handlers (onClick, onSubmit), never to lifecycle methods (componentDidMount, useEffect, viewDidLoad).

### 2. Missing Properties That Make Analysis Impossible

**The failure**: `page_viewed` fires without a `page_name` property.

**The symptom**: You can count total page views but can't break them down by page. The most basic question — "which page gets the most views?" — is unanswerable.

**The fix**: Define required properties in the tracking plan. Validate them in the SDK or a middleware layer. Alert on missing required properties.

### 3. Events That Fire Multiple Times Per Action

**The failure**: A React component re-renders 5 times on state change, and each render fires a `feature_used` event.

**The symptom**: Feature usage is inflated 5x. Correlation with outcomes is broken because the noise drowns the signal.

**The fix**: Debounce analytics calls. Use a flag to ensure one-time events fire only once. In React, use `useRef` to track whether the event has already been sent.

### 4. Client Clock Skew

**The failure**: Relying on client-side timestamps without a server-side `received_at`.

**The symptom**: Events appear out of order. A user "completes checkout" before "viewing the product page" because their device clock is wrong.

**The fix**: Always record both `timestamp` (client clock) and `received_at` (server clock). Use `received_at` for ordering when precision matters. Use `timestamp` for user-local time analysis.

### 5. Schema Drift

**The failure**: Version 2.1 of the app sends `plan_type: "professional"` while version 2.0 sends `plan_type: "pro"`. Nobody updated the tracking plan.

**The symptom**: Queries that filter on `plan_type = 'pro'` miss half the professional users. The dashboard shows a sudden 50% drop in pro users.

**The fix**: Version your event schemas. Use a schema registry or validation layer. When changing property values, update ALL live versions simultaneously or use a mapping table.

### 6. Silent Instrumentation Removal

**The failure**: An engineer refactors a component and the analytics call disappears. No test catches it because there are no tests for instrumentation.

**The symptom**: An event's volume drops to zero. Nobody notices for weeks because nobody monitors event volumes.

**The fix**: Add event volume monitors with alerts. If `order_completed` drops more than 50% day-over-day, something is broken. Consider automated tests that verify critical events fire in E2E test suites.

## Platform-Specific Guidance

### Segment (Customer Data Platform)

**Best for**: Companies using multiple analytics tools. Segment is a router — send events once, route to many destinations.

**Key patterns**:
- Use `.identify()` on login/signup with user traits
- Use `.track()` for events, `.page()` for page views
- Use `.group()` for B2B account-level tracking
- Implement server-side tracking for revenue events (more reliable than client-side)
- Use Protocols (Segment's schema enforcement) to validate events against your tracking plan

**Gotcha**: Segment's `.page()` sends a `page` event AND updates the user's `last_seen` property. If you also send a custom `page_viewed` event, you're double-counting. Pick one.

### Amplitude

**Best for**: Product analytics with behavioral cohorting and funnel analysis built in.

**Key patterns**:
- Use Taxonomy (event/property governance) to enforce naming conventions
- Use User Properties for persistent traits, Event Properties for per-event context
- Behavioral cohorts can be defined in the UI — but document them in the tracking plan too
- Revenue events should use Amplitude's revenue API (`logRevenue`) for accurate LTV calculations

**Gotcha**: Amplitude's default session definition (30-min inactivity timeout) may not match your product's concept of a session. Customize it if needed.

### Mixpanel

**Best for**: Event analytics with strong funnel and retention visualization.

**Key patterns**:
- Use `mixpanel.people.set()` for user profile properties (plan, signup date)
- Use Super Properties for properties that should attach to every event (plan_type, experiment_group)
- JQL (JavaScript Query Language) enables custom analysis beyond the UI

**Gotcha**: Mixpanel charges by event volume (MTUs in some plans). High-frequency events (scroll, hover) can dramatically increase costs. Be selective.

### Warehouse-Native (BigQuery / Snowflake + dbt)

**Best for**: Companies that want full control over their data, need to join product events with business data, or have outgrown SaaS analytics tools.

**Key patterns**:
- Raw events land in a staging table (append-only)
- dbt models transform raw events into:
  - `dim_users` — user dimension table with latest properties
  - `fct_events` — cleaned, deduplicated event facts
  - `fct_sessions` — sessionized events with session-level metrics
  - Retention, funnel, and cohort models as materialized views
- Use a schema registry (e.g., JSON Schema, Protobuf) to validate events at ingestion
- Looker / Metabase / Mode for visualization on top of the warehouse

**Gotcha**: Warehouse queries can be expensive. Partition tables by date. Use incremental models in dbt to avoid re-processing historical data.

## Instrumentation Audit Process

When auditing existing instrumentation for gaps:

1. **Map the user journey**: Draw every step from first visit to core value moment to payment to retention loop
2. **List expected events**: For each journey step, what event SHOULD fire?
3. **Query for actual events**: `SELECT event_name, COUNT(*) FROM events WHERE event_date >= CURRENT_DATE - 30 GROUP BY 1 ORDER BY 2 DESC`
4. **Compare expected vs actual**: Missing events = instrumentation gaps. Extra events = potential noise or deprecated events still firing.
5. **Check property completeness**: For each live event, what % of required properties are non-null?
6. **Check volume anomalies**: Any events with suspicious volumes (0 for days, 100x spikes, steady decline)?
7. **Document findings**: Gap list with priority (Tier 1/2/3), effort estimate, and owner

## References

- [The Product Analytics Playbook](https://www.productcompass.pm/p/the-product-analytics-playbook-aarrr)
- [Are You Tracking the Right Metrics?](https://www.productcompass.pm/p/are-you-tracking-the-right-metrics)
- Segment Documentation: [Spec](https://segment.com/docs/connections/spec/)
- Amplitude Documentation: [Taxonomy](https://help.amplitude.com/hc/en-us/articles/360061399191)
- Avo.app — Schema-first analytics governance tool
- Iteratively — Tracking plan management with CI/CD integration
