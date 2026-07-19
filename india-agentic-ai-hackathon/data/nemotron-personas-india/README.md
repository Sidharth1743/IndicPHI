# Nemotron-Personas-India (seed)

Source dataset: [`nvidia/Nemotron-Personas-India`](https://huggingface.co/datasets/nvidia/Nemotron-Personas-India)

This folder holds the local shard used by S1 persona sampling:

- `en_IN-00000-of-00011.parquet` — local HF shard (symlink to repo `artifacts/hf_shards/` in the parent monorepo)
- `shard_probe.json` — probe metadata from download

Pipeline configs point here via:

```yaml
persona_sampling:
  dataset_id: nvidia/Nemotron-Personas-India
  local_shard_path: data/nemotron-personas-india/en_IN-00000-of-00011.parquet
```
