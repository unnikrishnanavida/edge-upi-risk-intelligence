<h1 align="center">Edge AI UPI Behavioural Risk Intelligence System</h1>

<p align="center">
AI-Powered Fraud Detection Platform for Digital Payments
</p>

<p align="center">

![Python](https://img.shields.io/badge/Python-3.10-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red)
![Machine Learning](https://img.shields.io/badge/Machine-Learning-orange)
![Graph Analytics](https://img.shields.io/badge/Graph-NetworkX-purple)
![License](https://img.shields.io/badge/license-MIT-blue)

</p>

---

# Overview

The **Edge AI UPI Behavioural Risk Intelligence System** is an advanced fraud detection platform designed to simulate how modern fintech systems monitor and prevent fraudulent transactions in real time.

Digital payment systems such as **UPI process millions of transactions every second**, making fraud detection a critical challenge.

Traditional fraud detection systems rely on fixed rule-based logic, which struggles to detect modern attack patterns such as:

• velocity attacks
• behavioural manipulation
• coordinated fraud rings
• account takeover attempts

This project demonstrates how **Artificial Intelligence, Behavioural Analytics, and Graph Intelligence** can be combined to build a smarter fraud detection system.

Instead of relying only on predefined rules, the system analyzes **transaction behaviour patterns** and generates an intelligent fraud risk score.

---

# Project Vision

The vision behind this project is to simulate a **modern fintech fraud monitoring platform** capable of:

• analysing behavioural transaction patterns
• detecting anomalies in real time
• identifying fraud networks using graph analytics
• explaining AI decisions using explainable AI techniques

This system illustrates how **AI-driven risk intelligence platforms** can enhance financial security and fraud prevention.

---

# Key Capabilities

The platform demonstrates the following capabilities.

### Behavioural Risk Scoring

Each transaction is evaluated using behavioural signals such as:

• transaction amount deviation
• time between transactions
• night transaction detection
• transaction velocity patterns

These signals help identify abnormal user behaviour.

---

### Machine Learning Fraud Detection

The system uses anomaly detection techniques to identify suspicious transactions.

Models used include:

• Isolation Forest
• Logistic Regression
• Behavioural sequence analysis

The models generate a **fraud risk score** representing the probability of fraudulent activity.

---

### Graph Fraud Detection

Fraud is often performed by **groups of accounts working together**.

The system analyzes relationships between users and merchants using **graph analysis**.

This enables detection of:

• suspicious transaction clusters
• circular transaction patterns
• coordinated fraud networks

---

### Explainable AI

Fraud detection models must be explainable to support investigation and compliance.

The system integrates **Explainable AI techniques** to show how each feature contributes to the fraud decision.

Example explanation:

```
amount_contribution: 500
time_gap_contribution: -0.2
night_risk: 50
```

This makes the system transparent and interpretable.

---

# System Architecture

The architecture follows a layered structure similar to production fintech fraud detection platforms.

```
                ┌────────────────────┐
                │   UPI Transaction  │
                │   User Payment     │
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
        │ • Behavioural sequence ML   │
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
        │ • Fraud intelligence        │
        │ • Fraud network graph       │
        │ • Risk heatmap              │
        │ • Fraud alerts              │
        │ • Explainable AI            │
        └─────────────────────────────┘
```

---

# Dashboard Features

The Streamlit dashboard acts as a **fraud monitoring console**.

It provides multiple analysis modules.

---

# Fraud Intelligence Dashboard

![Fraud Intelligence](screenshots/Screenshot%20\(536\).png)

Provides an overview of transaction analytics and risk statistics.

---

# Live Transaction Simulator

![Transaction Simulator](screenshots/Screenshot%20\(538\).png)

Simulates real-time transactions and evaluates fraud risk based on behavioural indicators.

---

# Fraud Network Graph

![Fraud Network Graph](screenshots/Screenshot%20\(539\).png)

Visualizes relationships between users and merchants to identify suspicious transaction networks.

---

# Fraud Rings Detection

![Fraud Rings](screenshots/Screenshot%20\(540\).png)

Detects clusters of interconnected accounts that may indicate coordinated fraud.

---

# Fraud Heatmap

![Fraud Heatmap](screenshots/Screenshot%20\(541\).png)

Displays transaction risk distribution across simulated datasets.

---

# Explainable AI (SHAP Analysis)

![Explainable AI](screenshots/Screenshot%20\(542\).png)

Provides feature importance values explaining why a transaction was flagged as suspicious.

---

# Fraud Alerts

![Fraud Alerts](screenshots/Screenshot%20\(543\).png)

Displays high-risk transactions detected by the system in real time.

---

# GNN Fraud Detection
![GNN Fraud Detection](screenshots/Screenshot%20\(544\).png)
The system also explores **Graph Neural Network based fraud detection techniques** to detect suspicious nodes within financial transaction networks.

---

# Running the Project

### Clone the Repository

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

### Start FastAPI Backend

```
uvicorn backend.api:app --reload
```

API endpoint

```
http://127.0.0.1:8000
```

Swagger documentation

```
http://127.0.0.1:8000/docs
```

---

### Run Dashboard

```
streamlit run dashboard/dashboard.py
```

Dashboard

```
http://localhost:8501
```

---

# Project Structure

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
├ screenshots
│
├ requirements.txt
└ README.md
```

---

# Technologies Used

• Python
• FastAPI
• Streamlit
• Scikit-Learn
• NetworkX
• Pandas
• NumPy
• Matplotlib

---

# Real-World Applications

This system demonstrates how AI can power modern fraud detection platforms in:

• fintech payment gateways
• banking transaction monitoring systems
• digital wallet security platforms
• financial risk intelligence engines

---

# Future Improvements

Potential future enhancements include:

• Graph Neural Networks for fraud detection
• Kafka real-time transaction streaming
• PostgreSQL data warehouse
• distributed risk scoring services
• cloud deployment on AWS or GCP

---

# Author

**N. Unni Krishna**

AI / ML Developer

Focused on building intelligent systems for:

• Fraud Detection
• Behavioural Analytics
• Financial Risk Intelligence

---

# Support

If you found this project interesting, consider giving the repository a **star ⭐** to support development.
