import networkx as nx
from pyvis.network import Network
import streamlit as st
import tempfile


class FraudClusterVisualizer:

    def build_graph(self, transactions):

        G = nx.Graph()

        for tx in transactions:

            sender = tx.get("sender")
            receiver = tx.get("receiver")

            if sender and receiver:

                G.add_edge(sender, receiver)

        return G

    def render(self, transactions):

        G = self.build_graph(transactions)

        net = Network(height="600px", width="100%")

        for node in G.nodes():

            net.add_node(node)

        for u, v in G.edges():

            net.add_edge(u, v)

        tmp = tempfile.NamedTemporaryFile(delete=False)

        net.save_graph(tmp.name)

        HtmlFile = open(tmp.name, "r", encoding="utf-8")

        st.components.v1.html(HtmlFile.read(), height=600)