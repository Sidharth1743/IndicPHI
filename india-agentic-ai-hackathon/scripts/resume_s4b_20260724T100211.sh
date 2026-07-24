#!/usr/bin/env bash
# Resume S4b after DNS/timeout storm (docs: row checkpoint + recover language at S4b).
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

echo "[dns] $(getent hosts api.sarvam.ai | head -1 || echo 'FAIL — fix systemd-resolved / resolv.conf first')"
python3 - <<'PY'
import socket
print("[dns]", socket.getaddrinfo("api.sarvam.ai", 443)[0][4])
PY

exec .venv/bin/python -u -m main.pipeline.run_pipeline \
  --config data/generated/runs/20260724T100211/pipeline.resolved.yaml \
  --run-id 20260724T100211 \
  --from-stage s4b_translation \
  2>&1 | tee /tmp/pipeline_diversity_seed5051_n506_s4bresume.log
