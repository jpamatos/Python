import requests
from datetime import datetime
import os
# To load on VSCode
from dotenv import load_dotenv
load_dotenv()

APP_ID = os.environ.get("NUTRI_ID")
API_KEY = os.environ.get("NUTRI_KEY")
API_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
GENDER = "male"
WEIGHT = 90
HEIGHT = 171
AGE = 30
SHEET_ENDPOINT = os.environ.get("SHEETY_POST")
BEARER = os.environ.get("SHEETY_BEARER")

# Nutritionix Headers
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

# Config of nutrition post
exercises_config = {
    "query": input("Tell me which exercises you did: "),
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": 30
}

# Post a request to get exercises specifics
response = requests.post(
    API_ENDPOINT,
    json=exercises_config,
    headers=headers
)

# Config of Sheety API
today = datetime.now()
result = response.json()
bearer = {
    "Authorization": f"Bearer {BEARER}"
}

# Post a request to save the workout
for exercise in result["exercises"]:
    sheet_config = {
        "workout": {
            "date": today.strftime("%d/%m/%Y"),
            "time": today.strftime("%H:%M:%S"),
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheets_response = requests.post(
        SHEET_ENDPOINT,
        json=sheet_config,
        headers=bearer)
    print(sheets_response.text)
