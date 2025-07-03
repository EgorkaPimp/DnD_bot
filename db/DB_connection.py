import sqlite3

def db_con():
    with sqlite3.connect('dnd.db') as conn:
        conn.execute("PRAGMA foreign_keys = ON")
        cursor = conn.cursor()
        return conn, cursor