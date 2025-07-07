import logging

from aiogram import types, Router
from aiogram.fsm.context import FSMContext

from ClassFilter import CallbackDataFilter
from registration_user import reg_user_start

router = Router()

@router.callback_query(CallbackDataFilter("reg"))
async def handle_like(callback: types.CallbackQuery, state: FSMContext):
    logging.warning(f'Pass button \\register')
    await callback.answer()
    await reg_user_start(callback.message.chat.id, state)



