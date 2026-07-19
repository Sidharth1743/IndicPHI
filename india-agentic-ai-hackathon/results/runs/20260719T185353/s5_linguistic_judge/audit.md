# Stage 5 — Linguistic Judge Audit

- provider/model: `azure_foundry` / `grok-4.3`
- requests_per_minute: `500.0`
- rows_judged: **10**
- failure_count: **1**
- pass_rate: **0.900**
- label_distribution: `{'fail': 0.1, 'pass': 0.9}`
- positional_length_bias: `{'pearson_r': -0.21226501072305431, 'n': 10.0}`

## Failures (audited — not silent)

- `396f437fcf6a45e6b7f38f4fe5cf5e48` · `er_triage_notes` · `gu` · score=0.55 · None
