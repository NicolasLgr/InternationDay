from email.message import EmailMessage
import ssl
import smtplib
from people_celebration import get_lastname_json
from day_celebration import get_day_celebration
from dotenv import load_dotenv
import os
import json
import random

load_dotenv()
lastname = get_lastname_json()
tab_celebrations = get_day_celebration()
str_celebrations = ''
fichier_mots = "mot_liste.txt"
fichier_mots_utilises = "mot_utilise.txt"

def charger_liste(fichier):
    try:
        with open(fichier, "r") as f:
            return [mot.strip() for mot in f.readlines()]
    except FileNotFoundError:
        return []
    
def sauvegarder_liste(fichier, liste):
    with open(fichier, "w") as f:
        f.write("\n".join(liste))

mots_disponibles = charger_liste(fichier_mots)
mots_utilises = charger_liste(fichier_mots_utilises)

if tab_celebrations != None:
    for celebration in tab_celebrations:
        str_celebrations += celebration.lstrip() + '\n'

receiver_value = os.getenv("RECEIVER_LIST")
list_receiver = json.loads(receiver_value)

def core_email(receiver, mot=None):
    email_sender = os.getenv("SENDER")
    email_password = os.getenv("PASSWORD_SCIPT_MAIL")

    subject = "News Letter Python script"
    body = "Aujourd'hui c'est la fête des {} ! \n{}\n".format(lastname, str_celebrations)
    if mot : body += mot
    em = EmailMessage()

    em['From'] = email_sender
    em['To'] = receiver
    em['Subject'] = subject
    em.set_content(body)

    context = ssl._create_unverified_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context = context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, receiver, em.as_string())



for receiver in list_receiver:
    if mots_disponibles:
        if receiver == list_receiver[1]:
        # Choisir un mot aléatoire pour le destinataire spécial
            mot = random.choice(mots_disponibles)
            mot_a_envoyer = "\nMot du jour pour Margot Ferry : " + mot

            # Ajouter le mot aux mots utilisés et l'enlever des mots disponibles
            mots_disponibles.remove(mot)
            mots_utilises.append(mot)

            # Sauvegarder les nouvelles listes
            sauvegarder_liste(fichier_mots, mots_disponibles)
            sauvegarder_liste(fichier_mots_utilises, mots_utilises)

            # Envoyer l'email avec le mot spécial
            core_email(receiver, mot_a_envoyer)
        else:
            core_email(receiver, None)
    else:
        core_email(receiver)