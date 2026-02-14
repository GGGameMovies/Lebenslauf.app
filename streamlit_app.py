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
    for path in Path(__file__).parent.rglob("streamlit_app_styles.css"):
        with open(path, encoding="utf-8") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
        return

    st.error("CSS file not found!")

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

st.markdown("<h1>DANIEL GONZALEZ</h1>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Datenanalyst für Prozessoptimierung mit Entwickler-Mindset</div>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.markdown(
        "<div class='contact-info'>📧 Danielgonzalez1988@web.de | 📱 015252874894 | 📍 Leipzig, Deutschland</div>",
        unsafe_allow_html=True
    )


# Main content
col_left, col_right = st.columns([2, 1])

# Projects Section
with col_left:
    st.markdown("## 🚀 Featured Projects")
    
    # Project 1
    st.markdown("""
    <div class='project-card'>
        <div class='project-title'>MaStR-Analyse-Tool</div>
        <div class='project-desc'>
            Desktop-Anwendung zur Analyse des Marktstammdatenregisters mit 500.000+ Datensätzen. 
            Automatisierte CSV-Verarbeitung und interaktive Datenvisualisierung.
        </div>
        <div class='tech-tags'>
            <span class='tech-tag'>Python</span>
            <span class='tech-tag'>Pandas</span>
            <span class='tech-tag'>Tkinter</span>
            <span class='tech-tag'>Data Viz</span>
        </div>
        <div class='impact-metric'>
            <strong>Impact:</strong> Produktiv bei Stadt Leipzig • 80% Zeitersparnis
        </div>
    </div>            
    """, unsafe_allow_html=True)
    
    # Project 2
    st.markdown("""
    <div class='project-card'>
        <div class='project-title'>Buchungsanalyse-System</div>
        <div class='project-desc'>
            Automatisierte Auswertung von 12.000+ Raumbuchungen pro Jahr mit zeitbasierten Reports 
            für strategische Planungsentscheidungen.
        </div>
        <div class='tech-tags'>
            <span class='tech-tag'>Python</span>
            <span class='tech-tag'>NumPy</span>
            <span class='tech-tag'>Matplotlib</span>
            <span class='tech-tag'>Analytics</span>
        </div>
        <div class='impact-metric'>
            <strong>Impact:</strong> 15 Std./Woche Zeitersparnis für Verwaltungsteam
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Project 3
    st.markdown("""
    <div class='project-card'>
        <div class='project-title'>IoT-Sensordaten-System</div>
        <div class='project-desc'>
            Datenbankentwicklung für IoT-Sensordaten zur Überwachung von Heizkörpern 
            bei Stadtwerke Leipzig. SQL-Abfragen für Energie-Monitoring.
        </div>
        <div class='tech-tags'>
            <span class='tech-tag'>SQL</span>
            <span class='tech-tag'>MySQL</span>
            <span class='tech-tag'>IoT</span>
            <span class='tech-tag'>GitLab</span>
        </div>
        <div class='impact-metric'>
            <strong>Impact:</strong> Echtzeit-Monitoring für Energieeffizienz
        </div>
    </div>
    """, unsafe_allow_html=True)

# Skills Section
with col_right:
    st.markdown("## 🎓 Ausbildung Timeline")
    
    timeline_data = [
        ("08/2023 - 06/2025", "Fachinformatiker Daten- und Prozessanalyse", "WBS Schulung"),
        ("10/2024 - 05/2025", "Praktikum - Datenanalyst", "Referat Digitale Stadt Leipzig"),
        ("09/2019 - 08/2021", "Fachinformatiker Anwendungsentwicklung", "Z&P Weiterbildung"),
        ("11/2020 - 04/2021", "Praktikum - Junior Software Developer", "Stadtwerke Leipzig")
        
    ]
    
    for date, title, org in timeline_data:
        st.markdown(f"""
        <div class='timeline-item'>
            <div class='timeline-dot'></div>
            <div class='timeline-date'>{date}</div>
            <div class='timeline-title'>{title}</div>
            <div class='timeline-org'>{org}</div>
        </div>
        """, unsafe_allow_html=True)

# Charts Section
col_chart1, col_chart2 = st.columns([2, 1])

with col_chart1:
    st.markdown("## 🧠 Sprach-Stack")
    
    # Radar Chart
    categories = ['Python', 'T-SQL', 'C++', 'HMTL/CSS', 'JS', 'PHP']
    values = [70, 75, 50, 60, 50, 60]
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatterpolar(
        r=values + [values[0]],
        theta=categories + [categories[0]],
        fill='toself',
        fillcolor='rgba(0, 212, 255, 0.2)',
        line=dict(color='#00d4ff', width=2),
        marker=dict(color='#00d4ff', size=8),
        name='Kenntnisse'
    ))
    
    fig.update_layout(
        polar=dict(
            bgcolor='rgba(19, 23, 41, 0.5)',
            radialaxis=dict(
                visible=True,
                range=[0, 100],
                gridcolor='rgba(255, 255, 255, 0.1)',
                showticklabels=False,
                tickfont=dict(color='#94a3b8')
            ),
            angularaxis=dict(
                gridcolor='rgba(255, 255, 255, 0.1)',
                tickfont=dict(color='#ffffff', size=12)
            )
        ),
        showlegend=False,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        height=400
    )
    
    st.plotly_chart(fig, use_container_width=True, key="radar1")

with col_chart2:
    st.markdown("## Top Skills")
    
    skills = [
        ("Python", 70),
        ("T-SQL", 75),
        ("C++", 50),
        ("HMTL/CSS", 60),
        ("JavaScript", 50),
        ("PHP", 60)
    ]
    
    for skill_name, skill_level in skills:
        st.markdown(f"""
        <div class='skill-item'>
            <div class='skill-header'>
                <span class='skill-name'>{skill_name}</span>
                <span class='skill-percentage'>{skill_level}%</span>
            </div>
            <div class='skill-bar'>
                <div class='skill-fill' style='width: {skill_level}%'></div>
            </div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# Charts Section
col_chart3, col_chart4 = st.columns([2, 1])

with col_chart3:
    st.markdown("## 🎯 Tool-Stack")
    
    # Radar Chart
    categories = ['IDE', 'MSSQL/Azur', 'Power BI', 'UnrealEngine', 'Git', 'Streamlit']
    values = [70, 75, 50, 25, 50, 50]
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatterpolar(
        r=values + [values[0]],
        theta=categories + [categories[0]],
        fill='toself',
        fillcolor='rgba(0, 212, 255, 0.2)',
        line=dict(color='#00d4ff', width=2),
        marker=dict(color='#00d4ff', size=8),
        name='Kenntnisse'
    ))
    
    fig.update_layout(
        polar=dict(
            bgcolor='rgba(19, 23, 41, 0.5)',
            radialaxis=dict(
                visible=True,
                range=[0, 100],
                gridcolor='rgba(255, 255, 255, 0.1)',
                showticklabels=False,
                tickfont=dict(color='#94a3b8')
            ),
            angularaxis=dict(
                gridcolor='rgba(255, 255, 255, 0.1)',
                tickfont=dict(color='#ffffff', size=12)
            )
        ),
        showlegend=False,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        height=400
    )
    
    st.plotly_chart(fig, use_container_width=True, key="radar2")

