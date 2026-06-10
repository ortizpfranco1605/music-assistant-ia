import sqlite3

connection = sqlite3.connect("songs.db")

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS songs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    artist TEXT NOT NULL
)
""")

connection.commit()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = cursor.fetchall()

print(tables)

print("Table created")

cursor.execute("""
INSERT INTO songs (title, artist)
VALUES (?, ?)
""", ("AC/DC", "You shook me all night long"))

connection.commit()

cursor.execute("SELECT * FROM songs")

songs = cursor.fetchall()

print(songs)