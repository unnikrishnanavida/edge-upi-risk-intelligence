# 🚀 Edge UPI Behavioural Risk Intelligence System

AI-powered behavioural fraud detection system for **UPI transactions** using **FastAPI, Machine Learning, and Streamlit**.

This project simulates how modern fintech companies detect suspicious transactions using behavioural patterns, machine learning models, and real-time monitoring dashboards.

---

# 🧠 Key Features

* Behavioural fraud detection
* Real-time transaction risk scoring
* Trust score modelling
* Fraud activity monitoring dashboard
* Fraud heatmap visualization
* Fraud ring detection
* Machine learning risk prediction
* API-based risk engine

---

# 🏗 System Architecture

```
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
```

---

# 🔌 API Endpoints

## Score Transaction Risk

```
POST /score
```

Example Input:

```json
{
  "user_id": 101,
  "amount": 5000,
  "time_gap": 10,
  "is_night": 1
}
```

Example Output:

```json
{
  "risk_score": 0.78,
  "decision": "HIGH_RISK",
  "trust_score": 0.45
}
```

---

## User Risk History

```
GET /risk-history/{user_id}
```

Returns historical risk trends for the specified user.

---

## Fraud Heatmap

```
GET /fraud-heatmap
```

Visualizes geographic distribution of suspicious transactions.

---

## Fraud Feed

```
GET /fraud-feed
```

Displays a real-time stream of detected suspicious transactions.

---

## Fraud Ring Detection

```
GET /fraud-rings
```

Identifies groups of users exhibiting coordinated fraud behaviour.

---

# 📊 Dashboard Features

The **Streamlit dashboard** provides:

* Transaction risk simulation
* User risk trend visualization
* Fraud heatmap monitoring
* Live fraud activity feed
* Fraud ring detection panel

This allows analysts to monitor fraud behaviour in real time.

---

# ▶️ Running the Project

## 1️⃣ Clone Repository

```bash
git clone https://github.com/unnikrishnanavida/edge-upi-risk-intelligence.git
cd edge-upi-risk-intelligence
```

---

## 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 3️⃣ Start FastAPI Server

```bash
uvicorn api:app --reload
```

API will run at:

```
http://127.0.0.1:8000
```

---

## 4️⃣ Run Dashboard

```bash
streamlit run dashboard.py
```

Dashboard opens at:

```
http://localhost:8501
```

---

# 📸 Dashboard Preview

Add screenshots inside the `screenshots` folder.

Example:

```
screenshots/dashboard.png
screenshots/fraud_heatmap.png
screenshots/risk_trend.png
screenshots/fraud_ring.png
```

These screenshots help demonstrate system capabilities visually.

---

# 📂 Project Structure

```
edge-upi-risk-intelligence
│
├── backend
│   ├── app
│   │   ├── core
│   │   ├── services
│   │   └── api.py
│
├── dashboard
│   └── dashboard.py
│
├── models
│   ├── logistic_model.pkl
│   └── lstm_model.pt
│
├── data
│   └── risk_history.json
│
├── logs
│   └── risk_engine.log
│
├── requirements.txt
└── README.md
```

---

# 🎯 Project Goals

This project demonstrates how **AI + behavioural analytics** can strengthen fraud detection in digital payment ecosystems.

The system models how fintech platforms monitor transactions and evaluate behavioural risk in real time.

It is designed as a **prototype risk intelligence platform for modern digital payment systems**.

---

# 🚀 Future Improvements

Planned upgrades for the system include:

* Graph-based fraud detection
* SHAP explainability for model decisions
* Real-time Kafka transaction stream
* PostgreSQL transaction storage
* JWT authentication for APIs
* Production deployment with Docker
* Advanced anomaly detection models
* Real-time fraud alert system

---

# 👨‍💻 Author

**N. Unnikrishna**

AI / ML Developer
Focused on **AI systems, fraud detection, and intelligent risk analytics**.

---

⭐ If you find this project useful, consider **starring the repository**.
