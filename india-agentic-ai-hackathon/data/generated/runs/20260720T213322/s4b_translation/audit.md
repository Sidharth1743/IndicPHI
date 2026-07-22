# Stage 4b — Translation Audit

- model: `sarvam-105b`
- rows_translated: **65**
- rows_skipped: `4`
- soft_fail_count: **9**
- script_fail_count: `8`
- generator_repaired_count: `1`
- max_workers: `24`

## Soft failures (audited — not silent)

- `8b08baf3bcbf412eaace2d648074de01` · `lab_report` · `bn` · error=no_valid_entity_tags_to_protect;invalid_type_tags:এম.আর.এন,রোগীর_নাম,বয়স,লিঙ্গ,ডক্টর_নাম,রোগী_আইডি,ফোন_নম্বর,জেলা,ছাত্র_আইডি
- `c56b228238e847d393141f0a17d86444` · `er_triage_notes` · `hi` · error=script_purity_failed:target_script_ratio:0.011<0.35 attempt=1;generator_repair_failed:target_script_ratio:0.000<0.35
- `442b760204fb4430b6745545930228cd` · `prescription` · `ks` · error=script_purity_failed:target_script_ratio:0.000<0.35 attempt=1;generator_repair_failed:target_script_ratio:0.000<0.35
- `51fc0c57ffcc40c6ae5d2fb055d07030` · `lab_report` · `mni` · error=script_purity_failed:target_script_ratio:0.000<0.35 attempt=1;generator_repair_failed:target_script_ratio:0.000<0.35
- `51fc0c57ffcc40c6ae5d2fb055d07030` · `opd_slip` · `mni` · error=script_purity_failed:wrong_indic_script:Bengali>Meitei attempt=1;generator_repair_failed:wrong_indic_script:Devanagari>Meitei
- `51fc0c57ffcc40c6ae5d2fb055d07030` · `phc_register` · `mni` · error=script_purity_failed:target_script_ratio:0.000<0.35 attempt=1;generator_repair_failed:wrong_indic_script:Devanagari>Meitei
- `944cf9bf2c4d48b2974bb723f704bded` · `referral_letter` · `sat` · error=Translation lost protected ID tag '[[AGE|32]]'
- `944cf9bf2c4d48b2974bb723f704bded` · `radiology_report` · `sat` · error=script_purity_failed:target_script_ratio:0.000<0.35 attempt=1
- `944cf9bf2c4d48b2974bb723f704bded` · `er_triage_notes` · `sat` · error=script_purity_failed:target_script_ratio:0.000<0.35 attempt=1;generator_repair_failed:target_script_ratio:0.000<0.35
