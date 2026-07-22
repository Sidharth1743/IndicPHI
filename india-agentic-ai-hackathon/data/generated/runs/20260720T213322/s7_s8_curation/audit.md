# Stages 7–8 — Curation Audit

- rows_in: **48**
- rows_out: **20**
- dedup_dropped: **0**
- dedup_text_mode: `english_pivot_or_masked`
- discarded_by_balance: **26**
- pre_balance_counts: `{'as': 2, 'bn': 2, 'doi': 2, 'en': 2, 'gu': 3, 'hi': 2, 'kn': 3, 'kok': 3, 'ks': 1, 'mai': 3, 'ml': 3, 'mr': 3, 'ne': 3, 'or': 3, 'pa': 1, 'sa': 2, 'sd': 1, 'ta': 2, 'te': 2, 'ur': 3}`
- language_counts_out: `{'as': 1, 'bn': 1, 'doi': 1, 'en': 1, 'gu': 1, 'hi': 1, 'kn': 1, 'kok': 1, 'ks': 1, 'mai': 1, 'ml': 1, 'mr': 1, 'ne': 1, 'or': 1, 'pa': 1, 'sa': 1, 'sd': 1, 'ta': 1, 'te': 1, 'ur': 1}`
- balancing_warning: `large_balance_discard: discarded 26/46 rows (56.5%) while equalizing to 1 docs/language`
- balancing: `{'enabled': True, 'equalize_mode': True, 'target_docs_per_language': 1, 'min_docs_per_language': None, 'allow_underfill': True, 'pre_balance_counts': {'as': 2, 'bn': 2, 'doi': 2, 'en': 2, 'gu': 3, 'hi': 2, 'kn': 3, 'kok': 3, 'ks': 1, 'mai': 3, 'ml': 3, 'mr': 3, 'ne': 3, 'or': 3, 'pa': 1, 'sa': 2, 'sd': 1, 'ta': 2, 'te': 2, 'ur': 3}, 'per_language': {'as': 1, 'bn': 1, 'doi': 1, 'en': 1, 'gu': 1, 'hi': 1, 'kn': 1, 'kok': 1, 'ks': 1, 'mai': 1, 'ml': 1, 'mr': 1, 'ne': 1, 'or': 1, 'pa': 1, 'sa': 1, 'sd': 1, 'ta': 1, 'te': 1, 'ur': 1}, 'discarded_by_balance': 26, 'discard_ratio': 0.5652, 'rows_out': 20, 'underfilled': {}, 'warning': 'large_balance_discard: discarded 26/46 rows (56.5%) while equalizing to 1 docs/language'}`
