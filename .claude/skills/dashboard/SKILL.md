---
name: dashboard
description: Build a live, shareable dashboard from the executive's BigQuery data. Use when they ask for a dashboard, a live view, a scorecard, or "something I can check any time" rather than a one-off report.
---

# Dashboard

Turn the metrics the executive watches into a live view they open any time, not a static
report.

## When to use
When they ask for a "dashboard," a "live view," a "scorecard," or "something I can check
whenever," especially for numbers they currently pull by hand on a cadence.

## Two ways to build it
1. **Looker Studio** (best for a polished, always-live BI view): build the BigQuery views
   the dashboard needs, connect Looker Studio to them, and hand back the share link.
2. **A self-contained HTML dashboard** (fast and portable): one HTML file with the charts
   (Chart.js), reading from a query the agent runs and refreshes. Good for a quick,
   shareable snapshot or a PDF (see the `pdf-print` skill).

## Workflow
1. Confirm the handful of metrics that matter. Ask if it is unclear; do not guess the
   whole thing.
2. Use the `bigquery` skill to find the right tables and write the queries. Prefer the
   modeled layer.
3. Build the view. Lead with the KPIs they care about, one trend over time, and one
   breakdown. Keep it to what they will actually look at.
4. Show it, take one round of feedback, then share the link.
5. If it should stay current, schedule the underlying query or refresh (see `automate`).

## Keep it honest
- Real numbers only, from their data. No invented figures on anything they will share.
- Report month over month, matching how they read the business.
