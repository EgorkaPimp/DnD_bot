from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def start_inline():
    inline_kb_list = [
        [InlineKeyboardButton(text="Регистрация",
                              callback_data='reg')],

        [InlineKeyboardButton(text="My_Git 😺",
                              url='https://github.com/EgorkaPimp/DnD_bot')]
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_kb_list)

def class_inline():
    inline_kb_list = [
        [InlineKeyboardButton(text="Бард",
                              callback_data='reg')],

        [InlineKeyboardButton(text="My_Git 😺",
                              url='https://github.com/EgorkaPimp/DnD_bot')]
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_kb_list)