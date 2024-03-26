import requests

url = "http://fetedujour.fr/api/v2/Kmp8YooLJomgowgh/text-normal"
header = {'User-agent':''}
response = requests.get(url, headers= header)
prenom = str(response.content).split(' ')[-1].replace('.', '').replace("'",'')

