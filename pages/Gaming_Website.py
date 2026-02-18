import streamlit as st
from pathlib import Path
from datetime import date
import sqlite3

BASE = Path(__file__).resolve().parent.parent
HTML_PATH = BASE / "assets/web/index.html"
DB = BASE / "assets/data/game.db"

def db():
    return sqlite3.connect(DB)

def img(p):
    if not p: return ""
    return f"assets/{p.lstrip('/')}"

today = date.today()
c = db()

released = c.execute("""
SELECT SpielName,Beschreibung,Cover,Rating
FROM spiele WHERE Datum < ?
ORDER BY Datum DESC LIMIT 5
""",(today,)).fetchall()

upcoming = c.execute("""
SELECT SpielName,Beschreibung,Cover,Rating
FROM spiele WHERE Datum >= ?
ORDER BY Datum ASC LIMIT 5
""",(today,)).fetchall()

c.close()

def thumbs(games):
    html=""
    for t,_,imgp,_ in games[1:]:
        html += f'<img src="{img(imgp)}">'
    return html

html = HTML_PATH.read_text(encoding="utf-8")

h = released[0]
u = upcoming[0]

html = html.replace("{{HERO_IMAGE}}", img(h[2]))
html = html.replace("{{HERO_TITLE}}", h[0])
html = html.replace("{{HERO_DESC}}", h[1])
html = html.replace("{{HERO_RATING}}", str(h[3]))
html = html.replace("{{THUMBNAILS}}", thumbs(released))

html = html.replace("{{UP_IMAGE}}", img(u[2]))
html = html.replace("{{UP_TITLE}}", u[0])
html = html.replace("{{UP_DESC}}", u[1])
html = html.replace("{{UP_RATING}}", str(u[3]))
html = html.replace("{{UP_THUMBS}}", thumbs(upcoming))

st.components.v1.html(html, height=1800, scrolling=True)
