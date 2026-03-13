class FraudReasoningEngine:

    def explain(self, transaction, risk_score):

        reasons = []

        if transaction["amount"] > 50000:
            reasons.append("Large transaction amount")

        if transaction.get("new_device", False):
            reasons.append("New device detected")

        if transaction.get("location_change", False):
            reasons.append("Location anomaly")

        if transaction.get("rapid_transactions", False):
            reasons.append("High transaction velocity")

        if risk_score > 0.8:
            reasons.append("ML model high risk score")

        return {
            "risk_score": risk_score,
            "reasons": reasons
        }