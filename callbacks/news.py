from aiogram.filters.callback_data import CallbackData


class News(CallbackData, prefix="my"):
    id: int
    type: str