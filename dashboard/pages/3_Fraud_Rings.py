import streamlit as st
import requests

API = "http://127.0.0.1:8000"

st.title("Fraud Rings Detection")

if st.button("Detect Rings"):

    try:
        res = requests.get(API + "/fraud-rings")

        if res.status_code == 200:
            data = res.json()

            if not data["rings"]:
                st.info("No fraud rings detected")

            else:
                st.json(data)

        else:
            st.error(res.text)

    except Exception as e:
        st.error(e)