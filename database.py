# database.py
import sqlite3

def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS stats (
            id INTEGER PRIMARY KEY,
            clicks INTEGER,
            energy INTEGER,
            energy_limit INTEGER,
            multiplier INTEGER,
            energy_price INTEGER,
            multiplier_price INTEGER
        )
    ''')
    cursor.execute('''
        INSERT INTO stats (id, clicks, energy, energy_limit, multiplier, energy_price, multiplier_price)
        VALUES (1, 0, 1000, 1000, 1, 50, 100)
        ON CONFLICT(id) DO NOTHING
    ''')
    conn.commit()
    conn.close()

def get_clicks():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT clicks, energy, energy_limit, multiplier, energy_price, multiplier_price FROM stats WHERE id=1')
    row = cursor.fetchone()
    conn.close()
    return row

def update_clicks(clicks, energy, energy_limit, multiplier, energy_price, multiplier_price):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE stats
        SET clicks=?, energy=?, energy_limit=?, multiplier=?, energy_price=?, multiplier_price=?
        WHERE id=1
    ''', (clicks, energy, energy_limit, multiplier, energy_price, multiplier_price))
    conn.commit()
    conn.close()
