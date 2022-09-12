import requests
from flight_data import FlightData
from datetime import datetime
import os
# To load on VSCode
from dotenv import load_dotenv
load_dotenv()

KIWI_KEY = os.environ.get("KIWI_KEY")
KIWI_API = "https://api.tequila.kiwi.com"


class FlightSearch:
    """Search flights using Kiwi API"""
    def get_destination_code(self, city):
        """Use Kiwi API to get city code"""
        # API parameters
        query = {
            "term": city,
            "location_types": "city"
        }

        # API header
        header = {
            "apikey": KIWI_KEY
        }

        # Get request
        response = requests.get(
            url=f"{KIWI_API}/locations/query",
            params=query,
            headers=header
        )
        # Result
        response.raise_for_status()
        result = response.json()["locations"][0]
        airport = result["code"]

        return airport

    def check_flights(self, origin, destination, from_time, to_time):
        """Check if flight exists and return flight's data"""
        # API header
        header = {
            "apikey": KIWI_KEY
        }

        # API parameters
        query = {
            "fly_from": origin,
            "fly_to": destination,
            "date_from": from_time,
            "date_to": to_time,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "USD"
        }

        # Get request
        response = requests.get(
            url=f"{KIWI_API}/v2/search",
            params=query,
            headers=header
        )
        response.raise_for_status()

        # Try to see if a flight is found
        try:
            data = response.json()["data"][0]
        except IndexError:
            response = requests.get(
                url=f"{KIWI_API}/v2/search",
                params=query,
                headers=header
            )
            response.raise_for_status()
            data = response.json()["data"][0]

            flight = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][1]["cityTo"],
                destination_airport=data["route"][1]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][2]["local_departure"].split("T")[0],
                stop_overs=1,
                via_city=["route"][0]["cityTo"]
            )

            print(f"{flight.destination_city}: ${flight.price}")

            return flight
        # If found save flight's data
        else:
            flight = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0]
            )

            print(f"{flight.destination_city}: ${flight.price}")

            return flight
