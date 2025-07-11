from datetime import datetime

from folder_class.InitDBClass import INIT_DB
import asyncio
import logging

from aiogram import Dispatcher

import hendler_command,\
    callback,\
    work_with_user.handler_user,\
    work_with_user.callback_user,\
    work_with_user.registration_user,\
    create_character


from folder_class.ClassFilter import InstanceBot, Router



# Логирование в релизной версии
# logging.basicConfig(filename='bot.log', level=logging.DEBUG,
#                     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(asctime)s - %(name)s - %(message)s')

logging.warning('Start logging')

dp = Dispatcher()

async def main():
    await INIT_DB.initialize()

    dp.include_router(Router.router)

    await dp.start_polling(InstanceBot.bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print(f"script interrupted: {datetime.now()}")
    except Exception as e:
        logging.error(f'Buuuuuuug: {e} ')
