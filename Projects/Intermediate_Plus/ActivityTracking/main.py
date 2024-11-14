import os
import requests
from datetime import datetime as dt

PIXELA_USER_ENDPOINT = "https://pixe.la/v1/users"
PIXELA_USER = os.environ.get("PIXELA_USER_NAME")
PIXELA_TOKEN = os.environ.get("PIXELA_TOKEN")

pixela_user_params = {
    "token" : PIXELA_TOKEN,
    "username" : PIXELA_USER,
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes"
}

# ----- Create user in pixela -----
#response = requests.post(url=PIXELA_USER_ENDPOINT, json=pixela_user_params)
#print(response.text)

req_headers = {
    "X-USER-TOKEN" : PIXELA_TOKEN
}

# ----- Creae a new graph -----
graph_endpoint = f"{PIXELA_USER_ENDPOINT}/{PIXELA_USER}/graphs"
graph_config = {
    "id" : "graph1",
    "name" : "Cycling Graph",
    "unit" : "Km",
    "type" : "float",
    "color" : "sora"
}
#response = requests.post(url=graph_endpoint, json=graph_config, headers=req_headers)
#print(response.text)

# ----- Place a Pixel -----
graph_id = "graph1"
graph_pixel_endpoint = f"{PIXELA_USER_ENDPOINT}/{PIXELA_USER}/graphs/{graph_id}"
graph_pixel_config = {
    "date" : dt.today().strftime("%Y%m%d"),
    "quantity" : "5.0",
}
#response = requests.post(url=graph_pixel_endpoint, json=graph_pixel_config, headers=req_headers)
#print(response.text)

# ----- Update a Pixel -----
date = dt.today().strftime("%Y%m%d")
graph_update_endpoint = f"{PIXELA_USER_ENDPOINT}/{PIXELA_USER}/graphs/{graph_id}/{date}"
graph_pixel_config = {
    "quantity" : "7.50",
}
#response = requests.put(url=graph_update_endpoint, json=graph_pixel_config, headers=req_headers)
#print(response.text)

# ----- Delete a Pixel -----
graph_delete_endpoint = f"{PIXELA_USER_ENDPOINT}/{PIXELA_USER}/graphs/{graph_id}/{date}"
#response = requests.delete(url=graph_delete_endpoint, headers=req_headers)
#print(response.text)
