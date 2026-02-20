import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime
from pathlib import Path
st.write(Path(__file__).parent)

# Page configuration
st.set_page_config(
    page_title="Daniel Gonzalez - Data Analytics Portfolio",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

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

# Main content
col1, col2, col3 = st.columns([1, 6, 1])
# Projects Section
with col2:
    st.markdown("# 🚀 Projects")
    st.markdown("Diese Projekte wurden extern erstellt & zur Demonstration meiner Fähigkeiten, habe ich sie zu Teilen in Streamlit nachgestellt.")

    # Project 1
    st.markdown("""
    <div class='project-card'>
        <div class='project-title'> 📊 MaStR-Analyse-Tool (IHK-Abschlussarbeit)</div>
        <div class='project-desc'>
            Desktop-Anwendung zur Analyse des Marktstammdatenregisters mit bis zu 100.000+ Datensätzen, zur Nachverfolgung des Zubau´s, nach Zeitraum & Energieträger. 
            Automatisierte CSV-Verarbeitung und interaktive Datenvisualisierung. 
        </div>
        <div class='impact-metric'>
            <strong>Impact:</strong> 
                Produktiv bei Stadt Leipzig • 80% Zeitersparnis gegenüber manueller Analyse • 100% Genauigkeit bei der Datenverarbeitung
        </div>
    </div>            
    """, unsafe_allow_html=True)
    if st.button("Zum Projekt",key="P1"):
        st.switch_page("pages/MaStR_Analyse_Tool.py") 
    if st.button("Zum Prozessablaufplan",key="P5"):
        st.switch_page("pages/MaStR_plan.py") 
    
    # Project 2
    st.markdown("""
    <div class='project-card'>
        <div class='project-title'> 🌐 Gaming_Website (Privates Hobby)</div>
        <div class='project-desc'>
            Website für Gaming-Community, mit Informationen & Bewertungen zu Spielen, Rezensionen, Foren. Ziel ist es, eine tiefere Bewertung zu ermitteln.
            Spiele nicht im gesamten zu bewerten sondern nach Kriterien wie Gameplay, Graphic, Story, AI, Creativity, Immersion, Sound.
        </div>
        <div class='impact-metric'>
            <strong>Impact:</strong> Bessere Entscheidungsgrundlage für Gamer • Zeitersparnis bei der Spielauswahl • Bewertung von Nutzern 
        </div>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Zum Projekt",key="P2"):
        st.switch_page("pages/VS.py") 
    if st.button("Zum Prozessablaufplan",key="P6"):
        st.switch_page("pages/Website_plan.py") 

    # Project 3
    st.markdown("""
    <div class='project-card'>
        <div class='project-title'> ▶️ Youtube-Analyse</div>
        <div class='project-desc'>
            NOCH IN ARBEIT.
        </div>
        <div class='impact-metric'>
            <strong>Impact:</strong> Hier entsteht ein Analyse-Tool für YouTube-Kanäle. Per API und Power BI, werden Daten zu Abonnenten, Videoaufrufen gesammelt. 
                                     Ziel ist es, Trends zu visualisieren und Einblicke in die Performance von YouTube-Kanälen zu geben.
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
            NOCH IN ARBEIT.
        </div>
        <div class='impact-metric'>
            <strong>Impact:</strong> Hier entsteht ein Projekt mit der Unreal Engine. Ziel ist es, ein kleines Spiel oder eine interaktive Erfahrung zu entwickeln, um meine Fähigkeiten in der Spieleentwicklung zu vermitteln. 
                                     Das Projekt wird verschiedene Aspekte der Unreal Engine abdecken, einschließlich Level-Design, Blueprints und möglicherweise einfache KI-Implementierung.
        </div>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Zum Projekt",key="P4"):
        st.switch_page("pages/Unreal_Engine.py") 