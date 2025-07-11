import logging

from aiogram import types, Router
from aiogram.fsm.context import FSMContext

from folder_class.ClassFilter import CallbackDataFilter, Router, Form
from work_with_user.registration_user import reg_user_start
from work_with_user.setting_user import update_nick

router = Router.router

@router.callback_query(CallbackDataFilter("reg"))
async def handle_like(callback: types.CallbackQuery, state: FSMContext):
    logging.warning(f'Pass button \\register')
    await callback.answer()
    await reg_user_start(callback.message.chat.id, state)

@router.message(Form.waiting_for_new_nickname)
async def handle_like(message: types.Message):
    logging.warning(f'Input nickname {message.text}')
    await update_nick(message.chat.id, message)
