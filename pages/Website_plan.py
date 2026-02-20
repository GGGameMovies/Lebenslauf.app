import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import time
from datetime import datetime
from pathlib import Path

st.set_page_config(layout="wide")
st.write(Path(__file__).parent)

# Custom CSS for dark modern design
BASE_DIR = Path(__file__).resolve().parent

def load_css():
    css_path = Path(__file__).resolve().parent.parent / "assets" / "streamlit_app_styles.css"

    if css_path.exists():
        with open(css_path, encoding="utf-8") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    else:
        st.error(f"CSS nicht gefunden: {css_path}")

load_css()

# Header
#Navi
col1, col2, col3, col4, col5, col6, col7 = st.columns(7)

with col2:
    st.page_link("streamlit_app.py", label="🏠 Start")

with col4:
    st.page_link("pages/Projekte.py", label="📂 Projekte")

with col6:
    st.page_link("pages/Zeugnisse.py", label="📜 Zeugnisse")

st.title("🧠 Prozessablauf")
st.markdown("## Dies ist der Ablaufplan für die Website,wie sie komplett aufgebaut wäre.")

# =============================
# STYLE

st.markdown("""
<style>

.flow-row {
    display:flex;
    align-items:center;
    gap:20px;
    margin:15px 0;
}

.box {
    background:#0f172a;
    padding:18px 26px;
    border-radius:14px;
    border:1px solid #1e293b;
    box-shadow:0 0 18px rgba(0,255,255,.15);
    color:white;
    font-weight:600;
    text-align:center;
    min-width:160px;
    transition:.3s;
}

.box:hover {
    box-shadow:0 0 28px rgba(0,255,255,.6);
    transform:scale(1.03);
}

.arrow {
    font-size:28px;
    color:#38bdf8;
}

.subflow {
    margin-left:40px;
    padding:12px 0;
}

.divider {
    height:1px;
    background:#1e293b;
    margin:30px 0;
}

</style>
""", unsafe_allow_html=True)

# =============================
# STATE

if "open_flow" not in st.session_state:
    st.session_state.open_flow = None

def select(flow):
    st.session_state.open_flow = flow


# =============================
# MAIN FLOW (RECHTS – wie Skizze)

st.subheader("🌐 Hauptnavigation")

st.markdown("""
<div class="flow-row">  
<div class="box">Register/Login</div>    
<div class="arrow">→</div>    
<div class="box">Home</div>
<div class="arrow">↔</div>
<div class="box">VS</div>        
<div class="arrow">↔</div>   
<div class="box">Favorite</div> 
<div class="arrow">→</div>         
<div class="box">GamePage</div>
</div>
""", unsafe_allow_html=True)

st.divider()

# =============================
# CLICK BUTTONS
st.markdown("## Teilprozesse anzeigen:")
st.markdown("Klicken Sie auf die Buttons.")

c1,c2,c3,c4,c5 = st.columns(5)

with c1:
    st.button("📝 Register/Loggin", on_click=select, args=("register",))

with c2:
    st.button("🏠 Home", on_click=select, args=("Home",))

with c3:
    st.button("⚔ VS", on_click=select, args=("vs",))

with c4:
    st.button("❤️ Favorite", on_click=select, args=("favorite",))

with c5:
    st.button("🎮 GamePage", on_click=select, args=("game",))

st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

# =============================
# DETAIL FLOWS

if st.session_state.open_flow == "register":
    st.subheader("📝 Register Teilprozess")

    BASE_DIR = Path(__file__).resolve().parent.parent
    Register_plan_image = BASE_DIR / "assets" / "Plaene" / "Register_plan.png"

    st.markdown("""
    <div class="subflow">

    <div class="flow-row">
    <div class="box">Einloggen</div>
    <div class="arrow">→</div>
    <div class="box">Zugangsdaten prüfen</div>
    <div class="arrow">→</div>
    <div class="box">Voller Zugriff</div>
    </div>

    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="subflow">

    <div class="flow-row">
    <div class="box">Registrieren</div>
    <div class="arrow">→</div>
    <div class="box">Nutzerdaten erfassen</div>
    <div class="arrow">→</div>
    <div class="box">Verify-Link versenden</div>
    <div class="arrow">→</div>
    <div class="box">Link bestätigen</div>
    <div class="arrow">→</div>
    <div class="box">Account aktiv</div>
    <div class="arrow">→</div>
    <div class="box">Voller Zugriff</div>
    </div>

    </div>
    """, unsafe_allow_html=True)

    if Register_plan_image.exists():
        st.image(Register_plan_image, use_container_width=True)
    else:
        st.error("Register Plan PNG nicht gefunden")

