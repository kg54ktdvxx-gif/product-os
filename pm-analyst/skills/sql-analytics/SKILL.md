---
name: sql-analytics
description: "Generate SQL queries from natural language for BigQuery, PostgreSQL, MySQL, and Snowflake. Perform cohort analysis, funnel analysis, retention curves, LTV calculations, and power user analysis. Includes dialect-specific syntax, performance guidance, and common PM SQL mistakes to avoid."
---

# SQL Analytics

Generate production-ready SQL from natural language business questions. Covers cohort analysis, funnel analysis, retention curves, LTV calculations, and power user segmentation across BigQuery, PostgreSQL, MySQL, and Snowflake.

## Core Principles

1. **Every query gets comments** — PMs share queries with analysts, engineers, and stakeholders. Uncommented SQL is a maintenance liability.
2. **CTEs over nested subqueries** — Readable trumps clever. One CTE per logical step.
3. **Always handle NULLs explicitly** — `NULL` in a `WHERE` clause silently drops rows. `NULL` in aggregation silently skews results. Make your NULL handling visible.
4. **State the dialect** — `DATE_TRUNC('month', ts)` is PostgreSQL. `DATE_TRUNC(ts, MONTH)` is BigQuery. `DATE_FORMAT(ts, '%Y-%m-01')` is MySQL. Always declare which dialect you're writing for.
5. **Flag performance concerns** — If a query will scan a multi-billion-row table without partition pruning, say so before the user runs it on production.

## Dialect-Specific Syntax Reference

### Date/Time Functions

| Operation | PostgreSQL | BigQuery | MySQL | Snowflake |
|-----------|-----------|----------|-------|-----------|
| Truncate to month | `DATE_TRUNC('month', ts)` | `DATE_TRUNC(ts, MONTH)` | `DATE_FORMAT(ts, '%Y-%m-01')` | `DATE_TRUNC('MONTH', ts)` |
| Add interval | `ts + INTERVAL '7 days'` | `DATE_ADD(ts, INTERVAL 7 DAY)` | `DATE_ADD(ts, INTERVAL 7 DAY)` | `DATEADD('DAY', 7, ts)` |
| Date difference | `DATE_PART('day', ts2 - ts1)` | `DATE_DIFF(ts2, ts1, DAY)` | `DATEDIFF(ts2, ts1)` | `DATEDIFF('DAY', ts1, ts2)` |
| Current timestamp | `NOW()` | `CURRENT_TIMESTAMP()` | `NOW()` | `CURRENT_TIMESTAMP()` |
| Extract part | `EXTRACT(MONTH FROM ts)` | `EXTRACT(MONTH FROM ts)` | `MONTH(ts)` | `EXTRACT(MONTH FROM ts)` |

### Window Functions

All four dialects support standard window functions. Key patterns:

```sql
-- Running total
SUM(amount) OVER (PARTITION BY user_id ORDER BY event_date)

-- Row number for deduplication
ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY event_timestamp DESC) AS rn

-- Lag/Lead for session analysis
LAG(event_timestamp) OVER (PARTITION BY user_id ORDER BY event_timestamp) AS prev_event

-- Percentile (syntax varies)
-- PostgreSQL: PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY value)
-- BigQuery:   PERCENTILE_CONT(value, 0.5) OVER ()
-- Snowflake:  PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY value)
```

### String Functions

| Operation | PostgreSQL | BigQuery | MySQL | Snowflake |
|-----------|-----------|----------|-------|-----------|
| Concat | `'a' || 'b'` | `CONCAT('a', 'b')` | `CONCAT('a', 'b')` | `'a' || 'b'` |
| Regex match | `col ~ 'pattern'` | `REGEXP_CONTAINS(col, 'pattern')` | `col REGEXP 'pattern'` | `REGEXP_LIKE(col, 'pattern')` |
| Substring | `SUBSTRING(col, 1, 5)` | `SUBSTR(col, 1, 5)` | `SUBSTRING(col, 1, 5)` | `SUBSTR(col, 1, 5)` |

## Common SQL Mistakes PMs Make

### 1. JOINs That Duplicate Rows

