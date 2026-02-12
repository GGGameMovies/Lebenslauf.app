import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Daniel Gonzalez - Data Analytics Portfolio",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for dark modern design
st.markdown("""
<style>
    /* Import fonts */
    @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&family=Outfit:wght@300;400;600;700&display=swap');
    
    /* Main container */
    .stApp {
        background: linear-gradient(135deg, #0a0e27 0%, #1a1f3a 100%);
        font-family: 'Outfit', sans-serif;
    }
    
    /* Headers */
    h1 {
        font-size: 4rem !important;
        font-weight: 700 !important;
        background: linear-gradient(135deg, #00d4ff 0%, #7c3aed 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 0.5rem !important;
        letter-spacing: -2px;
    }
    
    h2 {
        color: #00d4ff !important;
        font-weight: 600 !important;
    }
    
    h3 {
        color: #ffffff !important;
        font-weight: 600 !important;
    }
    
    /* Subtitle */
    .subtitle {
        text-align: center;
        color: #94a3b8;
        font-size: 1.3rem;
        font-family: 'JetBrains Mono', monospace;
        margin-bottom: 1rem;
    }
    
    /* Contact info */
    .contact-info {
        text-align: center;
        color: #94a3b8;
        font-size: 1rem;
        margin-bottom: 3rem;
    }
    
    /* Metric cards */
    div[data-testid="metric-container"] {
        background: linear-gradient(135deg, rgba(19, 23, 41, 0.8) 0%, rgba(19, 23, 41, 0.6) 100%);
        border: 1px solid rgba(0, 212, 255, 0.3);
        border-radius: 16px;
        padding: 20px;
        box-shadow: 0 8px 32px rgba(0, 212, 255, 0.1);
        backdrop-filter: blur(10px);
    }
    
    div[data-testid="metric-container"]:hover {
        transform: translateY(-5px);
        border-color: #00d4ff;
        box-shadow: 0 20px 60px rgba(0, 212, 255, 0.3);
        transition: all 0.3s ease;
    }
    
    div[data-testid="stMetricValue"] {
        color: #00d4ff !important;
        font-size: 2.5rem !important;
        font-family: 'JetBrains Mono', monospace !important;
        font-weight: 700 !important;
    }
    
    div[data-testid="stMetricLabel"] {
        color: #94a3b8 !important;
        font-size: 0.9rem !important;
        text-transform: uppercase;
        letter-spacing: 1px;
        font-weight: 600 !important;
    }
    
    /* Project cards */
    .project-card {
        background: linear-gradient(135deg, rgba(19, 23, 41, 0.9) 0%, rgba(19, 23, 41, 0.7) 100%);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 16px;
        padding: 25px;
        margin-bottom: 20px;
        transition: all 0.3s ease;
        backdrop-filter: blur(10px);
    }
    
    .project-card:hover {
        border-color: #00d4ff;
        transform: translateX(8px);
        box-shadow: 0 10px 40px rgba(0, 212, 255, 0.2);
    }
    
    .project-title {
        color: #00d4ff;
        font-size: 1.4rem;
        font-weight: 600;
        margin-bottom: 12px;
    }
    
    .project-desc {
        color: #94a3b8;
        font-size: 1rem;
        line-height: 1.6;
        margin-bottom: 15px;
    }
    
    .tech-tags {
        display: flex;
        gap: 8px;
        flex-wrap: wrap;
        margin-bottom: 15px;
    }
    
    .tech-tag {
        padding: 6px 14px;
        background: rgba(0, 212, 255, 0.15);
        border: 1px solid rgba(0, 212, 255, 0.4);
        border-radius: 20px;
        font-size: 0.8rem;
        color: #00d4ff;
        font-family: 'JetBrains Mono', monospace;
        font-weight: 500;
    }
    
    .impact-metric {
        background: rgba(124, 58, 237, 0.15);
        border-left: 3px solid #7c3aed;
        padding: 12px;
        border-radius: 6px;
        margin-top: 15px;
    }
    
    .impact-metric strong {
        color: #7c3aed;
    }
    
    /* Timeline */
    .timeline-item {
        border-left: 2px solid rgba(255, 255, 255, 0.1);
        padding-left: 25px;
        padding-bottom: 25px;
        position: relative;
    }
    
    .timeline-dot {
        position: absolute;
        left: -7px;
        top: 0;
        width: 12px;
        height: 12px;
        border-radius: 50%;
        background: #00d4ff;
        box-shadow: 0 0 20px rgba(0, 212, 255, 0.6);
    }
    
    .timeline-date {
        color: #00d4ff;
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.9rem;
        font-weight: 600;
        margin-bottom: 8px;
    }
    
    .timeline-title {
        color: #ffffff;
        font-size: 1.1rem;
        font-weight: 600;
        margin-bottom: 5px;
    }
    
    .timeline-org {
        color: #94a3b8;
        font-size: 0.95rem;
    }
    
    /* CTA Section */
    .cta-section {
        background: linear-gradient(135deg, #7c3aed 0%, #00d4ff 100%);
        border-radius: 20px;
        padding: 50px;
        text-align: center;
        margin-top: 40px;
        box-shadow: 0 20px 60px rgba(124, 58, 237, 0.3);
    }
    
    .cta-title {
        font-size: 2rem;
        font-weight: 700;
        color: white;
        margin-bottom: 15px;
    }
    
    .cta-text {
        font-size: 1.1rem;
        color: rgba(255, 255, 255, 0.9);
        margin-bottom: 30px;
    }
    
    /* Buttons */
    .stButton > button {
        background: white;
        color: #7c3aed;
        border-radius: 50px;
        padding: 15px 35px;
        font-weight: 600;
        font-size: 1rem;
        border: none;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: translateY(-3px);
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
    }
    
    /* Skill progress bars */
    .skill-item {
        margin-bottom: 20px;
    }
    
    .skill-header {
        display: flex;
        justify-content: space-between;
        margin-bottom: 8px;
    }
    
    .skill-name {
        color: #ffffff;
        font-weight: 600;
    }
    
    .skill-percentage {
        color: #00d4ff;
        font-family: 'JetBrains Mono', monospace;
        font-weight: 700;
    }
    
    .skill-bar {
        height: 8px;
        background: rgba(255, 255, 255, 0.1);
        border-radius: 10px;
        overflow: hidden;
    }
    
    .skill-fill {
        height: 100%;
        background: linear-gradient(90deg, #00d4ff, #7c3aed);
        border-radius: 10px;
        transition: width 1.5s ease;
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Expander styling */
    .streamlit-expanderHeader {
        background: rgba(19, 23, 41, 0.8);
        border-radius: 10px;
        color: #00d4ff !important;
        font-weight: 600 !important;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("<h1>DANIEL GONZALEZ</h1>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Fachinformatiker für Daten- und Prozessanalyse (IHK)</div>", unsafe_allow_html=True)
st.markdown("""
<div class='contact-info'>
    📧 Danielgonzalez1988@web.de &nbsp;&nbsp;|&nbsp;&nbsp; 📱 015252874894 &nbsp;&nbsp;|&nbsp;&nbsp; 📍 Leipzig, Deutschland
</div>
""", unsafe_allow_html=True)

# Stats Section
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(label="Jahre Erfahrung", value="2")

with col2:
    st.metric(label="IHK Abschluss", value="91%")

with col3:
    st.metric(label="Große Projekte", value="4")

with col4:
    st.metric(label="Technologien", value="12+")

st.markdown("<br>", unsafe_allow_html=True)

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
    st.markdown("## ⚡ Top Skills")
    
    skills = [
        ("Python (Pandas, NumPy)", 97),
        ("SQL & Datenbanken", 96),
        ("Data Science & ML", 93),
        ("Power BI & Excel", 95),
        ("HTML/CSS/JavaScript", 98),
        ("Git & Agile/Scrum", 90)
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
col_chart1, col_chart2 = st.columns([2, 1])

with col_chart1:
    st.markdown("## 📊 Technologie-Stack")
    
    # Radar Chart
    categories = ['Python', 'SQL', 'Power BI', 'Excel', 'JavaScript', 'Data Science']
    values = [97, 96, 95, 93, 98, 93]
    
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
    
    st.plotly_chart(fig, use_container_width=True)

with col_chart2:
    st.markdown("## 🎓 Ausbildung Timeline")
    
    timeline_data = [
        ("2023 - 2025", "Fachinformatiker Daten- und Prozessanalyse", "WBS Schulung • Note: 2,0 (91%)"),
        ("2024 - 2025", "Praktikum Stadt Leipzig", "Referat Digitale Stadt"),
        ("2019 - 2020", "Junior Software Developer", "Stadtwerke Leipzig"),
        ("2009 - 2011", "Fachinformatiker Anwendungsentwicklung", "Z&P Weiterbildung")
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
