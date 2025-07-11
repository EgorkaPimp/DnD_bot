import asyncpg


async def create_conn():
    # Коннектимся к системной базе postgres
    conn = await asyncpg.connect(
        user='egor_dnd',
        password='dnd',
        host='localhost',
        database='postgres',
        port=2000,
        timeout=10
    )
    return conn

async def work_conn(database):
    # Коннектимся к системной базе postgres
    conn = await asyncpg.connect(
        user='egor_dnd',
        password='dnd',
        host='localhost',
        database=database,
        port=2000,
        timeout=10
    )
    return conn