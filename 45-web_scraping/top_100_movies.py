from audioop import reverse
from bs4 import BeautifulSoup
import requests
import json

URL = "https://www.empireonline.com/movies/features/best-movies-2/"


# Request empire's html
response = requests.get(URL)
web_page = response.text
soup = BeautifulSoup(web_page, "html.parser")
movies = json.loads(soup.select_one("#__NEXT_DATA__").contents[0])
movies_dict = movies["props"]["pageProps"]["apolloState"]

# Create a movie list
movies_list = []
for a, b in movies_dict.items():
    if a.startswith("ImageMeta"):
        movies_list.append(b.get("titleText"))

# Last entry is None, and list is from 100 to 1
movies_list = movies_list[:-1]
movies_list.reverse()

# Save list in a file
with open("movies_to_watch.txt", "w") as file:
    for movie in movies_list:
        file.write(f"{movie}\n")
