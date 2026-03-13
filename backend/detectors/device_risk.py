def device_check(tx):

    device_id = tx.get("device_id", "")

    risky_devices = [
        "unknown_device",
        "emulator",
        "rooted_device",
        "test_device"
    ]

    if device_id in risky_devices:
        return 0.9

    return 0.2