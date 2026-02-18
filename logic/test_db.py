import sqlite3

conn = sqlite3.connect("assets/data/game.db")
print(conn.execute("SELECT * FROM genres").fetchall())
print(conn.execute("SELECT * FROM ps").fetchall())
conn.close()