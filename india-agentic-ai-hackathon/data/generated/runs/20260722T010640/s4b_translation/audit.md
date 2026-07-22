# Stage 4b — Translation Audit

- model: `sarvam-105b`
- rows_translated: **114**
- rows_skipped: `24`
- soft_fail_count: **20**
- script_fail_count: `2`
- generator_repaired_count: `0`
- max_workers: `24`

## Soft failures (audited — not silent)

- `d89930b893984d4b96fbd0b492413321` · `hospital_billing` · `kn` · error=row_exception:The read operation timed out
- `c03b2ff49ffa439380a254bb9f8972f7` · `hospital_billing` · `kok` · error=row_exception:The read operation timed out
- `fc0833a3fd3a4916849cba96e415af4b` · `hospital_billing` · `kok` · error=row_exception:The read operation timed out
- `fc0833a3fd3a4916849cba96e415af4b` · `discharge_summary` · `kok` · error=row_exception:The read operation timed out
- `18a30340943543c59236f8f4e9379b8d` · `asha_worker_note` · `ks` · error=row_exception:The read operation timed out;dedicated_translate_failed:Translation lost or altered name/place TYPE 'RELIGION' (placeholder ⟦NM5⟧)
- `99d8e2b0dd9e42e6b270e50cb12c26c5` · `phc_register` · `ks` · error=row_exception:The read operation timed out;dedicated_translate_failed:Translation lost or altered name/place TYPE 'HOSPITAL_NAME' (placeholder ⟦NM0⟧)
- `80435bdcef24479390d6e6ae0b2aeeb1` · `hospital_billing` · `ml` · error=row_exception:The read operation timed out
- `1e23bb4e93b0465fa42494aee52e02ef` · `referral_letter` · `mni` · error=row_exception:The read operation timed out;dedicated_translate_failed:Translation lost protected ID tag '[[MRN|MRN-THB-2024-001]]'
- `d15c31be6c8e40a393e6e6f4f9562ea3` · `discharge_summary` · `mni` · error=row_exception:The read operation timed out;dedicated_translate_failed:Translation lost protected ID tag '[[PHONE_NUMBER|9876543210]]'
- `22eae34bd622448286f2f69f2f795893` · `er_triage_notes` · `pa` · error=row_exception:The read operation timed out
- `22eae34bd622448286f2f69f2f795893` · `telemedicine_transcript` · `pa` · error=row_exception:The read operation timed out
- `24405a884af14bcba6e9c3657baebf83` · `er_triage_notes` · `pa` · error=row_exception:The read operation timed out
- `22ef884ce12247309d07fc3f601a3c59` · `lab_report` · `sa` · error=row_exception:The read operation timed out
- `6e943dc3578249e38b9e61705d0912a9` · `prescription` · `sa` · error=row_exception:The read operation timed out
- `49e7eef3f6644cc689038f044f77f052` · `opd_slip` · `sat` · error=row_exception:The read operation timed out;dedicated_translate_failed:Translation lost or altered name/place TYPE 'HOSPITAL_NAME' (placeholder ⟦NM0⟧)
- `49e7eef3f6644cc689038f044f77f052` · `prescription` · `sat` · error=row_exception:The read operation timed out;dedicated_translate_failed:Translation lost protected ID tag '[[AGE|32]]'
- `c98c2d51b4ea4d0c947d6dfc0ee57383` · `asha_worker_note` · `sat` · error=script_purity_failed:wrong_indic_script:Devanagari>Ol Chiki attempt=1
- `c98c2d51b4ea4d0c947d6dfc0ee57383` · `insurance_claim` · `sat` · error=script_purity_failed:target_script_ratio:0.000<0.35 attempt=1
- `5c09bf9c92bb4474a1a128379f250e86` · `discharge_summary` · `sd` · error=row_exception:The read operation timed out
- `200f6b68373b4d389065d55262ec7847` · `automated_sms` · `te` · error=tag_restore_or_translate_failed:Translation lost or altered name/place TYPE 'DOCTOR_NAME' (placeholder ⟦NM1⟧)
