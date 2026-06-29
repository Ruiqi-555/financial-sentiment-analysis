# -*- coding: utf-8 -*-
import os
from pathlib import Path

BASE_DIR = Path(os.environ.get("STAT8307_BASE", Path(__file__).resolve().parent))
DATA_PATH = os.environ.get("STAT8307_DATA", str(BASE_DIR / "data" / "data.csv"))
OUTPUT_DIR = str(BASE_DIR)

RANDOM_STATE = 42
TEST_SIZE = 0.15
VAL_SIZE = 0.15

# Optional: set this locally as an environment variable if needed.
NEWSAPI_KEY = os.environ.get("NEWSAPI_KEY", "")