import requests
from datetime import datetime
import smtplib

# My email
EMAIL = "user_email@email.com"
PASSWORD = "user_password"
# My current position
MY_LAT = -19.810900
MY_LONG = -43.175861


def is_iss_overhead():
    """Get ISS position using API"""
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    data = response.json()  # Save data API in variable

    latitude = data["iss_position"]["longitude"]
    longitude = data["iss_position"]["latitude"]

    # if ISS is between +5 and -5 degrees from my position return true
    if MY_LAT - 5 <= latitude <= MY_LAT + 5 or \
            MY_LONG - 5 <= longitude <= MY_LONG + 5:
        return True


def is_night():
    """Using sunrise-sunset API to see if is nighttime in my location"""
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0
    }

    response = requests.get(
        "https://api.sunrise-sunset.org/json",
        params=parameters
    )
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    # If is it nighttime return true
    current_time = datetime.now().hour
    if current_time >= sunset or current_time <= sunrise:
        return True


if is_iss_overhead() and is_night():
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.ehlo()
        connection.starttls()  # Make the connection secure
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=EMAIL,
            msg=f"Subject:Look up👆\n\nThe ISS is above you in the sky.")
