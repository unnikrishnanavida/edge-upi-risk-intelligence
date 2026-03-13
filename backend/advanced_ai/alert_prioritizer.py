class AlertPrioritizer:

    def classify(self, risk_score):

        if risk_score >= 0.9:
            return "CRITICAL"

        elif risk_score >= 0.75:
            return "HIGH"

        elif risk_score >= 0.5:
            return "MEDIUM"

        else:
            return "LOW"