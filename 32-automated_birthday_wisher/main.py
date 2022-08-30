import datetime as dt
import smtplib
import random
import pandas as pd

EMAIL = "user_email@email.com"  # Sender email
PASSWORD = "user_password"  # Sender email's password or app password

data = pd.read_csv("birthdays.csv")  # Readh birthdays data

now = (dt.datetime.now().month, dt.datetime.now().day)

birthdays = {(data_row.month, data_row.day): data_row
             for (index, data_row) in data.iterrows()}

# Get a person birthday if it is today
if now in birthdays:
    person = birthdays[now]  # Get the birthday person

    # Choose a quote randomly
    with open("quotes.txt") as quote_file:
        quotes = quote_file.readlines()
        quote = random.choice(quotes)

    # Get a letter randomly
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter_file:
        letter = letter_file.read()

    # Change placeholders to replaced text
    letter = letter.replace("[NAME]", person["name"])
    letter = letter.replace("[QUOTE]", quote)

    # Send the email by SMTP connection
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.ehlo()
        connection.starttls()  # Make the connection secure
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=person["email"],
            msg=f"Subject:Happy Birthday\n\n{letter}")
