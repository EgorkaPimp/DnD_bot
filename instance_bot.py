from aiogram import Bot
from token_file import read_file

my_token = read_file()
bot = Bot(token=my_token)