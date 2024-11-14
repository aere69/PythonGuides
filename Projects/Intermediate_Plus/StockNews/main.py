import os
import requests
from datetime import datetime as dt, timedelta
import smtplib

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
SENDER_EMAIL = os.environ.get("EMAIL_ACC")
SENDER_PASSWORD = os.environ.get("EMAIL_PASS")

## Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
stock_parameters = {
    "function" : "TIME_SERIES_DAILY",
    "symbol" : STOCK,
    "outputsize" : "compact",
    "apikey" : os.environ.get("STOCKS_API_KEY")
}
request = requests.get(STOCK_ENDPOINT, params=stock_parameters)
request.raise_for_status()

today = str(dt.today()).split(" ")[0]
yesterday = str(dt.today() + timedelta(days=-1)).split(" ")[0]
day_before_yesterday = str(dt.today() + timedelta(days=-2)).split(" ")[0]

records = request.json()["Time Series (Daily)"]
yesterday_trade = records[yesterday]
yesterday_closing_price = yesterday_trade["4. close"]

day_before_yesterday_trade = records[day_before_yesterday]
day_before_yesterday_closing_price = day_before_yesterday_trade["4. close"]

# Workout the percent difference between closing prices
difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
up_down = None
if difference >= 0:
    up_down = "🔺"
else:
    up_down = "🔻"
diff_percent = round((abs(difference) / float(yesterday_closing_price)) * 100)

# If percentage is greater than 5 then get news
if diff_percent > 5:

    ## Use https://newsapi.org
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
    news_parameters = {
        "q" : "tesla",
        "searchIn" : "title",
        "from" : yesterday,
        "language" : "en",
        "sortBy" : "relevancy",
        "apiKey" : os.environ.get("NEWS_API_KEY")
    }
    request = requests.get(NEWS_ENDPOINT, params=news_parameters)
    request.raise_for_status()

    articles = request.json()["articles"]
    total_results = request.json()["totalResults"]

    message = ""
    # Option : Slice the articles array to get only the first 3.
    # first_three_articles = articles[:3]
    # formatted_articles = [f"{STOCK}: {up_down}{diff_percent}%\nTitle : {article["title"]}\nDesctiption : {article["description"]}\nURL : {article["url"]}\n\n" for article in articles]
    if total_results >= 3:
        for i in range(0,3):
            article = articles[i]
            message += f"{STOCK}: {up_down}{diff_percent}%\nTitle : {article["title"]}\nDesctiption : {article["description"]}\nURL : {article["url"]}\n\n"

    #print(message)
    
    ## Optional use https://www.twilio.com
    # Send a seperate message with the percentage change and each article's title and description to your phone number. 
    # Or Send an email.
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=SENDER_EMAIL, password=SENDER_PASSWORD)
        connection.send_message(
            from_addr=SENDER_EMAIL, 
            to_addrs=SENDER_EMAIL, 
            msg=f"Subject: {COMPANY_NAME} Stock News\n\n{message}"
        )
