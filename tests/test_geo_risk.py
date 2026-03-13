from backend.network_detector import GraphFraudDetector

def test_graph_creation():
    detector = GraphFraudDetector()
    assert detector is not None