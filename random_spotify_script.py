from spotipy import Spotify
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy_random import get_random


def daily_random_song():
    username = input("enter the Client_ID: ")
    password = input("enter the secret: ")
    # Authenticate with your Spotify credentials
    spotify_client = Spotify(auth_manager=SpotifyClientCredentials(
        client_id=username,
        client_secret=password
    ))

    # Get a random pop song (you can change genre or type)
    random_song = get_random(spotify=spotify_client, type="track", genre="pop")
    track = random_song
    print("🎵 Track Information")
    print("-------------------")
    print(f"Title:   {track['name']}")
    print(f"Artist:  {track['artists'][0]['name']}")
    print(f"Album:   {track['album']['name']}")
    print(f"Release: {track['album']['release_date']}")
    print(f"Duration: {track['duration_ms'] // 60000}:{(track['duration_ms'] // 1000) % 60:02d} minutes")
    print(f"Explicit: {'Yes' if track['explicit'] else 'No'}")
    print(f"Popularity: {track['popularity']}/100")
    print(f"Spotify Link: {track['external_urls']['spotify']}")
    print(f"Album Cover: {track['album']['images'][0]['url']}")

daily_random_song()
