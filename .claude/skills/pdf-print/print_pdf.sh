#!/usr/bin/env bash
# Render an HTML file to a PDF via headless Chrome.
# Usage: print_pdf.sh <input.html (absolute path)> <output.pdf (absolute path)>
set -euo pipefail
IN="${1:?absolute path to input .html required}"
OUT="${2:?absolute path to output .pdf required}"
case "$IN" in /*) ;; *) echo "input must be an absolute path"; exit 1;; esac

CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
if [ ! -x "$CHROME" ]; then
  CHROME="$(command -v google-chrome || command -v chromium || command -v chromium-browser || command -v google-chrome-stable || true)"
fi
[ -n "$CHROME" ] || { echo "Chrome or Chromium not found"; exit 1; }

mkdir -p "$(dirname "$OUT")"
"$CHROME" --headless=new --disable-gpu --no-sandbox --no-pdf-header-footer \
  --virtual-time-budget=12000 --run-all-compositor-stages-before-draw \
  --print-to-pdf="$OUT" "file://$IN"
echo "Wrote $OUT"
