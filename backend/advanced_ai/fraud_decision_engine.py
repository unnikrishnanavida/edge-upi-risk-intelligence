class FraudDecisionEngine:

    def __init__(self):
        self.rules = {
            "large_amount": 50000,
            "velocity_threshold": 5,
        }

    def evaluate(self, transaction, ml_score, behavior_flag, graph_flag):

        reasons = []

        if transaction["amount"] > self.rules["large_amount"]:
            reasons.append("Transaction amount unusually large")

        if transaction.get("new_device", False):
            reasons.append("Transaction from a new device")

        if transaction.get("location_change", False):
            reasons.append("Sudden location change detected")

        if transaction.get("rapid_transactions", False):
            reasons.append("High transaction velocity")

        if behavior_flag:
            reasons.append("Behavioral anomaly detected")

        if graph_flag:
            reasons.append("Connected to suspicious network cluster")

        if ml_score > 0.8:
            reasons.append("ML model indicates high fraud probability")

        decision = "ALLOW"

        if ml_score > 0.9:
            decision = "BLOCK"
        elif ml_score > 0.75:
            decision = "MANUAL_REVIEW"

        return {
            "decision": decision,
            "risk_score": ml_score,
            "reasons": reasons
        }