import streamlit as st
import sqlite3
import pandas as pd
from pathlib import Path
st.set_page_config(layout="wide")
st.title("❤️ Favorite")

# =====================
BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "assets" / "data" / "game.db"

def db():
    return sqlite3.connect(DB_PATH)

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
# LAYOUT: FILTER LINKS | TABELLE RECHTS

filter_col, main_col = st.columns([1.2, 4])

# =====================
# FILTER LEISTE

with filter_col:
    st.subheader("🎚 Filter")

    min_gameplay = st.slider("Gameplay ≥", 0, 100, 0, 5)
    min_graphic = st.slider("Graphic ≥", 0, 100, 0, 5)
    min_story = st.slider("Story ≥", 0, 100, 0, 5)
    min_ai = st.slider("AI ≥", 0, 100, 0, 5)
    min_creativity = st.slider("Creativity ≥", 0, 100, 0, 5)
    min_immersion = st.slider("Immersion ≥", 0, 100, 0, 5)
    min_sound = st.slider("Sound ≥", 0, 100, 0, 5)
    min_rating = st.slider("Rating ≥", 0, 100, 0, 5)

# =====================
# SQL QUERY

conn = db()

query = """
SELECT 
    SpielName,
    Gameplay, Graphic, Story, AI,
    Creativity, Immersion, Sound, Rating
FROM spiele
WHERE 
    COALESCE(Gameplay,0) >= ?
    AND COALESCE(Graphic,0) >= ?
    AND COALESCE(Story,0) >= ?
    AND COALESCE(AI,0) >= ?
    AND COALESCE(Creativity,0) >= ?
    AND COALESCE(Immersion,0) >= ?
    AND COALESCE(Sound,0) >= ?
    AND COALESCE(Rating,0) >= ?
"""

df = pd.read_sql_query(
    query,
    conn,
    params=[
        min_gameplay,
        min_graphic,
        min_story,
        min_ai,
        min_creativity,
        min_immersion,
        min_sound,
        min_rating
    ]
)

conn.close()

# =====================
# RESULT BEREICH

with main_col:
    st.subheader(f"🎯 Gefundene Spiele: {len(df)}")

    # Normale sortierbare Tabelle
    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )

    st.caption("⬆ Klick auf Spalten sortiert automatisch")

    st.markdown("---")
    st.subheader("🎮 Spiel öffnen")

    if len(df) == 0:
        st.info("Keine Spiele in der aktuellen Filterauswahl.")
    else:
        selected_game = st.selectbox(
            "Spiel auswählen",
            df["SpielName"].tolist()
        )

        if st.button("➡ Zur Gamepage öffnen"):
            st.session_state["selected_game"] = selected_game
            st.switch_page("pages/Gamepage.py")
