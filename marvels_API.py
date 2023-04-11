import hashlib
import requests

# Enter your API keys here
PUBLIC_KEY = "YOUR_PUBLIC_KEY"
PRIVATE_KEY = "YOUR_PRIVATE_KEY"

# Create a hash of the timestamp, public key, and private key
timestamp = "1"  # You can change the timestamp to the current time if you want
hash_input = timestamp + PRIVATE_KEY + PUBLIC_KEY
hash_output = hashlib.md5(hash_input.encode()).hexdigest()

# Set up the API request URL
url = "https://gateway.marvel.com/v1/public/characters"
params = {
    "apikey": PUBLIC_KEY,
    "ts": timestamp,
    "hash": hash_output,
    "name": "Spider-Man"  # You can change the character name here
}

# Send the API request and print the results
response = requests.get(url, params=params)
if response.status_code == 200:
    data = response.json()["data"]
    for result in data["results"]:
        print(result["name"])
        print(result["description"])
        print(result["thumbnail"]["path"] + "." + result["thumbnail"]["extension"])
else:
    print("Error:", response.status_code)
