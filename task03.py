import requests
import json

req = requests.get('https://open-meteo.com/en/docs')
data = req.text
data=json.dumps(data)
data=json.loads(data)

print(data)