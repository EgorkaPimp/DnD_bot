import logging

from aiogram.filters import Command
from aiogram import Router
from aiogram.types import Message
from aiogram import types

from inline_button_handler_commands import start_inline
from registration_user import reg_user_start

router = Router()

@router.message(Command("start"))
async def  cmd_start(message: types.Message):
    logging.warning(f'Enter command \\start')
    user_name = message.from_user.first_name
    user_last_name = message.from_user.last_name
    await message.answer(f'**Привет _{user_name} {user_last_name}!_**\n'
                         f'Меня зовут *Pimp* и это мой бот, он сделает мир ДнД проще.\n'
                         f'Если найдешь баг не стесняйся написать о нем на *GIT*!\n\n'
                         f'Не мог бы ты *зарегистрироваться?*\n\n'
                         f'Для этого нажми 👇🏻\n'
                         f'\n',
                         parse_mode="Markdown",
                         reply_markup=start_inline()
                         )

@router.message(Command("register"))
async def cmd_register(message: types.Message):
    logging.warning(f'Enter command \\register')
    await reg_user_start(message.chat.id)

