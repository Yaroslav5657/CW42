from aiogram import types, Dispatcher


async def set_default_commands(dp: Dispatcher):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Запуск бота"),
            types.BotCommand("help", "Допомога"),
            types.BotCommand("whattoread", "Обрати новини"),
            types.BotCommand("randomtopic", "Випадкова новина"),
            
        ]
    )