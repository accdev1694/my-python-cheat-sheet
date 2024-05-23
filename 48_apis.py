import requests
import sys
import json

# APIs are used to communicate with other programes, services and websites

# uses requests library

response = requests.get(f"https://itunes.apple.com/search?entity=song&limit=10&term={sys.argv[1]}")

# you can go on to format the response some more using the json library

# print(json.dumps(response.json(), indent=2))

# lets target the tracks

track = response.json()

for result in track['results']:
    print(result["trackName"])


