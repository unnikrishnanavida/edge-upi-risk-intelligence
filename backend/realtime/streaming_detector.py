import pandas as pd


class RealTimeFraudDetector:

    def __init__(self, model):
        self.model = model

    def detect(self, df):

        # Ensure timestamp exists
        if "timestamp" not in df.columns:
            df["timestamp"] = pd.Timestamp.now()

        df["timestamp"] = pd.to_datetime(df["timestamp"])

        # Create hour feature
        df["hour"] = df["timestamp"].dt.hour

        # Create feature dataframe
        features = pd.DataFrame()

        features["amount"] = df["amount"]

        features["hour"] = df["hour"]

        features["is_night"] = df["hour"].apply(
            lambda x: 1 if x < 6 or x > 22 else 0
        )

        features["rolling_avg_amount"] = df["amount"]

        features["rolling_txn_count"] = 1

        features["time_gap"] = 0

        risk_score = self.model.predict_risk(features)[0]

        return {
            "risk_score": float(risk_score)
        }