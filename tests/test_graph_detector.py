from backend.network_detector import FraudNetworkDetector

def test_network_detector():
    detector = FraudNetworkDetector()

    risk = detector.check_network_risk(1, 2)

    assert risk >= 0