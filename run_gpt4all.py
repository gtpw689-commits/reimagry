#!/data/data/com.termux/files/usr/bin/python3
import os
import json
from gpt4all import GPT4All

# Prompt input
prompt = input("Enter prompt for GPT4All: ")

# Path to your local GPT4All model
model_path = os.path.join(os.getcwd(), "models/gpt4all-lora-quantized.bin")
model = GPT4All(model_path)

# Generate response
response = model.generate(prompt)
print(json.dumps({"response": response}))
