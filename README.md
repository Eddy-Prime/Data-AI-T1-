# Data & AI Starter Workspace

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
