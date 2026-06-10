import requests

def generate_image(prompt):
    """Generate AI image from prompt"""
    url = "https://gen.pollinations.ai/image/" + prompt.replace(" ", "+")
    r = requests.get(url, timeout=30)
    return r.content
