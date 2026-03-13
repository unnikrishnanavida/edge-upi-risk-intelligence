import streamlit as st
import requests

API = "http://127.0.0.1:8000"

st.title("Explain Prediction")

tx = st.text_input("Transaction ID")

if st.button("Explain"):

    try:
        res = requests.get(f"{API}/explain/{tx}")

        data = res.json()

        if "error" in data:
            st.warning(data["error"])
        else:
            st.json(data)

    except:
        st.error("Backend server not running")