from backend.network_detector import detect_network_risk

def test_network_risk():
    result = detect_network_risk(1, "deviceA")
    assert result is not None