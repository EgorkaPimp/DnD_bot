import logging
import datetime

from db_postgres.add_value_in_db import add_user_in_db

from folder_class.ClassFilter import Form, InstanceBot, Router

from aiogram import types
from aiogram.fsm.context import FSMContext

from work_with_user.user_db import check_id_in_db, search_for_a_nickname_by_id

router = Router.router

async def reg_user_start(chat: int, state: FSMContext):
    if not await check_id_in_db(chat):
        await InstanceBot.bot.send_message(chat_id=chat,
                                           text="Настало время познакомится\n"
                                    "Придумай себе никнейм:")
        await state.set_state(Form.waiting_for_nickname)
    else:
        logging.warning(f'User {chat} already created')
        nickname = await search_for_a_nickname_by_id(chat)
        await InstanceBot.bot.send_message(chat_id=chat,
                             text='Вы уже зарегистрированы:\n\n'
                             f'Ваш ник _{nickname}_\n\n'
                             f'Для изменения ника введите "/setting\_user"',
                             parse_mode="Markdown")


@router.message(Form.waiting_for_nickname)
async def get_nickname(message: types.Message, state: FSMContext):
    logging.warning(f'Input nickname {message.text}')
    await state.clear()
    await add_user_in_db(message.chat.id,
                     message.text.lower(),
                     message.chat.first_name,
                     datetime.datetime.now().strftime("%Y.%m.%d"))
    await message.answer(f'Спасибо, теперь я буду называть тебя '
                         f'_{message.text.capitalize()}_'
                         , parse_mode="Markdown")


