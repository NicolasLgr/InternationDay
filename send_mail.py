from email.message import EmailMessage
import ssl
import smtplib

def core_email(receiver, team_mate):
    email_sender = "nico.leger99@gmail.com"
    email_password = "xdbq mtgg pfiq mref"

    subject = "Ton duo pour le nouvel an !!!!"
    body = "Salut la team ! Ton groupe est composé de {} !!! N'hésitez surtout pas à vous contacter !".format(team_mate)

    em = EmailMessage()

    em['From'] = email_sender
    em['To'] = receiver
    em['Subject'] = subject
    em.set_content(body)

    context = ssl._create_unverified_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context = context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, receiver, em.as_string())

