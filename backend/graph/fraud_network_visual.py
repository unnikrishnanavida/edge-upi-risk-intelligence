import streamlit as st
import requests
import networkx as nx
import matplotlib.pyplot as plt

st.header("Fraud Network Graph")

if st.button("Load Fraud Network"):

    try:

        response = requests.get(f"{API_URL}/fraud-network")

        graph_data = response.json()

        G = nx.Graph()

        # Case 1: backend returns list of edges
        if isinstance(graph_data, list):

            for edge in graph_data:
                if len(edge) == 2:
                    G.add_edge(edge[0], edge[1])

        # Case 2: backend returns dictionary
        elif isinstance(graph_data, dict):

            for node, neighbors in graph_data.items():
                for n in neighbors:
                    G.add_edge(node, n)

        if len(G.nodes) == 0:

            st.info("No transactions yet")

        else:

            pos = nx.spring_layout(G)

            edge_x = []
            edge_y = []

            for edge in G.edges():

                x0, y0 = pos[edge[0]]
                x1, y1 = pos[edge[1]]

                edge_x += [x0, x1, None]
                edge_y += [y0, y1, None]

            edge_trace = go.Scatter(
                x=edge_x,
                y=edge_y,
                mode='lines',
                line=dict(width=1, color="#888")
            )

            node_x = []
            node_y = []
            text = []

            for node in G.nodes():

                x, y = pos[node]

                node_x.append(x)
                node_y.append(y)
                text.append(node)

            node_trace = go.Scatter(
                x=node_x,
                y=node_y,
                mode='markers+text',
                text=text,
                textposition="bottom center",
                marker=dict(size=20, color="skyblue")
            )

            fig = go.Figure(data=[edge_trace, node_trace])

            st.plotly_chart(fig, use_container_width=True)

    except Exception as e:

        st.error(f"Graph error: {e}")