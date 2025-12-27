def publish(path: str):
    try:
        import subprocess
        result = subprocess.check_output(["ipfs", "add", "-r", path])
        print(result.decode())
    except FileNotFoundError:
        raise RuntimeError("ipfs binary not installed")
