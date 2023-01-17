import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import config

year = input("What year would you like to travel to? Type the date in this format YYYY-MM-DD\n")

html = requests.get(f"https://www.billboard.com/charts/hot-100/{year}")
soup = BeautifulSoup(html.text, "html.parser")
top_100 = soup.select("li[class*='o-chart-results-list__item'] h3[id='title-of-a-story']")
songs = [song_titles.getText().strip() for song_titles in top_100]
top_100_artists = soup.select("li[class*='o-chart-results-list__item'] span[class*='c-label a-no-trucate a-font-primary-s']")
artists = [artist.getText().strip() for artist in top_100_artists]

scope = "playlist-modify-private"
SPOTIPY_CLIENT_ID = config.client_id
SPOTIPY_CLIENT_SECRET = config.client_secret
SPOTIPY_REDIRECT_URI = 'http://example.com'

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET,
        redirect_uri=SPOTIPY_REDIRECT_URI,
        scope=scope
    )
)

user_id = sp.current_user()['id']

song_uris = []
for (song, artist) in zip(songs, artists):
    result = sp.search(q=f'track%3A{song}%artist%3A{artist}', type='track')
    try:
        uri = result['tracks']['items'][0]['uri']
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist_id = sp.user_playlist_create(user=user_id, name=f"Top 100 Songs of {year[:4]}", public=False)['id']

sp.playlist_add_items(playlist_id=playlist_id, items=song_uris, position=None)

