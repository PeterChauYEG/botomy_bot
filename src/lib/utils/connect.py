import requests

def connect(url):
    x = requests.post(url, json={"moves": ["move_left"]})
    return x
