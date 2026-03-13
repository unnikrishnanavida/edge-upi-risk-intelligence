import networkx as nx

def gnn_risk(edges):

    G = nx.Graph()

    # Build graph
    for e in edges:

        user = e.get("user")
        merchant = e.get("merchant")

        if user and merchant:
            G.add_edge(user, merchant)

    suspicious_nodes = []

    # Simple GNN-like heuristic
    for node in G.nodes():

        degree = G.degree(node)

        if degree >= 3:
            suspicious_nodes.append(node)

    return suspicious_nodes