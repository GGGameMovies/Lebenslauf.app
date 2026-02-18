import sqlite3
import csv

DB_PATH = "assets/data/game.db"
CSV_PATH = "assets/data/Spiele.csv"

def clean(value):
    if value is None:
        return None
    v = value.strip()
    if v == "" or v.upper() == "NULL":
        return None
    return v

conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()

# 🔥 Tabelle komplett leeren
cur.execute("DELETE FROM spiele")
cur.execute("DELETE FROM sqlite_sequence WHERE name='spiele'")  # reset autoincrement optional

with open(CSV_PATH, encoding="utf-8") as f:
    reader = csv.DictReader(f, delimiter=";")

    for row in reader:
        values = [clean(row[col]) for col in row]

        cur.execute("""
            INSERT INTO spiele (
                SpielID, SpielName, YoutubeURL, Beschreibung, KBeschreibung, Audio,
                Datum, BuyURLPS, BuyURLPC, BuyURLXbox, BuyURLNintendo,
                Logo, Orte, Cover,
                Gameplay, Graphic, Story, AI, Creativity, Immersion, Sound,
                Rating, WievieleUserVote, Geprüft
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, values)

conn.commit()
conn.close()

print("✅ DB vollständig neu aus CSV aufgebaut!")
