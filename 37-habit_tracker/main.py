import requests
from datetime import datetime
import os
# To load on VSCode
from dotenv import load_dotenv
load_dotenv()

pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = os.environ.get("PXL_USR")
TOKEN = os.environ.get("PXL_TK")
GRAPH_ID = "graph1"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# Uncomment to create a account at pixela
# response = requests.post(
#     url=pixela_endpoint,
#     json=user_params
# )


graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Coding Hours Graph",
    "unit": "minute",
    "type": "int",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# Uncomment to create a graph
# response = requests.post(
#     url=graph_endpoint,
#     json=graph_config,
#     headers=headers
# )

pixel_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

today = datetime.now()

pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many minutes did you code today?")
}

# Uncomment to create a pixel in your graph
# response = requests.post(
#     url=pixel_endpoint,
#     json=pixel_config,
#     headers=headers
# )

update_endpoint = f"{pixel_endpoint}/{today.strftime('%Y%m%d')}"

pixel_config = {
    "quantity": input("How many minutes are you correcting?")
}

# Uncomment to update a pixel in your graph
# response = requests.put(
#     url=update_endpoint,
#     json=pixel_config,
#     headers=headers
# )

delete_endpoint = f"{pixel_endpoint}/{today.strftime('%Y%m%d')}"

# Uncomment to delete a pixel in your graph
# response = requests.delete(
#     url=delete_endpoint,
#     headers=headers
# )
