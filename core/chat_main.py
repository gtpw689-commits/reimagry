from router import route
from state import init_db, record_run
from state_sign import sign_state

def main():
    init_db()
    record_run()

    while True:
        user = input("reimagry> ")
        if user.lower() in ("exit", "quit"):
            break
        result = route(user)
        print(result)
        print("state_signature:", sign_state())

if __name__ == "__main__":
    main()
