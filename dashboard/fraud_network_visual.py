import networkx as nx
from pyvis.network import Network
import streamlit.components.v1 as components

def show_fraud_network(edges):

    G = nx.Graph()

    for edge in edges:
        G.add_edge(edge[0], edge[1])

    net = Network(height="500px", width="100%")

    net.from_nx(G)

    net.save_graph("fraud_network.html")

    HtmlFile = open("fraud_network.html", "r", encoding="utf-8")

    components.html(HtmlFile.read(), height=500)