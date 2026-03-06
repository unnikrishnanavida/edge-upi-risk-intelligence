from app.core.database import get_connection

def generate_fraud_heatmap():

    conn = get_connection()
    cursor = conn.cursor()

    query = """
    SELECT DATE(created_at), COUNT(*)
    FROM risk_history
    WHERE risk_level='HIGH'
    GROUP BY DATE(created_at)
    ORDER BY DATE(created_at)
    """

    cursor.execute(query)

    rows = cursor.fetchall()

    heatmap = []

    for row in rows:

        heatmap.append({
            "date": str(row[0]),
            "fraud_count": row[1]
        })

    cursor.close()
    conn.close()

    return heatmap