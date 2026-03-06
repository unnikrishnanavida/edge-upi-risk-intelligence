# 🚀 Edge UPI Behavioural Risk Intelligence System

A modern AI-powered fraud detection platform designed to detect suspicious UPI transactions using behavioural analytics, machine learning, and explainable AI.

This project demonstrates how intelligent risk systems can monitor financial activity, identify fraud patterns, and provide real-time insights for safer digital payment ecosystems.

In a world where digital transactions happen every second, building secure and intelligent fraud detection systems is no longer optional — it is essential.

This system was developed with a mindset of **discipline, engineering clarity, and continuous learning**.

---

# 🌍 Vision

Financial fraud is becoming more sophisticated every day. Traditional rule-based systems are no longer enough.

This project aims to demonstrate how **AI-driven behavioural intelligence systems** can strengthen fraud detection by analyzing transaction patterns, user behaviour, and network relationships.

The goal is not just to detect fraud — but to **understand it, explain it, and prevent it**.

---

# 🧠 System Architecture

UPI Transaction  
│  
▼  
FastAPI Backend (Risk Engine)  
│  
▼  
Behaviour Analysis Layer  
│  
▼  
Machine Learning Models  
(Logistic Regression / LSTM)  
│  
▼  
Risk Score Generation  
│  
▼  
Fraud Monitoring Dashboard  
(Streamlit)

---

# 🔍 Core Transaction Inputs

The system analyzes the following transaction parameters:

### 1️⃣ user_id

Instead of using raw UPI IDs like:

```
rahul@ybl
user@okaxis
```

we use an internal identifier:

```
user_id = 101
```

### Why use user_id instead of UPI ID?

• Protects user privacy  
• Prevents exposure of sensitive payment IDs  
• Improves database indexing performance  
• Allows faster machine learning computations  
• Standard practice in financial systems  

Almost all large fintech companies internally map sensitive identifiers to secure numeric IDs.

---

### 2️⃣ amount

Transaction value being processed.

Large transactions are generally considered **higher risk**, especially if they deviate from normal user behaviour.

---

### 3️⃣ time_gap

Time gap represents the **difference between two consecutive transactions of the same user**.

Example:

```
Transaction 1 → 10:00:00
Transaction 2 → 10:00:10
```

Time Gap Calculation:

```
time_gap = current_transaction_time - previous_transaction_time
```

In this system the value is measured in **seconds**.

Small time gaps often indicate **velocity attacks**, where fraudsters rapidly execute multiple transactions.

---

### 4️⃣ night_transaction

Binary indicator showing whether the transaction occurred during late hours.

```
0 = Day Transaction
1 = Night Transaction
```

Binary encoding is used because machine learning models require numerical inputs rather than text values.

Night-time transactions often have higher fraud probability.

---

# 🧮 Risk Scoring Engine

The risk engine evaluates multiple behavioural signals to generate a **risk score**.

Example Output

```
risk_score: 780
decision: STEP_UP_AUTH
trust_score: 220
```

Decision levels:

| Risk Score | Decision |
|------|------|
0 – 300 | APPROVE |
300 – 600 | REVIEW |
600 – 800 | STEP_UP_AUTH |
800+ | BLOCK_TRANSACTION |

---

# 🤖 Explainable AI (Risk Explanation)

Most AI systems operate as **black boxes**, making decisions without explaining why.

This project introduces **Explainable AI** to provide transparency.

Example explanation:

```
amount_contribution: 500
time_gap_contribution: -0.2
night_risk: 50
```

This helps analysts understand **why a transaction was flagged as risky**.

Explainability is extremely important for:

• regulatory compliance  
• fraud investigations  
• customer dispute resolution  

---

# 📊 User Risk Trend

The system tracks a user's historical risk behaviour.

Example pattern:

```
Day 1 → Risk 200
Day 3 → Risk 420
Day 5 → Risk 760
```

A gradual increase in risk score may indicate:

• account takeover  
• credential compromise  
• behaviour manipulation  

Tracking risk trends helps analysts detect fraud earlier.

---

# 🌐 Fraud Ring Detection

Fraud is often not performed by a single account but by **organized networks of accounts working together**.

Example fraud ring:

```
User A → User B
User B → User C
User C → User A
```

This creates a suspicious transaction cycle.

Graph analysis helps detect these patterns and identify coordinated fraud groups.

---

# 📡 Live Fraud Feed

Provides a real-time stream of suspicious transactions.

Example output:

```
User 101 → Risk 850
User 204 → Risk 910
User 333 → Risk 780
```

This allows analysts to monitor fraud activity as it happens.

---

# 🚨 Live Fraud Alerts

Alerts are automatically generated when a transaction exceeds the high-risk threshold.

Example alert:

```
ALERT
User: 502
Risk Score: 920
Decision: BLOCK_TRANSACTION
```

This enables fast response to potentially fraudulent activity.

---

# 📊 Dashboard Capabilities

The Streamlit dashboard provides:

• transaction risk simulation  
• risk trend visualization  
• fraud heatmap monitoring  
• live fraud feed  
• fraud ring detection panel  
• explainable AI breakdown  

The dashboard acts as a **real-time fraud monitoring console**.

---

# ▶️ Running the Project

### Clone Repository

```
git clone https://github.com/unnikrishnanavida/edge-upi-risk-intelligence.git
cd edge-upi-risk-intelligence
```

---

### Install Dependencies

```
pip install -r requirements.txt
```

---

### Start FastAPI Server

```
uvicorn backend.api:app --reload
```

API runs at:

```
http://127.0.0.1:8000
```

Swagger API Documentation:

```
http://127.0.0.1:8000/docs
```

---

### Run Dashboard

```
streamlit run dashboard/dashboard.py
```

Dashboard runs at:

```
http://localhost:8501
```

---

# 📂 Project Structure

```
edge-upi-risk-intelligence
│
├ backend
│   ├ api.py
│   ├ app
│   │   ├ core
│   │   ├ services
│
├ dashboard
│   └ dashboard.py
│
├ models
│   ├ logistic_model.pkl
│   └ lstm_model.pt
│
├ data
│   └ risk_history.json
│
├ logs
│   └ risk_engine.log
│
├ requirements.txt
└ README.md
```

---

# 🎯 What This Project Demonstrates

This system showcases how AI can be used to build **intelligent risk engines for fintech systems**.

It integrates:

• behavioural analytics  
• machine learning risk scoring  
• explainable AI  
• fraud network detection  
• real-time monitoring dashboards  

These are the same foundational principles used in modern financial fraud detection systems.

---

# 🚀 Future Improvements

Planned upgrades include:

• Graph neural networks for fraud detection  
• Real-time transaction streaming with Kafka  
• PostgreSQL database integration  
• SHAP-based explainability models  
• Docker deployment  
• distributed risk engines  

---

# 👨‍💻 Author

**N. Unni Krishna**

AI / ML Developer  

Focused on building intelligent systems for:

• Fraud Detection  
• Behavioural Analytics  
• Financial Risk Intelligence  
