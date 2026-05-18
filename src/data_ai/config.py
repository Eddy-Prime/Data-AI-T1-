from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]

DATA_RAW_DIR = PROJECT_ROOT / "data" / "raw"
DATA_PROCESSED_DIR = PROJECT_ROOT / "data" / "processed"
ARTIFACT_MODELS_DIR = PROJECT_ROOT / "artifacts" / "models"
ARTIFACT_REPORTS_DIR = PROJECT_ROOT / "artifacts" / "reports"


def ensure_directories() -> None:
    for path in (
        DATA_RAW_DIR,
        DATA_PROCESSED_DIR,
        ARTIFACT_MODELS_DIR,
        ARTIFACT_REPORTS_DIR,
    ):
        path.mkdir(parents=True, exist_ok=True)
