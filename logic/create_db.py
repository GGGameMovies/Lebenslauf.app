import sqlite3

conn = sqlite3.connect("../assets/data/game.db")
conn.close()

print("DB erstellt!")