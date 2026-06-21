---
name: deck-builder
description: Turn a report, a set of numbers, or talking points into an editable PowerPoint (.pptx) the executive can open and tweak. Use when they ask for a deck, slides, a PowerPoint, or "something for the meeting."
---

# Deck Builder

Turn content into a clean, editable PowerPoint. Output is a real `.pptx` so the executive
can polish it in PowerPoint or Keynote afterward.

## When to use
Use automatically when the executive asks for a "deck," "slides," "PowerPoint,"
"presentation," or "something to present", often right after a `data-report`.

## Tool
Generate the file with `python-pptx`. If it isn't installed, run
`pip3 install python-pptx` once and tell the executive in plain English what you're doing.

## Workflow
1. **Get the content.** If it's from data, run `data-report` first. If they give talking
   points, use those.
2. **Plan the slides, keep it tight:** Title, one headline-takeaway slide, 2-4 content
   slides (one idea each), one next-steps slide. Fewer, cleaner slides beat dense ones.
3. **Build the .pptx** with python-pptx using the template below.
4. **Save** to the project folder and tell them the filename.
5. **Open it** so they can review, then offer to adjust.

## Template (branding)
- Title font: [BRAND FONT, or "Calibri"]. Accent color: [BRAND HEX].
- Title slide: organization name + deck title + date.
- One idea per slide. A big number or one-line takeaway as the headline; supporting detail
  beneath.
- Charts: use python-pptx native charts for any figures from `data-report`.
- Footer: organization name + page number. [ADJUST.]

## Guardrails
- Editable `.pptx` only (not a flattened image) so wording can be changed before
  presenting.
- Never put confidential specifics into a deck meant for an external audience without
  flagging it.

## Example
Executive: "Make a 5-slide deck from last month's report for the board meeting."
1. Use the numbers from `data-report`.
2. Slides: Title → "[Metric] up 9% to $312K" → breakdown chart → one highlight → risks /
   watch-items → next steps.
3. Save `board-meeting.pptx`, open it, ask "want the highlight slide expanded?"
