import streamlit as st
import requests
from datetime import datetime

API = "http://127.0.0.1:8000"

st.title("Live Transaction Simulator")

amount = st.number_input("Amount", value=5000)

device_score = st.slider("Device Score", 0.0, 1.0, 0.7)

location_score = st.slider("Location Score", 0.0, 1.0, 0.3)

velocity_score = st.slider("Velocity Score", 0.0, 10.0, 2.0)

sender = st.text_input("Sender", "user_1")

receiver = st.text_input("Receiver", "merchant_5")

if st.button("Simulate Transaction"):

    data = {
        "amount": amount,
        "device_score": device_score,
        "location_score": location_score,
        "velocity_score": velocity_score,
        "sender": sender,
        "receiver": receiver,
        "timestamp": str(datetime.now())
    }

    res = requests.post(API + "/predict", json=data)

    st.json(res.json())