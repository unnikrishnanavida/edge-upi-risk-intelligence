from backend.advanced_ai.ultra_risk_engine import ultra_engine


def evaluate_risk(*args):

    if len(args) == 3:
        ml_score = float(args[0])
        rule_score = float(args[1])
        velocity_score = float(args[2])
    else:
        ml_score = 0
        rule_score = 0
        velocity_score = 0

# -----------------------------------------
# Scale ML anomaly score for risk engine
# -----------------------------------------
    ml_score = abs(ml_score)

    if ml_score > 1:
        ml_score = 1

    # UPDATED: stronger ML scaling for anomaly detection
    ml_score = ml_score * 4

    risk_score = ultra_engine.compute(
        ml_score,
        rule_score,
        velocity_score
    )
    
    # -----------------------------------------
    # Normalize risk score to 0–1 range
    # -----------------------------------------
    if risk_score < 0:
        risk_score = 0

    if risk_score > 1:
        risk_score = 1

    if risk_score > 0.7:
        risk_level = "High"
    elif risk_score > 0.4:
        risk_level = "Medium"
    else:
        risk_level = "Low"

    return {
        "risk_score": risk_score,
        "risk_level": risk_level
    }