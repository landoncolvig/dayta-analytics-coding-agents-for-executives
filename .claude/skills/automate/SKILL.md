---
name: automate
description: Turn a recurring task into an automation. Use when the executive wants something to run on its own, a scheduled report, an alert, or a data sync. Two parts: decide what to automate first, then build it (a scheduled query, an API pipeline into BigQuery on Cloud Functions, or browser automation when there is no API).
---

# Automate a task

Two questions: which task first, and how to build it.

## Part 1, decide what to automate first
Rank the candidates from the time audit. For each, estimate two numbers:
- **Hours saved per month** = how often it runs times how long it takes by hand.
- **Effort to build** = low (the data is already in BigQuery), medium (an API exists and
  needs a pipeline), high (no API, needs browser automation or scraping).

Do the **most hours for the least effort** first. Bank the quick wins, then take on the
bigger builds. Report the ranking with the hours each returns, so the executive sees the
order and why.

## Part 2, build it (work down this tree, simplest first)
1. **Already in BigQuery?** Then it is a scheduled query plus a format-and-send step. Build
   it, schedule it, done. (see the `bigquery` and `data-report` skills)
2. **Is there an API for the source?**
   - Pull from the API into BigQuery (or the company warehouse) on a schedule. Parallelize
     and retry from the start for any multi-account or per-record pull.
   - Keep every credential in **Google Secret Manager**, never in code. When you write a
     new secret version, prune the old ones (they bill per enabled version). Grant the
     service account least privilege.
   - Deploy the job as a **Cloud Function**, tested locally first, triggered by **Cloud
     Scheduler**. Run analysis off the BigQuery data, not inside a long-running function.
     Run historical backfills locally, not in the deployed function.
3. **No API?**
   - **Browser automation** (Playwright or Puppeteer) for a tool that only has a UI.
   - Or a scheduled export and import: a CSV or report drop into Drive or GCS, then into
     BigQuery.
4. **Schedule and harden.** On Claude Code, use `/schedule` for the cadence. Add retries
   with backoff and an alert when a run fails, and watch the first few runs.

## Always
- Build the simplest thing that works: a scheduled query beats a Cloud Function, and a
  Cloud Function beats browser automation.
- Test locally before deploying.
- Secrets live in Secret Manager and get pruned; service accounts are least privilege;
  write only to the scratch dataset for intermediate results.
- Never mutate production data without explicit approval.
