import json
from prompt_generator import generate_prompt
from compute import compute_response

STATE_FILE = "data/state.json"

def load_state():
    with open(STATE_FILE, "r") as f:
        return json.load(f)

def save_state(state):
    with open(STATE_FILE, "w") as f:
        json.dump(state, f, indent=2)

def main():
    state = load_state()
    state["runs"] += 1
    save_state(state)

    while True:
        user = input("reimagry> ")
        if user.lower() in ("exit", "quit"):
            break
        prompt = generate_prompt(user)
        print(compute_response(prompt))

if __name__ == "__main__":
    main()
