from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3

app = FastAPI()

class Song(BaseModel):
    title: str
    artist: str

@app.get("/")
def home():
    return {"message": "AI Music Assistant API"}

@app.get("/songs")
def get_songs():

    connection = sqlite3.connect("songs.db")

    cursor = connection.cursor()

    cursor.execute("SELECT * FROM songs")

    songs = cursor.fetchall()

    return songs

@app.post("/songs")
def create_song(song: Song):

    connection = sqlite3.connect("songs.db")

    cursor = connection.cursor()

    cursor.execute("""
    INSERT INTO songs (title, artist)
    VALUES (?, ?)
    """, (song.title, song.artist))

    connection.commit()

    return {
        "message": "Song added"
    }

@app.delete("/songs/{song_id}")
def delete_song(song_id: int):

    connection = sqlite3.connect("songs.db")

    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM songs WHERE id = ?",
        (song_id,)
    )

    if cursor.rowcount == 0:
        return {
            "error": "Song not found"
        }

    connection.commit()

    return {
        "message": "Song deleted"
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