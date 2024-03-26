import requests
from bs4 import BeautifulSoup
from datetime import datetime

months_list = []

def transformer_tableau_en_dictionnaire(tableau):
    resultat = {}
    dic_celebration_days = []
    for element in tableau:
        mot = element.split(' ')
        jour, mois_valeur = mot[0], mot[1]
        # Gérer le cas spécial pour "1er janvier"
        if mois_valeur not in months_list:
            months_list.append(mois_valeur)
            dic_celebration_days.append({})
   
        celebration = element.split(':')[1]
        jour = int(jour.replace('er',''))
        if jour not in dic_celebration_days[len(months_list) - 1]:
        # Gérer le cas où la date existe déjà, en ajoutant la valeur
            dic_celebration_days[len(months_list) - 1][jour] = []
            dic_celebration_days[len(months_list) - 1][jour].append(celebration)
        else:
            dic_celebration_days[len(months_list) - 1][jour].append(celebration)
        
        resultat[mois_valeur] = dic_celebration_days[len(months_list) - 1]
        
    return resultat

def get_day_celebration():
    url = "https://www.journee-mondiale.com/les-journees-mondiales.htm"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
    }
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.text, 'html.parser')
    response = []
    article_elements = soup.find_all('article')
    i = -1
    for article in article_elements:
        i += 1
        fetes = article.find_all('li')
        for fete in fetes:
            response.append(fete.find('a').text)

    dict_of_all_celebration = transformer_tableau_en_dictionnaire(response)
    today_month, today_number = months_list[datetime.now().month - 1], datetime.now().day 
    
    return dict_of_all_celebration[today_month][today_number]

