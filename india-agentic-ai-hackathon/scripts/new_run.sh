#!/usr/bin/env bash
# Create a timestamped run folder from a base config and print the resolved path.
# Usage:
#   source <(./scripts/new_run.sh)   # exports PIPELINE_CONFIG + PIPELINE_RUN_ID
#   ./scripts/new_run.sh --config configs/synthetic-data/pipeline.smoke.yaml
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"
export PYTHONPATH="${ROOT}${PYTHONPATH:+:$PYTHONPATH}"

CONFIG="${1:-configs/synthetic-data/pipeline.yaml}"
if [[ "${1:-}" == "--config" ]]; then
  CONFIG="${2:?}"
fi

eval "$(
  .venv/bin/python - <<PY
from pathlib import Path
from main.pipeline.config_io import REPO_ROOT
from main.pipeline.run_layout import materialize_run_config
cfg = (REPO_ROOT / "${CONFIG}").resolve()
run_id, resolved, _ = materialize_run_config(cfg)
print(f'export PIPELINE_RUN_ID={run_id}')
print(f'export PIPELINE_CONFIG={resolved}')
print(f'echo "[run] run_id={run_id}"')
print(f'echo "[run] config={resolved}"')
PY
)"
