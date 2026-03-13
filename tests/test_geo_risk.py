from backend.network_detector import FraudNetworkDetector

def test_detector_creation():
    detector = FraudNetworkDetector()

    assert detector is not None