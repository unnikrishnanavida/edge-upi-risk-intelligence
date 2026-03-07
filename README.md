# 🚀 Edge UPI Behavioural Risk Intelligence System

![Python](https://img.shields.io/badge/Python-3.10-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red)
![Machine Learning](https://img.shields.io/badge/Machine-Learning-orange)
![License](https://img.shields.io/badge/license-MIT-blue)

An **AI-powered fraud detection system for UPI transactions** using behavioural analytics, anomaly detection, and machine learning.

This project demonstrates how modern fintech systems can analyze transaction behaviour, detect suspicious activity, and provide **real-time fraud monitoring dashboards**.

The platform combines:

• behavioural risk scoring  
• anomaly detection models  
• explainable AI  
• fraud network detection  
• real-time monitoring dashboard  

to simulate how modern financial platforms detect and manage fraud risk.

---

# 🌍 Vision

Digital payments are growing rapidly, but so are fraud attempts.

Traditional rule-based fraud systems struggle to detect modern attack patterns such as:

• velocity attacks  
• coordinated fraud rings  
• behavioural manipulation  
• account takeover attempts  

This project explores how **AI-driven behavioural intelligence systems** can strengthen fraud detection.

Instead of relying only on fixed rules, the system analyzes:

• transaction behaviour  
• historical user activity  
• anomaly patterns  
• network relationships between accounts  

The goal is not only to detect fraud but also to **understand and explain the risk behind each transaction**.

---

# 🚀 Live System Demo

This project simulates a **fraud monitoring console used in fintech platforms**.

Key capabilities demonstrated:

• Behaviour-based risk scoring  
• Explainable AI for transaction decisions  
• Fraud ring detection using graph analysis  
• Real-time fraud monitoring dashboard  
• Live fraud alerts and suspicious transaction feed  

---

# 🏗 System Architecture

The system follows a layered architecture similar to modern fintech fraud detection engines.

```
                ┌────────────────────┐
                │   UPI Transaction  │
                │  (User Payment)    │
                └─────────┬──────────┘
                          │
                          ▼
              ┌──────────────────────┐
              │   FastAPI Backend    │
              │   Risk Scoring API   │
              └─────────┬────────────┘
                        │
                        ▼
        ┌─────────────────────────────────┐
        │ Behaviour Analysis Engine       │
        │                                 │
        │ • Amount deviation              │
        │ • Time gap analysis             │
        │ • Night transaction detection   │
        │ • Velocity attack detection     │
        └─────────┬───────────────────────┘
                  │
                  ▼
        ┌─────────────────────────────┐
        │ Machine Learning Models     │
        │                             │
        │ • Isolation Forest          │
        │ • Logistic Regression       │
        │ • LSTM Behaviour Model      │
        └─────────┬───────────────────┘
                  │
                  ▼
        ┌─────────────────────────────┐
        │ Risk Decision Engine        │
        │                             │
        │ APPROVE                     │
        │ REVIEW                      │
        │ STEP_UP_AUTH                │
        │ BLOCK_TRANSACTION           │
        └─────────┬───────────────────┘
                  │
                  ▼
        ┌─────────────────────────────┐
        │ Monitoring Dashboard        │
        │ (Streamlit)                 │
        │                             │
        │ • Risk trend                │
        │ • Fraud rings               │
        │ • Live fraud feed           │
        │ • Fraud alerts              │
        │ • Explainable AI            │
        └─────────────────────────────┘
```

---

# 🔍 Core Transaction Inputs

The risk engine evaluates multiple transaction features.

---

## 1️⃣ user_id

Instead of using raw UPI IDs like:

```
rahul@ybl
user@okaxis
```

The system uses a numeric identifier:

```
user_id = 101
```

### Why?

• protects user privacy  
• prevents exposure of payment IDs  
• faster database indexing  
• better machine learning performance  

This is standard practice in financial systems.

---

## 2️⃣ amount

Represents the transaction value.

Large transactions often indicate **higher risk**, especially when they deviate from the user's normal spending pattern.

---

## 3️⃣ time_gap

Time difference between two consecutive transactions.

Example:

```
Transaction 1 → 10:00:00
Transaction 2 → 10:00:10
```

```
time_gap = current_time − previous_time
```

Small time gaps may indicate **velocity attacks**.

---

## 4️⃣ night_transaction

Binary indicator:

```
0 → Day Transaction
1 → Night Transaction
```

Night transactions often have higher fraud probability.

---

# 🧠 Behavioural Risk Scoring Engine

The system generates a **risk score** based on behavioural signals and machine learning predictions.

Example output:

```
risk_score: 780
decision: STEP_UP_AUTH
trust_score: 220
```

### Risk Decision Levels

| Risk Score | Decision |
|-----------|-----------|
| 0 – 300 | APPROVE |
| 300 – 600 | REVIEW |
| 600 – 800 | STEP_UP_AUTH |
| 800+ | BLOCK_TRANSACTION |

---

# 🤖 Explainable AI

Many machine learning systems behave like **black boxes**.

This project introduces **Explainable AI** to show how each feature contributes to the final risk decision.

Example explanation:

```
amount_contribution: 500
time_gap_contribution: -0.2
night_risk: 50
```

Explainability is essential for:

• regulatory compliance  
• fraud investigations  
• customer dispute resolution  

---

# 📈 User Risk Trend Monitoring

The system tracks historical behaviour.

Example pattern:

```
Day 1 → Risk 200
Day 3 → Risk 420
Day 5 → Risk 760
```

Sudden increases in risk score may indicate:

• account takeover  
• compromised credentials  
• abnormal behaviour  

---

# 🌐 Fraud Ring Detection

Fraud is often performed by **groups of accounts working together**.

Example:

```
User A → User B
User B → User C
User C → User A
```

Graph analysis detects suspicious transaction networks.

---

# 📡 Live Fraud Feed

Displays recent suspicious transactions.

Example:

```
User 101 → Risk 850
User 204 → Risk 910
User 333 → Risk 780
```

This allows real-time monitoring.

---

# 🚨 Live Fraud Alerts

Alerts trigger when risk exceeds threshold.

Example:

```
ALERT
User: 502
Risk Score: 920
Decision: BLOCK_TRANSACTION
```

---

# 📊 Dashboard Capabilities

The Streamlit dashboard provides:

• transaction risk simulation  
• explainable AI analysis  
• risk trend visualization  
• fraud ring network graph  
• live fraud feed  
• fraud alerts monitoring  

The dashboard acts as a **fraud monitoring console**.

---

# 📸 System Screenshots

## API Risk Scoring Endpoint

![API](screenshots/Screenshot%20(346).png)

---

## FastAPI Documentation

![Docs](screenshots/Screenshot%20(347).png)

---

## Risk Analysis Dashboard

![Dashboard](screenshots/Screenshot%20(348).png)

---

## Explainable AI Breakdown

![Explanation](screenshots/Screenshot%20(349).png)

---

## User Risk Trend

![Trend](screenshots/Screenshot%20(351).png)

---

## Fraud Ring Detection

![Fraud Rings](screenshots/Screenshot%20(353).png)

---

## Live Fraud Feed

![Fraud Feed](screenshots/Screenshot%20(354).png)

---

## Fraud Alerts Panel

![Fraud Alerts](screenshots/Screenshot%20(355).png)

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

API:

```
http://127.0.0.1:8000
```

Swagger Documentation:

```
http://127.0.0.1:8000/docs
```

---

### Run Dashboard

```
streamlit run dashboard/dashboard.py
```

Dashboard:

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
├ screenshots
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

This system demonstrates how AI can power **modern financial fraud detection platforms**.

Technologies demonstrated:

• behavioural analytics  
• anomaly detection  
• machine learning risk scoring  
• explainable AI  
• graph fraud detection  
• real-time monitoring dashboards  

---

# 🚀 Future Improvements

Planned upgrades include:

• Graph Neural Networks for fraud detection  
• Kafka transaction streaming  
• PostgreSQL database integration  
• SHAP explainability models  
• Docker deployment  
• distributed risk scoring engines  

---

# 👨‍💻 Author

**N. Unni Krishna**

AI / ML Developer

Focused on building intelligent systems for:

• Fraud Detection  
• Behavioural Analytics  
• Financial Risk Intelligence
