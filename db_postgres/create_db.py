import logging

from folder_class.DB_connection import work_conn, create_conn
from db_postgres.update_spell_db import spell_data_for_db


async def init_db(name_db, tables):
    conn = await create_conn()
    db_exists = await conn.fetchval(
        f"SELECT 1 FROM pg_database WHERE datname = $1",
        name_db
    )
    if not db_exists:
        await conn.execute(f'CREATE DATABASE {name_db}')
        logging.warning(f"DataBase {name_db} was created.")
        await create_table_db(name_db)
        logging.warning(f"All tables was created.")
    else:
        logging.warning(f"DataBase {name_db} already created.")
        await check_table_bd(name_db, tables)
    w_conn = await work_conn(name_db)
    await spell_data_for_db(w_conn)
    await conn.close()


async def create_table_db(name_db):
    conn = await work_conn(name_db)
    await conn.execute('''
        CREATE TABLE IF NOT EXISTS register_users (
            id SERIAL PRIMARY KEY,
            user_token INTEGER UNIQUE,
            nick_name TEXT,
            name TEXT,
            date TEXT
        )
    ''')

    await conn.execute('''
            CREATE TABLE IF NOT EXISTS characters (
                id SERIAL PRIMARY KEY,
                user_token INTEGER UNIQUE,
                name_character TEXT,
                class TEXT,
                race TEXT,
                modifier TEXT,
                level INTEGER,
                spell TEXT
            )
        ''')

    await conn.execute('''
                CREATE TABLE IF NOT EXISTS spell (
                    id SERIAL PRIMARY KEY,
                    spell_en TEXT,
                    spell_ru TEXT,
                    url TEXT
                )
            ''')

    await conn.execute('''
                    CREATE TABLE IF NOT EXISTS user_character (
                        id SERIAL PRIMARY KEY,
                        user_token INTEGER UNIQUE,
                        name_character TEXT,
                        name_json TEXT
                    )
                ''')
    await conn.close()

async def check_table_bd(name_db, tables):
    conn = await work_conn(name_db)
    for table in tables:
        exists = await conn.fetchval("""
                    SELECT EXISTS (
                        SELECT 1
                        FROM information_schema.tables
                        WHERE table_schema = 'public'
                          AND table_name = $1
                    )
                """, table)
        if not exists:
            logging.warning(f"Table {table} don't created. Start creating tables")
            await create_table_db(name_db)

    await conn.close()
