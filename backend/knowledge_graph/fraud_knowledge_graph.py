import networkx as nx


class FraudKnowledgeGraph:

    def __init__(self):

        self.graph = nx.Graph()

    def add_relation(self, user, device):

        self.graph.add_edge(user, device)

    def risk_score(self, entity):

        degree = self.graph.degree(entity)

        return min(degree / 10, 1)