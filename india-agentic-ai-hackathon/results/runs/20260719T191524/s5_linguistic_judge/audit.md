# Stage 5 — Linguistic Judge Audit

- provider/model: `azure_foundry` / `grok-4.3`
- requests_per_minute: `500.0`
- timeout_s: `600.0`
- network_retries: `4`
- rows_judged: **20**
- soft_fail_count: **0**
- failure_count: **2**
- pass_rate: **0.900**
- label_distribution: `{'fail': 0.1, 'pass': 0.9}`
- positional_length_bias: `{'pearson_r': -0.1429200991531435, 'n': 20.0}`

## Failures (audited — not silent)

- `396f437fcf6a45e6b7f38f4fe5cf5e48` · `opd_slip` · `gu` · score=0.3 soft=False · Clinical prose is predominantly English with sporadic Gujarati insertions instead of full Gujarati narrative as required; code-mixing violates script/language rule despite allowed Latin tags.
- `93bac4c7fd9e4e2bbdf66866e9203b8b` · `surgical_note` · `gu` · score=0.3 soft=False · Operative note format with psych admission content only; no procedure/findings; relative name gender implausible (Ramesh Devi as husband).
