import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
DB_PATH = BASE_DIR / "assets" / "data" / "game.db"

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()
cursor.execute("PRAGMA foreign_keys = ON;")

print("Verbunden mit DB")
genres = [
    "Action", "Action-Adventure", "Action-Rollenspiel", "Adventure",
    "Battle Royale", "Beat em Up", "Cardgame", "Escape Room",
    "Fighting", "Hack and Slay", "Hack-and-Slash", "Idle", "MMORPGs",
    "MOBA", "Party", "Point-and-Click-Adventures", "Puzzle",
    "Rennspiele", "Rhythmusspiel", "Rogue-like", "Roguelike", "RPG",
    "Sandbox", "Shooter", "Simulation", "Sports", "Stealth",
    "Survival Horror", "Tabletop", "Tower Defense", "Visual Novels"
]

for g in genres:
    cursor.execute(
        "INSERT OR IGNORE INTO genres (GenreName) VALUES (?)",
        (g,)
    )
conn.commit()
print("Genres importiert!")

print(cursor.execute("SELECT * FROM genres").fetchall())
conn.close()