elif st.session_state.open_flow == "Home":
    st.subheader("🏠 Home Teilprozess")

    BASE_DIR = Path(__file__).resolve().parent.parent
    Home_plan_image = BASE_DIR / "assets" / "Plaene" / "Home_plan.png"

    st.markdown("""
    <div class="subflow">

    <div class="flow-row">
    <div class="box">Zeigt zuletzt erschienene Spiele und bald erscheidende Spiele an</div>
    <div class="arrow">→</div>
    <div class="box">Spiel wählen</div>
    <div class="arrow">→</div>
    <div class="box">GamePage</div>
    </div>

    </div>
    """, unsafe_allow_html=True)

    if Home_plan_image.exists():
        st.image(Home_plan_image, use_container_width=True)
    else:
        st.error("Home Plan PNG nicht gefunden")

elif st.session_state.open_flow == "vs":
    st.subheader("⚔ VS Teilprozess")

    BASE_DIR = Path(__file__).resolve().parent.parent
    VS_plan_image = BASE_DIR / "assets" / "Plaene" / "VS_plan.png"

    st.markdown("""
    <div class="subflow">

    <div class="flow-row">
    <div class="box">Spiel1 wählen</div>
    <div class="arrow">→</div>
    <div class="box">Spiel2 wählen</div>
    <div class="arrow">→</div>
    <div class="box">Spielwerte Vergleich</div>
    <div class="arrow">→</div>
    <div class="box">Spiel wählen</div>
    <div class="arrow">→</div>
    <div class="box">GamePage</div>
    </div>

    </div>
    """, unsafe_allow_html=True)

    if VS_plan_image.exists():
        st.image(VS_plan_image, use_container_width=True)
    else:
        st.error("VS Plan PNG nicht gefunden")

elif st.session_state.open_flow == "favorite":
    st.subheader("❤️ Favorite Teilprozess")

    BASE_DIR = Path(__file__).resolve().parent.parent
    Favorite_plan_image = BASE_DIR / "assets" / "Plaene" / "Favorite_plan.png"

    st.markdown("""
    <div class="subflow">

    <div class="flow-row">
    <div class="box">Filter setzen</div>
    <div class="arrow">→</div>
    <div class="box">Spiele in dynamischer Tabelle anzeigen</div>
    <div class="arrow">→</div>
    <div class="box">Tabelle filtern</div>
    <div class="arrow">→</div>
    <div class="box">Spiel wählen</div>
    <div class="arrow">→</div>
    <div class="box">GamePage</div>
    </div>

    </div>
    """, unsafe_allow_html=True)

    if Favorite_plan_image.exists():
        st.image(Favorite_plan_image, use_container_width=True)
    else:
        st.error("Favorite Plan PNG nicht gefunden")

elif st.session_state.open_flow == "game":
    st.subheader("🎮 GamePage Teilprozess")

    BASE_DIR = Path(__file__).resolve().parent.parent
    Gamepage_plan_image = BASE_DIR / "assets" / "Plaene" / "Gamepage_plan.png"

    st.markdown("""
    <div class="subflow">

    <div class="flow-row">
    <div class="box">Cover & Info</div>
    <div class="arrow">→</div>
    <div class="box">Bewertungen ansehen</div>
    <div class="arrow">→</div>
    <div class="box">Spiele bewerten</div>
    <div class="arrow">→</div>
    <div class="box">Shop Links</div>
    </div>

    </div>
    """, unsafe_allow_html=True)

    if Gamepage_plan_image.exists():
        st.image(Gamepage_plan_image, use_container_width=True)
    else:
        st.error("Gamepage Plan PNG nicht gefunden")