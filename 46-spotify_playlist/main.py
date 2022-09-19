from bs4 import BeautifulSoup
import requests
import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pprint
# To load on VSCode
from dotenv import load_dotenv
load_dotenv()

date_year = input(
    "Choose: search by date or search by year (type date/year): "
).lower()
if date_year == "date":
    date = input("which year do you want to travel to? "
                 "Type the date in this format YYYY-MM-DD: ")
    URL = f"https://www.billboard.com/charts/hot-100/{date}"
    target_year = int(date.split("-")[0])
    year = str(f"{target_year - 2}-{target_year + 2}")
elif date_year == "year":
    date = input("Year must be at least 2006: ")
    URL = f"https://www.billboard.com/charts/year-end/{date}/hot-100-songs/"
    year = date


# Variables

SPOTIFY_CLIENT_ID = os.environ.get("SPOTIFY_ID")
SPOTIFY_CLIENT_SECRET = os.environ.get("SPOTIFY_SECRET")
REDIRECT = "http://localhost:8888/callback"


response = requests.get(URL)
web_page = response.text
soup = BeautifulSoup(web_page, "html.parser")
if date_year == "date":
    songs = soup.find_all("h3", class_="a-no-trucate")
elif date_year == "year":
    songs = soup.find_all("h3", class_="a-font-primary-bold-s")

title_list = [(song.getText().strip('\t\n')) for song in songs]

# Spotify API

spotify_auth = spotipy.oauth2.SpotifyOAuth(
    client_id=SPOTIFY_CLIENT_ID,
    client_secret=SPOTIFY_CLIENT_SECRET,
    redirect_uri=REDIRECT,
    scope="playlist-modify-private",
    cache_path="token.txt"
)

sp = spotipy.Spotify(oauth_manager=spotify_auth)

user_name = sp.current_user()["display_name"]
user_id = sp.current_user()["id"]

song_uris = []

for song in title_list:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

# Creating a new private playlist in Spotify
playlist = sp.user_playlist_create(
    user=user_id,
    name=f"{date} Billboard 100",
    public=False
)
print(playlist)

# Adding songs found into the new playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
