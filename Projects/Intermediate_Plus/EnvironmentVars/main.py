import os
from dotenv import load_dotenv, dotenv_values

PATH_TO_PROJECT = "./Projects/Intermediate_Plus/FlightDeals/"

# Load environment variables defined in .env file to os
load_dotenv()

DOMAIN = os.getenv("DOMAIN")
ADMIN_EMAIL = os.getenv("ADMIN_EMAIL")
ROOT_URL = os.getenv("ROOT_URL")

print(DOMAIN)
print(ADMIN_EMAIL)
print(ROOT_URL)

print("----------------------")

config = {
    **dotenv_values(PATH_TO_PROJECT+".env"), # load environment vars
    **dotenv_values(PATH_TO_PROJECT+".env.shared"), # load shared dev vars
    **dotenv_values(PATH_TO_PROJECT+".env.secret"), # load secret dev vars
    **os.environ, # Load environment variables (will override shared, secret if existing)
}

DOMAIN = config["DOMAIN"]
ADMIN_EMAIL = config["ADMIN_EMAIL"]
ROOT_URL = config["ROOT_URL"]

USER_NAME = config["USER_NAME"]
PASSWORD = config["PASSWORD"]

print(config)
print("----------------------")
print(DOMAIN)
print(ADMIN_EMAIL)
print(ROOT_URL)
print("----------------------")
print(USER_NAME)
print(PASSWORD)
