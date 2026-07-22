# Stages 7–8 — Curation Audit

- rows_in: **100**
- rows_out: **22**
- dedup_dropped: **0**
- dedup_text_mode: `english_pivot_or_masked`
- discarded_by_balance: **70**
- pre_balance_counts: `{'as': 5, 'bn': 6, 'brx': 3, 'doi': 4, 'en': 3, 'gu': 4, 'hi': 6, 'kn': 5, 'kok': 5, 'ks': 3, 'mai': 5, 'ml': 4, 'mr': 4, 'ne': 5, 'or': 6, 'pa': 3, 'sa': 3, 'sat': 1, 'sd': 1, 'ta': 6, 'te': 5, 'ur': 5}`
- language_counts_out: `{'as': 1, 'bn': 1, 'brx': 1, 'doi': 1, 'en': 1, 'gu': 1, 'hi': 1, 'kn': 1, 'kok': 1, 'ks': 1, 'mai': 1, 'ml': 1, 'mr': 1, 'ne': 1, 'or': 1, 'pa': 1, 'sa': 1, 'sat': 1, 'sd': 1, 'ta': 1, 'te': 1, 'ur': 1}`
- balancing_warning: `large_balance_discard: discarded 70/92 rows (76.1%) while equalizing to 1 docs/language`
- balancing: `{'enabled': True, 'equalize_mode': True, 'target_docs_per_language': 1, 'min_docs_per_language': None, 'allow_underfill': True, 'pre_balance_counts': {'as': 5, 'bn': 6, 'brx': 3, 'doi': 4, 'en': 3, 'gu': 4, 'hi': 6, 'kn': 5, 'kok': 5, 'ks': 3, 'mai': 5, 'ml': 4, 'mr': 4, 'ne': 5, 'or': 6, 'pa': 3, 'sa': 3, 'sat': 1, 'sd': 1, 'ta': 6, 'te': 5, 'ur': 5}, 'per_language': {'as': 1, 'bn': 1, 'brx': 1, 'doi': 1, 'en': 1, 'gu': 1, 'hi': 1, 'kn': 1, 'kok': 1, 'ks': 1, 'mai': 1, 'ml': 1, 'mr': 1, 'ne': 1, 'or': 1, 'pa': 1, 'sa': 1, 'sat': 1, 'sd': 1, 'ta': 1, 'te': 1, 'ur': 1}, 'discarded_by_balance': 70, 'discard_ratio': 0.7609, 'rows_out': 22, 'underfilled': {}, 'warning': 'large_balance_discard: discarded 70/92 rows (76.1%) while equalizing to 1 docs/language'}`
