"""Multilingual embedding-based semantic near-duplicate detection.

Runs **after** NeMo Curator fuzzy dedup on English-pivot / PHI-masked text.
Uses cosine similarity over bag-of-hashed character n-grams when
``sentence-transformers`` is unavailable (portable fallback), or a real
multilingual embedding model when installed.

This catches translated semantic duplicates that character MinHash on tagged
surface text cannot.
"""

from __future__ import annotations

import hashlib
import math
import re
from collections import defaultdict
from typing import Any, Mapping, Sequence

_WS_RE = re.compile(r"\s+")


class SemanticDedupError(RuntimeError):
    pass


def _tokenize(text: str, dim: int = 256, ngram: int = 4) -> list[float]:
    """Deterministic hashed n-gram bag (L2-normalized)."""
    clean = _WS_RE.sub(" ", text.lower()).strip()
    vec = [0.0] * dim
    if len(clean) < ngram:
        if clean:
            idx = int(hashlib.blake2b(clean.encode(), digest_size=4).hexdigest(), 16) % dim
            vec[idx] = 1.0
        return vec
    for i in range(len(clean) - ngram + 1):
        gram = clean[i : i + ngram]
        idx = int(hashlib.blake2b(gram.encode(), digest_size=4).hexdigest(), 16) % dim
        vec[idx] += 1.0
    norm = math.sqrt(sum(v * v for v in vec)) or 1.0
    return [v / norm for v in vec]


def _cosine(a: Sequence[float], b: Sequence[float]) -> float:
    return sum(x * y for x, y in zip(a, b))


def _try_st_embeddings(texts: Sequence[str]) -> list[list[float]] | None:
    try:
        from sentence_transformers import SentenceTransformer  # type: ignore
    except ImportError:
        return None
    model = SentenceTransformer("sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")
    vectors = model.encode(list(texts), normalize_embeddings=True, show_progress_bar=False)
    return [list(map(float, row)) for row in vectors]


def find_semantic_near_duplicates(
    documents: Sequence[tuple[str, str]],
    *,
    threshold: float = 0.92,
    seed: int = 42,
) -> tuple[set[str], dict[str, Any]]:
    """Return IDs to drop (keep first occurrence in input order).

    ``documents`` is ``(doc_id, text)``. Empty texts are skipped.
    """
    _ = seed  # reserved for future reservoir / LSH seeding
    usable = [(doc_id, text) for doc_id, text in documents if text and text.strip()]
    if len(usable) < 2:
        return set(), {
            "backend": "noop",
            "rows_in": len(documents),
            "pairs_checked": 0,
            "dropped": 0,
        }

    texts = [t for _, t in usable]
    ids = [i for i, _ in usable]
    vectors = _try_st_embeddings(texts)
    backend = "sentence_transformers_multilingual" if vectors is not None else "hashed_ngram_bag"
    if vectors is None:
        vectors = [_tokenize(t) for t in texts]

    drop: set[str] = set()
    clusters: list[list[str]] = []
    kept_idx: list[int] = []
    pairs_checked = 0

    for i, doc_id in enumerate(ids):
        if doc_id in drop:
            continue
        matched_cluster = [doc_id]
        for j in kept_idx:
            pairs_checked += 1
            sim = _cosine(vectors[i], vectors[j])
            if sim >= threshold:
                drop.add(doc_id)
                matched_cluster = [ids[j], doc_id]
                break
        if doc_id not in drop:
            kept_idx.append(i)
        elif len(matched_cluster) > 1:
            clusters.append(matched_cluster)

    # Compact cluster report (by first kept id)
    by_kept: dict[str, list[str]] = defaultdict(list)
    for cluster in clusters:
        by_kept[cluster[0]].extend(cluster[1:])

    report = {
        "backend": backend,
        "threshold": threshold,
        "rows_in": len(documents),
        "rows_usable": len(usable),
        "pairs_checked": pairs_checked,
        "dropped": len(drop),
        "dropped_ids": sorted(drop),
        "clusters": [
            {"kept": kept, "dropped": dropped}
            for kept, dropped in sorted(by_kept.items(), key=lambda x: -len(x[1]))[:50]
        ],
    }
    return drop, report
