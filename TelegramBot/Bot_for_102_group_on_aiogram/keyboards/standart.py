from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='/reg')
        ]
    ],
    resize_keyboard=True
)

help_a = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='/reg'),
            KeyboardButton(text='/add_link'),

        ],
        [
            KeyboardButton(text='/link'),
            KeyboardButton(text='/make_homework'),
        ],
        [
            KeyboardButton(text='/send_all'),
            KeyboardButton(text='/homework')
        ],
        [
            KeyboardButton(text='/add_new_admin')
        ]
    ],
    resize_keyboard=True
)

help_u = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='/reg'),
            KeyboardButton(text='/stop'),

        ],
        [
            KeyboardButton(text='/link'),
            KeyboardButton(text='/homework'),
        ]
    ],
    resize_keyboard=True
)

key_help = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='/help')
        ]
    ],
    resize_keyboard=True
)

