from django.core.mail import send_mail
from .models import Contact

def send(user_email):
    send_mail(
        'You registered',
        'Here is the message.',
        'jobirumirovmoliya@gmail.com',
        [user_email],
        fail_silently=False
    )

# def send_2(user_email):
#     for contact in Contact.objects.all():
#         send_mail(
#             'You registered',
#             'We send you a message in every 5 minute',
#             'jobirumirovmoliya@gmail.com',
#             [contact.user_email],
#             fail_silently=False,
#         )