with col_chart4:
    st.markdown("## Top Skills")
    
    skills = [
        ("IDE", 0),
        ("MSSQL/Azur", 70),
        ("Power BI", 0),
        ("UnrealEngine", 0),
        ("Git", 0),
        ("Streamlit", 0)
    ]
    
    for skill_name, skill_level in skills:
        st.markdown(f"""
        <div class='skill-item'>
            <div class='skill-header'>
                <span class='skill-name'>{skill_name}</span>
                <span class='skill-percentage'>{skill_level}%</span>
            </div>
            <div class='skill-bar'>
                <div class='skill-fill' style='width: {skill_level}%'></div>
            </div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# Charts Section
col_chart5, col_chart6 = st.columns([2, 1])

with col_chart5:
    st.markdown("## 📊 Kompetenz-Stack")
    
    # Radar Chart
    categories = ['Datenanalyse', 'Datenmodellierung', 'Reporting', 'Automatisierung', 'Anwendungsentwicklung', 'Performance-Optimierung']
    values = [70, 75, 50, 25, 50, 50]
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatterpolar(
        r=values + [values[0]],
        theta=categories + [categories[0]],
        fill='toself',
        fillcolor='rgba(0, 212, 255, 0.2)',
        line=dict(color='#00d4ff', width=2),
        marker=dict(color='#00d4ff', size=8),
        name='Kenntnisse'
    ))
    
    fig.update_layout(
        polar=dict(
            bgcolor='rgba(19, 23, 41, 0.5)',
            radialaxis=dict(
                visible=True,
                range=[0, 100],
                gridcolor='rgba(255, 255, 255, 0.1)',
                showticklabels=False,
                tickfont=dict(color='#94a3b8')
            ),
            angularaxis=dict(
                gridcolor='rgba(255, 255, 255, 0.1)',
                tickfont=dict(color='#ffffff', size=12)
            )
        ),
        showlegend=False,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        height=400
    )
    
    st.plotly_chart(fig, use_container_width=True, key="radar3")

with col_chart6:
    st.markdown("## Top Skills")
    
    skills = [
        ("Datenanalyse", 0),
        ("Datenmodellierung", 70),
        ("Reporting", 0),
        ("Automatisierung", 0),
        ("Anwendungsentwicklung", 0),
        ("Performance-Optimierung", 0)
    ]
    
    for skill_name, skill_level in skills:
        st.markdown(f"""
        <div class='skill-item'>
            <div class='skill-header'>
                <span class='skill-name'>{skill_name}</span>
                <span class='skill-percentage'>{skill_level}%</span>
            </div>
            <div class='skill-bar'>
                <div class='skill-fill' style='width: {skill_level}%'></div>
            </div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# CTA Section
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("""
<div class='cta-section'>
    <div class='cta-title'>Bereit für neue Herausforderungen</div>
    <div class='cta-text'>
        Lassen Sie uns darüber sprechen, wie ich Ihre Daten in handlungsorientierte Insights verwandeln kann.
    </div>
</div>
""", unsafe_allow_html=True)

col_btn1, col_btn2, col_btn3 = st.columns([1, 1, 1])

with col_btn2:
    if st.button("📧 Kontakt aufnehmen", use_container_width=True):
        st.write("E-Mail: Danielgonzalez1988@web.de")
