import streamlit as st
import requests
import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from datetime import datetime

API = "http://127.0.0.1:8000"

st.set_page_config(page_title="Edge AI UPI Fraud System", layout="wide")

st.title("🚨 Edge AI UPI Behaviour Risk System")

st.sidebar.title("Navigation")

page = st.sidebar.selectbox(
    "Select Page",
    [
        "Fraud Detection",
        "Fraud Network Graph",
        "Fraud Rings",
        "Fraud Heatmap",
        "Explainability",
        "Fraud Alerts",
        "System Monitor"
    ]
)

# ------------------------------------------------
# Fraud Detection
# ------------------------------------------------

if page == "Fraud Detection":

    st.header("Fraud Risk Prediction")

    col1, col2, col3 = st.columns(3)

    with col1:
        user_id = st.text_input("User ID")

    with col2:
        merchant = st.text_input("Merchant")

    with col3:
        amount = st.number_input("Amount", min_value=0.0)

    if st.button("Analyze Transaction"):

        payload = {
            "amount": amount,
            "device_score": 0.5,
            "location_score": 0.5,
            "velocity_score": 1,
            "sender": user_id,
            "receiver": merchant,
            "timestamp": str(datetime.now())
        }

        try:

            response = requests.post(f"{API}/predict", json=payload)

            if response.status_code != 200:
                st.error(response.text)

            else:

                result = response.json()

                col1, col2 = st.columns(2)

                with col1:
                    st.metric("Risk Score", result["risk_score"])

                with col2:
                    level = "HIGH" if result["risk"] == 1 else "LOW"
                    st.metric("Risk Level", level)

                st.success(f"Transaction ID: {result['transaction_id']}")

        except Exception as e:

            st.error(f"Connection Error: {e}")


# ------------------------------------------------
# Fraud Network Graph
# ------------------------------------------------

elif page == "Fraud Network Graph":

    st.header("Fraud Network Graph")

    try:

        data = requests.get(f"{API}/fraud-graph").json()

        edges = data["edges"]

        G = nx.Graph()

        for edge in edges:

            user = edge.get("user")
            merchant = edge.get("merchant")

            if user and merchant:
                G.add_edge(user, merchant)

        fig, ax = plt.subplots()

        nx.draw(G, with_labels=True)

        st.pyplot(fig)

    except:
        st.error("Network data unavailable")


# ------------------------------------------------
# Fraud Rings
# ------------------------------------------------

elif page == "Fraud Rings":

    st.header("Detected Fraud Rings")

    try:

        data = requests.get(f"{API}/fraud-rings").json()

        rings = data["rings"]

        if len(rings) == 0:

            st.success("No Fraud Rings Detected")

        else:

            for r in rings:
                st.warning(f"User {r[0]} → Merchant {r[1]}")

    except:
        st.error("Fraud ring data unavailable")


# ------------------------------------------------
# Fraud Heatmap
# ------------------------------------------------

elif page == "Fraud Heatmap":

    st.header("Fraud Activity Heatmap")

    try:

        data = requests.get(f"{API}/heatmap").json()

        if "error" in data:
            st.warning(data["error"])

        else:

            df = pd.DataFrame(data)

            st.scatter_chart(df)

    except:
        st.error("Heatmap unavailable")


# ------------------------------------------------
# Explainability
# ------------------------------------------------

elif page == "Explainability":

    st.header("Model Explainability")

    tx_id = st.text_input("Transaction ID")

    if st.button("Explain Prediction"):

        try:

            data = requests.get(f"{API}/explain/{tx_id}").json()

            st.json(data)

        except:

            st.error("Explainability service unavailable")


# ------------------------------------------------
# Fraud Alerts
# ------------------------------------------------

elif page == "Fraud Alerts":

    st.header("Fraud Alerts")

    try:

        tx = requests.get(f"{API}/transactions").json()

        alerts = [t for t in tx if t["risk"] == 1]

        if len(alerts) == 0:

            st.success("No alerts")

        else:

            for a in alerts:
                st.error(f"Fraud Transaction: {a['transaction_id']}  | Risk Score: {a['risk_score']}")

    except:

        st.error("Alert system unavailable")


# ------------------------------------------------
# System Monitor
# ------------------------------------------------

elif page == "System Monitor":

    st.header("System Health")

    try:

        data = requests.get(f"{API}/transactions").json()

        df = pd.DataFrame(data)

        st.dataframe(df)

    except:

        st.error("Backend not responding")