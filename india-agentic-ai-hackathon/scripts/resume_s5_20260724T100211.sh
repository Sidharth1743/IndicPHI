#!/usr/bin/env bash
# After S4b finalize: run S5+ on the host (not agent sandbox).
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

# Stop any sandboxed poison run still writing S5 soft-fails
pkill -9 -f 'run_pipeline.*20260724T100211' 2>/dev/null || true
sleep 1

# Drop network-poisoned S5 checkpoint rows (keep only ok)
python3 - <<'PY'
import json
from pathlib import Path
p = Path('data/generated/runs/20260724T100211/s5_linguistic_judge/checkpoint.jsonl')
p.parent.mkdir(parents=True, exist_ok=True)
if p.exists() and p.stat().st_size:
    bak = p.with_suffix('.jsonl.bak_pre_s5_resume')
    bak.write_text(p.read_text())
    kept = []
    by = {}
    for line in p.read_text().splitlines():
        if not line.strip():
            continue
        r = json.loads(line)
        by[r['row_key']] = r
    for r in by.values():
        if r.get('status') == 'ok':
            kept.append(r)
    p.write_text(''.join(json.dumps(r, ensure_ascii=False) + '\n' for r in kept))
    print(f'[s5] checkpoint kept ok={len(kept)} (backup {bak})')
else:
    p.write_text('')
    print('[s5] checkpoint empty — full judge')
PY

exec .venv/bin/python -u -m main.pipeline.run_pipeline \
  --config data/generated/runs/20260724T100211/pipeline.resolved.yaml \
  --run-id 20260724T100211 \
  --from-stage s5_linguistic_judge \
  2>&1 | tee /tmp/pipeline_diversity_seed5051_n506_s5.log
