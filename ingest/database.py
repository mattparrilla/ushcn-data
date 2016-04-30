import sqlite3

DATABASE = '../ushcn.db'


def init(database=DATABASE):
    """Initialize DB using python, just cuz"""
    conn = sqlite3.connect(database)
    c = conn.cursor()

    c.executescript('''
        CREATE TABLE station (
            id INTEGER PRIMARY KEY NOT NULL,
            name TEXT,
            state TEXT,
            latitude REAL,
            longitude REAL,
            elevation REAL
        );

        CREATE TABLE reading (
            id INTEGER PRIMARY KEY NOT NULL,
            value INTEGER,
            metric TEXT,
            m_flag TEXT,
            q_flag TEXT,
            s_flag TEXT,
            date DATETIME,
            station_id INTEGER
        );
    ''')

    conn.commit()
    conn.close()


def ingest_month(month, database=DATABASE):
    """Ingest an entire m of a single metric at a single USHCN station"""
    conn = sqlite3.connect(database)
    c = conn.cursor()

    entries = [(None, m['value'], m['metric'], m['m_flag'], m['q_flag'],
        m['s_flag'], m['date'], m['station_id']) for m in month]

    c.executemany('''INSERT INTO reading
        (id, value, metric, m_flag, q_flag, s_flag, date, station_id)
        VALUES (?,?,?,?,?,?,?,?)''', entries)

    conn.commit()
    conn.close()

if __name__ == '__main__':
    init()
