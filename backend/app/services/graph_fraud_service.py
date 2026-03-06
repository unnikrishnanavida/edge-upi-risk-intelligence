import networkx as nx
from backend.app.core.database import get_connection


def detect_fraud_rings():

    conn = get_connection()
    cur = conn.cursor()

    # Simulated relationships based on transactions
    cur.execute("""
        SELECT user_id, risk_score
        FROM risk_history
        WHERE risk_score > 400
    """)

    rows = cur.fetchall()

    cur.close()
    conn.close()

    G = nx.Graph()

    for row in rows:

        user = row[0]

        G.add_node(user)

    # connect users with similar high risk behaviour
    users = list(G.nodes())

    for i in range(len(users)):
        for j in range(i + 1, len(users)):

            G.add_edge(users[i], users[j])

    clusters = list(nx.connected_components(G))

    suspicious_clusters = []

    for c in clusters:

        if len(c) >= 3:

            suspicious_clusters.append(list(c))

    return suspicious_clusters