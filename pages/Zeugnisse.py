import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime
from pathlib import Path

# Custom CSS for dark modern design
BASE_DIR = Path(__file__).resolve().parent
ASSETS_DIR = BASE_DIR.parent / "assets"
ZERTIFIKATE_DIR = ASSETS_DIR / "Zertifikat"
ZEUGNISSE_DIR = ASSETS_DIR / "Arbeitszeugnis"

def load_css():
    css_path = Path(__file__).resolve().parent.parent / "assets" / "streamlit_app_styles.css"

    if css_path.exists():
        with open(css_path, encoding="utf-8") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    else:
        st.error(f"CSS nicht gefunden: {css_path}")

load_css()

def load_files(folder: Path, extensions=("pdf", "png", "jpg", "jpeg")):
    files = []
    for ext in extensions:
        files.extend(folder.glob(f"*.{ext}"))
    return sorted(files)

st.write(Path(__file__).parent)

# Header
#Navi
col1, col2, col3 = st.columns(3)

with col1:
    st.page_link("streamlit_app.py", label="🏠 Start")

with col2:
    st.page_link("pages/Projekte.py", label="📂 Projekte")

with col3:
    st.page_link("pages/Zeugnisse.py", label="📜 Zeugnisse")

st.header("📜 Praktikumszeugnisse")

zeugnisse = load_files(ZEUGNISSE_DIR)

if not zeugnisse:
    st.info("Keine Zeugnisse gefunden.")
else:
    for file in zeugnisse:
        if file.suffix.lower() == ".pdf":
            with open(file, "rb") as f:
                st.download_button(
                    label=f"📥 {file.stem}",
                    data=f,
                    file_name=file.name,
                    mime="application/pdf"
                )
        else:
            st.image(str(file), caption=file.stem, use_column_width=True)

st.header("🏅 Zertifikate")

zertifikate = load_files(ZERTIFIKATE_DIR)

if not zertifikate:
    st.info("Keine Zertifikate gefunden.")
else:
    for file in zertifikate:
        if file.suffix.lower() == ".pdf":
            with open(file, "rb") as f:
                st.download_button(
                    label=f"📥 {file.stem}",
                    data=f,
                    file_name=file.name,
                    mime="application/pdf"
                )
        else:
            st.image(str(file), caption=file.stem, use_column_width=True)