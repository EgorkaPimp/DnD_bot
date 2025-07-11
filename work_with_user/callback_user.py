import logging

from folder_class.ClassFilter import CallbackDataFilter, Router

from aiogram import types
from aiogram.fsm.context import FSMContext

from work_with_user.setting_user import change_nickname_user, delete_user, view_user

router = Router.router

@router.callback_query(CallbackDataFilter("change_nickname_user"))
async def handle_like(callback: types.CallbackQuery, state: FSMContext):
    logging.warning(f'Pass button \\change_nickname_user')
    await callback.answer()
    await change_nickname_user(callback.message.chat.id, state)

@router.callback_query(CallbackDataFilter("delete_user"))
async def handle_like(callback: types.CallbackQuery, state: FSMContext):
    logging.warning(f'Pass button \\delete_user')
    await callback.answer()
    await delete_user(callback.message.chat.id)

@router.callback_query(CallbackDataFilter("view_user"))
async def handle_like(callback: types.CallbackQuery, state: FSMContext):
    logging.warning(f'Pass button \\view_user')
    await callback.answer()
    await view_user(callback.message.chat.id)