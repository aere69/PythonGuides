import os
import requests
from twilio.rest import Client

# ----- Constants -----
OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
OWM_API_KEY = os.environ.get("OWM_APIKEY")
MY_LAT = 51.357372
MY_LON = -0.175281
TWILIO_ACC_SID = os.environ.get("TWILIO_ACC_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")

parameters = {
    "lat": 53.214470,
    "lon": 6.566480,
    "cnt": 4,
    "appid": OWM_API_KEY,
}

request = requests.get(OWM_ENDPOINT, params=parameters)
request.raise_for_status()

forecasts = request.json()["list"]

will_rain = False
for forecast_entry in forecasts:
    weather = forecast_entry["weather"]
    for weather_entry in weather:
        if int(weather_entry["id"])<700:
            will_rain = True

if will_rain:
    client = Client(TWILIO_ACC_SID,TWILIO_AUTH_TOKEN)
    message = client.messages \
        .create(
            body="It will rain - Take your umbrella",
            from_="sender-phone#",
            to="recipient-phone#"
        )
    print(message.sid)
