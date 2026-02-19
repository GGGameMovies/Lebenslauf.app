import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
DB_PATH = BASE_DIR / "assets" / "data" / "game.db"

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()
cursor.execute("PRAGMA foreign_keys = ON;")

cursor.executescript("""
CREATE TABLE IF NOT EXISTS besucher (
    BesucherID INTEGER PRIMARY KEY AUTOINCREMENT,
    Benutzername TEXT,
    Passwort TEXT,
    Email TEXT,
    Profilbild TEXT,
    Pruefcode TEXT,
    Bgeprueft INTEGER
);

CREATE TABLE IF NOT EXISTS genres (
    GenreID INTEGER PRIMARY KEY AUTOINCREMENT,
    GenreName TEXT UNIQUE
);

CREATE TABLE IF NOT EXISTS plattform (
    PlattformID INTEGER PRIMARY KEY AUTOINCREMENT,
    PlattformName TEXT UNIQUE
);

CREATE TABLE IF NOT EXISTS player (
    PlayerID INTEGER PRIMARY KEY AUTOINCREMENT,
    PlayerName TEXT UNIQUE
);

CREATE TABLE IF NOT EXISTS ps (
    PSID INTEGER PRIMARY KEY AUTOINCREMENT,
    PSName TEXT UNIQUE,
    PSLogo TEXT
);

CREATE TABLE IF NOT EXISTS spiele (
    SpielID INTEGER PRIMARY KEY AUTOINCREMENT,
    SpielName TEXT,
    YoutubeURL TEXT,
    Beschreibung TEXT,
    KBeschreibung TEXT,
    Audio TEXT,
    Datum TEXT,
    BuyURLPS TEXT,
    BuyURLPC TEXT,
    BuyURLXbox TEXT,
    BuyURLNintendo TEXT,
    Logo TEXT,
    Orte TEXT,
    Cover TEXT,
    Gameplay INTEGER,
    Graphic INTEGER,
    Story INTEGER,
    AI INTEGER,
    Creativity INTEGER,
    Immersion INTEGER,
    Sound INTEGER,
    Rating INTEGER,
    WievieleUserVote INTEGER,
    Geprüft INTEGER
);

CREATE TABLE IF NOT EXISTS bewertungen (
    BewertungID INTEGER PRIMARY KEY AUTOINCREMENT,
    BesucherID INTEGER,
    SpielID INTEGER,
    GameplayB INTEGER,
    GraphicB INTEGER,
    StoryB INTEGER,
    AIB INTEGER,
    CreativityB INTEGER,
    ImmersionB INTEGER,
    SoundB INTEGER,
    Rating INTEGER,
    FOREIGN KEY (BesucherID) REFERENCES besucher(BesucherID),
    FOREIGN KEY (SpielID) REFERENCES spiele(SpielID)
);

CREATE TABLE IF NOT EXISTS spiel_Genre (
    SpielID INTEGER,
    GenreID INTEGER,
    PRIMARY KEY (SpielID, GenreID),
    FOREIGN KEY (SpielID) REFERENCES spiele(SpielID),
    FOREIGN KEY (GenreID) REFERENCES genres(GenreID)
);

CREATE TABLE IF NOT EXISTS spiel_Plattform (
    SpielID INTEGER,
    PlattformID INTEGER,
    PRIMARY KEY (SpielID, PlattformID),
    FOREIGN KEY (SpielID) REFERENCES spiele(SpielID),
    FOREIGN KEY (PlattformID) REFERENCES plattform(PlattformID)
);

CREATE TABLE IF NOT EXISTS spiel_Player (
    SpielID INTEGER,
    PlayerID INTEGER,
    PRIMARY KEY (SpielID, PlayerID),
    FOREIGN KEY (SpielID) REFERENCES spiele(SpielID),
    FOREIGN KEY (PlayerID) REFERENCES player(PlayerID)
);

CREATE TABLE IF NOT EXISTS spiel_PS (
    SpielID INTEGER,
    PSID INTEGER,
    PRIMARY KEY (SpielID, PSID),
    FOREIGN KEY (SpielID) REFERENCES spiele(SpielID),
    FOREIGN KEY (PSID) REFERENCES ps(PSID)
);
""")

conn.commit()
conn.close()

print("SQLite Schema komplett erstellt!")
