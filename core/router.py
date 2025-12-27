from compute import compute_response
from image_analysis import analyze_image
from state import load_state

def route(command: str):
    if command.startswith("/hash "):
        return compute_response(command[6:])
    if command.startswith("/image "):
        return analyze_image(command[7:].strip())
    if command == "/state":
        return load_state()
    return compute_response(command)
