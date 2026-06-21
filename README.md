# Dayta Analytics, Coding Agents for Executives

> A starter kit that turns a coding agent (Claude Code or Codex) into a chief of staff
> for your data, your reports, your decks, and your inbox, so you can buy back the hours
> those tasks quietly eat.

## The idea in one minute

You are the constraint. Not as an insult, as arithmetic: in most organizations the
reports, the decks, the "quick replies," and the document reviews all route through one
desk, and the place can't move faster than that desk clears. The usual answer is to work
longer. That doesn't move the constraint; it just runs it hotter.

There's a better answer. Most of what lands on that desk is repeatable, low-leverage, and
quietly draining, work that ended up there by default, not by design. A coding agent can
take that work and do it in seconds. Your hours move up to the judgment, the
relationships, and the decisions that only you can make.

The sequence is deliberate:

1. **Audit**, an honest time-and-energy audit (run the `time-audit` skill). You can't
   hand off a week you won't look at honestly.
2. **Automate**, point the agent at the draining, repeatable tasks first: reports, decks,
   email, document review.
3. **Reinvest**, put the reclaimed hours into the work only you can do.

## What's inside

| File | What it is |
|------|-----------|
| `CLAUDE.md` / `AGENTS.md` | The agent's standing instructions, a template you personalize once |
| `.claude/skills/` | Five ready-to-use automations (below) |
| `.env.example` | The shape of the credentials file (your real one is delivered to you privately) |
| `prompts-cheatsheet.md` | The prompts you'll reach for most |

### The five skills

| Skill | What it does |
|-------|--------------|
| `time-audit` | Walks you through the time-and-energy audit and tells you what to automate first |
| `data-report` | Ask your data a question in plain English, get a written report (BigQuery) |
| `email-reply` | Drafts replies in your voice, you read, tweak, and send |
| `deck-builder` | Turns numbers or notes into an editable PowerPoint |
| `doc-summarize` | Turns a long contract or document into a clear summary with risks and next steps |

## Getting started

You'll have received a short setup guide (PDF) and, separately and securely, a `.env`
file that gives the agent read access to your data. In short:

1. Install the agent (Claude Code or Codex), the guide walks you through it.
2. Put your `.env` file into this folder.
3. Ask the agent to confirm it can see your data.
4. Run the time audit, then automate the top of the list.

## Safety

- **This repository contains no credentials and no private data. It is safe to share.**
- Your `.env` file and any key are delivered separately and must never be committed or
  shared. `.gitignore` already excludes them.
- The agent **drafts; you approve.** Nothing leaves your hands without your yes.

## About

Built by Dayta Analytics. Questions or a key that needs replacing: contact your Dayta
point of contact.

Licensed under the MIT License, see `LICENSE`.
