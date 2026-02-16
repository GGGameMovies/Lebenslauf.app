import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime
from pathlib import Path
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
col1, col2, col3 = st.columns(3)

with col1:
    st.page_link("streamlit_app.py", label="🏠 Start")

with col2:
    st.page_link("pages/Projekte.py", label="📂 Projekte")

with col3:
    st.page_link("pages/Feedback.py", label="📧 Feedback")






    