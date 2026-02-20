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
    st.page_link("pages/Zeugnisse.py", label="📜 Zeugnisse")

st.markdown("<h1>DANIEL GONZALEZ</h1>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Datenanalyst für Prozessoptimierung mit Entwickler-Mindset</div>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.markdown(
        "<div class='contact-info'>📧 Danielgonzalez1988@web.de | 📱 015252874894 | 📍 Leipzig, Deutschland</div>",
        unsafe_allow_html=True
    )


# Main content
col0, col1, col2,col4 = st.columns([1, 2, 2, 1])

with col1:
    st.markdown("## 🎓 Ausbildung")
    st.markdown("""
##  Fachinformatiker für Daten- und Prozessanalyse
    WBS Schulung, Leipzig, Deutschland

    Vertieft:
                
    -  Netzwerke und Internettechnologien
    -  MS Office
    -  Daten- und Prozessanalyse
    -  Datenbanken und SQL
                
    Grundlagen:
                
    -  Programmiersprache C, Python
    -  Windows Server
    -  Informationssicherheit und Datenschutz
    -  Virtualisierung VM
    -  IT-Hardware und Betriebssysteme
    -  HTML und CSS
    -  Rechnungswesen, Buchführung
    -  Projektmanagement
    -  Datenwissenschaft
                
    """)

    st.markdown("## 📋 Praktikum")
    st.markdown("""
##  Fachinformatiker für Daten- & Prozessanalyse
    Referat Digitale Stadt Leipzig, Leipzig, Deutschland

    - Entwicklung Buchungsanalyse-Tool (Python) zur automatisierten Auswertung von Raumbuchungsdaten per CSV,
    - Analyse von internen & externen Nutzungsmustern für Büros,Büros, Ausstellungsräume & Veranstaltungsflächen
    
    Technologie-Stack: VS Code, Jupiter, Python, Pandas, NumPy, Matplotlib, CSVVerarbeitung, Jira, Confluence
    
    - Enge Abstimmung mit Projektleitung zur Anforderungsanalyse und Ergebnisvalidierung
    - Teilnahme an internen/externen Meetings und Workshops zur Projektkoordination
    - Dienstplanung und Betreuung des Ausstellungsraumes 
    - Büroarbeit
    
    Technologie-Stack: Excel, PowerPoint, Teams, Miro, Slack
                
    """)

    st.markdown("## 🎓 Ausbildung")
    st.markdown("""
##  Fachinformatiker für Anwendungsentwicklung
    Z&P Weiterbildung, Leipzig, Deutschland

    Vertieft:
                
    - Datenbanken und SQL - Grundlagen
    - Programmiersprache C, C#, Java - Grundlagen
    - OOP mit MVC
                
    Grundlagen:
                
    - MS Office
    - Netzwerke und Internettechnologien
    - HTML und CSS
    - Rechnungswesen, Buchführung
    - Projektmanagement
                
    """)   

    st.markdown("## 📋 Praktikum")
    st.markdown("""
##  Junior-Software Entwickler
    Stadtwerke Leipzig, Leipzig, Deutschland

    - Datenbankentwicklung & -verwaltung für IoT-Sensordaten (Heizkörper-Monitoring)
    - Implementierung von SQL-Abfragen zur Auswertung von Sensorwerten und Betriebsdaten
    - Einblick in IT-Sicherheitsstandards und organisatorische Abläufe der Energiewirtschaft
    
    Technologie-Stack: SQL, GitLab, Scrum/Agile, Slack, VS Studio Code, Jira, Confluence
                
    """)

    st.markdown("## 💼 Beruf")
    st.markdown("""
##  Privater Arbeitsvermittler
    AIW International, Leipzig, Deutschland

    - Kundenbetreuung und Vermittlung zwischen Arbeitnehmern und Arbeitgebern
    - Telefonische und schriftliche Kommunikation mit Kunden und Partnern
    - Datenerfassung und -verwaltung von Kundendaten und Vermittlungsprozessen
    - Organisation von Vorstellungsgesprächen und Unterstützung bei der Bewerbungsprozesss
    
    Technologie-Stack: MS Office, Outlook, PC-Kaufmann
                
    """)

