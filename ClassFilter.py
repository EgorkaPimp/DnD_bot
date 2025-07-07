from aiogram.filters import Filter
from aiogram.types import CallbackQuery
from aiogram.fsm.state import State, StatesGroup

class CallbackDataFilter(Filter):
    def __init__(self, data: str) -> None:
        self.data = data

    async def __call__(self, callback: CallbackQuery) -> bool:
        return callback.data == self.data

class Form(StatesGroup):
    waiting_for_nickname = State()
    waiting_for_name_character = State()
