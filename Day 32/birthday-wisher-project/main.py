##################### Extra Hard Starting Project ######################
import datetime as dt
import os
import smtplib
import random
import pandas as pd
from email.message import EmailMessage

# 1. Update the birthdays.csv - DONE

# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
current_month = now.date().month
current_day = now.date().day
sender = os.environ["EMAIL_ADDRESS"]
app_password = os.environ["EMAIL_APP_PASSWORD"]

data = pd.read_csv("./birthdays.csv")
birthday_filter = (data["month"] == current_month) & (data["day"] == current_day)
birthday_row = data[birthday_filter]
birthday_dict = birthday_row.to_dict(orient="records")

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
for person in birthday_dict:
    random_letter_num = random.randint(1, 3)

    with open(f"./letter_templates/letter_{random_letter_num}.txt", mode="r", encoding="utf-8") as file:
        letter_template = file.read()
        letter = letter_template.replace("[NAME]", person["name"])

    # 4. Send the letter generated in step 3 to that person's email address.
    message = EmailMessage()
    message["Subject"] = "Happy Birthday"
    message["From"] = sender
    message["To"] = person["email"]
    message.set_content(letter)

    with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=sender, password=app_password)
        connection.send_message(message)
