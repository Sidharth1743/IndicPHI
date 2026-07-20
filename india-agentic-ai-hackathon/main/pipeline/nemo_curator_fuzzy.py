"""NeMo Curator fuzzy dedup runner (pip ``nemo-curator``).

Wraps ``FuzzyDeduplicationWorkflow`` + ``TextDuplicatesRemovalWorkflow`` as
documented in Curator fuzzy dedup guides. Requires Ray + GPU workers.

Does **not** import from the cloned ``Curator/`` tree — only the installed package.
"""

from __future__ import annotations

import shutil
from pathlib import Path
from typing import Any, Mapping, Sequence

import pyarrow as pa
import pyarrow.parquet as pq


class NemoCuratorDedupError(RuntimeError):
    pass


def _require_nemo_curator() -> None:
    try:
        import nemo_curator  # noqa: F401
    except ImportError as exc:
        raise NemoCuratorDedupError(
            "nemo_curator is not installed. Install with:\n"
            "  uv pip install 'nemo-curator[deduplication-cuda12]==1.2.0' "
            "--extra-index-url https://pypi.nvidia.com\n"
            "Do not import from the cloned Curator/ reference tree."
        ) from exc

    # Curator 1.2.0 pins RAPIDS 25.10.* for fuzzy dedup. 26.6 breaks imports
    # (rapidsmpf.buffer / utils.ray_utils moved). Fail closed with the fix.
    try:
        import cudf  # noqa: F401
        import rapidsmpf  # noqa: F401
        from rapidsmpf.buffer.buffer import MemoryType  # noqa: F401
    except ImportError as exc:
        raise NemoCuratorDedupError(
            f"NeMo Curator RAPIDS stack incomplete or wrong series ({exc}). "
            "Curator 1.2 requires RAPIDS **25.10.***, not 26.6. Reinstall:\n\n"
            "  uv pip uninstall -y cudf-cu12 cugraph-cu12 pylibcugraph-cu12 "
            "pylibraft-cu12 raft-dask-cu12 rapidsmpf-cu12 librapidsmpf-cu12 "
            "rmm-cu12 libcudf-cu12 libcugraph-cu12 libraft-cu12 librmm-cu12 "
            "dask-cudf-cu12 cuml-cu12 2>/dev/null || true\n"
            "  uv pip install 'nemo-curator[deduplication-cuda12]==1.2.0' "
            "--extra-index-url https://pypi.nvidia.com\n\n"
            "Then verify: python -c \"import cudf, rapidsmpf.buffer.buffer; "
            "print(cudf.__version__)\"  # expect 25.10.x"
        ) from exc


def write_curator_input(
    rows: Sequence[Mapping[str, Any]],
    *,
    staging_dir: Path,
    id_field: str,
    text_field: str,
) -> Path:
    """Write a single parquet shard Curator can read (id + text)."""
    staging_dir.mkdir(parents=True, exist_ok=True)
    # Clear prior shards so we never mix runs.
    for path in staging_dir.glob("*.parquet"):
        path.unlink()

    ids: list[str] = []
    texts: list[str] = []
    for row in rows:
        doc_id = str(row[id_field])
        text = str(row.get(text_field, ""))
        if not text.strip():
            raise NemoCuratorDedupError(f"Empty {text_field} for {doc_id}")
        ids.append(doc_id)
        texts.append(text)

    table = pa.table({id_field: ids, text_field: texts})
    out_path = staging_dir / "documents.parquet"
    pq.write_table(table, out_path)
    return out_path


def read_kept_ids(output_dir: Path, *, id_field: str) -> set[str]:
    kept: set[str] = set()
    parquet_files = sorted(output_dir.rglob("*.parquet"))
    if not parquet_files:
        raise NemoCuratorDedupError(
            f"No parquet outputs under {output_dir} after Curator removal"
        )
    for path in parquet_files:
        table = pq.read_table(path, columns=[id_field])
        column = table.column(id_field)
        for index in range(len(column)):
            kept.add(str(column[index].as_py()))
    return kept


