import requests
import sys
import json

# APIs are used to communicate with other programes, services and websites

# uses requests library



# you can go on to format the response some more using the json library

# print(json.dumps(response.json(), indent=2))

# validate that the user types in the right response
if len(sys.argv) == 2:
    try:
        response = requests.get(f"https://itunes.apple.com/search?entity=song&limit=10&term={sys.argv[1]}")        
        track = response.json()
        for result in track['results']:
            print(result["trackName"])
    except:
        sys.exit("Please add a argument")
        
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")
    
elif len(sys.argv) < 2:
    sys.exit("Too few arguments")


