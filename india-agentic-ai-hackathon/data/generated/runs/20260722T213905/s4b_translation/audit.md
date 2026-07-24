# Stage 4b — Translation Audit

- model: `sarvam-105b`
- rows_translated: **49**
- rows_skipped: `20`
- soft_fail_count: **17**
- script_fail_count: `0`
- generator_repaired_count: `0`
- max_workers: `12`

## Soft failures (audited — not silent)

- `269a94e437d84643b728d5b86d5d08be` · `automated_sms` · `brx` · error=tag_restore_or_translate_failed:None
- `269a94e437d84643b728d5b86d5d08be` · `hospital_billing` · `brx` · error=tag_restore_or_translate_failed:None
- `e6a759d47c084de984729dfaf40785e1` · `hospital_billing` · `doi` · error=tag_restore_or_translate_failed:None
- `e6a759d47c084de984729dfaf40785e1` · `discharge_summary` · `doi` · error=tag_restore_or_translate_failed:None
- `e6a759d47c084de984729dfaf40785e1` · `referral_letter` · `doi` · error=tag_restore_or_translate_failed:None
- `1bd09fe5a4884629b02cbfd7660b402c` · `asha_worker_note` · `ks` · error=tag_restore_or_translate_failed:None
- `1bd09fe5a4884629b02cbfd7660b402c` · `automated_sms` · `ks` · error=tag_restore_or_translate_failed:None
- `1bd09fe5a4884629b02cbfd7660b402c` · `insurance_claim` · `ks` · error=tag_restore_or_translate_failed:None
- `2f97625028784d7ab66673d76e697478` · `phc_register` · `mni` · error=tag_restore_or_translate_failed:None
- `6e943dc3578249e38b9e61705d0912a9` · `asha_worker_note` · `sa` · error=tag_restore_or_translate_failed:None
- `6e943dc3578249e38b9e61705d0912a9` · `automated_sms` · `sa` · error=tag_restore_or_translate_failed:None
- `b5204bb0fe954a2cb47f1c994a300872` · `er_triage_notes` · `sat` · error=tag_restore_or_translate_failed:None
- `b5204bb0fe954a2cb47f1c994a300872` · `telemedicine_transcript` · `sat` · error=tag_restore_or_translate_failed:None
- `b5204bb0fe954a2cb47f1c994a300872` · `opd_slip` · `sat` · error=tag_restore_or_translate_failed:None
- `e9ec69ab351340d49920d8203b96c015` · `asha_worker_note` · `sd` · error=tag_restore_or_translate_failed:None
- `e9ec69ab351340d49920d8203b96c015` · `phc_register` · `sd` · error=tag_restore_or_translate_failed:None
- `e9ec69ab351340d49920d8203b96c015` · `automated_sms` · `sd` · error=tag_restore_or_translate_failed:None
