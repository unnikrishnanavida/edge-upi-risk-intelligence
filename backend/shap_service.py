import shap
import numpy as np

# Dummy explanation model
# (since your risk score is rule-based right now)

def explain_transaction(amount, time_gap, is_night):

    features = {
        "amount": amount * 0.1,
        "time_gap": -time_gap * 0.01,
        "is_night": is_night * 0.5
    }

    return features