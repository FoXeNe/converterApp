import asyncio
import logging
import sys
import os

from values import CurrencyConverter
from aiogram import Bot, Dispatcher
import aiogram.utils.markdown as fmt
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TOKEN')

dp = Dispatcher()

bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

currency = CurrencyConverter()

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer("Что бы увидеть все команды напишите /help")

@dp.message(Command("help"))
async def help_handler(message: Message) -> None:
    await message.answer("Что бы увидеть курс валют напишите /check \nЧто бы увидеть все команды напишите /help")

@dp.message(Command("check"))
async def rate_handler(message: Message) -> None:
    curr = currency.check_currency_rate()
    await message.answer(f"Текущий курс валют: {curr}")

async def main() -> None:
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())