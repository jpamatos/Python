import requests
import os
from twilio.rest import Client
# To load on VSCode
from dotenv import load_dotenv
load_dotenv()

STOCK_NAME = "AAPL"
COMPANY_NAME = "Apple Inc."

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_API_KEY = os.environ.get("STOCK_KEY")
NEWS_API_KEY = os.environ.get("NEWS_KEY")
TWILIO_SID = os.environ.get("TWI_SID")
TWILIO_KEY = os.environ.get("TWI_AUTH")
MESSAGING_SERVICE_SID = os.environ.get("MSG_SERVICE_SID")
NUMBER = os.environ.get("MY_NUMBER")

# API's parameters
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}

# Get API data
response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]

# Getting yesterday's closing price
yd_data = data_list[0]
yd_closing_price = yd_data["4. close"]

# Getting the day before yesterday's closing price
day_bf_yd_data = data_list[1]
day_bf_yd_closing_price = day_bf_yd_data["4. close"]

# Positive diference between the two last days
difference = float(yd_closing_price) - float(day_bf_yd_closing_price)
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

# Getting the percentage difference
diff_percent = round(difference / float(yd_closing_price) * 100)

# Get news if the difference is greater than 3%
if abs(diff_percent) > 0:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    }

    # Get API data
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]

    # Get three articles to send to specified number
    three_articles = articles[:3]

    # Format the articles
    formatted_articles = [
        f"{STOCK_NAME}: {up_down}{diff_percent}%\nHeadline: {article['title']}"
        f". \nBrief: {article['description']}" for
        article in three_articles
    ]
    client = Client(TWILIO_SID, TWILIO_KEY)  # Create twitio client

    # Sending message for each article
    for article in formatted_articles:
        message = client.messages.create(
            messaging_service_sid=MESSAGING_SERVICE_SID,
            body=article,
            to=NUMBER
        )
