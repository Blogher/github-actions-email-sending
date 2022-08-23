from email import message
from http import server
import smtplib, ssl
import os

port = 465  # For SSL

smtp_server = "smtp.gmail.com"
USER_EMAIL = os.environ.get('USER_EMAIL')
USER_PASSWORD = os.environ.get('USER_PASSWORD')
RECIPIENT_PASSWORD = os.environ.get('RECIPIENT_PASSWORD')

message = """\
        Subject: Hey there!

        This email was sent with Python, sorry for the troubles, I'm a newbie who's exploring the world of Python.

        With kind regards,

        Bidemi.
    """

context = ssl.create_default_context()

server = smtplib.SMTP_SSL(smtp_server, port, context=context)

server.login(USER_EMAIL, USER_PASSWORD)
server.sendmail(USER_EMAIL, USER_EMAIL, message)