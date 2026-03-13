from collections import deque
import time

fraud_alerts = deque(maxlen=100)

fraud_history = []


def log_alert(user, risk):

    fraud_alerts.append({
        "user": user,
        "risk": risk,
        "time": time.time()
    })


def record_risk(risk):

    fraud_history.append(risk)


def fraud_rate():

    if not fraud_history:
        return 0

    high = sum(1 for r in fraud_history if r > 0.7)

    return high / len(fraud_history)