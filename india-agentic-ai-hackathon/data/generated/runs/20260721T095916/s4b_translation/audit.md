# Stage 4b — Translation Audit

- model: `sarvam-105b`
- rows_translated: **66**
- rows_skipped: `3`
- soft_fail_count: **9**
- script_fail_count: `9`
- generator_repaired_count: `1`
- max_workers: `24`

## Soft failures (audited — not silent)

- `a24958482d8b463ab3daeee28d5f5365` · `automated_sms` · `brx` · error=script_purity_failed:wrong_indic_script:Bengali>Devanagari attempt=1;generator_repair_failed:wrong_indic_script:Bengali>Devanagari
- `217fa134e0d64da4962f287453b86c70` · `prescription` · `ks` · error=script_purity_failed:target_script_ratio:0.000<0.35 attempt=1;generator_repair_failed:target_script_ratio:0.000<0.35
- `217fa134e0d64da4962f287453b86c70` · `insurance_claim` · `ks` · error=script_purity_failed:target_script_ratio:0.000<0.35 attempt=1;generator_repair_failed:target_script_ratio:0.000<0.35
- `217fa134e0d64da4962f287453b86c70` · `asha_worker_note` · `ks` · error=script_purity_failed:target_script_ratio:0.000<0.35 attempt=1;generator_repair_failed:target_script_ratio:0.000<0.35
- `1e23bb4e93b0465fa42494aee52e02ef` · `telemedicine_transcript` · `mni` · error=script_purity_failed:wrong_indic_script:Devanagari>Meitei attempt=1;generator_repair_failed:wrong_indic_script:Devanagari>Meitei
- `1e23bb4e93b0465fa42494aee52e02ef` · `surgical_note` · `mni` · error=script_purity_failed:wrong_indic_script:Devanagari>Meitei attempt=1;generator_repair_failed:target_script_ratio:0.010<0.35
- `1e23bb4e93b0465fa42494aee52e02ef` · `lab_report` · `mni` · error=script_purity_failed:target_script_ratio:0.000<0.35 attempt=1;generator_repair_failed:target_script_ratio:0.000<0.35
- `7604eaf4ec554261b752518c0f8a656e` · `referral_letter` · `sat` · error=script_purity_failed:wrong_indic_script:Devanagari>Ol Chiki attempt=1
- `7604eaf4ec554261b752518c0f8a656e` · `er_triage_notes` · `sat` · error=script_purity_failed:target_script_ratio:0.000<0.35 attempt=1;generator_repair_failed:target_script_ratio:0.000<0.35
