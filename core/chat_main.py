from prompt_generator import generate_prompt
from compute import compute_response

def main():
    while True:
        user = input("reimagry> ")
        if user.lower() in ("exit", "quit"):
            break
        prompt = generate_prompt(user)
        print(compute_response(prompt))

if __name__ == "__main__":
    main()
