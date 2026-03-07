import numpy as np
import joblib
from sklearn.ensemble import IsolationForest

# generate synthetic transactions

np.random.seed(42)

normal_transactions = np.random.normal(loc=1000, scale=300, size=(1000, 3))
fraud_transactions = np.random.normal(loc=8000, scale=2000, size=(50, 3))

X = np.vstack([normal_transactions, fraud_transactions])

model = IsolationForest(
    n_estimators=200,
    contamination=0.02,
    random_state=42
)

model.fit(X)

joblib.dump(model, "isolation_forest.pkl")

print("Model trained and saved.")