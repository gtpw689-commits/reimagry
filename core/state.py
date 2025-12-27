import sqlite3
from datetime import datetime

DB_PATH = "data/state.db"

def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("""
        CREATE TABLE IF NOT EXISTS runs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT
        )
        """)

def record_run():
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(
            "INSERT INTO runs (timestamp) VALUES (?)",
            (datetime.utcnow().isoformat(),)
        )

def load_state():
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.execute("SELECT COUNT(*) FROM runs")
        return {"runs": cur.fetchone()[0]}
