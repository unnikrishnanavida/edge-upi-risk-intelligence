import torch
import torch.nn as nn
from torch_geometric.nn import SAGEConv


class TemporalGNN(nn.Module):

    def __init__(self, input_dim=16, hidden=32):

        super().__init__()

        self.conv1 = SAGEConv(input_dim, hidden)
        self.conv2 = SAGEConv(hidden, hidden)

        self.fc = nn.Linear(hidden, 1)

    def forward(self, x, edge_index):

        x = self.conv1(x, edge_index)
        x = torch.relu(x)

        x = self.conv2(x, edge_index)
        x = torch.relu(x)

        risk = self.fc(x)

        return torch.sigmoid(risk)