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
