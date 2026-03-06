import shap
import pandas as pd
import numpy as np
# ---------------------------------------------------
# SHAP Explainability Service
# ---------------------------------------------------

def explain_transaction(amount, time_gap, is_night):
    """
    Simulates explainable AI feature contributions
    for the fraud risk model.
    """

    # Feature contributions
    amount_contribution = round(amount * 0.10, 2)
    time_gap_contribution = round(-time_gap * 0.01, 2)

    if is_night == 1:
        night_risk = 50
    else:
        night_risk = 0

    # Total impact estimation
    total_impact = round(
        amount_contribution +
        time_gap_contribution +
        night_risk,
        2
    )

    explanation = {
        "feature_contributions": {
            "amount": amount_contribution,
            "time_gap": time_gap_contribution,
            "night_transaction": night_risk
        },
        "total_model_impact": total_impact,
        "explanation_summary": generate_summary(
            amount,
            time_gap,
            is_night
        )
    }

    return explanation


# ---------------------------------------------------
# Explanation Summary Generator
# ---------------------------------------------------

def generate_summary(amount, time_gap, is_night):

    reasons = []

    if amount > 5000:
        reasons.append("High transaction amount")

    if time_gap < 10:
        reasons.append("Rapid transaction behaviour")

    if is_night == 1:
        reasons.append("Night-time transaction")

    if len(reasons) == 0:
        reasons.append("Normal behavioural pattern")

    return reasons