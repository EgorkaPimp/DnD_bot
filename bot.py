from datetime import datetime


from token_file import read_file
import asyncio
import logging

from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

# Логирование в релизной версии
# logging.basicConfig(filename='bot.log', level=logging.DEBUG,
#                     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Тестовое логирование

logging.basicConfig(level=logging.INFO)
my_token = read_file()

async def main():
    bot = Bot(token=my_token)
    dp = Dispatcher()


    from hendler_command import handlers_commands
    await handlers_commands(dp)

    await dp.start_polling(bot)



if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print(f"script interrupted: {datetime.now()}")
    except Exception as e:
        logging.error(f'Buuuuuuug: {e} ')
