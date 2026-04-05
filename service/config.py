import os
from pathlib import Path
curr_file = Path(__file__).resolve()
PROJECT_ROOT = curr_file.parent.parent
SSL_CRT_FILE = PROJECT_ROOT / "SSL" / "_.taipower.com.tw.crt"
RAW_JSON_DIR = PROJECT_ROOT / "DATA" / "raw_json"
DB_PATH = PROJECT_ROOT / "database"