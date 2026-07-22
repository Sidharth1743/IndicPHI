# Stages 7–8 — Curation Audit

- rows_in: **126**
- rows_out: **69**
- dedup_dropped: **0**
- dedup_text_mode: `english_pivot_or_masked`
- discarded_by_balance: **52**
- pre_balance_counts: `{'as': 5, 'bn': 6, 'brx': 3, 'doi': 6, 'en': 6, 'gu': 6, 'hi': 4, 'kn': 5, 'kok': 6, 'ks': 6, 'mai': 6, 'ml': 4, 'mni': 4, 'mr': 6, 'ne': 6, 'or': 6, 'pa': 6, 'sa': 5, 'sat': 3, 'sd': 4, 'ta': 6, 'te': 6, 'ur': 6}`
- language_counts_out: `{'as': 3, 'bn': 3, 'brx': 3, 'doi': 3, 'en': 3, 'gu': 3, 'hi': 3, 'kn': 3, 'kok': 3, 'ks': 3, 'mai': 3, 'ml': 3, 'mni': 3, 'mr': 3, 'ne': 3, 'or': 3, 'pa': 3, 'sa': 3, 'sat': 3, 'sd': 3, 'ta': 3, 'te': 3, 'ur': 3}`
- balancing_warning: `large_balance_discard: discarded 52/121 rows (43.0%) while equalizing to 3 docs/language`
- balancing: `{'enabled': True, 'equalize_mode': True, 'target_docs_per_language': 3, 'min_docs_per_language': None, 'allow_underfill': True, 'pre_balance_counts': {'as': 5, 'bn': 6, 'brx': 3, 'doi': 6, 'en': 6, 'gu': 6, 'hi': 4, 'kn': 5, 'kok': 6, 'ks': 6, 'mai': 6, 'ml': 4, 'mni': 4, 'mr': 6, 'ne': 6, 'or': 6, 'pa': 6, 'sa': 5, 'sat': 3, 'sd': 4, 'ta': 6, 'te': 6, 'ur': 6}, 'per_language': {'as': 3, 'bn': 3, 'brx': 3, 'doi': 3, 'en': 3, 'gu': 3, 'hi': 3, 'kn': 3, 'kok': 3, 'ks': 3, 'mai': 3, 'ml': 3, 'mni': 3, 'mr': 3, 'ne': 3, 'or': 3, 'pa': 3, 'sa': 3, 'sat': 3, 'sd': 3, 'ta': 3, 'te': 3, 'ur': 3}, 'discarded_by_balance': 52, 'discard_ratio': 0.4298, 'rows_out': 69, 'underfilled': {}, 'warning': 'large_balance_discard: discarded 52/121 rows (43.0%) while equalizing to 3 docs/language'}`
