import psycopg2

class PostgresService:

    def __init__(self):

        self.conn = psycopg2.connect(
            host="localhost",
            database="upi_risk",
            user="postgres",
            password="password"
        )

        self.cursor = self.conn.cursor()

    def save_transaction(self, user_id, amount, risk_score):

        self.cursor.execute(
            """
            INSERT INTO transactions (user_id, amount, risk_score)
            VALUES (%s,%s,%s)
            """,
            (user_id, amount, risk_score)
        )

        self.conn.commit()

    def get_user_history(self, user_id):

        self.cursor.execute(
            """
            SELECT risk_score FROM transactions
            WHERE user_id=%s
            ORDER BY id DESC
            LIMIT 20
            """,
            (user_id,)
        )

        return self.cursor.fetchall()