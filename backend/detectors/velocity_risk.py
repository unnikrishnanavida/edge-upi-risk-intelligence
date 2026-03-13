def velocity_check(tx):

    amount = tx.get("amount", 0)

    if amount > 50000:
        return 0.9

    elif amount > 10000:
        return 0.6

    elif amount > 2000:
        return 0.4

    return 0.2