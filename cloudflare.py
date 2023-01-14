import requests
import json

api_key = "API_KEY"

zone_id = "ZONE_ID OF YOUR DOMAIN"

api_endpoint = "https://api.cloudflare.com/client/v4/zones/"API_KEY"/dns_records"

dns_records = {
    "type": "",
    "name": "SUBDOMAIN",
    "content": "",
    "proxied": False # False/True - If True, It will be proxied like a mask by cloudflare which blocks the identity of that domain
}

headers = {
    "Content-Type": "application/json",
    "X-Auth-Email": "CLOUDFLARE-EMAIL",
    "X-Auth-Key": "API_KEY"
}

response = requests.post(api_endpoint, headers=headers, json=dns_records)

if response.status_code == 200:
    print("DNS Records added Successfully!")
else:
    print(f"Error adding DNS Records : {response.json()['errors']}")
