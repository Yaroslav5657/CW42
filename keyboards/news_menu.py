from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

what_to_read = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text = "Політичні новини"),
            KeyboardButton(text = "Економічні новини"),
        ]
    ],
    one_time_keyboard=True,
)