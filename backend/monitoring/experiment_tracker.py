import json
import os

FILE_PATH = "data/risk_history.json"


def log_prediction(transaction, score):

    os.makedirs("data", exist_ok=True)

    record = {
        "transaction": transaction,
        "risk_score": float(score)
    }

    with open(FILE_PATH, "a") as f:
        f.write(json.dumps(record) + "\n")