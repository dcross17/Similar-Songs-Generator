# Similar Songs Generator

## Overview
This a microservice program that is designed to be called by another music program for generating playlists. It uses Python and FastAPI for lightweight implementation in conjunction with Spotify API.

## Features
- Mood Detection : Determine a song's mood using Spotify's audio features.
- Track Recommendations: Fetches list of songs based on the identified mood.
- Customizable: Can alter the parameters that will be filtered for like energy, valence, and danceability.
- Lightweight: Can easily be integrated with larger systems due to it microservice design.

## Installation

### Prerequisites

- Python 3.9+

- Spotify Developer account with API credentials (client ID and client secret)

### Steps


#### Clone repository

```
git clone https://github.com/dcross17/Similar-Songs-Generator.git
cd Similar-Songs-Generator
```

#### Run FastAPI
```
pip install "fastapi[standard]"
fastapi dev main.py
```



## Usage

| Method | Endpoint           | Description                     |
|--------|--------------------|---------------------------------|
| `GET`  | `/recommendations` | Get song recommendations by mood|

## Example Request
```song_id = "2LlQb7Uoj1kKyGhlkBf9aC" ```

GET ```/recommendations/{song_id}```

#### Example Call in Python
```
import requests
import json

req = requests.get("http://localhost:8000/recommendations/" + song_id)
```

#### HTTP Request Header
```
Request URL: http://localhost:8000/recommendations/2LlQb7Uoj1kKyGhlkBf9aC
Request Method: GET
Status Code: 200 OK
```

## Example Response
```
res = req.text
info = json.loads(res)
recommendations = info["recommendations"]
```

Body:
```
{
  "mood": "amusing",
  "recommendations": [
    {
      "song_id": "0ikz6tENMONtK6qGkOrU3c",
      "name": "Wake Me Up Before You Go-Go",
      "artist": "Wham!",
      "url": "https://open.spotify.com/track/0ikz6tENMONtK6qGkOrU3c"
    },
    {
      "song_id": "4IHc6SzGPnzSPuHVEPzpJc",
      "name": "Wouldn't It Be Nice",
      "artist": "The Beach Boys",
      "url": "https://open.spotify.com/track/4IHc6SzGPnzSPuHVEPzpJc"
    },
    {
      "song_id": "0rmGAIH9LNJewFw7nKzZnc",
      "name": "You Give Love A Bad Name",
      "artist": "Bon Jovi",
      "url": "https://open.spotify.com/track/0rmGAIH9LNJewFw7nKzZnc"
    },
    {
      "song_id": "6b8Be6ljOzmkOmFslEb23P",
      "name": "24K Magic",
      "artist": "Bruno Mars",
      "url": "https://open.spotify.com/track/6b8Be6ljOzmkOmFslEb23P"
    },
    {
      "song_id": "3ZFTkvIE7kyPt6Nu3PEa7V",
      "name": "Hips Don't Lie (feat. Wyclef Jean)",
      "artist": "Shakira, Wyclef Jean",
      "url": "https://open.spotify.com/track/3ZFTkvIE7kyPt6Nu3PEa7V"
    },
    {
      "song_id": "58XWGx7KNNkKneHdprcprX",
      "name": "Rock You Like A Hurricane",
      "artist": "Scorpions",
      "url": "https://open.spotify.com/track/58XWGx7KNNkKneHdprcprX"
    },
    {
      "song_id": "0G21yYKMZoHa30cYVi1iA8",
      "name": "Welcome To The Jungle",
      "artist": "Guns N' Roses",
      "url": "https://open.spotify.com/track/0G21yYKMZoHa30cYVi1iA8"
    },
    {
      "song_id": "3SnGymj6ijE2iuUfWxLo1q",
      "name": "I'm Coming Out",
      "artist": "Diana Ross",
      "url": "https://open.spotify.com/track/3SnGymj6ijE2iuUfWxLo1q"
    },
    {
      "song_id": "6wpGqhRvJGNNXwWlPmkMyO",
      "name": "I Still Haven't Found What I'm Looking For",
      "artist": "U2",
      "url": "https://open.spotify.com/track/6wpGqhRvJGNNXwWlPmkMyO"
    },
    {
      "song_id": "4hfIVhq0F0zFUcrbecsYmo",
      "name": "Let's Get It Started - Spike Mix",
      "artist": "Black Eyed Peas",
      "url": "https://open.spotify.com/track/4hfIVhq0F0zFUcrbecsYmo"
    }
  ]
}

```
## UML Sequence Diagram

![UML class (2)](https://github.com/user-attachments/assets/a6cef070-66e6-4483-aa37-6dca9d82064c)


