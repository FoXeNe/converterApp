from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

greet_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="12"),
            KeyboardButton(text="15"),
            KeyboardButton(text="18"),
            KeyboardButton(text="21"),
            KeyboardButton(text="00")
        ],
    ],
    resize_keyboard=True,
)