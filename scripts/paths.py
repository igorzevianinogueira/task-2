"""Paths centralizados — TerraOps Fusion."""

from pathlib import Path

TASK_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = TASK_ROOT / "data"
DEFAULT_CSV = DATA_DIR / "fusion_dataset.csv"
GROUND_CSV = DATA_DIR / "ground_truth.csv"
ORBITAL_CSV = DATA_DIR / "orbital_readings.csv"
DB_PATH = DATA_DIR / "terraops.db"
SNAPSHOT_PATH = DATA_DIR / "snapshot.json"
MODEL_PATH = TASK_ROOT / "models" / "fusion_model.joblib"
DASHBOARD_APP = TASK_ROOT / "dashboard" / "app.py"
MISSION_HTML = TASK_ROOT / "dashboard" / "mission_control" / "index.html"
