import spotipy
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials
from fastapi import FastAPI, HTTPException

# Spotify API setup
SPOTIFY_CLIENT_ID = "44b5276668fe42c5b0262af5515433e4"
SPOTIFY_CLIENT_SECRET = "4ae692520ba74f5b8768f2d938076914"
REDIRECT_URI = "http://localhost:8000/callback"
spotify = Spotify(
    auth_manager=SpotifyOAuth(
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET,
        redirect_uri=REDIRECT_URI,
        scope="user-library-read",
    )
)

# Define the artist URI for example purposes
# taylor_uri = "spotify:artist:06HL4z0CvFAxyc27GXpf02"
# results = spotify.artist_albums(taylor_uri, album_type="album")
# albums = results["items"]
# while results["next"]:
#     results = spotify.next(results)
#     albums.extend(results["items"])

# for album in albums:
#     print(album["name"])

thriller_uri = "2RlgNHKcydI9sayD2Df2xp"

app = FastAPI()


@app.get("/recommendations/{song_id}")
async def get_recommendations(song_id: str):
    """
    Generate recommendations based on the song_id provided.
    """
    try:
        audio_features = spotify.audio_features(song_id)[0]
        if not audio_features:
            raise HTTPException(status_code=404, detail="Song not found.")
        return audio_features
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