# Skills Section
with col2:
    st.markdown("## 🎓 Lebenslauf Timeline")
    
    timeline_data = [
        ("08/2023 - 06/2025", "Fachinformatiker Daten- und Prozessanalyse - Weiterbildung", "WBS Schulung"),
        ("10/2024 - 05/2025", "Praktikum - Datenanalyst", "Referat Digitale Stadt Leipzig"),
        ("09/2019 - 08/2021", "Fachinformatiker Anwendungsentwicklung - Weiterbildung", "Z&P Weiterbildung"),
        ("11/2020 - 04/2021", "Praktikum - Junior Software Developer", "Stadtwerke Leipzig"),
        ("10/2018 - 08/2019", "Privater Arbeitsvermittler", "AIW International "),
        ("08/2017 - 09/2018", "Abi abgebrochen für Arbeitsaufnahme","Leipzig Kolleg"),
        ("09/2012 - 06/2014", "Realschulabschluss","Abendoberschule Leipzig"),
        ("06/2012 - 07/2012", "Hauptschulabschluss","Extern über Landesamt für Schule und Bildung"),
        ("10/2011 - 12/2011", "Lagerist über Weihnachtsgeschäft","Amazon Distribution GmbH - Leipzig"),
        ("06/2009 - 06/2010", "Lagerist", "Headwaylogistik - Recklinghausen"),
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
col_chart0, col_chart1, col_chart2,col_chart3 = st.columns([1, 2, 2, 1])

with col_chart1:
    st.markdown("## 🧠 Sprach-Stack")
    
    # Radar Chart
    categories = ['T-SQL', 'PHP', 'Excel', 'Python', 'HMTL/CSS', 'PHP', 'C++']
    values = [75, 75, 70, 65, 65, 40]
    
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
        ("T-SQL", 75),
        ("PHP", 75),
        ("Excel", 70),
        ("HMTL/CSS", 65),
        ("Python", 65),
        ("C++", 40)
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
col_chart4, col_chart5, col_chart6,col_chart7 = st.columns([1, 2, 2, 1])

with col_chart5:
    st.markdown("## 🎯 Tool-Stack")
    
    # Radar Chart
    categories = ['IDE', 'MSSQL/Azur', 'Github', 'Power BI', 'UnrealEngine', 'Streamlit']
    values = [70, 70, 70, 50, 40, 30]
    
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

with col_chart6:
    st.markdown("## Top Skills")
    
    skills = [
        ("IDE", 70),
        ("MSSQL/Azur", 70),
        ("Github", 70),
        ("Power BI", 50),
        ("UnrealEngine", 40),
        ("Streamlit", 30)
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
col_chart8, col_chart9, col_chart10,col_chart11 = st.columns([1, 2, 2, 1])

with col_chart9:
    st.markdown("## 📊 Kompetenz-Stack")
    
    # Radar Chart
    categories = ['Automatisierung', "Datenanalyse", "Datenmodellierung", 'Anwendungsentwicklung', "Reporting", "Performance-Optimierung"]
    values = [75, 70, 70, 70, 60, 50]
    
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

with col_chart10:
    st.markdown("## Top Skills")
    
    skills = [
        ("Automatisierung", 75),
        ("Datenanalyse", 70),
        ("Datenmodellierung", 70),
        ("Anwendungsentwicklung", 70),
        ("Reporting", 60),
        ("Performance-Optimierung", 50)
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
        st.markdown("Adresse:Jupiterstraße 36, 04205 Leipzig")
        st.markdown("E-Mail: Danielgonzalez1988@web.de")
        st.markdown("Mobile: 015252874894")
