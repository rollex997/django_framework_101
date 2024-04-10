#email related imports
from django.core.mail import EmailMessage
from django.conf import settings

def send_email(name,email,review):
    # Send PDF via email (you can use the email sending logic here)
    email_id = 'aryan268859@gmail.com'  # Replace with recipient's email
    subject = f"Review written by {name}"
    message = f"{review}"
    email = EmailMessage(subject, message, to=[email_id])
    #email.attach(temp_pdf.name, temp_pdf.read(), 'application/pdf') -->Not needed here for now
    return email.send(fail_silently=False)