import streamlit as st
import requests
import networkx as nx
import matplotlib.pyplot as plt

st.title("Fraud Network Graph")

if st.button("Refresh Graph"):

    res = requests.get("http://localhost:8000/fraud-graph")

    data = res.json()

    edges = data["edges"]

    G = nx.Graph()

    for e in edges:
        G.add_edge(e["user"], e["merchant"])

    fig, ax = plt.subplots()

    nx.draw(G, with_labels=True)

    st.pyplot(fig)