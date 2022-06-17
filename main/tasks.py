from django.core.mail import send_mail
from sendemail.celery import app
from django.core.mail import EmailMessage
from time import sleep

#from .service import send
from .models import Contact

@app.task
def send_email(email, body):
    mail_subject = 'Celery test message'
    email = EmailMessage(mail_subject, body, to=[email])
    email.send()


# @app.task
# def send_beat_email(email, body):
#     for contact in Contact.objects.all():
#         mail_subject = 'Celery test message in every 1 minut'
#         mail = EmailMessage(mail_subject, body, to=[email])
#         email.send()

@app.task
def send_beat_email():
    for contact in Contact.objects.all():
        send_mail(
            'Celery test message in every 1 minute',
            'you will get message again in 1 minute',
            "moliya@gmail.com",
            [contact.email],
            fail_silently=False,
        )
