# Stage 4b — Translation Audit

- model: `sarvam-105b`
- rows_translated: **18**
- rows_skipped: `2`
- soft_fail_count: **1**
- script_fail_count: `1`
- max_workers: `12`

## Soft failures (audited — not silent)

- `bfcd0a5ac1664137a563f86f8f72d85a` · `insurance_claim` · `ml` · error=script_purity_failed:target_script_ratio:0.000<0.35 attempt=1
