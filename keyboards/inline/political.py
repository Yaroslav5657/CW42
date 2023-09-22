from aiogram.utils.keyboard import InlineKeyboardBuilder
from parsing import parse
from callbacks import News

builder = InlineKeyboardBuilder()


def get_political_keyboard():
    tmp_data = parse(
        "https://www.pravda.com.ua",
        [
            ".article_header > a",
            ".post__text > p",
        ],
    )

    for index, item in enumerate(tmp_data):
        builder.button(
            text=f"{item.get('header')}",
            callback_data=News(
                id = index,
                type = 'political',
            ).pack(),
        )
    builder.adjust(
        1,
    )
    return builder.as_markup(), tmp_data