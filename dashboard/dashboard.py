import streamlit as st
import requests
import pandas as pd

API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="Edge UPI Risk Intelligence", layout="wide")

st.title("🚀 Edge UPI Behavioural Risk Intelligence Dashboard")

# ---------------------------------
# Transaction Tester
# ---------------------------------

st.header("Test Transaction Risk")

user_id = st.number_input("User ID", value=1)

amount = st.number_input("Amount", value=500)

time_gap = st.number_input("Time Gap", value=60)

is_night = st.selectbox("Night Transaction", [0,1])


if st.button("Check Risk"):

    payload = {
        "user_id": user_id,
        "amount": amount,
        "time_gap": time_gap,
        "is_night": is_night
    }

    response = requests.post(f"{API_URL}/score", json=payload)

    if response.status_code == 200:

        data = response.json()

        st.success("Risk Analysis Complete")

        st.write("Risk Score:", data["risk_score"])
        st.write("Decision:", data["decision"])
        st.write("Trust Score:", data["trust_score"])


# ---------------------------------
# User Risk Trend
# ---------------------------------

st.header("User Risk Trend")

history = requests.get(f"{API_URL}/risk-history/{user_id}")

if history.status_code == 200:

    response = history.json()

    risk_records = response["history"]

    if len(risk_records) > 0:

        df = pd.DataFrame({
            "Risk Score": risk_records
        })

        st.line_chart(df)

    else:

        st.info("No risk history available yet")


# ---------------------------------
# Fraud Heatmap
# ---------------------------------

st.header("Fraud Heatmap")

heatmap = requests.get(f"{API_URL}/fraud-heatmap")

if heatmap.status_code == 200:

    data = heatmap.json()

    df = pd.DataFrame(data)

    if not df.empty:

        df = df.rename(columns={
            "user_id": "User",
            "risk_score": "Risk Score"
        })

        st.bar_chart(df.set_index("User"))


# ---------------------------------
# Live Fraud Feed
# ---------------------------------

st.header("Live Fraud Feed")

feed = requests.get(f"{API_URL}/fraud-feed")

if feed.status_code == 200:

    records = feed.json()

    df = pd.DataFrame(records)

    if not df.empty:

        df = df.rename(columns={
            "user_id": "User",
            "risk_score": "Risk Score"
        })

        st.dataframe(df)


# ---------------------------------
# Fraud Ring Detection
# ---------------------------------

st.header("Fraud Ring Detection")

rings = requests.get(f"{API_URL}/fraud-rings")

if rings.status_code == 200:

    data = rings.json()

    suspicious = data["suspicious_clusters"]

    if len(suspicious) > 0:

        st.error(f"Suspicious Fraud Ring Detected: {suspicious}")

    else:

        st.success("No fraud rings detected")