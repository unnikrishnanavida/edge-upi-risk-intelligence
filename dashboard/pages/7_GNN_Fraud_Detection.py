import streamlit as st
import requests

API = "http://127.0.0.1:8000"

st.title("GNN Fraud Detection")

if st.button("Run GNN Detection"):

    try:
        res = requests.get(API + "/gnn-fraud-detection")

        if res.status_code != 200:
            st.error(res.text)
        else:
            data = res.json()

            if not data["suspicious_nodes"]:
                st.info("No suspicious nodes detected")

            else:
                st.json(data)

    except Exception as e:
        st.error(f"Backend error: {e}")