**The bug**: Joining `users` to `events` produces one row per event, not one row per user. If a user has 50 events, `COUNT(*)` counts them 50 times.

```sql
-- WRONG: counts events, not users
SELECT plan_type, COUNT(*) AS user_count
FROM users u
JOIN events e ON u.id = e.user_id
GROUP BY plan_type;

-- RIGHT: counts distinct users
SELECT plan_type, COUNT(DISTINCT u.id) AS user_count
FROM users u
JOIN events e ON u.id = e.user_id
GROUP BY plan_type;

-- ALSO RIGHT: pre-aggregate before joining
WITH active_users AS (
    SELECT DISTINCT user_id FROM events
    WHERE event_date >= CURRENT_DATE - INTERVAL '30 days'
)
SELECT u.plan_type, COUNT(*) AS user_count
FROM users u
JOIN active_users a ON u.id = a.user_id
GROUP BY u.plan_type;
```

### 2. NULL Handling Failures

```sql
-- WRONG: this silently excludes users with NULL plan_type
SELECT * FROM users WHERE plan_type != 'enterprise';

-- RIGHT: explicitly handle NULLs
SELECT * FROM users WHERE plan_type != 'enterprise' OR plan_type IS NULL;

-- WRONG: AVG ignores NULLs, which may or may not be what you want
SELECT AVG(nps_score) FROM surveys;  -- excludes non-respondents

-- RIGHT: if non-response should count as 0 (or some default)
SELECT AVG(COALESCE(nps_score, 0)) FROM surveys;
```

### 3. Timezone Mishandling

```sql
-- WRONG: comparing UTC timestamps to a date without timezone context
SELECT COUNT(*) FROM events WHERE event_timestamp::date = '2026-01-15';
-- A user active at 11pm PST on Jan 15 = 7am UTC on Jan 16 — you miss them

-- RIGHT: convert to the business timezone first
SELECT COUNT(*)
FROM events
WHERE (event_timestamp AT TIME ZONE 'UTC' AT TIME ZONE 'America/Los_Angeles')::date = '2026-01-15';
```

### 4. Missing GROUP BY Columns

```sql
-- WRONG: which user_name does this return? Undefined behavior.
SELECT user_id, user_name, COUNT(*) AS events
FROM events
GROUP BY user_id;
-- MySQL: picks an arbitrary user_name (ONLY_FULL_GROUP_BY off)
-- PostgreSQL/BigQuery/Snowflake: ERROR

-- RIGHT: include all non-aggregated columns
SELECT user_id, MAX(user_name) AS user_name, COUNT(*) AS events
FROM events
GROUP BY user_id;
```

### 5. Incomplete Period Bias

```sql
-- WRONG: comparing a full month to a partial month
SELECT DATE_TRUNC('month', event_date) AS month, COUNT(*) AS events
FROM events
GROUP BY 1
ORDER BY 1;
-- The current month always looks worse because it's not over yet

-- RIGHT: exclude the incomplete current period
SELECT DATE_TRUNC('month', event_date) AS month, COUNT(*) AS events
FROM events
WHERE event_date < DATE_TRUNC('month', CURRENT_DATE)  -- exclude current month
GROUP BY 1
ORDER BY 1;
```

## Advanced SQL Patterns

### Pattern 1: Retention Table (Cohort x Period)

The foundation of cohort analysis. Produces the classic retention heatmap.

