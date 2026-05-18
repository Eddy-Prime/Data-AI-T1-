# Data & AI Starter Workspace

This repository is scaffolded for the outcomes you highlighted:

- **DAI-04 (purple):** ETL data pipeline (script-driven, reproducible)
- **DAI-07 (orange):** Supervised model training and evaluation
- **DAI-08 (orange):** Unsupervised model training and interpretation
- **DAI-10 (dark green):** Deploy ML model via FastAPI
- **DAI-12 (dark green):** Hypothesis testing workflow
- **DAI-14 (dark green):** LLM API integration starter

## Project structure

```text
src/data_ai/
  api/main.py                  # FastAPI app for model inference
  llm/feature_stub.py          # LLM integration starter
  ml/supervised.py             # DAI-07
  ml/unsupervised.py           # DAI-08
  pipelines/etl.py             # DAI-04
  stats/hypothesis_test.py     # DAI-12
scripts/
  run_etl.py
  train_supervised.py
  train_unsupervised.py
  run_hypothesis_test.py
tests/
```

## Quick start

1. Create and activate a virtual environment.
2. Install dependencies:

```bash
python3 -m pip install -r requirements.txt
```

3. Run the reproducible pipeline and ML steps:

```bash
python3 scripts/run_etl.py
python3 scripts/train_supervised.py
python3 scripts/train_unsupervised.py
python3 scripts/run_hypothesis_test.py
```

4. Start the API:

```bash
uvicorn src.data_ai.api.main:app --reload
```

5. Run tests:

```bash
python3 -m pytest -q
```

## Suggested task split for you

- Start with **`src/data_ai/pipelines/etl.py`** and improve data quality rules / transformations.
- Then iterate in **`src/data_ai/ml/supervised.py`** and **`src/data_ai/ml/unsupervised.py`** with better feature engineering, model choices, and metrics.
- Deploy/extend inference in **`src/data_ai/api/main.py`**.
- Add deeper stats methodology in **`src/data_ai/stats/hypothesis_test.py`**.
- Implement a real product feature in **`src/data_ai/llm/feature_stub.py`**.
