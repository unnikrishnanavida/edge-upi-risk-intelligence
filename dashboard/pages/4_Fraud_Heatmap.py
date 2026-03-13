import streamlit as st
import requests
import pandas as pd

API = "http://127.0.0.1:8000"

st.title("Fraud Heatmap")

try:

    res = requests.get(API + "/heatmap")

    data = res.json()

    if "error" in data:
        st.warning(data["error"])

    else:
        df = pd.DataFrame(data)

        st.scatter_chart(df)

except:
    st.error("Backend not running")