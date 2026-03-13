from backend.network_detector import FraudNetworkDetector

def test_network_risk():
    detector = FraudNetworkDetector()

    risk = detector.check_network_risk(1, 2)

    assert risk is not None