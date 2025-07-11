from db_postgres.create_db import init_db
import json

class INIT_DB:
    name_db = 'dnd'
    tables = ['register_users', 'characters', 'spell', 'user_character']

    @classmethod
    async def initialize(cls):
        await init_db(cls.name_db, cls.tables)
