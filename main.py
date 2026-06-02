from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Song(BaseModel):
    title: str
    artist: str

songs = []
next_id = 1

@app.get("/")
def home():
    return {"message": "AI Music Assistant API"}

@app.get("/songs")
def get_songs():
    return songs

@app.post("/songs")
def create_song(song: Song):

    global next_id

    new_song = {
        "id": next_id,
        "title": song.title,
        "artist": song.artist
    }

    songs.append(new_song)

    next_id += 1

    return {
        "message": "Song added",
        "song": new_song
    }

@app.delete("/songs/{song_id}")
def delete_song(song_id: int):

    for song in songs:

        if song["id"] == song_id:

            songs.remove(song)

            return {
                "message": "Song deleted"
            }

    return {
        "error": "Song not found"
    }

@app.put("/songs/{song_id}")
def update_song(song_id: int, song_data: Song):

    for song in songs:

        if song["id"] == song_id:

            song["title"] = song_data.title
            song["artist"] = song_data.artist

            return {
                "message": "Song updated",
                "song": song
            }

    return {
        "error": "Song not found"
    }