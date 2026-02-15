import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

st.set_page_config(page_title="MaStR Analyse", layout="wide")

# =====================================================
# Datenladen
# =====================================================

DEFAULT_CSV = Path(__file__).resolve().parent.parent / "assets" / "data" / "mastr_default.csv"

@st.cache_data
def load_csv(file):
    return pd.read_csv(
        file,
        sep=";",
        decimal=",",
        encoding="utf-8-sig",
        low_memory=False
    )

uploaded = st.file_uploader(
    "Eigene MaStR CSV hochladen, nicht mehr aktuell, deshalb default CSV hinterlegt)",
    type="csv"
)

if uploaded:
    daten = load_csv(uploaded)
    st.success("Eigene CSV geladen")
elif DEFAULT_CSV.exists():
    daten = load_csv(DEFAULT_CSV)
    st.info("Standard-Datensatz geladen")
else:
    st.error("Keine CSV vorhanden")
    st.stop()

# =====================================================
# Datenvorbereiten
# =====================================================

daten["Bruttoleistung der Einheit"] = pd.to_numeric(
    daten["Bruttoleistung der Einheit"], errors="coerce"
) / 1000

daten["DatumAnalyse"] = pd.to_datetime(
    daten["Inbetriebnahmedatum der Einheit"],
    errors="coerce",
    dayfirst=True
)

daten = daten.dropna(subset=["DatumAnalyse"])

daten["Jahr"] = daten["DatumAnalyse"].dt.year
daten["Monat"] = daten["DatumAnalyse"].dt.month_name(locale="de_DE")

# =====================================================
# Datumsrange
# =====================================================

clean = daten.copy()

clean["Leistung"] = pd.to_numeric(
    clean["Bruttoleistung der Einheit"], errors="coerce"
)

clean = clean[
    (clean["Leistung"].notna()) &
    (clean["Leistung"] > 0.01) &
    (clean["Jahr"].notna())
]

year_activity = (
    clean.groupby("Jahr")["Leistung"]
    .sum()
    .reset_index()
)

year_activity = year_activity[year_activity["Leistung"] > 1]

min_year = int(year_activity["Jahr"].min())
max_year = int(year_activity["Jahr"].max())

display_min = min_year - 1   # = Gesamt
display_max = max_year + 1

# =====================================================
# FILTER UI
# =====================================================

st.subheader("🔎 Filter ", help="""
    Wenn Min & Max Jahre gewählt sind, wird der gesamte Zeitraum analysiert.
    Wenn Filter auf 'Alle' stehen, werden Energieträger miteinander verglichen.
    Wenn Filter ausgewählt sind, gibt es Jahreszeitstrahl.""") 

c1, c2, c3, c4 = st.columns(4)

with c1:
    energietraeger = st.selectbox(
        "Energieträger",
        ["Alle"] + sorted(daten["Energieträger"].dropna().unique())
    )

with c2:
    status = st.selectbox(
        "Betriebsstatus",
        ["Alle"] + sorted(daten["Betriebs-Status"].dropna().unique())
    )

with c3:
    jahr_von = st.number_input(
        "Jahr von",
        display_min,
        display_max,
        display_min
    )

with c4:
    jahr_bis = st.number_input(
        "Jahr bis",
        display_min,
        display_max,
        display_max
    )

if jahr_von > jahr_bis:
    jahr_von, jahr_bis = jahr_bis, jahr_von

filter_gesetzt = energietraeger != "Alle" or status != "Alle"
jahr_gesetzt = not (jahr_von == display_min and jahr_bis == display_max)

# =====================================================
# FILTER
# =====================================================

filtered = daten.copy()

if jahr_gesetzt:
    filtered = filtered[
        (filtered["Jahr"] >= jahr_von) &
        (filtered["Jahr"] <= jahr_bis)
    ]

if energietraeger != "Alle":
    filtered = filtered[filtered["Energieträger"] == energietraeger]

if status != "Alle":
    filtered = filtered[filtered["Betriebs-Status"] == status]

# =====================================================
# AGGREGATION
# =====================================================

if not filter_gesetzt and not jahr_gesetzt:
    title = "Alle Energieträger – gesamter Zeitraum"
    grouped = daten.groupby("Energieträger")["Bruttoleistung der Einheit"].sum().reset_index()
    x_col = "Energieträger"

elif not filter_gesetzt and jahr_gesetzt:
    title = f"Alle Energieträger – {jahr_von} bis {jahr_bis}"
    grouped = filtered.groupby("Energieträger")["Bruttoleistung der Einheit"].sum().reset_index()
    x_col = "Energieträger"

elif filter_gesetzt and jahr_gesetzt:
    title = f"Gefiltert – {jahr_von} bis {jahr_bis}"
    grouped = (
        filtered.groupby(["Energieträger", "Jahr"])["Bruttoleistung der Einheit"]
        .sum()
        .reset_index()
    )
    x_col = "Jahr"

else:
    title = "Gefiltert – gesamter Zeitraum"
    grouped = filtered.groupby("Energieträger")["Bruttoleistung der Einheit"].sum().reset_index()
    x_col = "Energieträger"

if grouped.empty:
    st.warning("Keine Daten für diese Kombination")
    st.stop()

grouped = grouped.sort_values("Bruttoleistung der Einheit", ascending=False)

# =====================================================
# Diagramm
# =====================================================

fig = px.bar(
    grouped,
    x=x_col,
    y="Bruttoleistung der Einheit",
    color="Energieträger" if "Energieträger" in grouped.columns else None,
    color_discrete_sequence=px.colors.sequential.Turbo,
    title=title,
    labels={"Bruttoleistung der Einheit": "Zubau (MW)"}
)

fig.update_layout(
    template="plotly_dark",
    height=520
)

st.plotly_chart(fig, use_container_width=True)

# =====================================================
# Ort
# =====================================================

st.subheader("📍 Herkunft der Anlagen")

for col in ["Ort", "Gemeinde", "Landkreis"]:
    if col in filtered.columns:
        vals = filtered[col].dropna().unique()
        if len(vals):
            st.write(f"**{col}:**", ", ".join(map(str, vals[:15])))

# =====================================================
# Sortierte Tabelle
# =====================================================

st.subheader("📊 Zeitliche Entwicklung je Energieträger")

trend_table = (
    filtered.groupby(["Energieträger", "Jahr"])["Bruttoleistung der Einheit"]
    .sum()
    .reset_index()
    .sort_values(["Energieträger", "Jahr"])
)

st.dataframe(trend_table, use_container_width=True)

# =====================================================
# Ergebnis 
# =====================================================