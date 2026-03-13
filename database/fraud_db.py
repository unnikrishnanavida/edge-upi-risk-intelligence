import sqlite3

DB_NAME = "fraud_monitor.db"

def init_db():

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS flagged_transactions(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        amount REAL,
        risk_score REAL,
        decision TEXT
    )
    """)

    conn.commit()
    conn.close()


def save_flagged(user_id, amount, risk_score, decision):

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO flagged_transactions(user_id,amount,risk_score,decision) VALUES (?,?,?,?)",
        (user_id, amount, risk_score, decision)
    )

    conn.commit()
    conn.close()


def get_flagged():

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM flagged_transactions")

    rows = cursor.fetchall()

    conn.close()

    return rows