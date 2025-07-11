import logging

from aiogram.fsm.context import FSMContext
from aiogram import types
from selenium.webdriver.common.devtools.v137.runtime import await_promise

from folder_class.ClassFilter import InstanceBot, Form
from work_with_user.user_db import view_user_for_db, delete_user_for_db, update_nick_user, check_id_in_db


async def change_nickname_user(chat: int, state: FSMContext):
    if await view_user_for_db(chat):
        await InstanceBot.bot.send_message(chat_id=chat,
                                       text="Введи новый ник:")
        await state.set_state(Form.waiting_for_new_nickname)
    else:
        await InstanceBot.bot.send_message(chat_id=chat,
                                           text='Прости но ты не зарегистрирован')

async def delete_user(chat: int):
    if await check_id_in_db(chat):
        await delete_user_for_db(chat)
        await InstanceBot.bot.send_message(chat_id=chat,
                                           text='Все, теперь ты мне незнаком')
    else:
        await InstanceBot.bot.send_message(chat_id=chat,
                                           text='Я о тебе ничего не знаю, ты наверное не зарегистрирован')

async def view_user(chat: int):
    user_info = await view_user_for_db(chat)
    if user_info is None:
        logging.warning('View empty user_id')
        await InstanceBot.bot.send_message(chat_id=chat,
                                           text="Странно но я ничего о тебе не знаю")
    else:
        logging.warning(f'User information received from DB {user_info}')
        await InstanceBot.bot.send_message(chat_id=chat,
                                       text="Вот вся информация что у меня на тебя есть)\n"
                                            f"Твое имя = {user_info['name']}\n"
                                            f"Твой ник = {user_info['nick_name'].capitalize()}\n"
                                            f"Дата регистрации = {user_info['date']}")

async def update_nick(chat: int, message: types.Message):
    await update_nick_user(chat, message.text)
    await InstanceBot.bot.send_message(chat_id=chat,
                                 text='Теперь твой ник: \n'
                                      f'_{message.text.capitalize()}_',
                                 parse_mode="Markdown")

