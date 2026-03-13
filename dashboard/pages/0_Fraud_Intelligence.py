import streamlit as st
import requests
import pandas as pd

st.title("Fraud Intelligence Center")

API = "http://127.0.0.1:8000"

try:

    res = requests.get(f"{API}/transactions")

    if res.status_code != 200:
        st.error("Backend error")
        st.stop()

    data = res.json()

    if not data:
        st.info("No transactions yet. Run simulator first.")
        st.stop()

    df = pd.DataFrame(data)

    st.metric("Total Transactions", len(df))

    if "risk" in df.columns:

        frauds = df[df["risk"] == 1]

        st.metric("Fraud Transactions", len(frauds))

    st.subheader("Transaction Amount Distribution")

    st.bar_chart(df["amount"])

except Exception as e:

    st.error(f"Backend connection error: {e}")