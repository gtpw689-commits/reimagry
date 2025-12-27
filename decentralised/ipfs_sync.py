import subprocess

def publish(path="data"):
    try:
        out = subprocess.check_output(["ipfs", "add", "-r", path])
        return out.decode()
    except FileNotFoundError:
        return "ipfs not installed"
