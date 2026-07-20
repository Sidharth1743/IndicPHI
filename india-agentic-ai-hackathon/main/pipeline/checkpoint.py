"""Row-level checkpoint store for expensive LLM stages.

Stages append completed rows atomically to ``checkpoint.jsonl`` keyed by a
stable ``row_key``. Resume skips rows whose status is ``ok`` (or optionally
``soft_fail``). Hard failures are recorded and can be retried.

This makes S2b / S4 / S4b / S5 idempotent across process restarts.
"""

from __future__ import annotations

import hashlib
import json
import os
import tempfile
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence


@dataclass(frozen=True)
class CheckpointRecord:
    row_key: str
    status: str  # ok | soft_fail | hard_fail | skipped
    request_hash: str
    updated_utc: str
    payload: dict[str, Any]
    error: str | None = None


class CheckpointStore:
    """Append-only JSONL checkpoint with atomic finalization helpers."""

    def __init__(self, path: Path) -> None:
        self.path = path
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self._by_key: dict[str, CheckpointRecord] = {}
        if self.path.is_file():
            self._load()

    def _load(self) -> None:
        with self.path.open("r", encoding="utf-8") as handle:
            for line in handle:
                text = line.strip()
                if not text:
                    continue
                raw = json.loads(text)
                record = CheckpointRecord(
                    row_key=str(raw["row_key"]),
                    status=str(raw["status"]),
                    request_hash=str(raw.get("request_hash", "")),
                    updated_utc=str(raw.get("updated_utc", "")),
                    payload=dict(raw.get("payload") or {}),
                    error=raw.get("error"),
                )
                # Last write wins for a key.
                self._by_key[record.row_key] = record

    def get(self, row_key: str) -> CheckpointRecord | None:
        return self._by_key.get(row_key)

    def done_keys(self, *, accept_soft_fail: bool = True) -> set[str]:
        accepted = {"ok", "skipped"}
        if accept_soft_fail:
            accepted.add("soft_fail")
        return {
            key
            for key, record in self._by_key.items()
            if record.status in accepted
        }

    def append(
        self,
        *,
        row_key: str,
        status: str,
        request_hash: str,
        payload: Mapping[str, Any],
        error: str | None = None,
    ) -> CheckpointRecord:
        record = CheckpointRecord(
            row_key=row_key,
            status=status,
            request_hash=request_hash,
            updated_utc=datetime.now(timezone.utc).isoformat(),
            payload=dict(payload),
            error=error,
        )
        line = json.dumps(
            {
                "row_key": record.row_key,
                "status": record.status,
                "request_hash": record.request_hash,
                "updated_utc": record.updated_utc,
                "payload": record.payload,
                "error": record.error,
            },
            ensure_ascii=False,
        )
        with self.path.open("a", encoding="utf-8") as handle:
            handle.write(line + "\n")
            handle.flush()
            os.fsync(handle.fileno())
        self._by_key[row_key] = record
        return record

    def completed_payloads(
        self, *, accept_soft_fail: bool = True
    ) -> list[dict[str, Any]]:
        keys = self.done_keys(accept_soft_fail=accept_soft_fail)
        # Preserve insertion order of last-seen keys as loaded from file order
        # by sorting on updated_utc then key.
        records = [self._by_key[k] for k in keys]
        records.sort(key=lambda r: (r.updated_utc, r.row_key))
        return [dict(r.payload) for r in records]


def request_hash(parts: Sequence[Any]) -> str:
    """Stable blake2b digest of request-defining fields."""
    blob = json.dumps(list(parts), ensure_ascii=False, sort_keys=True, default=str)
    return hashlib.blake2b(blob.encode("utf-8"), digest_size=16).hexdigest()


def row_key_from_prompt(row: Mapping[str, Any]) -> str:
    uuid = str(row.get("uuid") or row.get("document_id") or "unknown")
    slot = row.get("doc_slot", 0)
    return f"{uuid}__{slot}"


def atomic_write_jsonl(path: Path, rows: Iterable[Mapping[str, Any]]) -> None:
    """Write JSONL via temp file + rename so readers never see a partial file."""
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp_name = tempfile.mkstemp(
        prefix=f".{path.name}.", suffix=".tmp", dir=str(path.parent)
    )
    tmp_path = Path(tmp_name)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            for row in rows:
                handle.write(json.dumps(dict(row), ensure_ascii=False) + "\n")
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(tmp_path, path)
    finally:
        if tmp_path.exists():
            tmp_path.unlink(missing_ok=True)
