---
name: data-report
description: Pull numbers from the executive's BigQuery data and turn them into a clean, plain-English report. Use when they ask for a report, a summary, "the numbers on X," monthly/weekly figures, or anything answerable from their data.
---

# Data Report

Turn a plain-English request into a query against the executive's BigQuery data, then a
clean written report they can read or forward.

## When to use
Use automatically when the executive:
- asks for "a report," "a summary," "the numbers," "how did we do on X"
- asks anything answerable from their data
- describes a report they pull on a recurring basis

## Credentials
Read `GOOGLE_APPLICATION_CREDENTIALS`, `GCP_PROJECT_ID`, `BQ_DATASET`, and
`BQ_SCRATCH_DATASET` from the `.env` in the project root. Pass the key file explicitly to
the BigQuery client. Never use application-default credentials. You may write intermediate
tables only to `BQ_SCRATCH_DATASET`.

## Workflow
1. **Clarify in one question, max.** If the date range or metric is obvious, proceed and
   state your assumption rather than asking.
2. **Find the data.** If you don't know the tables yet, list them
   (`bq ls <project>:<dataset>`) and inspect the relevant schema before writing SQL.
3. **Write a safe query.** Always include a date filter or LIMIT. Never SELECT * a large
   table. For multi-step analysis, materialize intermediate results in the scratch dataset.
4. **Run it and sanity-check.** Totals in a believable range, no unexpected nulls, no row
   explosion from a bad join.
5. **Write the report in plain English:** a 2-3 sentence headline that answers the question
   first, then the key figures as a short bulleted list or small table. No SQL in the final
   report unless they ask to see it.
6. **Offer the next step:** "Want this as a deck?" (→ `deck-builder`) or "Want me to draft
   an email with this?" (→ `email-reply`).

## Output style
- Answer first. The executive should get it in the opening sentence.
- Round sensibly ($48.2K, not $48,231.04) unless precision matters.
- Flag anything surprising, and say why in a few words.

## Recurring reports
If a report is recurring, offer to save it as a one-line command and, on Claude Code, to
schedule it so it lands automatically.

## Example
Executive: "How much did we bring in last month by [category]?"
1. Assume "last month" = previous calendar month; state it.
2. Query the total grouped by category for that range.
3. Report: headline number, up/down vs prior month, the 3-4 line breakdown, one notable
   driver.
4. "Want this as a board-ready deck?"
