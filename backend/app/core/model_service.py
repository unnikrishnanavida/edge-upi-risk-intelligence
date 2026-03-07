import joblib
import numpy as np

class FraudModelService:

    def __init__(self):

        self.model = joblib.load("backend/models/isolation_forest.pkl")

    def predict_risk(self, amount, time_gap, night):

        features = np.array([[amount, time_gap, night]])

        score = self.model.decision_function(features)[0]

        risk_score = int((1 - score) * 1000)

        if risk_score < 0:
            risk_score = 0

        return risk_score