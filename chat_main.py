from core.chat_backends import GPT4AllRemoteBackend

# Initialize GPT4All remote backend
gpt4all_backend = GPT4AllRemoteBackend()

def chat(prompt, backend="gpt4all"):
    if backend != "gpt4all":
        return "Invalid backend selected."
    return gpt4all_backend.chat(prompt)

if __name__ == "__main__":
    print("Reimagry GPT4All Remote Chat - type 'exit' to quit")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        response = chat(user_input, backend="gpt4all")
        print(f"GPT4All: {response}")
