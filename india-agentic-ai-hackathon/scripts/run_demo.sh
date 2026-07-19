#!/usr/bin/env bash
# Demo entrypoint: run smoke (or point at an existing latest run) and print
# where to find failures.md + the eval report for judges.
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

RUN_SMOKE=1
CONFIG="configs/synthetic-data/pipeline.smoke.yaml"

usage() {
  cat <<'EOF'
Usage: ./scripts/run_demo.sh [--no-run] [--config PATH]

  --no-run     Skip live API smoke; only print paths to samples + reports
  --config     Pipeline YAML (default: configs/synthetic-data/pipeline.smoke.yaml)
EOF
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --no-run) RUN_SMOKE=0; shift ;;
    --config) CONFIG="${2:?}"; shift 2 ;;
    -h|--help) usage; exit 0 ;;
    *) echo "Unknown arg: $1" >&2; usage; exit 1 ;;
  esac
done

echo "=== HackGrid demo ==="
echo "Root: $ROOT"
echo "Docs: docs/architecture.md | docs/demo-script.md | docs/evaluation-plan.md"
echo "Eval: results/eval_report.md"
echo "Samples: data/samples/"
echo

if [[ "$RUN_SMOKE" -eq 1 ]]; then
  if [[ ! -f .env && ! -f ../.env ]]; then
    echo "[demo] No .env found. Copy configs/nim.env.example → .env or use --no-run." >&2
    echo "[demo] Continuing only if keys are already exported in the shell." >&2
  fi
  # Prefer local .env; also allow parent monorepo .env via symlink/copy by user
  if [[ -f ../.env && ! -f .env ]]; then
    echo "[demo] Tip: ln -s ../.env .env  (do not commit secrets)" >&2
  fi
  echo "[demo] Running smoke: $CONFIG"
  ./scripts/smoke_test.sh "$CONFIG"
else
  echo "[demo] --no-run: skipping live generation"
fi

LATEST="${ROOT}/results/runs/latest"
echo
if [[ -L "$LATEST" || -d "$LATEST" ]]; then
  echo "[demo] Latest packaged run: $LATEST"
  [[ -f "$LATEST/failures.md" ]] && echo "[demo] Failures audit: $LATEST/failures.md"
else
  echo "[demo] No results/runs/latest yet."
fi
LIVE="${ROOT}/data/generated/runs/latest"
if [[ -L "$LIVE" || -d "$LIVE" ]]; then
  echo "[demo] Latest live run: $LIVE"
fi
echo "[demo] Logs: ${ROOT}/results/logs/"
echo "[demo] Summary report: ${ROOT}/results/eval_report.md"
echo "=== Done ==="
