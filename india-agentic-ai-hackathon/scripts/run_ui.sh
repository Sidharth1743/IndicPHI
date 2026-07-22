#!/usr/bin/env bash
# Start the HackGrid pipeline demo API (and optionally print UI instructions).
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

HOST="${HOST:-127.0.0.1}"
PORT="${PORT:-8765}"

usage() {
  cat <<'EOF'
Usage: ./scripts/run_ui.sh [--host HOST] [--port PORT]

  Starts FastAPI (uvicorn) for the pipeline demo UI.
  Frontend (separate terminal):  cd ui && npm run dev

  API:  http://127.0.0.1:8765
  UI:   http://127.0.0.1:5173
EOF
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --host) HOST="${2:?}"; shift 2 ;;
    --port) PORT="${2:?}"; shift 2 ;;
    -h|--help) usage; exit 0 ;;
    *) echo "Unknown arg: $1" >&2; usage; exit 1 ;;
  esac
done

if [[ -f .env ]]; then
  set -a
  # shellcheck disable=SC1091
  source .env
  set +a
elif [[ -f ../.env ]]; then
  echo "[ui] Tip: ln -s ../.env .env  (do not commit secrets)" >&2
fi

echo "[ui] API → http://${HOST}:${PORT}"
echo "[ui] Frontend: cd ui && npm run dev  → http://127.0.0.1:5173"
echo "[ui] Replay a past run via POST /api/replay/{run_id} (e.g. 20260721T095916)"

if [[ -x "$ROOT/.venv/bin/uvicorn" ]]; then
  exec "$ROOT/.venv/bin/uvicorn" main.ui_api.app:app --host "$HOST" --port "$PORT" --reload
fi
exec uv run uvicorn main.ui_api.app:app --host "$HOST" --port "$PORT" --reload
