# Stage 4b — Translation Audit

- model: `sarvam-105b`
- rows_translated: **124**
- rows_skipped: `14`
- soft_fail_count: **8**
- script_fail_count: `0`
- generator_repaired_count: `3`
- max_workers: `24`

## Soft failures (audited — not silent)

- `1e23bb4e93b0465fa42494aee52e02ef` · `hospital_billing` · `mni` · error=row_exception:The read operation timed out
- `d15c31be6c8e40a393e6e6f4f9562ea3` · `hospital_billing` · `mni` · error=row_exception:The read operation timed out
- `d15c31be6c8e40a393e6e6f4f9562ea3` · `discharge_summary` · `mni` · error=row_exception:The read operation timed out
- `d15c31be6c8e40a393e6e6f4f9562ea3` · `referral_letter` · `mni` · error=row_exception:The read operation timed out
- `49e7eef3f6644cc689038f044f77f052` · `opd_slip` · `sat` · error=row_exception:The read operation timed out
- `c98c2d51b4ea4d0c947d6dfc0ee57383` · `asha_worker_note` · `sat` · error=row_exception:The read operation timed out
- `c98c2d51b4ea4d0c947d6dfc0ee57383` · `insurance_claim` · `sat` · error=row_exception:The read operation timed out
- `9952571815ae4558a362507fc4a9539f` · `surgical_note` · `ur` · error=row_exception:The read operation timed out
