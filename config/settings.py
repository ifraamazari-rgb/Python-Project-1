from pathlib import Path

APP_NAME = "task-cli"
APP_VERSION = "1.0.0"

BASE_DIR = Path(__file__).resolve().parent.parent

CONFIG_PATH = BASE_DIR / "config" / "config.json"
LOG_DIR = BASE_DIR / "logs"
LOG_FILE = LOG_DIR / "app.log"

STATE_FILE = BASE_DIR / "scheduler_state.json"

WATCHED_FOLDER = BASE_DIR / "watched_folder"
PROCESSED_FOLDER = BASE_DIR / "processed_files"

LOG_DIR.mkdir(exist_ok=True)
WATCHED_FOLDER.mkdir(exist_ok=True)
PROCESSED_FOLDER.mkdir(exist_ok=True)