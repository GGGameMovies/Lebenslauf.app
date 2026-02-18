import pandas as pd
from pathlib import Path


def load_mastr_data():
    base_path = Path(__file__).resolve().parent.parent
    csv_path = base_path / "assets" / "data" / "MaStR_Analyse.csv"

    print("Lade CSV:", csv_path)

    if not csv_path.exists():
        return pd.DataFrame()

    df = pd.read_csv(
        csv_path,
        sep=";",
        encoding="utf-8",
        low_memory=False
    )

    # Datum
    df["Inbetriebnahmedatum der Einheit"] = pd.to_datetime(
        df["Inbetriebnahmedatum der Einheit"],
        errors="coerce"
    )
    df["Jahr"] = df["Inbetriebnahmedatum der Einheit"].dt.year

    # Leistung
    df["Bruttoleistung der Einheit"] = pd.to_numeric(
        df["Bruttoleistung der Einheit"],
        errors="coerce"
    )

    return df


def apply_filters(df, energietraeger, jahr_von, jahr_bis):
    """
    Umsetzung DEINER Regeln
    """

    work_df = df.copy()

    # Energieträger
    if energietraeger != "Alle":
        work_df = work_df[work_df["Energieträger"] == energietraeger]

    # Jahre nur anwenden wenn gesetzt
    if jahr_von is not None and jahr_bis is not None:
        work_df = work_df[
            (work_df["Jahr"] >= jahr_von) &
            (work_df["Jahr"] <= jahr_bis)
        ]

    return work_df


def aggregate_by_energy(df):
    return (
        df.groupby("Energieträger")["Bruttoleistung der Einheit"]
        .sum()
        .reset_index()
        .sort_values("Bruttoleistung der Einheit", ascending=False)
    )
