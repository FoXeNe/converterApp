import asyncio
import aioschedule
import logging
import sys
import os

from keyboards import greet_kb
from values import CurrencyConverter

from datetime import datetime
from aiogram import Bot, Dispatcher
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
    await message.answer("Что бы увидеть курс валют напишите /check \nЧто бы увидеть все команды напишите /help \nЕсли хотите узнать, как поменяется валюта в определенное время /wait")

@dp.message(Command("check"))
async def rate_handler(message: Message) -> None:
    curr = currency.check_currency_rate()
    await message.answer(f"Текущий курс валют: {curr}")

@dp.message(Command("wait"))
async def wait_handler(message: Message) -> None:
    await message.reply("Во сколько ты хочешь получить уведомление об курсе валют?", reply_markup=greet_kb)
    if message.text == "00":
        if datetime.now() == "00":
            rate_handler(message)
    elif message.text == "12":
        if datetime.now() == "12":
            rate_handler(message)
    elif message.text == "15":
        if datetime.now() == "15":
            rate_handler(message)
    elif message.text == "18":
        if datetime.now() == "18":
            rate_handler(message)
    elif message.text == "21":
        if datetime.now() == "21":
            rate_handler(message)
        

async def main() -> None:
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())