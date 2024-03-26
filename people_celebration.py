import requests

def get_lastname():    
    url = "http://fetedujour.fr/api/v2/Kmp8YooLJomgowgh/text-normal"
    header = {'User-agent':''}
    response = requests.get(url, headers= header)
    lastname = str(response.content).split(' ')[-1].replace('.', '').replace("'",'')
    
    return lastname
