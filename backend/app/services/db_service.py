from app.core.database import get_connection


def save_transaction(user_id, amount, risk_score, decision):

    conn = get_connection()
    cursor = conn.cursor()

    amount = float(amount)
    risk_score = float(risk_score)

    query = """
    INSERT INTO transactions (user_id, amount, risk_score, decision)
    VALUES (%s, %s, %s, %s)
    """

    cursor.execute(query, (user_id, amount, risk_score, decision))

    conn.commit()
    cursor.close()
    conn.close()


def save_risk_history(user_id, risk_score, risk_level):

    conn = get_connection()
    cursor = conn.cursor()

    risk_score = float(risk_score)

    query = """
    INSERT INTO risk_history (user_id, risk_score, risk_level)
    VALUES (%s, %s, %s)
    """

    cursor.execute(query, (user_id, risk_score, risk_level))

    conn.commit()
    cursor.close()
    conn.close()


def update_trust_score(user_id, trust_score):

    conn = get_connection()
    cursor = conn.cursor()

    trust_score = float(trust_score)

    query = """
    INSERT INTO trust_scores (user_id, trust_score)
    VALUES (%s, %s)
    ON CONFLICT (user_id)
    DO UPDATE SET trust_score = EXCLUDED.trust_score
    """

    cursor.execute(query, (user_id, trust_score))

    conn.commit()
    cursor.close()
    conn.close()


def get_risk_history(user_id):

    conn = get_connection()
    cursor = conn.cursor()

    query = """
    SELECT risk_score, risk_level, created_at
    FROM risk_history
    WHERE user_id=%s
    ORDER BY created_at DESC
    LIMIT 50
    """

    cursor.execute(query, (user_id,))

    rows = cursor.fetchall()

    history = []

    for row in rows:
        history.append({
            "risk_score": float(row[0]),
            "risk_level": row[1],
            "timestamp": str(row[2])
        })

    cursor.close()
    conn.close()

    return history