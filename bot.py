import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from aiogram import F
from aiogram.utils.markdown import hbold
from parsing import parse
from callbacks import News

# from utils.set_commands import set_default_commands
from keyboards import (
    what_to_read,
    get_economy_keyboard,
    get_political_keyboard,
)

data = {
    "economy": [],
    "political": [],
}
# Bot token can be obtained via https://t.me/BotFather
TOKEN = "6166859922:AAHTelA_UwYNMc9-BCL8vcwWf4cMViu4IKc"

# All handlers should be attached to the Router (or Dispatcher)
dp = Dispatcher()
# set_default_commands(dp)


@dp.message(CommandStart())
async def command_start(message: Message) -> None:
    await message.answer(f"Hello, {hbold(message.from_user.full_name)}!")


@dp.message(Command(commands="whattoread"))
async def command_whattoread(message: Message) -> None:
    await message.answer("Виберіть тип новин", reply_markup=what_to_read)


@dp.message(Command(commands="randomtopic"))
async def command_randomtopic(message: Message) -> None:
    await message.answer("Виберіть тип новин", reply_markup=what_to_read)


@dp.message(F.text == "Економічні новини")
async def economy_news(message: Message) -> None:
    kb, data["economy"] = get_economy_keyboard()
    await message.answer("Виберіть новину", reply_markup= kb)


@dp.message(F.text == "Політичні новини")
async def political_news(message: Message) -> None:
    await message.answer("Виберіть новину", reply_markup=get_political_keyboard())


@dp.callback_query(News.filter(F.type == "political"))
async def show_political_article(query: CallbackQuery, callback_data: News):
    await query.answer(str(callback_data.id))


@dp.callback_query(News.filter(F.type == "economy"))
async def show_economy_article(query: CallbackQuery, callback_data: News):
    await query.answer(str(callback_data.id))


async def main() -> None:
    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)

    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
