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
- positional_length_bias: `{'pearson_r': 0.13347925038857067, 'n': 20.0}`

## Failures (audited — not silent)

- `89d785f5c9f64f119b428efc6d0c259e` · `telemedicine_transcript` · `bn` · score=0.45 soft=False · Chat prose mostly Romanized Latin script after opening lines; expected Bengali script for clinical narrative.
- `396f437fcf6a45e6b7f38f4fe5cf5e48` · `prescription` · `gu` · score=0.25 soft=False · All clinical prose in English; Gujarati script required for narrative.
