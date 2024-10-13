from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings


@shared_task
def send_password_reset_email(email):
    subject = 'Password Reset Request'
    message = 'Please click the link below to reset your password.'
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [email])
