from django.conf import settings
from celery import shared_task

from mailersend import emails

mailer = emails.NewEmail("mlsn.00d1d7cc359b3cfa0781da1571d6c3631ac85af4a577e130d0648412c669ba30")


@shared_task
def send_email(random_code: int, user_email: str):
    try:
        subject='Authentication Code',
        text=f'Your authentication code {random_code}'
        html=f'Your authentication code {random_code}'
        my_email=settings.EMAIL_HOST_USER, recipient_list=[user_email]
        subscriber_list = [].append(user_email)
        mailer.send(my_mail, subscriber_list, subject, html, text)
        return True
    except:
        return False
