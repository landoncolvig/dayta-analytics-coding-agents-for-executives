---
name: brief
description: Produce a one-page briefing before a meeting, a call, or the day. Use when the executive asks to "prep me," "what do I need for the X meeting," or "give me my morning brief."
---

# Brief

A one-page prep, pulled together from what the executive already has, so they walk in
ready.

## When to use
"Prep me for the [client] call," "what do I need before the partner meeting," "give me my
morning brief."

## What goes in a brief
- **Who and what:** the people, the matter or topic, and why this meeting is happening.
- **The latest numbers:** the few figures relevant to this meeting, from BigQuery (use the
  `data-report` and `bigquery` skills).
- **Recent history:** the last few touches, from email or the matter record, if connected.
- **Open items:** what is owed, by whom, and any deadline.
- **A suggested outcome:** one line on what a good result looks like.

## Workflow
1. Identify the meeting from the calendar, if connected, or ask which one.
2. Pull the relevant numbers and history. Use the `bigquery` skill so you query the right
   tables, and prefer the modeled layer.
3. Write it to one page, in plain English, most important thing first.
4. Offer to turn it into talking points or a short deck (`deck-builder`).

## Keep it tight
One page. Lead with what matters. Leave a [bracketed blank] rather than guess a fact.
