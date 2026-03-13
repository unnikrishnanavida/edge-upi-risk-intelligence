from backend.network_detector import GraphFraudDetector

def test_graph_detector():
    detector = GraphFraudDetector()

    detector.add_transaction("user1", "user2")
    detector.add_transaction("user2", "user3")

    clusters = detector.detect_suspicious_clusters()

    assert clusters is not None