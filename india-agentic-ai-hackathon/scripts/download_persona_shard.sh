#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUT_DIR="$ROOT/artifacts/hf_shards"
mkdir -p "$OUT_DIR"
cd "$OUT_DIR"

URL="https://huggingface.co/datasets/nvidia/Nemotron-Personas-India/resolve/main/data/en_IN-00000-of-00011.parquet"
OUT="en_IN-00000-of-00011.parquet"

echo "[download] starting $(date -Is)" | tee download.log
curl -L --fail --show-error --retry 10 --retry-delay 3 \
  -o "$OUT" "$URL" 2>&1 | tee -a download.log
echo "[download] done $(date -Is) size=$(stat -c%s "$OUT")" | tee -a download.log

"$ROOT/.venv/bin/python" - <<'PY'
import json
from collections import Counter
from pathlib import Path
import pyarrow.parquet as pq

path = Path("en_IN-00000-of-00011.parquet")
table = pq.read_table(path)
langs = Counter(table.column("first_language").to_pylist())
sample = {name: table.column(name)[0].as_py() for name in table.column_names}
probe = {
    "path": str(path.resolve()),
    "rows": table.num_rows,
    "cols": list(table.column_names),
    "first_language_counts": langs.most_common(),
    "sample_preview": {
        k: (v[:240] + "...") if isinstance(v, str) and len(v) > 240 else v
        for k, v in sample.items()
    },
}
out = Path("shard_probe.json")
out.write_text(json.dumps(probe, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print(f"[probe] rows={table.num_rows} langs={len(langs)} -> {out.resolve()}")
for name, count in langs.most_common(40):
    print(f"  {count:6d}  {name}")
PY
