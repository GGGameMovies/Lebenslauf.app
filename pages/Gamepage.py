import streamlit as st
import sqlite3
from pathlib import Path

# =====================
# BASE PATHS
# =====================

BASE_DIR = Path(__file__).resolve().parent.parent
ASSETS = BASE_DIR / "assets"
DB_PATH = ASSETS / "data" / "game.db"

def db():
    return sqlite3.connect(DB_PATH)

# Robust image loader (cloud safe)
def img(path):
    if not path:
        return None

    path = path.lstrip("/")
    p = ASSETS / path

    return p if p.exists() else None


# =====================
# PAGE CONFIG
# =====================

st.set_page_config(layout="wide")


# =====================
# NAVIGATION
# =====================

col5, col1, col6, col2, col7, col3, col4 = st.columns(7)

with col1:
    st.page_link("streamlit_app.py", label="🏠 Start")

with col2:
    st.page_link("pages/Projekte.py", label="📂 Projekte")

with col3:
    st.page_link("pages/Zeugnisse.py", label="📜 Zeugnisse")


col5, col1, col6, col2, col7 = st.columns(5)

with col1:
    st.page_link("pages/VS.py", label="⚔️ VS")

with col2:
    st.page_link("pages/favorite.py", label="❤️ Favorite")


# =====================
# SESSION CHECK
# =====================

if "selected_game" not in st.session_state:
    st.warning("Kein Spiel ausgewählt.")
    st.stop()

game = st.session_state["selected_game"]


# =====================
# DATABASE LOAD
# =====================

conn = db()

row = conn.execute("""
SELECT Beschreibung, Audio,
       BuyURLPS, BuyURLPC, BuyURLXbox, BuyURLNintendo,
       Logo, Cover,
       Gameplay, Graphic, Story, AI,
       Creativity, Immersion, Sound, Rating
FROM spiele WHERE SpielName=?
""", (game,)).fetchone()

conn.close()

(
 desc, audio,
 ps, pc, xbox, nin,
 logo, cover,
 gameplay, graphic, story, ai,
 creativity, immersion, sound, rating
) = row


# =====================
# HEADER
# =====================

st.title(game)
st.caption(desc)
st.write(f"🎧 Audio: {audio}")

st.markdown("---")


# =====================
# IMAGE STYLE
# =====================

st.markdown("""
<style>
div[data-testid="stImage"] img {
    width: 30%;
    border-radius: 16px;
    box-shadow: 0 0 18px rgba(0,0,0,.5);
    display: block;
    margin: auto;
}
div[data-testid="stImage"] {
    background:#141a22;
    padding:24px;
    border-radius:18px;
    text-align:center;
}
</style>
""", unsafe_allow_html=True)


# =====================
# LOGO
# =====================

logo_img = img(logo)

if logo_img:
    st.image(logo_img, width="stretch")
else:
    st.info("Kein Logo vorhanden")


st.markdown("---")


# =====================
# METRIC GRID
# =====================

labels = [
    "Gameplay","Graphic","Story","AI",
    "Creativity","Immersion","Sound","Rating"
]

values = [
    gameplay, graphic, story, ai,
    creativity, immersion, sound, rating
]

values = [float(v or 0) for v in values]

cols = st.columns(4)

for i in range(8):
    with cols[i % 4]:
        st.markdown(f"""
        <div style="
            background:#141a22;
            padding:24px;
            border-radius:16px;
            text-align:center;
            margin-bottom:20px;
            box-shadow:0 0 18px rgba(0,0,0,.5);
        ">
            <h3>{labels[i]}</h3>
            <h1 style="color:#4adeff;font-size:48px">{values[i]}</h1>
        </div>
        """, unsafe_allow_html=True)


# =====================
# BUY LINKS
# =====================

st.markdown("---")
st.markdown("### 🛒 Kaufen auf:")

b1, b2, b3, b4 = st.columns(4)

with b1:
    if ps:
        st.link_button("PlayStation", ps)

with b2:
    if pc:
        st.link_button("PC", pc)

with b3:
    if xbox:
        st.link_button("Xbox", xbox)

with b4:
    if nin:
        st.link_button("Nintendo", nin)


# =====================
# BACK
# =====================

st.markdown("---")

if st.button("⬅ Zurück zum Vergleich"):
    st.switch_page("pages/VS.py")