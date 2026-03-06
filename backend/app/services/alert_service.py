alerts = []

def add_alert(user_id, risk_score, decision):

    alert = {
        "user_id": user_id,
        "risk_score": risk_score,
        "decision": decision
    }

    alerts.insert(0, alert)

    if len(alerts) > 20:
        alerts.pop()

def get_alerts():

    return alerts