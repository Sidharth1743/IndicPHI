# Results

Evidence from HackGrid **SDG synthetic-data** pipeline runs (not just failure notes).

| Path | Contents |
|------|----------|
| `runs/` | Full timestamped pipeline outputs (`s1`…`s9`, `failures.md`, `pipeline.resolved.yaml`, curated/GLiNER artifacts). `latest` → newest complete smoke. |
| `logs/` | Console logs from smoke / medium / resume runs. |
| `audits/` | Copied `failures_*.md` for quick reading of key runs. |
| `eval_report.md` | Summary of smoke metrics. |
| `screenshots/` | Demo screenshots (add as needed). |

Key runs:

- `runs/20260719T185353` — tiny smoke seed 101
- `runs/20260719T191524` — medium seed 202 (20 docs)
- `runs/20260719T211827` — medium seed 303 (20 docs) ← `latest`
