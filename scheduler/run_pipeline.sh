#!/usr/bin/env bash
set -euo pipefail

SYMBOL="${1:-AAPL}"
curl -sS -X POST "http://127.0.0.1:8000/predict?symbol=${SYMBOL}" >/tmp/stock-ai-last-run.json
