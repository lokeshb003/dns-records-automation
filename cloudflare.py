import requests
import json

api_key = "f92de1c5ba4ea75bfe3fe6f5c952cc8c495d2"

zone_id = "c7571ec09e85a9e59afc601845e8dd98"

api_endpoint = "https://api.cloudflare.com/client/v4/zones/c7571ec09e85a9e59afc601845e8dd98/dns_records"

dns_records = {
    "type": "A",
    "name": "linkedin",
    "content": "192.46.215.40",
    "proxied": False
}

headers = {
    "Content-Type": "application/json",
    "X-Auth-Email": "lokeshbalaji2021@gmail.com",
    "X-Auth-Key": "f92de1c5ba4ea75bfe3fe6f5c952cc8c495d2"
}

response = requests.post(api_endpoint, headers=headers, json=dns_records)

if response.status_code == 200:
    print("DNS Records added Successfully!")
else:
    print(f"Error adding DNS Records : {response.json()['errors']}")