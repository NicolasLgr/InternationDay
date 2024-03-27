import requests
from dotenv import load_dotenv
import os

load_dotenv() 
def get_lastname():    
    url = os.getenv("URL_PEOPLE_CELEBRATION")
    header = {'User-agent':''}
    response = requests.get(url, headers= header)
    lastname = str(response.content).split(' ')[-1].replace('.', '').replace("'",'')
    
    return lastname
