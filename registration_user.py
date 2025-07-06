import logging

from aiohttp.web_middlewares import middleware

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
    await state.update_data(nickname_user=message.text)
    data = await state.get_data()
    await message.answer(f'Спасибо теперь я буду называть тебя '
                         f'_{data['nickname_user'].capitalize()}_'
                         ,parse_mode="Markdown"
                         )
    await state.clear()













    # Пример
    # @dp.message(Form.waiting_for_age)
    # async def process_age(message: types.Message, state: FSMContext):
    #     await state.update_data(age=message.text)
    #     data = await state.get_data()
    #     await message.answer(f"Тебя зовут {data['name']}, тебе {data['age']} лет.")
    #     await state.clear()  # Завершаем диалог