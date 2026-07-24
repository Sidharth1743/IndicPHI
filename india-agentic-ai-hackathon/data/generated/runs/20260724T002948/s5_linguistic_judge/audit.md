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
- positional_length_bias: `{'pearson_r': -0.25534514053756435, 'n': 3.0}`

## Failures (audited — not silent)

- `02efb3b1960548978e14d333bab94234` · `radiology_report` · `ta` · score=0.25 soft=False · All clinical prose in English; Tamil script required for narrative body.
