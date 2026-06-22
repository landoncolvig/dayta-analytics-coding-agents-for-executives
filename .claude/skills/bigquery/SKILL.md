---
name: bigquery
description: How to query the executive's BigQuery data correctly. Discover the live schema, keep a data dictionary, and write safe queries. Use before any data-report, dashboard, or analysis so the agent never guesses table or column names.
---

# BigQuery

The rule: **never guess table or column names.** Learn the schema, then query. This skill
is the foundation the data-report, dashboard, and analysis work sits on.

## Credentials
Read `GOOGLE_APPLICATION_CREDENTIALS`, `GCP_PROJECT_ID`, `BQ_DATASET`, and
`BQ_SCRATCH_DATASET` from the `.env`. Pass the key file explicitly to the BigQuery client.
Never use application-default credentials. You may write only to `BQ_SCRATCH_DATASET`.

## Know the schema before you query
1. **Check for a cached dictionary.** If `DATA_DICTIONARY.md` exists in the project, read
   it first. It lists every dataset, table, column, type, and description.
2. **If it is missing or looks stale, build it.** Introspect the live schema (this is the
   source of truth, metadata reads are free and contain no row data):
   ```bash
   bq ls <project>:<dataset>                                   # tables in a dataset
   bq show --schema --format=prettyjson <project>:<dataset>.<table>
   ```
   Or query `INFORMATION_SCHEMA` per dataset:
   ```sql
   SELECT table_name, column_name, data_type, description
   FROM `<project>.<dataset>.INFORMATION_SCHEMA.COLUMN_FIELD_PATHS`
   ORDER BY table_name, column_name
   ```
   To regenerate the whole dictionary at once, run the bundled generator (writes
   `DATA_DICTIONARY.md` + `schema.json`, schema only):
   ```bash
   python3 generate_data_dictionary.py --project $GCP_PROJECT_ID \
     --key ./service-account.json --out .
   ```
3. **Prefer the clean layer.** Start in the modeled / analytics dataset (named in
   `BQ_DATASET`). Drop to `raw_*` only when a detail is not there.

## Write a safe query
- Always add a date filter or `LIMIT`. Never `SELECT *` a large table.
- For multi-step analysis, materialize intermediate tables in `BQ_SCRATCH_DATASET`.
- Sanity-check results: believable totals, no unexpected nulls, no row explosion from a
  bad join.

## When a query fails on an unknown column
That means the dictionary is stale. Re-introspect that table (`bq show --schema`), update
`DATA_DICTIONARY.md`, then retry. Do not guess an alternate name.

## Keep it fresh
Refresh the dictionary when the schema changes, or on a schedule (on Claude Code, ask to
"schedule a weekly data-dictionary refresh"). A stale dictionary is only a hint; live
introspection always wins for anything you are unsure about.

## One-time investment that pays off
Business meaning belongs at the source. Where you can, set table and column **descriptions**
in BigQuery on the modeled layer (`bq update --description`, or `ALTER TABLE ... SET
OPTIONS(description=...)` and column `OPTIONS`). Every dictionary you generate then carries
that meaning automatically.
