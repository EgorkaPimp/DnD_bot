import logging

from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram import types

from folder_class.ClassFilter import Router
from create_character import start_create_character
from inline_button_handler_commands import start_inline

router = Router.router

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

@router.message(Command("create_character"))
async def cmd_register(message: types.Message, state: FSMContext):
    logging.warning(f'Enter command \\create_character')
    await start_create_character(message.chat.id, state)

@router.message(Command("set"))
async def cmd_set(message: types.Message):
    await message.answer('123123123')