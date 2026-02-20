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
    st.page_link("pages/Feedback.py", label="📧 Feedback")

st.title("🧠 Prozessablauf")
st.markdown("## Dies ist der Ablaufplan für das MaStR-Tool, wie es komplett aufgebaut wäre.")

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
<div class="box">CSV auswählen</div>    
<div class="arrow">→</div>    
<div class="box">CSV einlesen</div>
<div class="arrow">→</div>
<div class="box">Daten Validieren</div>        
<div class="arrow">→</div>   
<div class="box">Daten Transformieren</div> 
<div class="arrow">→</div>         
<div class="box">Load/Visualize</div>
</div>
""", unsafe_allow_html=True)

st.divider()

BASE_DIR = Path(__file__).resolve().parent.parent
MaStR_plan_image = BASE_DIR / "assets" / "Plaene" / "MaStR_plan.png"

if MaStR_plan_image.exists():
    st.image(MaStR_plan_image, use_container_width=True)
else:
    st.error("MaStR Plan PNG nicht gefunden")

# =============================