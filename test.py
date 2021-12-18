from pprint import pprint

import requests


url = 'http://127.0.0.1:5000/api/v1/users'

data = {
    "name": "Eder Reis",
    "email": "ederreis@gamil.com",
    "phone": "067765434567",
    "address": "mauricio de nassak",
    "country": "caruaru"
}
response = requests.post(url, json=data)
pprint(response.json())

response = requests.get(url)
pprint(response.json())

assert response.status_code == 200
