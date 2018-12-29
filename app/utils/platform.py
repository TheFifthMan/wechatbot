import requests
import os 
from flask import current_app

def get_access_token():
    url = current_app.config["ACCESS_URL"]
    r = requests.get(url,verify=False)
    return r.json()

