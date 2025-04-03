from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID="YOUR_CLIENT_ID"
CLIENT_SECRET="YOUR_CLIENT_SECRET"

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}/",headers=header)
billboard_webpage=response.text

soup = BeautifulSoup(billboard_webpage,"html.parser")
titles = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in titles]


# Create a Spotify client
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope="playlist-modify-private"
                     ,redirect_uri="https://example.com",
                     client_id=CLIENT_ID,client_secret=CLIENT_SECRET,
                     show_dialog=True,cache_path="token.txt",
                     username="Shubhang"))

# Get user ID
user_id = sp.current_user()["id"]
song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

# Creating a new private playlist in Spotify
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
print(playlist)

# Adding songs found into the new playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)

