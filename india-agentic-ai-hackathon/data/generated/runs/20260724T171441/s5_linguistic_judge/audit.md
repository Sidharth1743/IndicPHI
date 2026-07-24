# Stage 5 — Linguistic Judge Audit

- provider/model: `azure_foundry` / `grok-4.3`
- requests_per_minute: `500.0`
- timeout_s: `600.0`
- network_retries: `4`
- rows_judged: **3**
- soft_fail_count: **0**
- failure_count: **1**
- judge_repaired_count: **0**
- pass_rate: **0.667**
- label_distribution: `{'fail': 0.3333333333333333, 'pass': 0.6666666666666666}`
- positional_length_bias: `{'pearson_r': 0.3050738315369815, 'n': 3.0}`

## Failures (audited — not silent)

- `7bf3bb21a61f42a2b7508e16d069b22f` · `asha_worker_note` · `bn` · score=0.6 soft=False · Odia script in 'হিতଧିକାରୀ' breaks expected Bengali prose; all other elements (tags, content, persona fit) acceptable.
