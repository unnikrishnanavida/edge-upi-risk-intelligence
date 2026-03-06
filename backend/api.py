from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import RedirectResponse

# Core services
from backend.app.core.database import get_connection

# Behaviour services
from backend.app.services.velocity_service import check_velocity
from backend.app.services.drift_service import detect_risk_drift
from backend.app.services.graph_fraud_service import detect_fraud_rings

# AI + Alerts
from backend.app.services.alert_service import add_alert, get_alerts
from backend.app.services.shap_service import explain_transaction


app = FastAPI(title="Edge UPI Behavioural Risk Intelligence System")


# ---------------------------------------------------
# Home Route
# ---------------------------------------------------

@app.get("/")
def home():
    return RedirectResponse(url="/docs")


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

    # Base risk
    risk_score = tx.amount * 0.1

    # Velocity check
    velocity = check_velocity(tx.user_id)

    if velocity["velocity_attack"]:
        risk_score += 200

    # Risk drift detection
    drift = detect_risk_drift(risk_score)

    # Final decision
    decision = decision_engine(risk_score)

    trust_score = max(0, 1000 - risk_score)

    # Fraud alert trigger
    if risk_score > 800:
        add_alert(tx.user_id, risk_score, decision)

    # Explainable AI
    explanation = explain_transaction(
        tx.amount,
        tx.time_gap,
        tx.is_night
    )

    # Store transaction
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
        "trust_score": trust_score,
        "explanation": explanation
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


# ---------------------------------------------------
# Live Fraud Alerts
# ---------------------------------------------------

@app.get("/fraud-alerts")
def fraud_alerts():

    alerts = get_alerts()

    return {
        "alerts": alerts
    }