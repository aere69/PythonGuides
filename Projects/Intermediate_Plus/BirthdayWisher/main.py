##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import pandas
from random import randint
import datetime as dt
import smtplib

# --- CONSTANTS ---
PATH_TO_PROJECT = "./Projects/Intermediate_Plus/BirthdayWisher/"
SENDER_EMAIL = "myemail@gmail.com"
SENDER_PASSWORD = "12345Pass!"
birthdays = {}

# --- import birthdays ---
def load_birthdays():
    data = pandas.read_csv(PATH_TO_PROJECT+"birthdays.csv")
    birthday_dic = data.to_dict(orient="records")
    return birthday_dic

# --- import random letters ---
def load_random_letter():
    idx = randint(1,3)
    with open(PATH_TO_PROJECT+f"letter_templates/letter_{idx}.txt") as letter_file:
        letter1 = letter_file.read()
    return letter1

# --- Send email
def send_email(email_address, message):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=SENDER_EMAIL, password=SENDER_PASSWORD)
        connection.send_message(
            from_addr=SENDER_EMAIL, 
            to_addrs=email_address, 
            msg=f"Subject:Happy Bithday!!!\n\n{message}"
        )

# ----------------------------------------------------------------

today = dt.datetime.now()
today_tuple = (today.month, today.day)

birthdays = load_birthdays()

for bd in birthdays:
    if (bd["month"], bd["day"]) == today_tuple:
        letter = load_random_letter()
        letter = letter.replace("[NAME]", bd["name"])
        send_email(bd["email"], letter)
