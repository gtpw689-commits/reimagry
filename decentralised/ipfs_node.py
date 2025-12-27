try:
    import ipfshttpclient
except ImportError:
    ipfshttpclient = None

def connect():
    if not ipfshttpclient:
        raise RuntimeError("ipfshttpclient not installed")
    return ipfshttpclient.connect()
