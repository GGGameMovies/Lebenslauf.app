import streamlit as st
import sqlite3
from pathlib import Path

# =====================
BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "assets" / "data" / "game.db"

def db():
    return sqlite3.connect(DB_PATH)

st.set_page_config(layout="wide")
st.title("⚔️ Game VS")

conn = db()

games = conn.execute("""
SELECT SpielID, SpielName FROM spiele ORDER BY SpielName
""").fetchall()

game_map = {name: gid for gid, name in games}

#Navi =====================
col5, col1, col6, col2, col7, col3, col4 = st.columns(7)

with col1:
    st.page_link("streamlit_app.py", label="🏠 Start")

with col2:
    st.page_link("pages/Projekte.py", label="📂 Projekte")

with col3:
    st.page_link("pages/Zeugnisse.py", label="📜 Zeugnisse")

# =====================
#Navi2 =====================
col5, col1, col6, col2, col7 = st.columns(5)

with col1:
    st.page_link("pages/VS.py", label="⚔️ VS")

with col2:
    st.page_link("pages/favorite.py", label="❤️ Favorite")

# =====================
c1, c2 = st.columns(2)

with c1:
    g1_name = st.selectbox("🎮 Spiel 1", game_map.keys())

with c2:
    g2_name = st.selectbox("🎮 Spiel 2", game_map.keys())

def load_game(gid):
    return conn.execute("""
    SELECT Gameplay, Graphic, Story, AI, Creativity, Immersion, Sound, Rating
    FROM spiele WHERE SpielID=?
    """, (gid,)).fetchone()

g1 = load_game(game_map[g1_name])
g2 = load_game(game_map[g2_name])

metrics = [
    "Gameplay","Graphic","Story","AI",
    "Creativity","Immersion","Sound","Rating"
]

def safe(v):
    return float(v) if v not in (None,"","-") else 0

def colors(a,b):
    if a > b: return "#33ff77", "#ff4d4d"
    if b > a: return "#ff4d4d", "#33ff77"
    return "#aaaaaa", "#aaaaaa"

# =====================
st.markdown("---")

title_left, spacer, title_right = st.columns([4,2,4])

with title_left:
    if st.button(f"🎮 {g1_name}", key="open_game1", help="""
    Sie kommen zur Gamepage, wenn sie auf den Titel Klicken."""):
        st.session_state["selected_game"] = g1_name
        st.switch_page("pages/Gamepage.py")

with title_right:
    if st.button(f"🎮 {g2_name}", key="open_game2", help="""
    Sie kommen zur Gamepage, wenn sie auf den Titel Klicken."""):
        st.session_state["selected_game"] = g2_name
        st.switch_page("pages/Gamepage.py")

st.subheader("📊 Vergleich")

wins1 = wins2 = 0

for i, label in enumerate(metrics):

    v1 = safe(g1[i])
    v2 = safe(g2[i])

    if v1 > v2: wins1 += 1
    elif v2 > v1: wins2 += 1

    left, mid, right = st.columns([4,2,4])

    c1_col, c2_col = colors(v1, v2)

    with left:
        st.progress(v1/100)
        st.markdown(
            f"<h2 style='color:{c1_col};text-align:center'>{v1}</h2>",
            unsafe_allow_html=True
        )

    with mid:
        st.markdown(
            f"<div style='text-align:center;font-size:22px;font-weight:600'>{label}</div>",
            unsafe_allow_html=True
        )

    with right:
        st.progress(v2/100)
        st.markdown(
            f"<h2 style='color:{c2_col};text-align:center'>{v2}</h2>",
            unsafe_allow_html=True
        )

    st.markdown("---")

# =====================
st.subheader("🏆 Ergebnis")

r1, r2 = st.columns(2)

with r1:
    st.metric(g1_name, wins1)

with r2:
    st.metric(g2_name, wins2)

if wins1 > wins2:
    st.success(f"🥇 Sieger: {g1_name}")
elif wins2 > wins1:
    st.success(f"🥇 Sieger: {g2_name}")
else:
    st.info("🤝 Unentschieden")

conn.close()
