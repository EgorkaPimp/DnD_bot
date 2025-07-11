import asyncio
import logging

from folder_class.DB_connection import work_conn
from folder_class.InitDBClass import INIT_DB

async def search_for_a_nickname_by_id(user_id: int):
    conn = await work_conn(INIT_DB.name_db)
    nickname = await conn.fetchval("""
                            SELECT nick_name
                            FROM register_users
                            WHERE user_token = $1
                    """, user_id)
    return nickname

async def check_id_in_db(user_id: int):
    conn = await work_conn(INIT_DB.name_db)
    result = await conn.fetchval("""
                    SELECT EXISTS (
                               SELECT nick_name
                               FROM register_users
                               WHERE user_token = $1
                       )""", user_id)
    return result

async def view_user_for_db(user_id: int):
    conn = await work_conn(INIT_DB.name_db)
    result = await conn.fetchrow("""
                                   SELECT *
                                   FROM register_users
                                   WHERE user_token = $1
                                   ORDER BY id ASC
                           """, user_id)
    return result

async def delete_user_for_db(user_id: int):
    try:
        logging.warning(f'delete user {user_id}')
        conn = await work_conn(INIT_DB.name_db)
        await conn.execute("""
                            DELETE 
                            FROM register_users 
                            WHERE user_token = $1;
                        """, user_id)
    except Exception as e:
        print(e)
        logging.error(f'Delete user bug: {e}')


async def update_nick_user(user_id: int, new_nick_name):
    try:
        logging.warning(f'update nick user {user_id}')
        conn = await work_conn(INIT_DB.name_db)
        await conn.execute("""
                            UPDATE register_users
                            SET  nick_name = $1
                            WHERE user_token = $2;
                        """, new_nick_name, user_id)
    except Exception as e:
        print(e)
        logging.error(f'Delete user bug: {e}')