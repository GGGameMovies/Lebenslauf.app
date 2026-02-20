import streamlit as st
from pathlib import Path
import base64

# ----------------------------
# Paths
# ----------------------------

BASE_DIR = Path(__file__).resolve().parent
ASSETS_DIR = BASE_DIR.parent / "assets"

ZERTIFIKATE_DIR = ASSETS_DIR / "Plaene" / "Zertifikat"
ZEUGNISSE_DIR  = ASSETS_DIR / "Plaene" / "Arbeitszeugnis"

CSS_PATH = ASSETS_DIR / "streamlit_app_styles.css"


# ----------------------------
# Load CSS
# ----------------------------

def load_css():
    if CSS_PATH.exists():
        with open(CSS_PATH, encoding="utf-8") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()


# ----------------------------
# Helpers
# ----------------------------

def load_pdfs(folder):
    if not folder.exists():
        return []
    return sorted(folder.glob("*.pdf"))


def pdf_card(file):
    st.markdown(f"### 📄 {file.stem.replace('_',' ')}")

    with open(file, "rb") as f:
        st.download_button(
            "⬇ Öffnen / Download",
            f,
            file_name=file.name,
            mime="application/pdf",
            use_container_width=True,
        )

    st.markdown("---")


def show_grid(files, cols=3):
    if not files:
        st.info("Keine PDFs gefunden.")
        return

    columns = st.columns(cols)

    for i, file in enumerate(files):
        with columns[i % cols]:
            pdf_card(file)


# ----------------------------
# Navigation
# ----------------------------

col1, col2, col3 = st.columns(3)

with col1:
    st.page_link("streamlit_app.py", label="🏠 Start")

with col2:
    st.page_link("pages/Projekte.py", label="📂 Projekte")

with col3:
    st.page_link("pages/Zeugnisse.py", label="📜 Zeugnisse")


# ----------------------------
# Content
# ----------------------------

st.title("📜 Zeugnisse & Zertifikate")

st.subheader("🏫 Praktikumszeugnisse")
show_grid(load_pdfs(ZEUGNISSE_DIR))

st.subheader("🏅 Zertifikate")
show_grid(load_pdfs(ZERTIFIKATE_DIR))