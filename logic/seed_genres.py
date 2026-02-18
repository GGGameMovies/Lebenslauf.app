import sqlite3

conn = sqlite3.connect("assets/data/game.db")
cur = conn.cursor()

genres = [
    "Action","Action-Adventure","Action-Rollenspiel","Adventure","Battle Royale",
    "Beat em Up","Cardgame","Escape Room","Fighting","Hack and Slay",
    "Hack-and-Slash","Idle","MMORPGs","MOBA","Party",
    "Point-and-Click-Adventures","Puzzle","Rennspiele","Rhythmusspiel",
    "Rogue-like","Roguelike","RPG","Sandbox","Shooter","Simulation",
    "Sports","Stealth","Survival Horror","Tabletop","Tower Defense","Visual Novels"
]

for g in genres:
    cur.execute("INSERT OR IGNORE INTO genres (GenreName) VALUES (?)", (g,))

conn.commit()
conn.close()

print("Genres importiert!")
