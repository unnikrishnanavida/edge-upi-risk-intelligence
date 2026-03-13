import joblib
import numpy as np


class FraudModelService:

    def __init__(self):

        self.model = joblib.load("backend/models/isolation_forest.pkl")

        # ----------------------------
        # V2 upgrade: behaviour memory
        # ----------------------------
        self.last_amount = {}
        self.transaction_count = {}

    def predict_risk(self, amount, time_gap, night, user_id=None):

        features = np.array([[amount, time_gap, night]])

        score = self.model.decision_function(features)[0]

        risk_score = int((1 - score) * 1000)

        if risk_score < 0:
            risk_score = 0

        # ---------------------------------
        # V2 Behaviour anomaly detection
        # ---------------------------------

        if user_id:

            prev = self.last_amount.get(user_id, amount)

            if amount > prev * 5:
                risk_score += 150

            self.last_amount[user_id] = amount

        # ---------------------------------
        # V3 Fraud spike detection
        # ---------------------------------

        if user_id:

            count = self.transaction_count.get(user_id, 0) + 1
            self.transaction_count[user_id] = count

            if count > 10:
                risk_score += 100

        return risk_score