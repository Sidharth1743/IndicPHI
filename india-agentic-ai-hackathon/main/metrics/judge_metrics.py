"""Judge meta-evaluation helpers (calibration, consistency, bias, label dist)."""

from __future__ import annotations

from collections import Counter
from typing import Any, Mapping, Sequence


def label_distribution(verdicts: Sequence[str]) -> dict[str, float]:
    counts = Counter(verdicts)
    total = sum(counts.values()) or 1
    return {label: counts[label] / total for label in sorted(counts)}


def pass_rate(verdicts: Sequence[str], *, pass_label: str = "pass") -> float:
    if not verdicts:
        return 0.0
    return sum(1 for verdict in verdicts if verdict == pass_label) / len(verdicts)


def positional_length_bias(
    rows: Sequence[Mapping[str, Any]],
    *,
    text_key: str = "generated_text",
    pass_key: str = "judge_verdict",
    pass_label: str = "pass",
) -> dict[str, float]:
    """Pearson correlation between note length (chars) and pass indicator."""
    lengths: list[float] = []
    passes: list[float] = []
    for row in rows:
        text = str(row.get(text_key, ""))
        lengths.append(float(len(text)))
        passes.append(1.0 if row.get(pass_key) == pass_label else 0.0)
    return {"pearson_r": _pearson(lengths, passes), "n": float(len(rows))}


def consistency_rate(repeated_verdicts: Sequence[Sequence[str]]) -> float:
    """Fraction of samples with identical verdict across all repeats."""
    if not repeated_verdicts:
        return 0.0
    identical = 0
    for group in repeated_verdicts:
        if group and all(item == group[0] for item in group):
            identical += 1
    return identical / len(repeated_verdicts)


def _pearson(xs: Sequence[float], ys: Sequence[float]) -> float:
    n = len(xs)
    if n < 2 or n != len(ys):
        return 0.0
    mean_x = sum(xs) / n
    mean_y = sum(ys) / n
    num = sum((x - mean_x) * (y - mean_y) for x, y in zip(xs, ys))
    den_x = sum((x - mean_x) ** 2 for x in xs) ** 0.5
    den_y = sum((y - mean_y) ** 2 for y in ys) ** 0.5
    if den_x == 0 or den_y == 0:
        return 0.0
    return num / (den_x * den_y)
