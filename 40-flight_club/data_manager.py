import os
import requests
from pprint import pprint
# To load on VSCode
from dotenv import load_dotenv
load_dotenv()

SHEETY_GET = os.environ.get("FLIGHT_GET")
SHEETY_PUT = os.environ.get("FLIGHT_PUT")
SHEETY_POST = os.environ.get("FLIGHT_POST")
BEARER = os.environ.get("FLIGHT_BEARER")
bearer = {
    "Authorization": f"Bearer {BEARER}"
}


class DataManager:
    """Manage the data from the Prices Sheet"""
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        """Fetch data from the Prices Sheet"""
        response = requests.get(url=f"{SHEETY_GET}/prices", headers=bearer)
        response.raise_for_status()
        self.destination_data = response.json()["prices"]
        return self.destination_data

    def update_destination_codes(self):
        """Update Prices' Sheet data"""
        for city in self.destination_data:
            data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PUT}/prices/{city['id']}",
                json=data,
                headers=bearer
            )
            response.raise_for_status()
            print(response.text)

    def get_customer_emails(self):
        """Fetch user's email from the sheet"""
        response = requests.get(
            url=f"{SHEETY_GET}/users",
            headers=bearer
        )
        response.raise_for_status()
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data
