import asyncio
import datetime
import logging

from db_postgres.DB_connection import work_conn
from db_postgres.InitDBClass import INIT_DB

name_db = INIT_DB.name_db

async def add_user_in_db(user_id: int, nickname_user: str,
                         name_user: str, data_now: str):
    try:
        logging.warning('Start write user nick in db')
        conn = await work_conn(name_db)
        await conn.execute("""
        INSERT INTO register_users
        (user_token, nick_name, name, date)
        VALUES($1, $2, $3, $4)
            """, user_id, nickname_user, name_user, data_now
        )
    except Exception as e:
        logging.error(f'In write user bd log: {e}')
