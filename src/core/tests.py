from app.wsgi import *
from app import settings

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from django.template.loader import render_to_string
from core.user.models import User
from django.template.loader import get_template
from weasyprint import HTML, CSS


def send_email():
    try:
        mail_server = smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT)
        print(mail_server.ehlo())
        mail_server.starttls()
        print(mail_server.ehlo())
        mail_server.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
        print('Conectado..')

        email_to = 'agonzalezl22@miumg.edu.gt'

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


def print_ticket():
    template = get_template("ticket.html")
    context = {"name": "William Jair Dávila Vargas"}
    html_template = template.render(context)
    css_url = os.path.join(settings.BASE_DIR, 'static/lib/bootstrap-4.4.1-dist/css/bootstrap.min.css')
    HTML(string=html_template).write_pdf(target="ticket.pdf", stylesheets=[CSS(css_url)])


print_ticket()
# send_email()
