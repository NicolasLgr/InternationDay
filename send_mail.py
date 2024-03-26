from email.message import EmailMessage
import ssl
import smtplib
from people_celebration import get_lastname
from day_celebration import get_day_celebration

lastname = get_lastname()
tab_celebrations = get_day_celebration()
str_celebrations = ''
for celebration in tab_celebrations:
    str_celebrations += celebration.lstrip() + '\n'

my_mail = "nico.leger99@gmail.com"

def core_email(receiver):
    email_sender = "nico.leger99@gmail.com"
    email_password = "xdbq mtgg pfiq mref"

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

core_email(my_mail)

    # email_sender = "nico.leger99@gmail.com"
    # email_password = "xdbq mtgg pfiq mref"