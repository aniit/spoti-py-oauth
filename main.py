import dotenv
import json
import requests
import os
import base64
import time
from fastapi import FastAPI


app = FastAPI()

@app.get("/")
def init_token_gen():
    dotenv.load_dotenv()
    id = os.getenv("SPOTIFY_CLIENT_ID")
    secret = os.getenv("SPOTIFY_CLIENT_SECRET")
    auth_code = os.getenv("AUTHORIZATION_CODE")

    print(auth_code)
    print(id)
    print(secret)
        
    auth_d = f"{id}:{secret}"
    #print(auth_d)

    auth_b64 = base64.b64encode(auth_d.encode()).decode()
    #print(auth_b64)

    body_at = {
        "grant_type": "authorization_code",
        "code" : auth_code,
        "redirect_uri": "https://127.0.0.1/callback"
    }

    print(body_at)

    headers_at = {
        'content-type': 'application/x-www-form-urlencoded',
        'Authorization' : f'Basic {auth_b64}'
    }

    #print(headers_at)


    init_token_req = requests.post(url="https://accounts.spotify.com/api/token", data=body_at, headers=headers_at)
    print(init_token_req.json())
    init_token_req = init_token_req.json()

    print(init_token_req)

    a_t= init_token_req['access_token']
    r_t = init_token_req['refresh_token']
    e_i = int(time.time()) + init_token_req['expires_in'] - 60

    print(a_t)
    print(r_t)
    print(e_i)

    init_dump = {
        "access_token": a_t,
        "refresh_token": r_t,
        "expires_in": e_i
    }

    init_values = open("init_values.json", "w")

    json.dump(init_dump, init_values)
    print(init_values)

    


   







#import time
#expiry = 3600
#expires_in = int(time.time()) + expiry
#print(time.time())
#print(expires_in)




#print(access_token)

#pdata = {
 #   "Authorization": f"Bearer {access_token}"
#}

#test_req = requests.get(url="https://api.spotify.com/v1/me/tracks")