```sql
-- PostgreSQL dialect
WITH cohorts AS (
    -- Define cohort: user's first activity month
    SELECT
        user_id,
        DATE_TRUNC('month', MIN(event_date)) AS cohort_month
    FROM events
    WHERE event_type IN ('page_view', 'action_performed')  -- define "active"
    GROUP BY user_id
),
user_activity AS (
    -- Monthly activity per user
    SELECT DISTINCT
        user_id,
        DATE_TRUNC('month', event_date) AS activity_month
    FROM events
    WHERE event_type IN ('page_view', 'action_performed')
),
retention AS (
    SELECT
        c.cohort_month,
        -- Period number: 0 = signup month, 1 = next month, etc.
        EXTRACT(YEAR FROM AGE(ua.activity_month, c.cohort_month)) * 12
            + EXTRACT(MONTH FROM AGE(ua.activity_month, c.cohort_month)) AS period_number,
        COUNT(DISTINCT c.user_id) AS active_users
    FROM cohorts c
    JOIN user_activity ua ON c.user_id = ua.user_id
        AND ua.activity_month >= c.cohort_month
    GROUP BY c.cohort_month, period_number
),
cohort_sizes AS (
    SELECT cohort_month, COUNT(DISTINCT user_id) AS cohort_size
    FROM cohorts
    GROUP BY cohort_month
)
SELECT
    r.cohort_month,
    cs.cohort_size,
    r.period_number,
    r.active_users,
    ROUND(100.0 * r.active_users / cs.cohort_size, 1) AS retention_pct
FROM retention r
JOIN cohort_sizes cs ON r.cohort_month = cs.cohort_month
WHERE r.period_number <= 12  -- limit to 12 months
ORDER BY r.cohort_month, r.period_number;
```

**Handling incomplete periods**: Exclude cohort-period combinations where the observation window hasn't closed yet. If today is March 15, the January cohort's "Month 2" (March) is incomplete — either exclude it or annotate it.

### Pattern 2: Funnel Analysis

```sql
-- PostgreSQL dialect
-- Conversion funnel: Signup -> Onboarding -> Core Action -> Upgrade
WITH funnel AS (
    SELECT
        user_id,
        -- Each step: 1 if completed, 0 if not
        1 AS step_1_signup,
        CASE WHEN EXISTS (
            SELECT 1 FROM events e
            WHERE e.user_id = u.user_id AND e.event_type = 'onboarding_completed'
              AND e.event_timestamp <= u.signup_timestamp + INTERVAL '7 days'
        ) THEN 1 ELSE 0 END AS step_2_onboarding,
        CASE WHEN EXISTS (
            SELECT 1 FROM events e
            WHERE e.user_id = u.user_id AND e.event_type = 'core_action_completed'
              AND e.event_timestamp <= u.signup_timestamp + INTERVAL '14 days'
        ) THEN 1 ELSE 0 END AS step_3_core_action,
        CASE WHEN EXISTS (
            SELECT 1 FROM events e
            WHERE e.user_id = u.user_id AND e.event_type = 'plan_upgraded'
              AND e.event_timestamp <= u.signup_timestamp + INTERVAL '30 days'
        ) THEN 1 ELSE 0 END AS step_4_upgrade
    FROM signups u
    WHERE u.signup_date BETWEEN '2026-01-01' AND '2026-01-31'
      AND u.signup_date <= CURRENT_DATE - INTERVAL '30 days'  -- complete observation window
)
SELECT
    'Step 1: Signup' AS step,
    COUNT(*) AS users,
    100.0 AS pct_of_total,
    100.0 AS pct_of_prev
UNION ALL
SELECT
    'Step 2: Onboarding',
    SUM(step_2_onboarding),
    ROUND(100.0 * SUM(step_2_onboarding) / COUNT(*), 1),
    ROUND(100.0 * SUM(step_2_onboarding) / COUNT(*), 1)
FROM funnel
UNION ALL
SELECT
    'Step 3: Core Action',
    SUM(step_3_core_action),
    ROUND(100.0 * SUM(step_3_core_action) / COUNT(*), 1),
    ROUND(100.0 * SUM(step_3_core_action) / NULLIF(SUM(step_2_onboarding), 0), 1)
FROM funnel
UNION ALL
SELECT
    'Step 4: Upgrade',
    SUM(step_4_upgrade),
    ROUND(100.0 * SUM(step_4_upgrade) / COUNT(*), 1),
    ROUND(100.0 * SUM(step_4_upgrade) / NULLIF(SUM(step_3_core_action), 0), 1)
FROM funnel;
```

### Pattern 3: LTV Calculation

