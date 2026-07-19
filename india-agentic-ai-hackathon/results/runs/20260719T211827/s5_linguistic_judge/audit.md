# Stage 5 — Linguistic Judge Audit

- provider/model: `azure_foundry` / `grok-4.3`
- requests_per_minute: `500.0`
- timeout_s: `600.0`
- network_retries: `4`
- rows_judged: **20**
- soft_fail_count: **0**
- failure_count: **3**
- pass_rate: **0.850**
- label_distribution: `{'fail': 0.15, 'pass': 0.85}`
- positional_length_bias: `{'pearson_r': -0.24518165378433013, 'n': 20.0}`

## Failures (audited — not silent)

- `bfcd0a5ac1664137a563f86f8f72d85a` · `insurance_claim` · `ml` · score=0.3 soft=False · All prose and labels in English; expected Malayalam script for narrative in ml TPA form.
- `648f69965d61431083f8e5566b64f74d` · `telemedicine_transcript` · `pa` · score=0.65 soft=False · Female doctor (Harpreet Kaur) uses masculine verb forms ('ਸਮਝਦਾ ਹਾਂ') and is addressed as 'ਸਰ'; all other elements (Gurmukhi prose, entity types, TB symptoms, persona anchors) align.
- `66f87f0087064abda3938f2c4aba879e` · `telemedicine_transcript` · `pa` · score=0.65 soft=False · Female persona uses repeated masculine verb forms (ਰਿਹਾ, ਖੰਘਦਾ, ਕਰਦਾ) in Punjabi prose; all entity tags and script otherwise valid.
