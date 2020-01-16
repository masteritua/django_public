from django.core.mail import send_mail
from django.conf import settings
from smtplib import SMTPException
from django.core.files import File


def save_to_file(text):
    with open(settings.EMAIL_FILE_PATH_REPORT, 'w') as f:
        myfile = File(f)
        myfile.write(text)
    myfile.closed
    f.closed


def email(subject, message):
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['masteritua@gmail.com']

    try:
        send_mail(
            subject,
            message,
            email_from,
            recipient_list,
            fail_silently=True
        )

        save_to_file('Письмо успешно отправилось!')

    except SMTPException as e:

        save_to_file(f'Ошибка отправки письма: {e}')
