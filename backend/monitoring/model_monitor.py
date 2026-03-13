import time


class ModelMonitor:

    def __init__(self):

        self.total_predictions = 0
        self.fraud_detected = 0

    def log_prediction(self, fraud):

        self.total_predictions += 1

        if fraud:
            self.fraud_detected += 1

    def metrics(self):

        if self.total_predictions == 0:
            return {}

        fraud_rate = self.fraud_detected / self.total_predictions

        return {
            "total_predictions": self.total_predictions,
            "fraud_rate": fraud_rate
        }