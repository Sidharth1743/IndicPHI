# Stage 5 — Linguistic Judge Audit

- provider/model: `azure_foundry` / `grok-4.3`
- requests_per_minute: `500.0`
- timeout_s: `600.0`
- network_retries: `4`
- rows_judged: **2**
- soft_fail_count: **0**
- failure_count: **2**
- judge_repaired_count: **0**
- pass_rate: **0.000**
- label_distribution: `{'fail': 1.0}`
- positional_length_bias: `{'pearson_r': 0.0, 'n': 2.0}`

## Failures (audited — not silent)

- `7bf3bb21a61f42a2b7508e16d069b22f` · `asha_worker_note` · `bn` · score=0.68 soft=False · Odia script in 'হিতଧିକାରୀ' label breaks Bengali prose requirement; single instance but still impurity in clinical note.
- `aacd23f3495f49f988205edb97f1e20e` · `discharge_summary` · `brx` · score=0.45 soft=False · Prose is Hindi (not Bodo) despite correct Devanagari script and valid entity tags.
