#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"
export PYTHONPATH="${ROOT}${PYTHONPATH:+:$PYTHONPATH}"
CONFIG="${PIPELINE_CONFIG:-configs/synthetic-data/pipeline.yaml}"
if [[ -x "$ROOT/.venv/bin/python" ]]; then
  PY="$ROOT/.venv/bin/python"
elif [[ -x "$ROOT/../.venv/bin/python" ]]; then
  PY="$ROOT/../.venv/bin/python"
else
  PY="python3"
fi

exec "$PY" -m main.designers.linguistic_judge --config "$CONFIG" "$@"
