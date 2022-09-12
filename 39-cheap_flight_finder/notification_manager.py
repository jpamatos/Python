from twilio.rest import Client
import os
# To load on VSCode
from dotenv import load_dotenv
load_dotenv()

TWILIO_SID = os.environ.get("TWI_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWI_AUTH")
TWILIO_VIRTUAL_NUMBER = os.environ.get("TWI_NUMBER")
TWILIO_VERIFIED_NUMBER = os.environ.get("MY_NUMBER")


class NotificationManager:
    """If price is lower than expected, send a message with ticket info"""
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
