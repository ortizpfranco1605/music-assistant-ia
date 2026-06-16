from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3
from fastapi import HTTPException

app = FastAPI()

class Song(BaseModel):
    title: str
    artist: str

class SongResponse(BaseModel):
    id: int
    title: str
    artist: str

@app.get("/")
def home():
    return {"message": "AI Music Assistant API"}

@app.get("/songs", response_model=list[SongResponse])
def get_songs():

    connection = sqlite3.connect("songs.db")

    connection.row_factory = sqlite3.Row

    cursor = connection.cursor()

    cursor.execute("SELECT * FROM songs")

    songs = cursor.fetchall()

    return [dict(song) for song in songs]


@app.get("/songs/{song_id}", response_model=SongResponse)
def get_song(song_id: int):

    connection = sqlite3.connect("songs.db")

    connection.row_factory = sqlite3.Row

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT * FROM songs
        WHERE id = ?
        """,
        (song_id,)
    )

    song = cursor.fetchone()

    if song is None:
        raise HTTPException(
            status_code=404,
            detail="Song not found"
        )

    return dict(song)


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

    connection = sqlite3.connect("songs.db")

    cursor = connection.cursor()

    cursor.execute(
        """
        UPDATE songs
        SET title = ?, artist = ?
        WHERE id = ?
        """,
        (
            song_data.title,
            song_data.artist,
            song_id
        )
    )

    if cursor.rowcount == 0:
        return {
            "error": "Song not found"
        }

    connection.commit()

    return {
        "message": "Song updated"
    }