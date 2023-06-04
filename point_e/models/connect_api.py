import spotipy

from spotipy.oauth2 import SpotifyClientCredentials

client_id = '33516f8f2e7e44a7b36187958b842509'
client_secret = 'aab30e34154241ea9b733e077791682b'

def connect():
    client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    return sp

def get_genre():
    sp = connect()
    genres = sp.recommendation_genre_seeds()
    return genres

def get_recommed_song(genres):
    sp = connect()
    songs = sp.recommendations(seed_genres=genres, limit=10)
    return songs