import requests

print(requests.get("http://ip-api.com/json").json()['query'])