import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
DB_PATH = BASE_DIR / "assets" / "data" / "game.db"

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

plattformen = [
    (19, 'Android'),
    (23, 'Amazon Luna'),
    (17, 'GeForce Now'),
    (18, 'iOS'),
    (10, 'Mobile'),
    (12, 'New Nintendo 3DS'),
    (11, 'Nintendo 3DS'),
    (4, 'Nintendo Switch'),
    (1, 'PC'),
    (14, 'PS3'),
    (5, 'PS4'),
    (2, 'PS5'),
    (13, 'Wii U'),
    (15, 'Xbox 360'),
    (6, 'Xbox One'),
    (3, 'Xbox X'),
]

cursor.executemany("""
INSERT OR IGNORE INTO plattform (PlattformID, PlattformName)
VALUES (?, ?)
""", plattformen)

conn.commit()

print("Plattformen importiert!")
print(cursor.execute("SELECT * FROM plattform").fetchall())

conn.close()
