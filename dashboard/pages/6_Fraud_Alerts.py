import streamlit as st
import requests

API = "http://127.0.0.1:8000"

st.title("Fraud Alerts")

try:

    res = requests.get(f"{API}/transactions")

    if res.status_code != 200:
        st.error("Backend not responding")
        st.stop()

    transactions = res.json()

    if len(transactions) == 0:
        st.info("No transactions yet. Run simulator first.")
        st.stop()

    alerts = [t for t in transactions if t["risk"] == 1]

    if len(alerts) == 0:
        st.success("No fraud alerts detected")

    else:

        for a in alerts:

            st.error(
                f"⚠ Fraud Transaction: {a['transaction_id']} | Risk Score: {a['risk_score']}"
            )

except Exception as e:

    st.error(f"Connection error: {e}")