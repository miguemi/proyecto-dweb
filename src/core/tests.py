from app.wsgi import *
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from django.template.loader import render_to_string

from app import settings
from core.user.models import User


def send_email():
    try:
        mail_server = smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT)
        print(mail_server.ehlo())
        mail_server.starttls()
        print(mail_server.ehlo())
        mail_server.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
        print('Conectado..')

        email_to = 'agonzalezl22@miumg.edu.gt'

        # Construimos el message simple
        message = MIMEMultipart()
        message['From'] = settings.EMAIL_HOST_USER
        message['To'] = email_to
        message['Subject'] = "Tienes un correo"

        content = render_to_string('send_email.html', {'user': User.objects.get(pk=1)})
        message.attach(MIMEText(content, 'html'))
        mail_server.sendmail(settings.EMAIL_HOST_USER, email_to, message.as_string())
        print('Correo enviado correctamente')
    except Exception as e:
        print(e)


send_email()
