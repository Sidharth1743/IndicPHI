#!/usr/bin/env bash
# Small smoke: 10 languages × 1 persona × 1 doc → 10 docs (pipeline.smoke.yaml).
# Medium: configs/synthetic-data/pipeline.smoke.medium.yaml (20 docs).
# Writes timestamped results under data/generated/runs/<timestamp>/ + failures.md.
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"
export PYTHONPATH="${ROOT}${PYTHONPATH:+:$PYTHONPATH}"

CONFIG="configs/synthetic-data/pipeline.smoke.yaml"
EXTRA=()
if [[ $# -gt 0 && "${1}" != -* ]]; then
  CONFIG="$1"
  shift
fi
EXTRA=("$@")

if [[ -x "$ROOT/.venv/bin/python" ]]; then
  PY="$ROOT/.venv/bin/python"
elif [[ -x "$ROOT/../.venv/bin/python" ]]; then
  PY="$ROOT/../.venv/bin/python"
else
  PY="python3"
fi

exec "$PY" -m main.pipeline.run_pipeline \
  --config "$CONFIG" \
  ${EXTRA[@]+"${EXTRA[@]}"}
