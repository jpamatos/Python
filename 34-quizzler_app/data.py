import requests

# Parameters to fetch API data
parameters = {
    "amount": 10,
    "type": "boolean"
}

# Fetching API data
response = requests.get("https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
data = response.json()
question_data = data["results"]
