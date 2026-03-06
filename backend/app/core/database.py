import psycopg2
from psycopg2.extras import RealDictCursor

def get_connection():
    conn = psycopg2.connect(
        host="localhost",
        database="edge_upi_risk",
        user="postgres",
        password="unni0666"
    )
    return conn