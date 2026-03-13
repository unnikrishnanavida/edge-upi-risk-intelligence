import numpy as np
import pandas as pd
import joblib
import os

from sklearn.ensemble import IsolationForest
from sklearn.linear_model import LogisticRegression

os.makedirs("models", exist_ok=True)

n = 2000

df = pd.DataFrame({
    "amount": np.random.uniform(10, 200000, n),
    "hour": np.random.randint(0, 24, n)
})

df["is_night"] = df["hour"].apply(lambda x: 1 if x < 6 or x > 22 else 0)
df["rolling_avg_amount"] = df["amount"] * np.random.uniform(0.7, 1.2, n)
df["rolling_txn_count"] = np.random.randint(1, 10, n)
df["time_gap"] = np.random.uniform(0, 5000, n)

# IsolationForest features
iso_features = [
    "amount",
    "is_night",
    "rolling_avg_amount"
]

iso_model = IsolationForest(contamination=0.05, random_state=42)
iso_model.fit(df[iso_features])

# LogisticRegression features
log_features = [
    "amount",
    "is_night",
    "rolling_avg_amount",
    "rolling_txn_count",
    "time_gap"
]

labels = (
    (df["amount"] > 80000) |
    (df["rolling_txn_count"] > 7) |
    (df["time_gap"] < 50)
).astype(int)


log_model = LogisticRegression(max_iter=500)
log_model.fit(df[log_features], labels)

joblib.dump(iso_model, "models/isolation_forest.pkl")
joblib.dump(log_model, "models/logistic_model.pkl")

print("Models trained successfully")