def geo_check(tx):

    location = tx.get("location", "").lower()

    high_risk_locations = [
        "russia",
        "north_korea",
        "iran",
        "darknet"
    ]

    if location in high_risk_locations:
        return 0.9

    return 0.3