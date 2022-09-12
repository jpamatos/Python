import smtplib
from twilio.rest import Client
import os
# To load on VSCode
from dotenv import load_dotenv
load_dotenv()

TWILIO_SID = os.environ.get("TWI_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWI_AUTH")
TWILIO_VIRTUAL_NUMBER = os.environ.get("TWI_NUMBER")
TWILIO_VERIFIED_NUMBER = os.environ.get("MY_NUMBER")
MY_EMAIL = os.environ.get("EMAIL")
MY_PASSWORD = os.environ.get("EMAIL_PASSWORD")
MAIL_SMTP = os.environ.get("MAIL_SMTP")


class NotificationManager:
    """If price is lower than expected, send a message with ticket info
    or an e-mail"""
    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        """Send message"""
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)

    def send_emails(self, emails, message, flight_link):
        with smtplib.SMTP(MAIL_SMTP, port=587) as connection:
            connection.starttls()  # Make connection secure
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject: New Low Price Flight!\n\n{message}"
                    f"\n{flight_link}".encode("utf-8")
                )
