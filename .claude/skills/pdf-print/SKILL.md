---
name: pdf-print
description: Turn an HTML file into a clean, branded PDF using headless Chrome. Use when asked to make a PDF of a report, a one-pager, a branded document, or any HTML the agent built. Pairs with deck-builder (which makes an editable .pptx); use pdf-print when the output should be a fixed, polished PDF.
---

# PDF print

Render an HTML file to a print-quality PDF with headless Chrome. Chrome honors full CSS
(web fonts, colors, page breaks), so a well-styled HTML page becomes a clean PDF.

## Make a PDF
```bash
.claude/skills/pdf-print/print_pdf.sh <input.html (absolute path)> <output.pdf (absolute path)>
```
The script finds Chrome or Chromium, waits for fonts to load, and writes the PDF.

## Writing print-ready HTML
- Set `@page { size: Letter; margin: ... }`, and use `break-before: page` and
  `break-inside: avoid` to control pagination.
- Put `print-color-adjust: exact` (and `-webkit-print-color-adjust: exact`) on colored
  elements so backgrounds and accents actually print.
- Keep the file self-contained: inline the CSS, and load fonts from a CDN (Google Fonts)
  so they embed.
- `<a href>` links stay clickable in the finished PDF.

## When to use which
- **pdf-print** for fixed documents: reports, summaries, branded one-pagers, this guide.
- **deck-builder** when the recipient needs to edit it (an editable PowerPoint).

Generated PDFs stay out of git; the repo's `.gitignore` already ignores `*.pdf`.
