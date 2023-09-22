from aiogram.utils.keyboard import InlineKeyboardBuilder
from callbacks import News
from parsing import parse

builder = InlineKeyboardBuilder()

def get_economy_keyboard():
    tmp_data = parse(
        "https://www.epravda.com.ua",
        [
            ".article__title > a",
            ".post__text > p",
        ],
    )

    for index, item in enumerate(tmp_data):
        builder.button(
            text=f"{item.get('header')}",
            callback_data=News(
                id = index,
                type = 'economy',
            ).pack(),
        )
    builder.adjust(
        1,
    )
    return builder.as_markup(), tmp_data
    