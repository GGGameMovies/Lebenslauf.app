import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
DB_PATH = BASE_DIR / "assets" / "data" / "game.db"

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

players = [
    (9, 'Online-KOOP'),
    (4, 'Couch-Koop'),
    (2, 'Lokaler-Multiplayer'),
    (7, 'Multiplayer'),
    (3, 'Online-Koop'),
    (5, 'Online-Multiplayer'),
    (1, 'Singleplayer'),
]

cursor.executemany("""
INSERT OR IGNORE INTO player (PlayerID, PlayerName)
VALUES (?, ?)
""", players)

conn.commit()

print("Player importiert!")
print(cursor.execute("SELECT * FROM player").fetchall())

conn.close()
