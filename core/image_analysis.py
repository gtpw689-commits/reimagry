from PIL import Image

def analyze_image(path):
    img = Image.open(path)
    return {
        "size": img.size,
        "mode": img.mode,
        "format": img.format
    }
