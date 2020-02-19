import email_writer
import os
import smtplib
from email.message import EmailMessage
from datetime import date

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

# contacts to receive email
contacts = ['email address here', 'another email address']

msg = EmailMessage()
msg['Subject'] = 'Happy Monday! Ethan\'s Newsletter for the week of ' + str(date.today())
msg['From'] = EMAIL_ADDRESS
msg['To'] = ', '.join(contacts)

msg.set_content('Error: HTML Email not supported.')
msg.add_alternative(email_writer.full_email, subtype='html')


def send_message():
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)