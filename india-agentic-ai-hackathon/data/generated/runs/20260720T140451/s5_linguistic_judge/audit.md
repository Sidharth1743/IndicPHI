# Stage 5 — Linguistic Judge Audit

- provider/model: `azure_foundry` / `grok-4.3`
- requests_per_minute: `500.0`
- timeout_s: `600.0`
- network_retries: `4`
- rows_judged: **10**
- soft_fail_count: **0**
- failure_count: **2**
- pass_rate: **0.800**
- label_distribution: `{'fail': 0.2, 'pass': 0.8}`
- positional_length_bias: `{'pearson_r': 0.2594746790899271, 'n': 10.0}`

## Failures (audited — not silent)

- `6549c3143bf44b4d81915ab4b5eea4ef` · `er_triage_notes` · `gu` · score=0.3 soft=False · Clinical prose body is English-dominant; only isolated Gujarati fragments present despite gu/Gujarati requirement.
- `f6d9e443342646fdb70285e45d2a3a48` · `automated_sms` · `te` · score=0.6 soft=False · PATIENT_NAME value in Latin script; prose otherwise Telugu but entity shift violates script expectation for document.
