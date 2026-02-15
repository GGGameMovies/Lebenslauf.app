import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime
from pathlib import Path
st.write(Path(__file__).parent)


# Custom CSS for dark modern design
BASE_DIR = Path(__file__).resolve().parent

def load_css():
    css_path = Path(__file__).resolve().parent.parent / "assets" / "Projekte.css"

    if css_path.exists():
        with open(css_path, encoding="utf-8") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    else:
        st.error(f"CSS nicht gefunden: {css_path}")

load_css()

# Header
#Navi
col5, col1, col6, col2, col7, col3, col4 = st.columns(7)

with col1:
    st.page_link("streamlit_app.py", label="🏠 Start")

with col2:
    st.page_link("pages/Projekte.py", label="📂 Projekte")

with col3:
    st.page_link("pages/Feedback.py", label="📧 Feedback")

# Main content
col1, col2, col3 = st.columns([1, 6, 1])
# Projects Section
with col2:
    st.markdown("## 🚀 Featured Projects")
    
    # Project 1
    st.markdown("""
    <div class='project-card'>
        <div class='project-title'> 📊 MaStR-Analyse-Tool</div>
        <div class='project-desc'>
            Desktop-Anwendung zur Analyse des Marktstammdatenregisters mit 500.000+ Datensätzen. 
            Automatisierte CSV-Verarbeitung und interaktive Datenvisualisierung.
        </div>
        <div class='impact-metric'>
            <strong>Impact:</strong> 
                Produktiv bei Stadt Leipzig • 80% Zeitersparnis
        </div>
    </div>            
    """, unsafe_allow_html=True)
    if st.button("Zum Projekt",key="P1"):
        st.switch_page("pages/MaStR_Analyse_Tool.py") 
    
    # Project 2
    st.markdown("""
    <div class='project-card'>
        <div class='project-title'> 🌐 Gaming_Website</div>
        <div class='project-desc'>
            TEST.
        </div>
        <div class='impact-metric'>
            <strong>Impact:</strong> TEST
        </div>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Zum Projekt",key="P2"):
        st.switch_page("pages/Gaming_Website.py") 

    # Project 3
    st.markdown("""
    <div class='project-card'>
        <div class='project-title'> ▶️ Youtube-Analyse</div>
        <div class='project-desc'>
            TEST.
        </div>
        <div class='impact-metric'>
            <strong>Impact:</strong> TEST
        </div>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Zum Projekt",key="P3"):
        st.switch_page("pages/Youtube_Analyse.py") 

    # Project 4
    st.markdown("""
    <div class='project-card'>
        <div class='project-title'> 🎮 Unreal Engine</div>
        <div class='project-desc'>
            TEST.
        </div>
        <div class='impact-metric'>
            <strong>Impact:</strong> TEST
        </div>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Zum Projekt",key="P4"):
        st.switch_page("pages/Unreal_Engine.py") 