import numpy as np

risk_window = []

def detect_risk_drift(new_risk):

    risk_window.append(new_risk)

    if len(risk_window) > 100:
        risk_window.pop(0)

    if len(risk_window) < 20:
        return {"drift_detected": False}

    mean_risk = np.mean(risk_window)

    if mean_risk > 600:
        return {
            "drift_detected": True,
            "mean_risk": float(mean_risk)
        }

    return {
        "drift_detected": False,
        "mean_risk": float(mean_risk)
    }