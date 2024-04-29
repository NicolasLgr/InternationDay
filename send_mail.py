from email.message import EmailMessage
import ssl
import smtplib
from people_celebration import get_lastname_json
from day_celebration import get_day_celebration
from dotenv import load_dotenv
import os
import json

load_dotenv() 
lastname = get_lastname_json()
tab_celebrations = get_day_celebration()
str_celebrations = ''

if tab_celebrations != None:
    for celebration in tab_celebrations:
        str_celebrations += celebration.lstrip() + '\n'

receiver_value = os.getenv("RECEIVER_LIST")
list_receiver = json.loads(receiver_value)

def core_email(receiver):
    email_sender = os.getenv("SENDER")
    email_password = os.getenv("PASSWORD_SCIPT_MAIL")

    subject = "News Letter Python script"
    body = "Aujourd'hui c'est la fête des {} ! \n{}".format(lastname, str_celebrations)

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
    core_email(receiver)