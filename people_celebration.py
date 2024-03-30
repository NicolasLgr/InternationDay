import requests
from dotenv import load_dotenv
import os
import json

load_dotenv() 

def get_lastname_json():    
    url = os.getenv("URL_PEOPLE_CELEBRATION_JSON")
    header = {'User-agent':''}
    response = requests.get(url, headers= header)
    encode_response = response.content
    decode_response = encode_response.decode('utf-8')
    objet_json = json.loads(decode_response)
    lastname = objet_json["name"]
    
    return lastname
