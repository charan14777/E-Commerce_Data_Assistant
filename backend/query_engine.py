import sqlite3
import os

def run_query(sql_query: str):
    # Use absolute path regardless of where you run the app from
    db_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'db', 'ecommerce.db'))

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    try:
        cursor.execute(sql_query)
        rows = cursor.fetchall()
        cols = [desc[0] for desc in cursor.description]
        result = [dict(zip(cols, row)) for row in rows]
    except Exception as e:
        result = {"error": str(e)}
    finally:
        conn.close()
    return result
