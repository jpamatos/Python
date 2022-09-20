from bs4 import BeautifulSoup
import requests
import smtplib

# Variables
URL = "https://www.amazon.com/Duo-Evo-Plus-esterilizadora-vaporizador/"
"dp/B07W55DDFB/ref=sr_1_4?qid=1597660904"
BUY_PRICE = 200
YOUR_SMTP_ADDRESS = ""
YOUR_EMAIL = ""
YOUR_PASSWORD = ""

# Headers
headers = {
    "Accept-Language": "en-US,en;q=0.9,pt-BR;q=0.8,pt;q=0.7",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/"
    "537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
}

# Scrape webpage
response = requests.get(URL, headers=headers)

soup = BeautifulSoup(response.text, "lxml")
price = soup.find(name='span', class_='a-price-whole').getText()
title = soup.find(id="productTitle").get_text().strip()
price_without_currency = price.split("$")[0]
price_as_float = float(price_without_currency)

# If price is less than buy price, send an email
if price_as_float < BUY_PRICE:
    message = f"{title} is now {price}"

    with smtplib.SMTP(YOUR_SMTP_ADDRESS, port=587) as connection:
        connection.starttls()
        result = connection.login(YOUR_EMAIL, YOUR_PASSWORD)
        connection.sendmail(
            from_addr=YOUR_EMAIL,
            to_addrs=YOUR_EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{URL}"
        )
