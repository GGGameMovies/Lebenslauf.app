import sqlite3

conn = sqlite3.connect("assets/data/game.db")
cur = conn.cursor()

ps_list = [
    "Nintendo",
    "Sony Interactive Entertainment",
    "Xbox Game Studios",
    "EA",
    "Ubisoft",
    "Square Enix",
    "Bethesda",
    "Capcom",
    "Epic Games"
]

for ps in ps_list:
    cur.execute("INSERT OR IGNORE INTO ps (PSName) VALUES (?)", (ps,))

conn.commit()
conn.close()

print("PS importiert!")
