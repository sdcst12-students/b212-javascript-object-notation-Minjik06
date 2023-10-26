import requests
import json

req = requests.get('https://sdcaf.hungrybeagle.com/menu.php')
data = req.text
data=json.loads(data)