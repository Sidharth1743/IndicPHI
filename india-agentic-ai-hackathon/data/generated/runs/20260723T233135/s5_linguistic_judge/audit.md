# Stage 5 — Linguistic Judge Audit

- provider/model: `azure_foundry` / `grok-4.3`
- requests_per_minute: `500.0`
- timeout_s: `600.0`
- network_retries: `2`
- rows_judged: **138**
- soft_fail_count: **0**
- failure_count: **1**
- judge_repaired_count: **25**
- pass_rate: **0.993**
- label_distribution: `{'fail': 0.007246376811594203, 'pass': 0.9927536231884058}`
- positional_length_bias: `{'pearson_r': -0.057824713344977755, 'n': 138.0}`

## Failures (audited — not silent)

- `fe3a6e05b50a4eb1b679f5fba0c5440b` · `hospital_billing` · `sd` · score=0.65 soft=False · Sindhi Arabic-script prose and allow-listed tags are correct with plausible 75F TB+NCD billing content; meta leakage '(سادو نثر — قسم ناهي)' indicates instruction_drift.
