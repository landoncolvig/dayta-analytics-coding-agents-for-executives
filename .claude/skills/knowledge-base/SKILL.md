---
name: knowledge-base
description: Answer questions across the executive's own documents and data, a company brain. Use when they ask something that lives in their files, matters, or numbers and want one answer instead of digging.
---

# Knowledge base

Let the executive ask their own firm anything and get one answer, pulled from their
documents and their data together.

## When to use
"What did we agree with [client] on fees?", "which matters mention [issue]?", "what is our
policy on [X]?", "pull everything we have on [topic]." Questions whose answer is spread
across files, the matter record, and BigQuery.

## Where the answers live
- **Structured data:** BigQuery (use the `bigquery` skill). Numbers, matters, billing,
  intake.
- **Documents:** their connected Drive or document folder. Contracts, policies, memos,
  notes.
- **Threads:** email, when connected.

## Workflow
1. **Decide where the answer lives** (data, documents, or both) and look there. Do not
   guess.
2. **Pull the specific evidence:** the row, the clause, the message. Do not answer from a
   vague memory.
3. **Answer in one place:** the direct answer first, then the few sources it came from, each
   citable so they can open it.
4. If the answer is not in what you can reach, say so, and say where it probably is.

## Keep it honest
- Ground every answer in a real source from their own material. Quote or cite it.
- Never fabricate a document, a number, or a quote. "I do not see it" is a valid answer.
- Read-only, and nothing leaves the firm without approval.
