from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def setting_user_inline():
    inline_kb_list = [
        [InlineKeyboardButton(text="Изменить ник",
                              callback_data='change_nickname_user')],

        [InlineKeyboardButton(text="Удалить профиль",
                              callback_data='delete_user')],

        [InlineKeyboardButton(text="Посмотреть профиль",
                              callback_data='view_user')],

        [InlineKeyboardButton(text="Регистрация",
                              callback_data='reg')]
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_kb_list)