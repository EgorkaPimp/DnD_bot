import logging

from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram import types

from folder_class.ClassFilter import Router
from work_with_user.inline_user import setting_user_inline
from work_with_user.registration_user import reg_user_start

router = Router.router

@router.message(Command("register"))
async def cmd_register(message: types.Message, state: FSMContext):
    logging.warning(f'Enter command \\register')
    await reg_user_start(message.chat.id, state)

@router.message(Command('setting_user'))
async def cmd_setting_user(message: types.Message, state: FSMContext):
    logging.warning(f'Enter command \\setting_user')
    await message.answer('Что ты хочешь изменить?:',
                         parse_mode="Markdown",
                         reply_markup=setting_user_inline())