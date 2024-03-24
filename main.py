import requests
from bs4 import BeautifulSoup

url = "https://www.journee-mondiale.com/les-journees-mondiales.htm"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}
page = requests.get(url, headers=headers)
soup = BeautifulSoup(page.text, 'html.parser')

response = []

article_elements = soup.find_all('article')
i = -1

def transformer_tableau_en_dictionnaire(tableau):
    resultat = {}
    for element in tableau:
        mot = element.split('')
        jour, mois_valeur = mot[0], mot[1]
        # Gérer le cas spécial pour "1er janvier"
        if 'er' in jour:
            jour = jour.replace('er', '')
        mois, valeur = mois_valeur.split(' ')[1], mois_valeur.split(' ')[0]
        if mois not in resultat:
            resultat[mois] = {}
        if int(jour) in resultat[mois]:
            # Gérer le cas où la date existe déjà, en ajoutant la valeur
            resultat[mois][int(jour)] += ", " + valeur
        else:
            resultat[mois][int(jour)] = valeur
    return resultat

for article in article_elements:
    i += 1
    fetes = article.find_all('li')
    month = article.find('h1').text
    for fete in fetes:
        response.append(fete.find('a').text)

final = {}
essai = 'test'
tests = ['1er janvier : Journée Mondiale de la Paix', '2 janvier : Journée Mondiale du proute', '3 fevrier : Journée Mondiale qui tue']
temp = {}
for test in tests:
    number, month= test.split(' ')[0], test.split(' ')[1]
    value = test.split(':')[1]
    number = number.replace('er','')
    number = int(number)
    temp[number] = value
    final[month] = temp
    temp.clear()
print(final)
print(temp)
