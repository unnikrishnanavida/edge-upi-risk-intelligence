from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import RedirectResponse

from app.core.database import get_connection
from app.services.velocity_service import check_velocity
from app.services.drift_service import detect_risk_drift
from app.services.graph_fraud_service import detect_fraud_rings


app = FastAPI(title="Edge UPI Behavioural Risk Intelligence System")


# ---------------------------------------------------
# Home Route (Fix for / Not Found)
# ---------------------------------------------------

@app.get("/")
def home():
    return RedirectResponse(url="/docs")
    return {
        "message": "Edge UPI Behavioural Risk Intelligence System API is running",
        "docs": "http://127.0.0.1:8000/docs"
    }


# ---------------------------------------------------
# Transaction Schema
# ---------------------------------------------------

class Transaction(BaseModel):

    user_id: int
    amount: float
    time_gap: float
    is_night: int


# ---------------------------------------------------
# Decision Engine
# ---------------------------------------------------

def decision_engine(score):

    if score < 300:
        return "APPROVE"

    elif score < 600:
        return "REVIEW"

    elif score < 800:
        return "STEP_UP_AUTH"

    else:
        return "BLOCK_TRANSACTION"


# ---------------------------------------------------
# Risk Scoring
# ---------------------------------------------------

@app.post("/score")
def score_transaction(tx: Transaction):

    risk_score = tx.amount * 0.1

    velocity = check_velocity(tx.user_id)

    if velocity["velocity_attack"]:
        risk_score += 200

    drift = detect_risk_drift(risk_score)

    decision = decision_engine(risk_score)

    trust_score = max(0, 1000 - risk_score)

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        INSERT INTO transactions (user_id, amount, risk_score, decision)
        VALUES (%s,%s,%s,%s)
        """,
        (tx.user_id, tx.amount, risk_score, decision)
    )

    cur.execute(
        """
        INSERT INTO risk_history (user_id, risk_score)
        VALUES (%s,%s)
        """,
        (tx.user_id, risk_score)
    )

    conn.commit()

    cur.close()
    conn.close()

    return {
        "risk_score": risk_score,
        "decision": decision,
        "velocity_attack": velocity["velocity_attack"],
        "risk_drift": drift,
        "trust_score": trust_score
    }


# ---------------------------------------------------
# Risk History
# ---------------------------------------------------

@app.get("/risk-history/{user_id}")
def risk_history(user_id: int):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        SELECT risk_score
        FROM risk_history
        WHERE user_id=%s
        ORDER BY id DESC
        LIMIT 20
        """,
        (user_id,)
    )

    rows = cur.fetchall()

    cur.close()
    conn.close()

    history = []

    for r in rows:
        history.append(r[0])

    return {
        "user_id": user_id,
        "history": history
    }


# ---------------------------------------------------
# Fraud Heatmap
# ---------------------------------------------------

@app.get("/fraud-heatmap")
def fraud_heatmap():

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        SELECT user_id, MAX(risk_score)
        FROM risk_history
        GROUP BY user_id
        """
    )

    rows = cur.fetchall()

    cur.close()
    conn.close()

    data = []

    for r in rows:

        data.append({
            "user_id": r[0],
            "risk_score": r[1]
        })

    return data


# ---------------------------------------------------
# Live Fraud Feed
# ---------------------------------------------------

@app.get("/fraud-feed")
def fraud_feed():

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        SELECT user_id, risk_score
        FROM risk_history
        ORDER BY id DESC
        LIMIT 20
        """
    )

    rows = cur.fetchall()

    cur.close()
    conn.close()

    data = []

    for r in rows:

        data.append({
            "user_id": r[0],
            "risk_score": r[1]
        })

    return data


# ---------------------------------------------------
# Fraud Ring Detection
# ---------------------------------------------------

@app.get("/fraud-rings")
def fraud_rings():

    rings = detect_fraud_rings()

    return {
        "suspicious_clusters": rings
    }