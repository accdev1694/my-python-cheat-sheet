import sys
import requests
import json


response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json').json()

#print(response['bpi']['USD']['rate'])
print(json.dumps(response, indent=2))
    





