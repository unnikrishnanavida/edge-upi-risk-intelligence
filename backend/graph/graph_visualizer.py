import networkx as nx
from backend.graph.graph_fraud_detector import get_graph

def export_graph():

    graph = get_graph()

    nodes = list(graph.nodes())
    edges = list(graph.edges())

    return {
        "nodes": nodes,
        "edges": edges
    }