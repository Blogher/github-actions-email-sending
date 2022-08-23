from email import message
from http import server
import smtplib, ssl
import os

port = 465  # For SSL

smtp_server = "smtp.gmail.com"
USER_EMAIL = os.environ.get('USER_EMAIL')
USER_PASSWORD = os.environ.get('USER_PASSWORD')

message = """\
        Subject: Welcome Bidemi

        This is your first email sent with Python.

        Your welcome email is running 
    """

context = ssl.create_default_context()

server = smtplib.SMTP_SSL(smtp_server, port, context=context)

server.login(USER_EMAIL, USER_PASSWORD)
server.sendmail(USER_EMAIL, USER_EMAIL, message)