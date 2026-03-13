import networkx as nx

# global graph
G = nx.Graph()

def add_edge(sender, receiver):
    G.add_edge(sender, receiver)

def graph_risk_score(user):

    if user not in G:
        return 0

    degree = G.degree(user)

    neighbors = list(G.neighbors(user))

    suspicious = 0

    for n in neighbors:
        if G.degree(n) > 5:
            suspicious += 1

    score = degree * 10 + suspicious * 20

    if score > 100:
        score = 100

    return score