```sql
-- PostgreSQL dialect
-- Simple historical LTV by signup cohort
WITH user_revenue AS (
    SELECT
        u.user_id,
        DATE_TRUNC('month', u.signup_date) AS cohort_month,
        SUM(p.amount) AS total_revenue,
        -- Months since signup
        EXTRACT(YEAR FROM AGE(MAX(p.payment_date), u.signup_date)) * 12
            + EXTRACT(MONTH FROM AGE(MAX(p.payment_date), u.signup_date)) AS lifetime_months
    FROM users u
    LEFT JOIN payments p ON u.user_id = p.user_id
    GROUP BY u.user_id, cohort_month
)
SELECT
    cohort_month,
    COUNT(*) AS cohort_size,
    -- Average revenue per user (including $0 users)
    ROUND(AVG(COALESCE(total_revenue, 0)), 2) AS avg_ltv,
    -- Median lifetime (months)
    PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY COALESCE(lifetime_months, 0)) AS median_lifetime_months,
    -- LTV by percentile
    ROUND(PERCENTILE_CONT(0.25) WITHIN GROUP (ORDER BY COALESCE(total_revenue, 0)), 2) AS ltv_p25,
    ROUND(PERCENTILE_CONT(0.75) WITHIN GROUP (ORDER BY COALESCE(total_revenue, 0)), 2) AS ltv_p75
FROM user_revenue
GROUP BY cohort_month
ORDER BY cohort_month;
```

### Pattern 4: Power User Analysis

```sql
-- PostgreSQL dialect
-- Identify power users: top 10% by engagement, analyze their behavior
WITH user_engagement AS (
    SELECT
        user_id,
        COUNT(DISTINCT event_date) AS active_days,
        COUNT(*) AS total_events,
        COUNT(DISTINCT event_type) AS distinct_actions,
        COUNT(*) FILTER (WHERE event_type = 'content_created') AS content_created
    FROM events
    WHERE event_date >= CURRENT_DATE - INTERVAL '30 days'
    GROUP BY user_id
),
percentiles AS (
    SELECT
        *,
        NTILE(10) OVER (ORDER BY active_days DESC) AS engagement_decile
    FROM user_engagement
)
SELECT
    engagement_decile,
    COUNT(*) AS users,
    ROUND(AVG(active_days), 1) AS avg_active_days,
    ROUND(AVG(total_events), 0) AS avg_events,
    ROUND(AVG(distinct_actions), 1) AS avg_distinct_actions,
    ROUND(AVG(content_created), 1) AS avg_content_created,
    -- What % of all events come from this decile?
    ROUND(100.0 * SUM(total_events) /
        SUM(SUM(total_events)) OVER (), 1) AS pct_of_all_events
FROM percentiles
GROUP BY engagement_decile
ORDER BY engagement_decile;
```

### Pattern 5: User Flow / Path Analysis

```sql
-- PostgreSQL dialect
-- Most common 3-step paths after signup
WITH ordered_events AS (
    SELECT
        user_id,
        event_type,
        ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY event_timestamp) AS event_order
    FROM events
    WHERE user_id IN (
        SELECT user_id FROM signups
        WHERE signup_date >= CURRENT_DATE - INTERVAL '30 days'
    )
    AND event_timestamp >= (
        SELECT signup_timestamp FROM signups s WHERE s.user_id = events.user_id
    )
),
paths AS (
    SELECT
        e1.user_id,
        e1.event_type AS step_1,
        e2.event_type AS step_2,
        e3.event_type AS step_3
    FROM ordered_events e1
    JOIN ordered_events e2 ON e1.user_id = e2.user_id AND e2.event_order = e1.event_order + 1
    JOIN ordered_events e3 ON e1.user_id = e3.user_id AND e3.event_order = e1.event_order + 2
    WHERE e1.event_order = 1
)
SELECT
    step_1, step_2, step_3,
    COUNT(*) AS user_count,
    ROUND(100.0 * COUNT(*) / SUM(COUNT(*)) OVER (), 1) AS pct_of_users
FROM paths
GROUP BY step_1, step_2, step_3
ORDER BY user_count DESC
LIMIT 20;
```

## Performance Guidance

### Rules of Thumb

| Issue | Impact | Fix |
|-------|--------|-----|
| `SELECT *` on wide tables | Reads all columns, wastes I/O | Select only needed columns |
| Missing partition filter | Full table scan on petabyte tables | Always filter on partition column (usually date) |
| `DISTINCT` on large result sets | Expensive sort/hash | Use `GROUP BY` or pre-filter instead |
| Subquery in `WHERE` clause | May execute per-row | Rewrite as JOIN or CTE |
| `ORDER BY` without `LIMIT` | Sorts entire result set | Add `LIMIT` or remove `ORDER BY` |
| Cross join (accidental) | Cartesian product explosion | Verify JOIN conditions |

