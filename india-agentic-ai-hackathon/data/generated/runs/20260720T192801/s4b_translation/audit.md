# Stage 4b — Translation Audit

- model: `sarvam-105b`
- rows_translated: **66**
- rows_skipped: `3`
- soft_fail_count: **9**
- script_fail_count: `9`
- generator_repaired_count: `5`
- max_workers: `24`

## Soft failures (audited — not silent)

- `2a0042e543f7400299209a84f31ceab7` · `er_triage_notes` · `brx` · error=script_purity_failed:target_script_ratio:0.000<0.35 attempt=1;generator_repair_failed:Sarvam HTTP 500: {"error":{"message":"Model call failed: Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': \"Function id '267194f7-f0a1-43cc-814b-83e44d440f2c': DEGRADED function cannot be invoked\"}","code":"model_call_failed","request_id":"20260720_c32f2a23-00ee-4269-9470-76dbde8dce2c"}}
- `442b760204fb4430b6745545930228cd` · `prescription` · `ks` · error=script_purity_failed:target_script_ratio:0.000<0.35 attempt=1;generator_repair_failed:target_script_ratio:0.000<0.35
- `51fc0c57ffcc40c6ae5d2fb055d07030` · `opd_slip` · `mni` · error=script_purity_failed:target_script_ratio:0.000<0.35 attempt=1;generator_repair_failed:wrong_indic_script:Devanagari>Meitei
- `51fc0c57ffcc40c6ae5d2fb055d07030` · `phc_register` · `mni` · error=script_purity_failed:target_script_ratio:0.000<0.35 attempt=1;generator_repair_failed:Sarvam HTTP 500: {"error":{"message":"Model call failed: Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': \"Function id '267194f7-f0a1-43cc-814b-83e44d440f2c': DEGRADED function cannot be invoked\"}","code":"model_call_failed","request_id":"20260720_9236bae5-964f-4d80-98b8-e617a994c551"}}
- `01f011a8da4d401ca4ff9810f7a35a19` · `insurance_claim` · `or` · error=script_purity_failed:target_script_ratio:0.000<0.35 attempt=1;generator_repair_failed:target_script_ratio:0.002<0.35
- `944cf9bf2c4d48b2974bb723f704bded` · `referral_letter` · `sat` · error=script_purity_failed:target_script_ratio:0.000<0.35 attempt=1;generator_repair_failed:wrong_indic_script:Devanagari>Ol Chiki
- `944cf9bf2c4d48b2974bb723f704bded` · `radiology_report` · `sat` · error=script_purity_failed:target_script_ratio:0.000<0.35 attempt=1;generator_repair_failed:target_script_ratio:0.047<0.35
- `944cf9bf2c4d48b2974bb723f704bded` · `er_triage_notes` · `sat` · error=script_purity_failed:target_script_ratio:0.000<0.35 attempt=1;generator_repair_failed:target_script_ratio:0.343<0.35
- `68da8d4342bc4e28a1a4cd69a55cc86f` · `telemedicine_transcript` · `sd` · error=script_purity_failed:wrong_indic_script:Devanagari>Arabic attempt=1;generator_repair_failed:wrong_indic_script:Devanagari>Arabic
