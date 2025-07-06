from datetime import datetime

from db_postgres.InitDBClass import INIT_DB
from token_file import read_file
import asyncio
import logging

from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

import hendler_command, callback, registration_user

from instance_bot import bot

# Логирование в релизной версии
# logging.basicConfig(filename='bot.log', level=logging.DEBUG,
#                     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Тестовое логирование
# logging.basicConfig(
#     filename='test_bot.log',
#     level=logging.DEBUG,
#     filemode='w',
#     format='%(levelname)s - %(asctime)s - %(name)s - %(message)s')

logging.basicConfig(level=logging.INFO)

logging.warning('Start logging')

# my_token = read_file()
# bot = Bot(token=my_token)
dp = Dispatcher()

async def main():
    await INIT_DB.initialize()

    dp.include_router(hendler_command.router)
    dp.include_router(callback.router)
    dp.include_router(registration_user.router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print(f"script interrupted: {datetime.now()}")
    except Exception as e:
        logging.error(f'Buuuuuuug: {e} ')
