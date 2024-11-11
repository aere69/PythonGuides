import smtplib
import datetime as dt
import random

SENDER_EMAIL = "sender@gmail.com"
SENDER_PASSWORD = "12345Pass!"

now = dt.datetime.now()
week_day = now.weekday()
if week_day == 0:
    # --- On Monday
    with open("quotes.tx") as quotes_file:
        all_quotes = quotes_file.readlines()
        quote = random.choice(all_quotes)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=SENDER_EMAIL, password=SENDER_PASSWORD)
        connection.send_message(
            from_addr=SENDER_EMAIL, 
            to_addrs="recipient@mailservice.com", 
            msg=f"Subject:Inspirational Quote\n\n{quote}"
        )

