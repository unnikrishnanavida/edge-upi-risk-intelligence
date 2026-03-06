# 🚀 Edge UPI Behavioural Risk Intelligence System

AI-powered behavioural fraud detection system for **UPI transactions**, designed to analyze transaction patterns, detect suspicious behaviour, and visualize fraud risks in real time.

The system combines **machine learning, behavioural analytics, and real-time monitoring dashboards** to identify fraudulent activity before financial damage occurs.

---

## 📌 Project Overview

Digital payment systems like **UPI** process millions of transactions daily. Traditional rule-based systems struggle to detect evolving fraud patterns.

This project introduces an **AI-driven behavioural risk engine** that:

• Evaluates user transaction behaviour  
• Detects velocity-based fraud patterns  
• Calculates dynamic trust scores  
• Identifies coordinated fraud rings  
• Visualizes suspicious activity using an interactive dashboard  

---

## 🧠 Key Features

### Behavioural Risk Scoring
Analyzes transaction behaviour patterns to generate real-time fraud risk scores.

### Velocity Fraud Detection
Detects abnormal transaction frequency within short time windows.

### Trust Score Calculation
Maintains dynamic trust scores for users based on historical behaviour.

### Fraud Ring Detection
Identifies clusters of suspicious accounts acting in coordinated patterns.

### Risk Drift Monitoring
Tracks changes in fraud patterns over time.

### Real-Time Monitoring Dashboard
Interactive dashboard to visualize risk trends, fraud activity, and alerts.

---

## ⚙️ Tech Stack

| Category | Technologies |
|--------|-------------|
Backend API | FastAPI |
Dashboard | Streamlit |
Language | Python |
Data Processing | Pandas, NumPy |
Machine Learning | Scikit-learn |
Visualization | Streamlit Charts |
Deployment Ready | Docker (optional) |

---

## 🏗 System Architecture
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

## 🔌 API Endpoints

### Score Transaction Risk

POST /score


Example Input:

```json
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

## 🔌 API Endpoints

### Score Transaction Risk

POST /score


Example Input:

```json
{
  "user_id": 101,
  "amount": 5000,
  "time_gap": 10,
  "is_night": 1
}

Output:

{
  "risk_score": 0.78,
  "decision": "HIGH_RISK",
  "trust_score": 0.45
}
User Risk History
GET /risk-history/{user_id}

Returns historical risk trends for the specified user.

Fraud Heatmap
GET /fraud-heatmap

Visualizes geographic distribution of suspicious transactions.

Fraud Feed
GET /fraud-feed

Real-time stream of detected suspicious activity.

Fraud Ring Detection
GET /fraud-rings

Identifies groups of users exhibiting coordinated fraud behaviour.

📊 Dashboard Features

The Streamlit dashboard provides:

• Transaction risk simulation
• User risk trend visualization
• Fraud heatmap monitoring
• Live fraud activity feed
• Fraud ring detection panel

▶️ Running the Project
1️⃣ Clone Repository
git clone https://github.com/unnikrishnanavida/edge-upi-risk-intelligence.git
cd edge-upi-risk-intelligence
2️⃣ Install Dependencies
pip install -r requirements.txt
3️⃣ Start FastAPI Server
uvicorn api:app --reload

API will run at:

http://127.0.0.1:8000
4️⃣ Run Dashboard
streamlit run dashboard.py

Dashboard opens at:

http://localhost:8501
📸 Dashboard Preview

(Add screenshots in the screenshots folder)

Example:

screenshots/dashboard.png
screenshots/fraud_heatmap.png
screenshots/risk_trend.png
screenshots/fraud_ring.png
📂 Project Structure
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
🎯 Project Goals

This project demonstrates how AI + behavioural analytics can strengthen fraud detection in digital payment ecosystems.

It is designed as a prototype risk intelligence platform for fintech applications.

🚀 Future Improvements

• Graph-based fraud detection
• SHAP explainability for model decisions
• Real-time Kafka transaction stream
• PostgreSQL transaction storage
• JWT authentication for APIs
• Production deployment with Docker

👨‍💻 Author

N.unnikrishna

AI / ML Developer
Focused on AI systems, fraud detection, and intelligent risk analytics.
