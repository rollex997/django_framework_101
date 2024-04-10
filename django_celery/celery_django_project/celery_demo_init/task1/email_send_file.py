from django.core.mail import EmailMessage
from django.conf import settings

def send_email(email_id,subject,message,attachment_name, attachment_content):
    # send PDF via email (You can use the email sending logic here )
    email = EmailMessage(subject, message, to=[email_id])
    email.attach(attachment_name, attachment_content, 'application/pdf')
    return str(email.send(fail_silently=False))