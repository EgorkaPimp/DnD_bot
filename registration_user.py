import logging
import datetime
from aiohttp.web_middlewares import middleware

from db_postgres.add_value_in_db import add_user_in_db
from instance_bot import bot

from ClassFilter import Form

from aiogram.filters import Command
from aiogram import types, Router
from aiogram.fsm.context import FSMContext

router = Router()

async def reg_user_start(chat: int, state: FSMContext):
    await bot.send_message(chat_id=chat,
                           text="Настало время познакомится\n"
                                "Придумай себе никнейм:")
    await state.set_state(Form.waiting_for_nickname)

@router.message(Form.waiting_for_nickname)
async def get_nickname(message: types.Message, state: FSMContext):
    logging.warning(f'Input nickname {message.text}')
    await message.answer(f'Спасибо, теперь я буду называть тебя '
                         f'_{message.text.capitalize()}_'
                         ,parse_mode="Markdown")
    await state.clear()
    await add_user_in_db(message.chat.id,
                         message.text.lower(),
                         message.chat.first_name,
                         datetime.datetime.now().strftime("%Y.%m.%d"))

