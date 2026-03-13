import networkx as nx

G = nx.Graph()

def detect_graph_fraud(user_id, merchant_id, amount):

    if user_id not in G:
        G.add_node(user_id, type="user")

    if merchant_id not in G:
        G.add_node(merchant_id, type="merchant")

    G.add_edge(user_id, merchant_id, weight=amount)

    score = G.degree(user_id)

    if score > 5:
        return {"fraud": True}

    return {"fraud": False}