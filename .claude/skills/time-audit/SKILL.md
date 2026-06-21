---
name: time-audit
description: Run a time-and-energy audit and produce a ranked "automate first" list. Use when the executive asks where their time is going, what to hand off, what to automate, or wants to start buying back their week.
---

# Time & Energy Audit

The entry point to this whole kit. Before automating anything, find the tasks worth
automating: the ones that are repeatable, draining, and below the executive's time. Then
map each to a skill here. The twist on the classic buy-back-your-time move: delegation
here means delegating to the agent, not hiring a person.

## When to use
Use automatically when the executive says any of:
- "Where is my time going?" / "What should I automate?" / "What can you take off me?"
- "I want to buy back my time" / "help me get started"
- describes a typical week and asks what to hand off

## The honest-snapshot rule
The audit only works on a real week, not a flattering memory. Ask for an actual recent
week (or the last few days, recalled honestly). Don't let vagueness through, "email" is
not a task; "triage and reply to client email, about 90 min/day" is. You can't hand off a
week you won't look at squarely.

## Workflow
1. **Capture the week.** Ask for recurring tasks and rough hours. Prompt by category if
   they stall: client communication, reports/numbers, slides/prep, document review,
   internal updates, scheduling, approvals.
2. **Rate each task on two axes:**
   - **Energy:** green (energizing), yellow (neutral), red (draining).
   - **Value:** roughly what the task is worth per hour, or simply above/below their
     buyback rate (next step).
3. **Compute the buyback rate.** Annual income ÷ 2,080 hours ÷ 4. Anything they do that's
   worth less than this number is a candidate to hand off. State the number plainly and
   note it's a guide, not a rule.
4. **Sort into four boxes** (value × energy) and find the target: **repeatable + draining +
   below the buyback rate.** That box gets automated first.
5. **Map candidates to this kit's skills:**
   - reports / "the numbers" → `data-report`
   - slides / prep decks → `deck-builder`
   - email replies → `email-reply`
   - reading long documents / contracts → `doc-summarize`
   - anything recurring → offer to save it as a reusable command (or schedule it on Claude
     Code)
   - tasks that need a human but not *this* human → flag for a real delegate, not the agent
6. **Deliver a ranked list:** the top 3-5 automate-first tasks, the skill that handles
   each, rough hours per week reclaimed, and a one-line first step for each.
7. **Close on reinvestment.** Ask the question that matters most: what will the reclaimed
   hours go to? An audit that doesn't end in a reinvestment plan just creates idle time
   that refills with more low-value work.

## Output style
- A short table: Task | Hours/wk | Energy | Automate with | Hours reclaimed.
- Lead with the single highest-leverage automation, not the longest list.
- Keep it to one screen. The point is to start, not to plan forever.

## Example
Executive: "I have no idea where my week goes, but I'm drowning."
1. Walk the categories; capture ~10 tasks with hours.
2. Rate them. The reds cluster in monthly + weekly reports (5 hrs), client/board decks
   (3 hrs), client email triage (7 hrs), contract review (4 hrs).
3. State the buyback rate.
4. Deliver the automate-first table, roughly 12-15 hrs/wk in reach across the four doing
   skills.
5. "If we get you 12 hours back, what's the first thing you'd put them toward?"
