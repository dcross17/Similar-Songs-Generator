import random
from audioAnalysis import determine_mood
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth
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

print(Spotify.recommendations)


def search_songs_by_mood(
    sp, mood, seed_tracks=None, seed_artists=None, seed_genres=None, limit=10
):
    # Access mood keywords and map moods to audio features
    mood_keywords = {
        "amusing": ["funny", "quirky", "light-hearted"],
        "annoying": ["irritating", "discordant", "chaotic"],
        "beautiful": ["elegant", "graceful", "melodic"],
        "calm": ["soothing", "peaceful", "relaxing"],
        "dreamy": ["ethereal", "floaty", "surreal"],
        "energizing": ["upbeat", "motivating", "powerful"],
        "desirous": ["romantic", "passionate", "seductive"],
        "indignant": ["angry", "defiant", "rebellious"],
        "joyful": ["happy", "celebratory", "cheerful"],
        "sad": ["melancholic", "sorrowful", "heartfelt"],
        "scary": ["dark", "eerie", "ominous"],
        "tense": ["intense", "suspenseful", "nerve-wracking"],
        "triumphant": ["epic", "victorious", "heroic"],
    }

    # Map moods to Spotify audio feature ranges (customize as needed)
    mood_to_features = {
        "amusing": {"valence": 0.8, "energy": 0.7, "danceability": 0.7},
        "annoying": {"valence": 0.4, "energy": 0.9, "danceability": 0.6},
        "beautiful": {"valence": 0.7, "energy": 0.5, "danceability": 0.5},
        "calm": {"valence": 0.6, "energy": 0.3, "danceability": 0.4},
        "dreamy": {"valence": 0.5, "energy": 0.4, "danceability": 0.4},
        "energizing": {
            "valence": 0.9,
            "energy": 0.8,
            "danceability": 0.8,
        },
        "desirous": {"valence": 0.7, "energy": 0.6, "danceability": 0.8},
        "indignant": {"valence": 0.3, "energy": 0.8, "danceability": 0.6},
        "joyful": {"valence": 0.9, "energy": 0.7, "danceability": 0.8},
        "sad": {"valence": 0.2, "energy": 0.4, "danceability": 0.3},
        "scary": {"valence": 0.1, "energy": 0.6, "danceability": 0.4},
        "tense": {"valence": 0.3, "energy": 0.9, "danceability": 0.5},
        "triumphant": {"valence": 0.8, "energy": 0.7, "danceability": 0.7},
    }

    def add_randomness(features):
        randomized_features = {}
        for key, value in features.items():
            randomized_value = value + random.uniform(-0.2, 0.2)
            # Ensure the value stays within the valid range [0, 1]
            randomized_value = max(0, min(1, randomized_value))
            randomized_features[key] = randomized_value
        return randomized_features

    # Use audio features for the specified mood
    audio_features = mood_to_features.get(mood, {})
    audio_features = add_randomness(audio_features)
    print(audio_features)
    seed_data = {
        "seed_tracks": seed_tracks or [],
        "seed_artists": seed_artists or [],
        "seed_genres": seed_genres or [],
    }

    # Call Spotify API for recommendations
    recommendations = sp.recommendations(
        limit=limit, **seed_data, **audio_features  # Spread audio feature filters
    )

    # Extract and format song details
    return [
        {
            "song_id": track["id"],
            "name": track["name"],
            "artist": ", ".join([artist["name"] for artist in track["artists"]]),
            "url": track["external_urls"]["spotify"],
        }
        for track in recommendations["tracks"]
    ]


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
        mood = determine_mood(audio_features)
        print(mood)
        recommendations = search_songs_by_mood(spotify, mood, [song_id])
        print(recommendations)
        return {"mood": mood, "recommendations": recommendations}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
