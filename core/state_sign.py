import hashlib
import sqlite3

def sign_state(db_path="data/state.db"):
    h = hashlib.blake2b(digest_size=32)
    with open(db_path, "rb") as f:
        h.update(f.read())
    return h.hexdigest()
