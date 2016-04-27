CREATE TABLE station (
    id INTEGER PRIMARY KEY,
    name TEXT,
    state TEXT,
    latitude REAL,
    longitude REAL,
    elevation REAL
);

CREATE TABLE tmax (
    id INTEGER PRIMARY KEY,
    value INTEGER,
    m_flag TEXT,
    q_flag TEXT,
    s_flag TEXT,
    date DATETIME,
    station_id INTEGER
);

CREATE TABLE tmin (
    id INTEGER PRIMARY KEY,
    value INTEGER,
    m_flag TEXT,
    q_flag TEXT,
    s_flag TEXT,
    date DATETIME,
    station_id INTEGER
);

CREATE TABLE prcp (
    id INTEGER PRIMARY KEY,
    value INTEGER,
    m_flag TEXT,
    q_flag TEXT,
    s_flag TEXT,
    date DATETIME,
    station_id INTEGER
);

CREATE TABLE snwd (
    id INTEGER PRIMARY KEY,
    value INTEGER,
    m_flag TEXT,
    q_flag TEXT,
    s_flag TEXT,
    date DATETIME,
    station_id INTEGER
);

CREATE TABLE snow (
    id INTEGER PRIMARY KEY,
    value INTEGER,
    m_flag TEXT,
    q_flag TEXT,
    s_flag TEXT,
    date DATETIME,
    station_id INTEGER
);
