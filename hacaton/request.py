import requests


req = requests.get("http://0.0.0.0:8000/hacaton_endpoint?category=web")
print(req.text)