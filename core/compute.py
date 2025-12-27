from hash_backend import hash_text

def compute_response(prompt: str) -> str:
    return f"Digest: {hash_text(prompt)}"
