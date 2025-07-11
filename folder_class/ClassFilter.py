from aiogram.filters import Filter
from aiogram.types import CallbackQuery
from aiogram.fsm.state import State, StatesGroup
from aiogram import Bot
from token_file import read_file
from aiogram import Router

class InstanceBot:
    my_token = read_file()
    bot = Bot(token=my_token)

class CallbackDataFilter(Filter):
    def __init__(self, data: str) -> None:
        self.data = data

    async def __call__(self, callback: CallbackQuery) -> bool:
        return callback.data == self.data

class Form(StatesGroup):
    waiting_for_nickname = State()
    waiting_for_name_character = State()
    waiting_for_new_nickname = State()

class Router:
    router = Router()
