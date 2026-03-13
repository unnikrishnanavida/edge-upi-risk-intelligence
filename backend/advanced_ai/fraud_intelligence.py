import time
from collections import defaultdict
import networkx as nx


# -----------------------------------------
# USER TRUST SCORE SYSTEM
# -----------------------------------------

user_trust = defaultdict(lambda: 0.5)


def update_trust(user, risk):

    if risk > 0.7:
        user_trust[user] -= 0.05
    else:
        user_trust[user] += 0.01

    user_trust[user] = max(0, min(1, user_trust[user]))

    return user_trust[user]


# -----------------------------------------
# TEMPORAL ANOMALY DETECTION
# -----------------------------------------

user_last_time = {}


def temporal_risk(user):

    now = time.time()

    if user not in user_last_time:
        user_last_time[user] = now
        return 0

    delta = now - user_last_time[user]
    user_last_time[user] = now

    if delta < 5:
        return 0.8

    if delta < 20:
        return 0.4

    return 0


# -----------------------------------------
# FRAUD PATTERN MEMORY
# -----------------------------------------

pattern_memory = defaultdict(int)


def pattern_risk(device, merchant):

    key = f"{device}-{merchant}"

    pattern_memory[key] += 1

    if pattern_memory[key] > 10:
        return 0.7

    return 0


# -----------------------------------------
# GRAPH INTELLIGENCE
# -----------------------------------------

def graph_intelligence(graph):

    G = nx.Graph()

    for edge in graph:
        G.add_edge(edge["user"], edge["merchant"])

    centrality = nx.degree_centrality(G)

    ranked = sorted(
        centrality.items(),
        key=lambda x: x[1],
        reverse=True
    )

    return ranked[:10]