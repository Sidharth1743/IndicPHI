# Stage 4b — Translation Audit

- model: `sarvam-105b`
- rows_translated: **132**
- rows_skipped: `6`
- soft_fail_count: **22**
- script_fail_count: `22`
- generator_repaired_count: `4`
- max_workers: `24`

## Soft failures (audited — not silent)

- `85cdb818ce5740ed85a9bfb29cf57098` · `er_triage_notes` · `gu` · error=script_purity_failed:target_script_ratio:0.000<0.35 attempt=1
- `8c410a2e98134e9a91f1d50d5811a470` · `er_triage_notes` · `gu` · error=script_purity_failed:target_script_ratio:0.000<0.35 attempt=1;generator_repair_failed:target_script_ratio:0.000<0.35
- `c03b2ff49ffa439380a254bb9f8972f7` · `hospital_billing` · `kok` · error=script_purity_failed:target_script_ratio:0.000<0.35 attempt=1;generator_repair_failed:target_script_ratio:0.000<0.35
- `18a30340943543c59236f8f4e9379b8d` · `asha_worker_note` · `ks` · error=script_purity_failed:target_script_ratio:0.000<0.35 attempt=1;generator_repair_failed:ok
- `18a30340943543c59236f8f4e9379b8d` · `automated_sms` · `ks` · error=script_purity_failed:wrong_indic_script:Devanagari>Arabic attempt=1;generator_repair_failed:ok
- `99d8e2b0dd9e42e6b270e50cb12c26c5` · `asha_worker_note` · `ks` · error=script_purity_failed:target_script_ratio:0.000<0.35 attempt=1;generator_repair_failed:target_script_ratio:0.000<0.35
- `99d8e2b0dd9e42e6b270e50cb12c26c5` · `insurance_claim` · `ks` · error=script_purity_failed:target_script_ratio:0.000<0.35 attempt=1
- `1e23bb4e93b0465fa42494aee52e02ef` · `hospital_billing` · `mni` · error=script_purity_failed:target_script_ratio:0.000<0.35 attempt=1;generator_repair_failed:target_script_ratio:0.000<0.35
- `1e23bb4e93b0465fa42494aee52e02ef` · `discharge_summary` · `mni` · error=script_purity_failed:target_script_ratio:0.000<0.35 attempt=1
- `1e23bb4e93b0465fa42494aee52e02ef` · `referral_letter` · `mni` · error=script_purity_failed:target_script_ratio:0.328<0.35 attempt=1;generator_repair_failed:target_script_ratio:0.000<0.35
- `d15c31be6c8e40a393e6e6f4f9562ea3` · `hospital_billing` · `mni` · error=script_purity_failed:target_script_ratio:0.000<0.35 attempt=1;generator_repair_failed:target_script_ratio:0.000<0.35
- `d15c31be6c8e40a393e6e6f4f9562ea3` · `discharge_summary` · `mni` · error=script_purity_failed:target_script_ratio:0.000<0.35 attempt=1;generator_repair_failed:target_script_ratio:0.000<0.35
- `d15c31be6c8e40a393e6e6f4f9562ea3` · `referral_letter` · `mni` · error=script_purity_failed:target_script_ratio:0.000<0.35 attempt=1;generator_repair_failed:target_script_ratio:0.000<0.35
- `6319018329714b92a0a64f8228dc39b6` · `prescription` · `ne` · error=script_purity_failed:target_script_ratio:0.082<0.35 attempt=1;generator_repair_failed:ok
- `49e7eef3f6644cc689038f044f77f052` · `opd_slip` · `sat` · error=Missing NM placeholder restore for ⟦NM6⟧;generator_repair_failed:target_script_ratio:0.000<0.35
- `49e7eef3f6644cc689038f044f77f052` · `phc_register` · `sat` · error=script_purity_failed:target_script_ratio:0.000<0.35 attempt=1
- `49e7eef3f6644cc689038f044f77f052` · `prescription` · `sat` · error=script_purity_failed:target_script_ratio:0.000<0.35 attempt=1;generator_repair_failed:target_script_ratio:0.000<0.35
- `c98c2d51b4ea4d0c947d6dfc0ee57383` · `automated_sms` · `sat` · error=script_purity_failed:wrong_indic_script:Devanagari>Ol Chiki attempt=1;generator_repair_failed:wrong_indic_script:Devanagari>Ol Chiki
- `c98c2d51b4ea4d0c947d6dfc0ee57383` · `insurance_claim` · `sat` · error=script_purity_failed:target_script_ratio:0.000<0.35 attempt=1;generator_repair_failed:target_script_ratio:0.000<0.35
- `5c09bf9c92bb4474a1a128379f250e86` · `discharge_summary` · `sd` · error=script_purity_failed:wrong_indic_script:Devanagari>Arabic attempt=1;generator_repair_failed:wrong_indic_script:Devanagari>Arabic
- `e9f9b9a22bcb47f28198db61b9bd4966` · `discharge_summary` · `sd` · error=script_purity_failed:wrong_indic_script:Devanagari>Arabic attempt=1;generator_repair_failed:wrong_indic_script:Devanagari>Arabic
- `e9f9b9a22bcb47f28198db61b9bd4966` · `referral_letter` · `sd` · error=script_purity_failed:wrong_indic_script:Devanagari>Arabic attempt=1;generator_repair_failed:target_script_ratio:0.011<0.35
