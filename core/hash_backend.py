import hashlib

def hash_text(text: str) -> str:
    return hashlib.blake2b(text.encode("utf-8"), digest_size=32).hexdigest()
