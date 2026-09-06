import json
from pathlib import Path
import time
import requests

file_path = Path(__file__).parent / "init_values.json"

with open(file_path, "r", encoding="utf-8") as file:
    data = json.load(file)
    expires_in = (data["expires_in"])

url = "https://api.spotify.com/v1/me/tracks?limit=50"

if int(time.time()) <= expires_in:
    response = requests.get(url = url, headers = {'Authorization': f'Bearer {data["access_token"]}'})
    print(response.json())

    with open("liked_tracks.json", "w+", encoding="utf-8") as file_t:
        json.dump(response.json(), file_t)
        
elif int(time.time()) > expires_in:
    print("Expired")