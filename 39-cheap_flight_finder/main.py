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
data = data_manager.get_destination_data()
if data[0]["iataCode"] == "":
    for line in data:
        line["iataCode"] = flight_search.get_destination_code(line["city"])

    data_manager.destination_data = data
    data_manager.update_destination_codes()

# Time interval today and six months from today
tomorrow = datetime.now() + timedelta(days=1)
six_month = datetime.now() + timedelta(days=(6 * 30))

# Test if price is lower than expected for each row in the sheet
for destination in data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow.strftime("%d/%m/%Y"),
        to_time=six_month.strftime("%d/%m/%Y")
    )

    # Send massage
    if flight and flight.price < destination["lowestPrice"]:
        notification_manager.send_sms(
            message=f"Low price alert! Only ${flight.price} to fly from"
            f"{flight.origin_city}-{flight.origin_airport} to "
            f"{flight.destination_city}-{flight.destination_airport}, "
            f"from {flight.out_date} to {flight.return_date}."
        )
