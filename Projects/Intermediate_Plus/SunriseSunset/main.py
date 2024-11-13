import requests

MY_LAT = 51.507351
MY_LON = -0.127758

parameters = {
    "lat": MY_LAT,
    "lng": MY_LON,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()

data = response.json()

sunrise = data["results"]["sunrise"].split("T")[1].split("+")[0]
sunset = data["results"]["sunset"].split("T")[1].split("+")[0]

print(f"Sunrise: {sunrise} - Sunset: {sunset}")
