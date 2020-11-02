from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

def send_a_email(title,content,receiver):
    # Creating message subject and sender
    subject = 'Notification'
    sender = 'Hood Watch'

    #passing in the context vairables
    text_content = render_to_string('email/email.txt',{"title": title,"content":content})
    html_content = render_to_string('email/email.html',{"title": title,"content":content})

    msg = EmailMultiAlternatives(subject,text_content,sender,[receiver])
    msg.attach_alternative(html_content,'text/html')
    msg.send()

