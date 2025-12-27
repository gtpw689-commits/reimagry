import sys
import hashlib

def main():
    print("Python:", sys.version)
    print("Blake2b OK:", hashlib.blake2b(b"test").hexdigest())

if __name__ == "__main__":
    main()
