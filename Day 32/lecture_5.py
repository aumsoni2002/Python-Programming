import random
import datetime as dt
import os
import smtplib
from email.message import EmailMessage

now = dt.datetime.now()
today = now.weekday()
sender = os.environ["EMAIL_ADDRESS"]
app_password = os.environ["EMAIL_APP_PASSWORD"]
recipient = os.environ["EMAIL_RECIPIENT"]

if today == 5:
    with open(file="./quotes.txt", mode="r", encoding="utf-8") as file:
        quotes = file.readlines()
    random_quote = random.choice(quotes)

    message = EmailMessage()
    message["Subject"] = "Monday Motivation Quote"
    message["From"] = sender
    message["To"] = recipient
    message.set_content(random_quote)

    with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=sender, password=app_password)
        connection.send_message(message)
