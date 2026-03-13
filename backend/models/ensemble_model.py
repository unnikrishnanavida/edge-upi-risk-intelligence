import joblib
import numpy as np

ISO_MODEL_PATH = "models/isolation_forest.pkl"
LOG_MODEL_PATH = "models/logistic_model.pkl"


class EnsembleModel:

    def __init__(self):

        self.iso_model = joblib.load(ISO_MODEL_PATH)
        self.log_model = joblib.load(LOG_MODEL_PATH)

    def predict_proba(self, X):

        X = np.array(X)

        amount = X[:, 0]
        is_night = X[:, 1]
        rolling_avg = X[:, 2]
        rolling_txn = X[:, 3]
        time_gap = X[:, 4]

        iso_features = np.column_stack([
            amount,
            is_night,
            rolling_avg
        ])

        log_features = np.column_stack([
            amount,
            is_night,
            rolling_avg,
            rolling_txn,
            time_gap
        ])

        # Logistic Regression probability
        log_prob = self.log_model.predict_proba(log_features)[:, 1]

        # Isolation Forest anomaly prediction
        iso_pred = self.iso_model.predict(iso_features)

        # Convert anomaly output
        iso_score = np.where(iso_pred == -1, 0.8, 0.2)

        # Weighted ensemble
        final_prob = (0.7 * log_prob) + (0.3 * iso_score)

        return np.column_stack([1 - final_prob, final_prob])


# IMPORTANT: This function MUST exist for main.py
def load_model():
    return EnsembleModel()