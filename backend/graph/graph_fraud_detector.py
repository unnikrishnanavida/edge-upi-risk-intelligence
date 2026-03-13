import networkx as nx

fraud_graph = nx.Graph()


def add_connection(user, merchant):

    fraud_graph.add_node(user, type="user")
    fraud_graph.add_node(merchant, type="merchant")

    fraud_graph.add_edge(user, merchant)


def get_graph():

    edges = []

    for u, v in fraud_graph.edges():
        edges.append({"user": u, "merchant": v})

    return edges


def detect_fraud_rings():

    rings = []

    for merchant in fraud_graph.nodes():

        neighbors = list(fraud_graph.neighbors(merchant))

        if len(neighbors) >= 3:

            rings.append({
                "merchant": merchant,
                "users": neighbors
            })

    return rings