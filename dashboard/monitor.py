import streamlit as st
import requests
import pandas as pd

st.title("🚨 Edge UPI Fraud Monitoring Console")

response = requests.get("http://127.0.0.1:8000/health")


data = response.json()

df = pd.DataFrame([data])

st.dataframe(df)

if not df.empty:

    st.subheader("Risk Scores")

    st.bar_chart(df["risk_score"])