import json
import os

RECORD_FILE = "record.json"

def load_record():
    if not os.path.exists(RECORD_FILE):
        return 0

    try:
        with open(RECORD_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)
            return int(data.get("best_score", 0))
    except (OSError, ValueError, TypeError):
        return 0

def save_record(score):
    best_score = load_record()

    if score > best_score:
        with open(RECORD_FILE, "w", encoding="utf-8") as file:
            json.dump({"best_score": score}, file)

        return score

    return best_score