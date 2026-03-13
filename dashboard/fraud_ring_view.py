import streamlit as st
import requests

API = "http://127.0.0.1:8000"

st.title("Detected Fraud Rings")

data = requests.get(f"{API}/fraud-rings").json()

rings = data["rings"]

if len(rings) == 0:

    st.success("No fraud rings detected")

else:

    for r in rings:

        user = r[0]
        merchant = r[1]

        st.warning(f"User: {user} → Merchant: {merchant}")