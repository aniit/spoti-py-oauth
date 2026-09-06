from urllib import response
import dotenv
import json
import requests
import os
import base64
import time
from fastapi import FastAPI
from pathlib import Path

#app = FastAPI()

#@app.get("/refresh_token")

#refresh_token_gen():
dotenv.load_dotenv()
id = os.getenv("SPOTIFY_CLIENT_ID")
secret = os.getenv("SPOTIFY_CLIENT_SECRET")
#print(id)
#print(secret)


#read the refresh token from the init_values.json file
from pathlib import Path
file_path = Path(__file__).parent / "init_values.json"
with open(file_path, "r", encoding="utf-8") as file:
     data = json.load(file)
     #print(data)
     refresh_token = (data["refresh_token"])
     expires_in_1 = (data["expires_in"])
     access_token1 = (data["access_token"])            
     #print(refresh_roken1)
     #print(expires_in)
     #print(access_token1)   

auth_d = f"{id}:{secret}"
#print(auth_d)

auth_b64 = base64.b64encode(auth_d.encode()).decode()
#print(auth_b64)

body_rt = {
    "grant_type": "refresh_token",
    "refresh_token": refresh_token 
}
#print(body_rt)

headers_rt = {
     'content-type': 'application/x-www-form-urlencoded',
     'Authorization' : f'Basic {auth_b64}'
     }
#print(headers_rt)

if expires_in_1 <= int(time.time()):
     refresh_token_req = requests.post(url="https://accounts.spotify.com/api/token", data=body_rt, headers=headers_rt)
     refresh_tok_js = refresh_token_req.json()
     #print(refresh_tok_js)
     if refresh_token_req.ok:
          #print(refresh_token_req)
          new_at = refresh_tok_js["access_token"]
          new_et = int(time.time()) + refresh_tok_js["expires_in"]

          with open(file_path, "r", encoding="utf-8") as file_r:
               data_1 = json.load(file_r)
               data_1["access_token"] = new_at
               data_1["expires_in"] = new_et

          with open(file_path, "w", encoding="utf-8") as file_w:
               json.dump(data_1, file_w, indent=4)

     else:
          print(f'Error refreshing token: {refresh_tok_js}')

elif expires_in_1 > int(time.time()):
     print("Access token is still valid. No need to refresh.")
     
