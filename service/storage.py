import json
import time
import gzip
from service.config import RAW_JSON_DIR

def backup_json(data: json):
    with gzip.open(f"{RAW_JSON_DIR}/{time.time()}.json.gz","wt") as file:
        json.dump(data,file)

