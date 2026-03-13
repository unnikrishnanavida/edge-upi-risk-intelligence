import torch
import torch.nn as nn
import networkx as nx
import numpy as np

class TemporalGNN(nn.Module):

    def __init__(self, input_dim=4, hidden_dim=16):
        super().__init__()

        self.layer1 = nn.Linear(input_dim, hidden_dim)
        self.layer2 = nn.Linear(hidden_dim, hidden_dim)
        self.output = nn.Linear(hidden_dim, 1)

    def forward(self, x):
        x = torch.relu(self.layer1(x))
        x = torch.relu(self.layer2(x))
        return torch.sigmoid(self.output(x))


class TemporalGraphFraudDetector:

    def __init__(self):
        self.model = TemporalGNN()

    def build_graph(self, transactions):

        G = nx.DiGraph()

        for tx in transactions:

            sender = tx["sender"]
            receiver = tx["receiver"]
            amount = tx["amount"]
            timestamp = tx["timestamp"]

            G.add_edge(sender, receiver, amount=amount, time=timestamp)

        return G

    def graph_features(self, G):

        features = []

        for node in G.nodes():

            degree = G.degree(node)
            in_degree = G.in_degree(node)
            out_degree = G.out_degree(node)

            features.append([degree, in_degree, out_degree, np.random.random()])

        return torch.tensor(features, dtype=torch.float32)

    def detect_fraud(self, transactions):

        G = self.build_graph(transactions)
        X = self.graph_features(G)

        scores = self.model(X)

        fraud_nodes = []

        for node, score in zip(G.nodes(), scores):
            if score.item() > 0.8:
                fraud_nodes.append(node)

        return fraud_nodes