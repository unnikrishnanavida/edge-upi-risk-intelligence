import os
import json
import joblib
import torch
import torch.nn as nn
import pandas as pd
import numpy as np
from torch.utils.data import Dataset, DataLoader
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
import networkx as nx

print("🚀 Edge AI UPI Risk System Initialized")

# ==============================
# File Paths
# ==============================

LOGISTIC_PATH = "logistic_model.pkl"
LSTM_PATH = "lstm_model.pt"
TRUST_PATH = "trust_store.json"

# ==============================
# Generate Data
# ==============================

np.random.seed(42)
num_samples = 10000
num_users = 500

data = pd.DataFrame({
    "user_id": np.random.randint(1, num_users + 1, num_samples),
    "amount": np.random.exponential(scale=2000, size=num_samples),
    "time_gap": np.random.exponential(scale=60, size=num_samples),
    "is_night": np.random.randint(0, 2, num_samples),
})

data["device_id"] = data["user_id"] * 10
data["attack_type"] = "normal"

# Fraud injection
attacker_users = np.random.choice(data["user_id"].unique(), size=30, replace=False)

for user in attacker_users:
    user_indices = data[data["user_id"] == user].index

    if len(user_indices) > 0:
        velocity_indices = np.random.choice(user_indices, size=min(20, len(user_indices)), replace=False)
        data.loc[velocity_indices, "time_gap"] = np.random.randint(1, 5)
        data.loc[velocity_indices, "amount"] = np.random.randint(6000, 12000)
        data.loc[velocity_indices, "is_night"] = 1

data["fraud"] = (
    (data["amount"] > 5000) &
    (data["is_night"] == 1) &
    (data["time_gap"] < 30)
).astype(int)

print("Fraud count:", data["fraud"].sum())

# ==============================
# Feature Engineering
# ==============================

data = data.sort_values(by=["user_id"]).reset_index(drop=True)

data["rolling_avg_amount"] = (
    data.groupby("user_id")["amount"]
    .rolling(window=3, min_periods=1)
    .mean()
    .reset_index(level=0, drop=True)
)

data["rolling_txn_count"] = data.groupby("user_id").cumcount()

feature_cols = [
    "amount",
    "time_gap",
    "is_night",
    "rolling_avg_amount",
    "rolling_txn_count"
]

X = data[feature_cols]
y = data["fraud"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ==============================
# Logistic Model (Persistent)
# ==============================

if os.path.exists(LOGISTIC_PATH):
    print("📦 Loading saved Logistic model...")
    model = joblib.load(LOGISTIC_PATH)
else:
    print("🧠 Training Logistic model...")
    model = LogisticRegression(class_weight="balanced", max_iter=1000)
    model.fit(X_train, y_train)
    joblib.dump(model, LOGISTIC_PATH)
    print("✅ Logistic model saved.")

predictions = model.predict(X_test)
print("\n📊 Logistic Report:")
print(classification_report(y_test, predictions, zero_division=0))

# ==============================
# LSTM Model (Persistent)
# ==============================

class BehavioralLSTM(nn.Module):
    def __init__(self, input_size, hidden_size=128):
        super(BehavioralLSTM, self).__init__()
        self.lstm = nn.LSTM(input_size, hidden_size, batch_first=True)
        self.dropout = nn.Dropout(0.3)
        self.fc = nn.Linear(hidden_size, 1)

    def forward(self, x):
        out, _ = self.lstm(x)
        out = out[:, -1, :]
        out = self.dropout(out)
        out = self.fc(out)
        return out

lstm_model = BehavioralLSTM(input_size=len(feature_cols))

if os.path.exists(LSTM_PATH):
    print("📦 Loading saved LSTM model...")
    lstm_model.load_state_dict(torch.load(LSTM_PATH))
    lstm_model.eval()
else:
    print("🧠 Training LSTM model...")

    class SimpleDataset(Dataset):
        def __init__(self, X, y):
            self.X = torch.tensor(X.values, dtype=torch.float32)
            self.y = torch.tensor(y.values, dtype=torch.float32)

        def __len__(self):
            return len(self.X)

        def __getitem__(self, idx):
            return self.X[idx].unsqueeze(0), self.y[idx]

    dataset = SimpleDataset(X_train, y_train)
    loader = DataLoader(dataset, batch_size=64, shuffle=True)

    criterion = nn.BCEWithLogitsLoss()
    optimizer = torch.optim.Adam(lstm_model.parameters(), lr=0.001)

    for epoch in range(5):
        total_loss = 0
        for features, labels in loader:
            outputs = lstm_model(features).squeeze()
            loss = criterion(outputs, labels)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            total_loss += loss.item()

        print(f"Epoch {epoch+1}, Loss: {total_loss:.4f}")

    torch.save(lstm_model.state_dict(), LSTM_PATH)
    print("✅ LSTM model saved.")

# ==============================
# Trust Engine (Persistent)
# ==============================

class TrustEngine:

    def __init__(self, user_ids):
        if os.path.exists(TRUST_PATH):
            with open(TRUST_PATH, "r") as f:
                self.trust_scores = json.load(f)
            print("📦 Loaded trust store.")
        else:
            self.trust_scores = {str(user): 800 for user in user_ids}
            self.save()

    def get_trust(self, user_id):
        return self.trust_scores.get(str(user_id), 800)

    def update_trust(self, user_id, decision):
        uid = str(user_id)

        if decision == "BLOCK":
            self.trust_scores[uid] -= 200
        elif decision == "STEP_UP_AUTH":
            self.trust_scores[uid] -= 50
        elif decision == "ALLOW":
            self.trust_scores[uid] += 5

        self.trust_scores[uid] = max(0, min(1000, self.trust_scores[uid]))
        self.save()

    def save(self):
        with open(TRUST_PATH, "w") as f:
            json.dump(self.trust_scores, f)

trust_engine = TrustEngine(data["user_id"].unique())

# ==============================
# Hybrid Risk Scoring
# ==============================

print("\n🚀 Running Persistent Risk Simulation...")

sample = X_test.iloc[[0]]
log_score = model.predict_proba(sample)[0][1]

lstm_model.eval()
with torch.no_grad():
    seq_input = torch.tensor(sample.values, dtype=torch.float32).unsqueeze(0)
    lstm_score = torch.sigmoid(lstm_model(seq_input)).item()

hybrid_score = 0.6 * log_score + 0.4 * lstm_score

user_id = int(data.iloc[0]["user_id"])
trust = trust_engine.get_trust(user_id)

adjusted_risk = hybrid_score * (1000 / (trust + 1))

if adjusted_risk * 1000 >= 800:
    decision = "BLOCK"
elif adjusted_risk * 1000 >= 500:
    decision = "STEP_UP_AUTH"
else:
    decision = "ALLOW"

print("User:", user_id)
print("Trust:", trust)
print("Hybrid Risk:", round(hybrid_score * 1000, 2))
print("Adjusted Risk:", round(adjusted_risk * 1000, 2))
print("Decision:", decision)

trust_engine.update_trust(user_id, decision)
print("Updated Trust:", trust_engine.get_trust(user_id))