### BigQuery-Specific

- Always filter on partition column (`_PARTITIONTIME` or custom) to avoid full scans
- Use `APPROX_COUNT_DISTINCT()` for cardinality estimates on huge tables (faster, ~1% error)
- Prefer `ARRAY_AGG()` over self-joins for sessionization
- Check bytes scanned with dry run before executing expensive queries

### PostgreSQL-Specific

- Use `EXPLAIN ANALYZE` to verify query plan and actual vs estimated rows
- Create indexes on columns used in `WHERE`, `JOIN`, and `ORDER BY`
- Use `VACUUM ANALYZE` on tables with heavy write activity
- Consider materialized views for expensive queries run repeatedly

## Cohort Analysis Deep Dive

### Defining Cohorts

A cohort must be **unambiguous** and **reproducible**. Two analysts running the same cohort definition on the same data must produce identical groups.

| Cohort Type | Definition | Best For |
|-------------|-----------|----------|
| **Signup cohort** | Month/week of first account creation | Retention analysis, onboarding changes |
| **Acquisition channel** | First-touch attribution source | Channel quality comparison |
| **Feature cohort** | First use of specific feature | Feature adoption impact |
| **Plan cohort** | Pricing tier at signup or upgrade | Revenue analysis |
| **Behavioral cohort** | Users who performed X in first N days | Activation analysis |

### Reading Retention Tables

A retention table is a matrix of `cohort x period`. Here's how to read it:

```
Cohort    | Size  | M0    | M1    | M2    | M3    | M4
----------|-------|-------|-------|-------|-------|------
Jan 2026  | 1,200 | 100%  | 42%   | 31%   | 28%   | 26%
Feb 2026  | 1,500 | 100%  | 45%   | 34%   | 30%   |
Mar 2026  | 1,800 | 100%  | 48%   | 37%   |       |
Apr 2026  | 2,000 | 100%  | 51%   |       |       |
```

**Read down columns** to see if retention is improving over time (M1: 42% -> 45% -> 48% -> 51% = improving).

**Read across rows** to see the retention curve for a single cohort (Jan: 100% -> 42% -> 31% -> 28% -> 26% = stabilizing around 26%).

**Empty cells** in the bottom-right are incomplete periods — do not fill them with zeros or interpolate them.

**Benchmark**: B2B SaaS Month-1 retention typically 40-60%. B2C apps Month-1 typically 25-40%. If you're below these, focus on activation before acquisition.

### Seasonality Awareness

Cohort differences can be calendar effects, not product effects. A December cohort may look worse simply because of holiday behavior patterns. Always check:
- Is the pattern present in the same period last year?
- Do adjacent cohorts (Nov, Jan) show similar patterns?
- Was there a product change that coincided with the calendar effect?

## Query Generation Workflow

When generating SQL from a natural language question:

1. **Clarify the question**: What exactly is being asked? What are the implicit assumptions?
2. **Identify the dialect**: PostgreSQL, BigQuery, MySQL, or Snowflake?
3. **Map to tables**: Which tables contain the needed data? What joins are required?
4. **Handle edge cases**: NULLs, timezone, deduplication, incomplete periods
5. **Write the query**: CTEs for readability, comments for each section
6. **Add performance notes**: Will this query be fast or slow? Any optimization suggestions?
7. **Explain the output**: What columns does this return? What does each row represent?

## References

- [The Product Analytics Playbook: AARRR, HEART, Cohorts & Funnels](https://www.productcompass.pm/p/the-product-analytics-playbook-aarrr)
- [Cohort Analysis 101: How to Reduce Churn](https://www.productcompass.pm/p/cohort-analysis)
- [Funnel Analysis 101](https://www.productcompass.pm/p/funnel-analysis)
- [How to Become a Technology-Literate PM](https://www.productcompass.pm/p/how-to-become-a-technology-literate)
