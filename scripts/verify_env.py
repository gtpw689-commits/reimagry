import sys, hashlib, sqlite3

print("Python OK:", sys.version)
print("Hash OK:", hashlib.blake2b(b"x").hexdigest())
print("SQLite OK:", sqlite3.sqlite_version)
