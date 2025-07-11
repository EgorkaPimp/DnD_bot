import logging
from aiogram.fsm.context import FSMContext

from inline_button_handler_commands import class_inline
# from instance_bot import bot

from folder_class.ClassFilter import Form, InstanceBot, Router

from aiogram import types

router = Router.router

async def start_create_character(chat: int, state: FSMContext):
    await InstanceBot.bot.send_message(chat_id=chat,
                                       text="Для начала придумай Имя персонажа:\n"
                                "_Не переживай его можно будет сменить_👌🏿",
                                       parse_mode="Markdown")
    await state.set_state(Form.waiting_for_name_character)

@router.message(Form.waiting_for_name_character)
async def get_nickname(message: types.Message, state: FSMContext):
    logging.warning(f'Input nickname_character {message.text}')
    await state.clear()
    await message.answer(f'Твоего персонажа зовут '
                         f'_{message.text.capitalize()}_\n\n'
                         f'Теперь выбери *Класс*'
                         ,parse_mode="Markdown")
    await message.answer("Классы:",
                         reply_markup=class_inline())
