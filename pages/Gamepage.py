import streamlit as st
import sqlite3
from pathlib import Path

# =====================
BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "assets" / "data" / "game.db"

def db():
    return sqlite3.connect(DB_PATH)

def img(path):
    if not path:
        return None
    p = BASE_DIR / "assets" / path.lstrip("/")
    return p if p.exists() else None

#Navi =====================
col5, col1, col6, col2, col7, col3, col4 = st.columns(7)

with col1:
    st.page_link("streamlit_app.py", label="🏠 Start")

with col2:
    st.page_link("pages/Projekte.py", label="📂 Projekte")

with col3:
    st.page_link("pages/Feedback.py", label="📧 Feedback")

# =====================
#Navi2 =====================
col5, col1, col6, col2, col7 = st.columns(5)

with col1:
    st.page_link("pages/VS.py", label="⚔️ VS")

with col2:
    st.page_link("pages/favorite.py", label="❤️ Favorite")

# =====================
st.set_page_config(layout="wide")

if "selected_game" not in st.session_state:
    st.warning("Kein Spiel ausgewählt.")
    st.stop()

game = st.session_state["selected_game"]

conn = db()

row = conn.execute("""
SELECT Beschreibung, Audio,
       BuyURLPS, BuyURLPC, BuyURLXbox, BuyURLNintendo,
       Logo, Cover,
       Gameplay, Graphic, Story, AI,
       Creativity, Immersion, Sound, Rating
FROM spiele WHERE SpielName=?
""", (game,)).fetchone()

(
 desc, audio,
 ps, pc, xbox, nin,
 logo, cover,
 gameplay, graphic, story, ai,
 creativity, immersion, sound, rating
) = row

# =====================
st.title(game)
st.caption(desc)
st.write(f"🎧 Audio: {audio}")

st.markdown("---")

# =====================
# Entwickler Kachel (Logo)

def img(rel_path):
    if not rel_path:
        return None
    p = BASE_DIR / "assets" / rel_path.lstrip("/")
    return p if p.exists() else None

st.markdown("""
<style>
/* Alle Streamlit Bilder stylen */
div[data-testid="stImage"] img {
    width: 30%;
    border-radius: 16px;
    box-shadow: 0 0 18px rgba(0,0,0,.5);
    display: block;
    margin: auto;
}

/* Optional Container Style */
div[data-testid="stImage"] {
    background:#141a22;
    padding:24px;
    border-radius:18px;
    text-align:center;
}
</style>
""", unsafe_allow_html=True)


logo_img = img(logo)

if logo_img:
    st.image(logo_img, use_container_width=True)
else:
    st.info("Kein Bild vorhanden")

st.markdown("</div>", unsafe_allow_html=True)


# =====================
# METRIC GRID 2x4

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
            width:30% !important;
            background:#141a22;
            padding:24px;
            border-radius:16px;
            text-align:center;
            margin-bottom:20px;
            box-shadow:0 0 18px rgba(0,0,0,.5);
        ">
            <h3 style="margin-bottom:8px;">{labels[i]}</h3>
            <h1 style="color:#4adeff;font-size:48px">{values[i]}</h1>
        </div>
        """, unsafe_allow_html=True)

st.markdown("---")

# =====================
# BUY PLATFORMS
st.markdown("Kaufen auf:")
b1, b2, b3, b4 = st.columns(4)

def shop(img_path, url, label):
    with img_path:
        if url:
            if st.button(label):
                st.markdown(f"[Weiter zu Shop]({url})")

with b1:
    if ps: st.link_button("PlayStation", ps)

with b2:
    if pc: st.link_button("PC", pc)

with b3:
    if xbox: st.link_button("Xbox", xbox)

with b4:
    if nin: st.link_button("Nintendo", nin)

st.markdown("---")

if st.button("⬅ Zurück zum Vergleich"):
    st.switch_page("pages/VS.py")

conn.close()
