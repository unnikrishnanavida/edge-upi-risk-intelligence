import sys
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uuid
import numpy as np
import pandas as pd
import shap

# SERVICES
from backend.app.services.transaction_store import (
    save_transaction,
    get_all_transactions,
    get_transaction
)

from backend.app.services.behavioral_biometrics import behavior_score
from backend.app.services.temporal_gnn import temporal_patterns
from backend.app.services.drift_monitor import detect_drift

# GRAPH
from backend.graph.graph_fraud_detector import (
    add_connection,
    get_graph,
    detect_fraud_rings
)

# MODEL
from backend.models.ensemble_model import load_model

# GNN
from backend.advanced_ai.gnn_fraud_detector import gnn_risk


app = FastAPI()

# --------------------------------------------------
# Load ML Model
# --------------------------------------------------

model = load_model()


# --------------------------------------------------
# SHAP Setup (FIXED)
# --------------------------------------------------

background_data = np.random.rand(50, 5)

def shap_predict(X):
    return model.predict_proba(X)[:, 1]

explainer = shap.Explainer(shap_predict, background_data)


# --------------------------------------------------
# Transaction Schema
# --------------------------------------------------

class Transaction(BaseModel):

    amount: float
    device_score: float
    location_score: float
    velocity_score: float
    sender: str
    receiver: str
    timestamp: str


# --------------------------------------------------
# Root
# --------------------------------------------------

@app.get("/")
def home():
    return {"message": "Edge AI UPI Behaviour Risk System Running"}


# --------------------------------------------------
# Fraud Prediction
# --------------------------------------------------

@app.post("/predict")
def predict(tx: Transaction):

    try:
        current_time = pd.to_datetime(tx.timestamp)
        hour = current_time.hour
    except:
        current_time = pd.Timestamp.now()
        hour = 12

    is_night = 1 if hour < 6 or hour > 22 else 0

    df = get_all_transactions()

    if df.empty:

        rolling_avg_amount = tx.amount
        rolling_txn_count = 1
        time_gap = 100

    else:

        rolling_avg_amount = df["amount"].tail(5).mean()
        rolling_txn_count = len(df.tail(5))

        try:
            last_time = pd.to_datetime(df.iloc[-1]["timestamp"])
            time_gap = (current_time - last_time).total_seconds()
        except:
            time_gap = 100

    # ML Features
    features = [
        tx.amount,
        is_night,
        rolling_avg_amount,
        rolling_txn_count,
        time_gap
    ]

    try:
        prob = float(model.predict_proba([features])[0][1])
    except:
        prob = 0.3

    # normalize probability
    prob = max(0.05, min(prob, 0.95))

    risk_score = int(prob * 100)

    if tx.amount > 70000 or tx.velocity_score > 7:
        risk = 1
    else:
        risk = 1 if risk_score >= 70 else 0

    tx_id = f"tx_{uuid.uuid4().hex[:6]}"

    transaction_data = {
        "transaction_id": tx_id,
        "amount": tx.amount,
        "device_score": tx.device_score,
        "location_score": tx.location_score,
        "velocity_score": tx.velocity_score,
        "sender": tx.sender,
        "receiver": tx.receiver,
        "timestamp": tx.timestamp,
        "risk": risk,
        "risk_score": risk_score
    }

    save_transaction(transaction_data)

    add_connection(tx.sender, tx.receiver)

    return {
        "transaction_id": tx_id,
        "risk": risk,
        "risk_score": risk_score
    }


# --------------------------------------------------
# Transactions
# --------------------------------------------------

@app.get("/transactions")
def transactions():

    df = get_all_transactions()

    if df.empty:
        return []

    df = df.fillna("")

    return df.to_dict(orient="records")


# --------------------------------------------------
# Fraud Heatmap
# --------------------------------------------------

@app.get("/heatmap")
def heatmap():

    df = get_all_transactions()

    if len(df) < 2:
        return {"error": "Not enough transactions"}

    return {
        "amount": df["amount"].tolist(),
        "risk": df["risk"].tolist()
    }


# --------------------------------------------------
# SHAP Explainability
# --------------------------------------------------

@app.get("/explain/{tx_id}")
def explain(tx_id: str):

    tx = get_transaction(tx_id)

    if tx is None:
        raise HTTPException(status_code=404, detail="Transaction Not Found")

    df = get_all_transactions()

    if df.empty:
        rolling_avg = tx["amount"]
        rolling_txn = 1
        time_gap = 100
        is_night = 0
    else:
        rolling_avg = df["amount"].tail(5).mean()
        rolling_txn = len(df.tail(5))
        time_gap = 100
        is_night = 0

    features = np.array([[

        tx["amount"],
        is_night,
        rolling_avg,
        rolling_txn,
        time_gap

    ]])

    shap_values = explainer(features)

    return {
        "transaction_id": tx_id,
        "features": [
            "amount",
            "is_night",
            "rolling_avg",
            "rolling_txn_count",
            "time_gap"
        ],
        "shap_values": shap_values.values.tolist()
    }


# --------------------------------------------------
# Fraud Graph
# --------------------------------------------------

@app.get("/fraud-graph")
def fraud_graph():

    edges = get_graph()

    return {"edges": edges}


# --------------------------------------------------
# Fraud Rings
# --------------------------------------------------

@app.get("/fraud-rings")
def fraud_rings():

    rings = detect_fraud_rings()

    return {"rings": rings}


# --------------------------------------------------
# Temporal Fraud
# --------------------------------------------------

@app.get("/temporal-patterns")
def temporal_api():

    df = get_all_transactions()

    if df.empty:
        return {"error": "No transactions"}

    return temporal_patterns(df)


# --------------------------------------------------
# Behavioral Biometrics
# --------------------------------------------------

@app.get("/behavior/{tx_id}")
def behavior(tx_id: str):

    tx = get_transaction(tx_id)

    if tx is None:
        raise HTTPException(status_code=404, detail="Transaction Not Found")

    result = behavior_score(
        tx["velocity_score"],
        tx["device_score"]
    )

    return {
        "transaction_id": tx_id,
        "behavior_risk": result
    }


# --------------------------------------------------
# Model Drift
# --------------------------------------------------

@app.get("/model-drift")
def model_drift():

    df = get_all_transactions()

    if len(df) < 20:
        return {"status": "Not enough data"}

    old_scores = df["risk"][:10]
    new_scores = df["risk"][-10:]

    drift = detect_drift(old_scores, new_scores)

    return {"drift_status": drift}


# --------------------------------------------------
# GNN Fraud Detection
# --------------------------------------------------

@app.get("/gnn-fraud-detection")
def gnn_detection():

    edges = get_graph()

    suspicious = gnn_risk(edges)

    return {"suspicious_nodes": suspicious}