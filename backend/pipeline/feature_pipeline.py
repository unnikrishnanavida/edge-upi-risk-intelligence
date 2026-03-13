import pandas as pd


class FeaturePipeline:

    def generate_features(self, df):

        # Ensure timestamp
        if "timestamp" not in df.columns:
            df["timestamp"] = pd.Timestamp.now()

        df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")
        df["timestamp"].fillna(pd.Timestamp.now(), inplace=True)

        # Encode sender and receiver
        sender_encoded = df["sender"].apply(lambda x: abs(hash(str(x))) % 10000)
        receiver_encoded = df["receiver"].apply(lambda x: abs(hash(str(x))) % 10000)

        amount = df["amount"]

        features = pd.DataFrame({
            "sender_encoded": sender_encoded,
            "receiver_encoded": receiver_encoded,
            "amount": amount
        })

        return features