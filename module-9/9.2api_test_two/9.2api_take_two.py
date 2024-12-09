# Keanu Foltz CSD-325 12/9/24
# Tests and formats a simple API's response

import requests

response = requests.get('https://thesimpsonsquoteapi.glitch.me/quotes')
print(response.status_code)

print(response.json())
import json

def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

jprint(response.json())


