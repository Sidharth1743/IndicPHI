# Stage 6 — Deterministic Auditor

- rows_audited: **123**
- rows_failed: **4**
- pass_rate: **0.967**
- mean_dics: **0.994**
- mean_ecr: **1.000**
- mean_bcr: **0.0000**

## Failures (audited — not silent)

- `57e0ccc76318480b91dca7f2d464c122` · `referral_letter` · `gu` · ['dics_below_threshold:0.7142857142857143']
- `5c5a472d66774bdc9e232a4893422f0c` · `referral_letter` · `mr` · ['dics_below_threshold:0.5']
- `825c4438c02440dc90d3ddec7ffec8ee` · `hospital_billing` · `sd` · ['persona_age_mismatch']
- `ce942a5fb5644181ac0db94b6c9c1314` · `insurance_claim` · `ta` · ['phi_residue:1']
