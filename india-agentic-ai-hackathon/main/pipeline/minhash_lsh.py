"""CPU MinHash + LSH near-duplicate detection (legacy helper).

Kept for offline unit tests / experiments. Production S7 **requires**
``curation.dedup.backend: nemo_curator``; ``cpu_minhash`` is rejected by
``main.pipeline.curate``.
"""

from __future__ import annotations

import hashlib
import struct
from collections import defaultdict
from dataclasses import dataclass
from typing import Sequence


def _stable_hash32(token: str, seed: int) -> int:
    digest = hashlib.blake2b(
        f"{seed}:{token}".encode("utf-8"),
        digest_size=8,
    ).digest()
    return struct.unpack(">Q", digest)[0] & 0xFFFFFFFF


def char_ngrams(text: str, n: int) -> list[str]:
    normalized = " ".join(text.split())
    if len(normalized) < n:
        return [normalized] if normalized else []
    return [normalized[i : i + n] for i in range(len(normalized) - n + 1)]


def minhash_signature(
    text: str,
    *,
    num_hashes: int,
    char_ngram: int,
    seed: int,
) -> tuple[int, ...]:
    grams = char_ngrams(text, char_ngram)
    if not grams:
        return tuple(0 for _ in range(num_hashes))
    signature: list[int] = []
    for hash_index in range(num_hashes):
        minimum = min(_stable_hash32(gram, seed + hash_index) for gram in grams)
        signature.append(minimum)
    return tuple(signature)


def jaccard_from_signatures(left: Sequence[int], right: Sequence[int]) -> float:
    if len(left) != len(right) or not left:
        return 0.0
    equal = sum(1 for a, b in zip(left, right) if a == b)
    return equal / len(left)


@dataclass(frozen=True)
class MinHashLSHConfig:
    seed: int = 42
    char_ngrams: int = 24
    num_bands: int = 20
    rows_per_band: int = 5
    jaccard_threshold: float = 0.8

    @property
    def num_hashes(self) -> int:
        return self.num_bands * self.rows_per_band


def find_near_duplicate_ids(
    documents: Sequence[tuple[str, str]],
    config: MinHashLSHConfig,
) -> set[str]:
    """Return document ids to drop as near-duplicates.

    ``documents`` is a sequence of ``(doc_id, text)``.
    Keeps the first-seen id in each near-duplicate cluster (stable order).
    """
    if config.jaccard_threshold <= 0 or config.jaccard_threshold > 1:
        raise ValueError("jaccard_threshold must be in (0, 1]")

    signatures: dict[str, tuple[int, ...]] = {}
    order: list[str] = []
    for doc_id, text in documents:
        signatures[doc_id] = minhash_signature(
            text,
            num_hashes=config.num_hashes,
            char_ngram=config.char_ngrams,
            seed=config.seed,
        )
        order.append(doc_id)

    buckets: dict[tuple[int, tuple[int, ...]], list[str]] = defaultdict(list)
    for doc_id in order:
        signature = signatures[doc_id]
        for band_index in range(config.num_bands):
            start = band_index * config.rows_per_band
            end = start + config.rows_per_band
            band = tuple(signature[start:end])
            buckets[(band_index, band)].append(doc_id)

    parent = {doc_id: doc_id for doc_id in order}
    order_index = {doc_id: index for index, doc_id in enumerate(order)}

    def find(node: str) -> str:
        while parent[node] != node:
            parent[node] = parent[parent[node]]
            node = parent[node]
        return node

    def union(left: str, right: str) -> None:
        root_l, root_r = find(left), find(right)
        if root_l == root_r:
            return
        # Prefer earlier document as canonical root
        if order_index[root_l] <= order_index[root_r]:
            parent[root_r] = root_l
        else:
            parent[root_l] = root_r

    # Candidate pairs from LSH buckets, confirm with signature Jaccard
    seen_pairs: set[tuple[str, str]] = set()
    for members in buckets.values():
        if len(members) < 2:
            continue
        unique_members = list(dict.fromkeys(members))
        for i, left in enumerate(unique_members):
            for right in unique_members[i + 1 :]:
                pair = (
                    (left, right)
                    if order_index[left] < order_index[right]
                    else (right, left)
                )
                if pair in seen_pairs:
                    continue
                seen_pairs.add(pair)
                score = jaccard_from_signatures(signatures[left], signatures[right])
                if score >= config.jaccard_threshold:
                    union(left, right)

    drop: set[str] = set()
    clusters: dict[str, list[str]] = defaultdict(list)
    for doc_id in order:
        clusters[find(doc_id)].append(doc_id)
    for members in clusters.values():
        if len(members) == 1:
            continue
        # keep first in original order
        keep = min(members, key=order_index.__getitem__)
        for doc_id in members:
            if doc_id != keep:
                drop.add(doc_id)
    return drop
