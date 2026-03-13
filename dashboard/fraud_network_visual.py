import streamlit as st
import requests
import networkx as nx
import matplotlib.pyplot as plt

API = "http://127.0.0.1:8000"

st.title("Fraud Network Graph")

data = requests.get(f"{API}/fraud-network").json()

G = nx.Graph()

for edge in data:

    user = edge.get("user")
    merchant = edge.get("merchant")

    if user and merchant:
        G.add_edge(user, merchant)

if len(G.nodes) == 0:

    st.info("No network data available")

else:

    fig, ax = plt.subplots()

    nx.draw(G, with_labels=True)

    st.pyplot(fig)