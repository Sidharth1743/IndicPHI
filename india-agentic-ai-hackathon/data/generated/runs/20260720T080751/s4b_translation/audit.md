# Stage 4b — Translation Audit

- model: `sarvam-105b`
- rows_translated: **18**
- rows_skipped: `2`
- soft_fail_count: **2**
- script_fail_count: `2`
- max_workers: `12`

## Soft failures (audited — not silent)

- `89d785f5c9f64f119b428efc6d0c259e` · `telemedicine_transcript` · `bn` · error=script_purity_failed:target_script_ratio:0.136<0.35 attempt=1
- `396f437fcf6a45e6b7f38f4fe5cf5e48` · `prescription` · `gu` · error=script_purity_failed:target_script_ratio:0.000<0.35 attempt=1
