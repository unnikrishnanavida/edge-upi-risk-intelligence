from backend.graph_fraud_detector import GraphFraudDetector

detector = GraphFraudDetector()

detector.add_transaction("user1", "user2")
detector.add_transaction("user2", "user3")
detector.add_transaction("user3", "user4")
detector.add_transaction("user4", "user5")
detector.add_transaction("user5", "user6")

clusters = detector.detect_suspicious_clusters()

print("Suspicious clusters:", clusters)