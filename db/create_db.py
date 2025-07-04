from DB_connection import db_con


def init_db():
    conn, cursor = db_con()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS register_users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_token INTEGER UNIQUE,
            nick_name TEXT,
            name TEXT,
            date TEXT
        )
    ''')
    conn.commit()

    cursor.execute('''
            CREATE TABLE IF NOT EXISTS characters (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_token INTEGER UNIQUE,
                name_character TEXT,
                class TEXT,
                race TEXT,
                modifier TEXT,
                level INTEGER,
                spell TEXT
            )
        ''')
    conn.commit()

    cursor.execute('''
                CREATE TABLE IF NOT EXISTS spell (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    spell_en TEXT,
                    spell_ru TEXT,
                    url TEXT
                )
            ''')
    conn.commit()

    cursor.execute('''
                    CREATE TABLE IF NOT EXISTS user_character (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        user_token INTEGER UNIQUE,
                        name_character TEXT,
                        name_json TEXT
                    )
                ''')
    conn.commit()