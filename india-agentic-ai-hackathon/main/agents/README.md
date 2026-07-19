# Agentic stages (S1–S9)

Implementation code lives in `main/designers/` and `main/pipeline/` so the
Python package is importable as `main.*`.

Import the stage index:

```python
from main.agents import run_pipeline, s4_generator, s5_linguistic_judge
```

Or run end-to-end:

```bash
python -m main.pipeline.run_pipeline --config configs/synthetic-data/pipeline.smoke.yaml
```
