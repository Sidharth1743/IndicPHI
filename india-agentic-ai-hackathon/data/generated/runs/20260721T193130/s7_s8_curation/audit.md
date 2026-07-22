# Stages 7–8 — Curation Audit

- rows_in: **122**
- rows_out: **46**
- dedup_dropped: **0**
- dedup_text_mode: `english_pivot_or_masked`
- discarded_by_balance: **68**
- pre_balance_counts: `{'as': 5, 'bn': 5, 'brx': 2, 'doi': 5, 'en': 5, 'gu': 6, 'hi': 5, 'kn': 5, 'kok': 5, 'ks': 6, 'mai': 6, 'ml': 5, 'mni': 2, 'mr': 5, 'ne': 6, 'or': 5, 'pa': 6, 'sa': 6, 'sat': 3, 'sd': 4, 'ta': 6, 'te': 6, 'ur': 5}`
- language_counts_out: `{'as': 2, 'bn': 2, 'brx': 2, 'doi': 2, 'en': 2, 'gu': 2, 'hi': 2, 'kn': 2, 'kok': 2, 'ks': 2, 'mai': 2, 'ml': 2, 'mni': 2, 'mr': 2, 'ne': 2, 'or': 2, 'pa': 2, 'sa': 2, 'sat': 2, 'sd': 2, 'ta': 2, 'te': 2, 'ur': 2}`
- balancing_warning: `large_balance_discard: discarded 68/114 rows (59.6%) while equalizing to 2 docs/language`
- balancing: `{'enabled': True, 'equalize_mode': True, 'target_docs_per_language': 2, 'min_docs_per_language': None, 'allow_underfill': True, 'pre_balance_counts': {'as': 5, 'bn': 5, 'brx': 2, 'doi': 5, 'en': 5, 'gu': 6, 'hi': 5, 'kn': 5, 'kok': 5, 'ks': 6, 'mai': 6, 'ml': 5, 'mni': 2, 'mr': 5, 'ne': 6, 'or': 5, 'pa': 6, 'sa': 6, 'sat': 3, 'sd': 4, 'ta': 6, 'te': 6, 'ur': 5}, 'per_language': {'as': 2, 'bn': 2, 'brx': 2, 'doi': 2, 'en': 2, 'gu': 2, 'hi': 2, 'kn': 2, 'kok': 2, 'ks': 2, 'mai': 2, 'ml': 2, 'mni': 2, 'mr': 2, 'ne': 2, 'or': 2, 'pa': 2, 'sa': 2, 'sat': 2, 'sd': 2, 'ta': 2, 'te': 2, 'ur': 2}, 'discarded_by_balance': 68, 'discard_ratio': 0.5965, 'rows_out': 46, 'underfilled': {}, 'warning': 'large_balance_discard: discarded 68/114 rows (59.6%) while equalizing to 2 docs/language'}`