def run_fuzzy_dedup(
    rows: Sequence[Mapping[str, Any]],
    *,
    work_dir: Path,
    id_field: str,
    text_field: str,
    seed: int,
    char_ngrams: int,
    num_bands: int,
    minhashes_per_band: int,
    use_64_bit_hash: bool = False,
    bands_per_iteration: int = 5,
    input_blocksize: str = "1GiB",
) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    """Identify near-duplicates via NeMo Curator and return kept rows.

    Parameters mirror Curator ``FuzzyDeduplicationWorkflow`` (not our CPU
    Jaccard threshold). Similarity is controlled by banding params.
    """
    _require_nemo_curator()

    from nemo_curator.core.client import RayClient
    from nemo_curator.stages.deduplication.fuzzy.workflow import (
        FuzzyDeduplicationWorkflow,
    )
    from nemo_curator.stages.text.deduplication.removal_workflow import (
        TextDuplicatesRemovalWorkflow,
    )

    work_dir = work_dir.resolve()
    input_dir = work_dir / "input"
    cache_dir = work_dir / "cache"
    dup_dir = work_dir / "duplicate_ids"
    output_dir = work_dir / "deduplicated"

    for path in (cache_dir, dup_dir, output_dir):
        if path.exists():
            shutil.rmtree(path)
        path.mkdir(parents=True, exist_ok=True)

    write_curator_input(
        rows, staging_dir=input_dir, id_field=id_field, text_field=text_field
    )

    ray_client = RayClient()
    ray_client.start()
    try:
        fuzzy = FuzzyDeduplicationWorkflow(
            input_path=str(input_dir),
            cache_path=str(cache_dir),
            output_path=str(dup_dir),
            input_filetype="parquet",
            input_file_extensions=[".parquet"],
            input_blocksize=input_blocksize,
            text_field=text_field,
            perform_removal=False,
            char_ngrams=char_ngrams,
            num_bands=num_bands,
            minhashes_per_band=minhashes_per_band,
            use_64_bit_hash=use_64_bit_hash,
            bands_per_iteration=bands_per_iteration,
            seed=seed,
        )
        fuzzy.run()

        duplicate_ids_path = dup_dir / "FuzzyDuplicateIds"
        id_generator_path = dup_dir / "fuzzy_id_generator.json"

        if not duplicate_ids_path.exists():
            # No near-duplicates: keep everything.
            kept_rows = [dict(row) for row in rows]
            report = {
                "backend": "nemo_curator",
                "rows_in": len(rows),
                "rows_kept": len(kept_rows),
                "rows_dropped": 0,
                "duplicate_ids_found": False,
                "work_dir": str(work_dir),
            }
            return kept_rows, report

        if not id_generator_path.is_file():
            raise NemoCuratorDedupError(
                f"Missing id generator at {id_generator_path} after fuzzy run"
            )

        removal = TextDuplicatesRemovalWorkflow(
            input_path=str(input_dir),
            ids_to_remove_path=str(duplicate_ids_path),
            output_path=str(output_dir),
            input_filetype="parquet",
            output_filetype="parquet",
            input_file_extensions=[".parquet"],
            # Curator auto-assigns `_curator_dedup_id`; our `document_id` is payload.
            id_field="_curator_dedup_id",
            duplicate_id_field="_curator_dedup_id",
            input_blocksize=input_blocksize,
            id_generator_path=str(id_generator_path),
        )
        removal.run()

        kept_ids = read_kept_ids(output_dir, id_field=id_field)
        kept_rows = [dict(row) for row in rows if str(row[id_field]) in kept_ids]
        dropped = len(rows) - len(kept_rows)
        report = {
            "backend": "nemo_curator",
            "rows_in": len(rows),
            "rows_kept": len(kept_rows),
            "rows_dropped": dropped,
            "duplicate_ids_found": True,
            "work_dir": str(work_dir),
            "char_ngrams": char_ngrams,
            "num_bands": num_bands,
            "minhashes_per_band": minhashes_per_band,
            "seed": seed,
        }
        return kept_rows, report
    finally:
        ray_client.stop()
