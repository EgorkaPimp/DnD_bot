from aiogram import types

from inline_button_handler_commands import start_inline

async def  cmd_start(message: types.Message):
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