from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

ORIGIN_CITY_IATA = "GRU"  # Airport origin code

# Instance classes objects
data_manager = DataManager()
notification_manager = NotificationManager()
flight_search = FlightSearch()

# Verify if all codes are filled in sheet
sheet = data_manager.get_destination_data()
if sheet[0]["iataCode"] == "":
    city_names = [row["city"] for row in sheet]
    data_manager.city_codes = flight_search.get_destination_codes(city_names)
    data_manager.update_destination_codes()
    sheet_data = data_manager.get_destination_data()

# Save the destinations in a variable
destinations = {
    data["iataCode"]: {
        "id": data["id"],
        "city": data["city"],
        "price": data["lowestPrice"]
    } for data in sheet_data}

# Time interval today and six months from today
tomorrow = datetime.now() + timedelta(days=1)
six_month = datetime.now() + timedelta(days=(6 * 30))

# Test if price is lower than expected for each row in the sheet
for destination in destinations:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow.strftime("%d/%m/%Y"),
        to_time=six_month.strftime("%d/%m/%Y")
    )

    # Send massage
    if flight and flight.price < destination["lowestPrice"]:
        users = data_manager.get_customer_emails()
        emails = [row["email"] for row in users]
        names = [row["firstName"] for row in users]

        message = f"Low price alert! Only £{flight.price} to fly from"
        f" {flight.origin_city}-{flight.origin_airport} to "
        f"{flight.destination_city}-{flight.destination_airport}, from "
        f"{flight.out_date} to {flight.return_date}."
        if flight.stop_overs > 0:
            message += f"\nFlight has {flight.stop_overs} stop over, "
            f"via {flight.via_city}."

        link = f"https://www.google.co.uk/flights?hl=en#flt="
        f"{flight.origin_airport}.{flight.destination_airport}."
        f"{flight.out_date}*{flight.destination_airport}."
        f"{flight.origin_airport}.{flight.return_date}"
        notification_manager.send_emails(emails, message, link)
