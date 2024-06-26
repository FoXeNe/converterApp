import requests
import asyncio
import logging
import sys
import os
import time

from aiogram import Bot, Dispatcher, html
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.types import Message
from aiogram.filters import CommandStart
from os import getenv
from dotenv import load_dotenv
from bs4 import BeautifulSoup

load_dotenv()

TOKEN = os.getenv('TOKEN')

dp = Dispatcher()
class CurrencyConverter:
    url = f"https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D0%B0+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&oq=%D0%BA%D1%83%D1%80%D1%81+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D0%B0&gs_lcrp=EgZjaHJvbWUqEggBEAAYQxiDARixAxiABBiKBTISCAAQRRg5GIMBGLEDGMkDGIAEMhIIARAAGEMYgwEYsQMYgAQYigUyEAgCEAAYgwEYkgMYsQMYgAQyDQgDEAAYkgMYgAQYigUyDQgEEAAYgwEYsQMYgAQyEggFEAAYQxiDARixAxiABBiKBTINCAYQABiDARixAxiABDIHCAcQABiABDIGCAgQRRg90gEINDA2N2owajGoAgCwAgE&sourceid=chrome&ie=UTF-8"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"} # хиадер делает вид, что ты человек, что бы можно было сделать запрос. #!Без него не работает

    curr_conv_price = 0
    diff = 5

    def __init__(self):
        self.curr_conv_price = float(self.get_currency_rate())

    def get_currency_rate(self):
        fullPage = requests.get(self.url, headers=self.headers) # получаем страницу с конвертором валют

        soup = BeautifulSoup(fullPage.content, 'html.parser')# парсим содержимое страницы

        convert = soup.find("span", {"class": "DFlfde", "data-precision":"2"}) # находим и выводим цифру конвертации
        
        return convert.text
    

    def check_currency_rate(self):
        currency_str = self.get_currency_rate()
        print(f"Currency string: {currency_str}")
        currency = float(currency_str.replace(',', '.').replace(' ', ''))
        print(f"Currency value: {currency}")
        if currency >= self.curr_conv_price + self.diff:
            print("Курс валюты вырос!")
        elif currency <= self.curr_conv_price - self.diff:
            print("Курс валюты упал!")
        print(currency)
        time.sleep(3)
        self.check_currency_rate()
    # def check_currency_rate(self):
    #     currency = float(self.get_currency_rate().replace(',', '.'))  # заменяем запятую на точку для того, что бы было float)
    #     if currency >= self.curr_conv_price + self.diff:
    #         print("Курс валюты вырос!")
    #     elif currency <= self.curr_conv_price - self.diff:
    #         print("Курс валюты упал!")
    #     print(currency)
    #     time.sleep(3) 
    #     self.check_currency_rate()

currency = CurrencyConverter()
currency.check_currency_rate()

# @dp.message(CommandStart())
# async def command_start_handler(message: Message) -> None:
#     await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!")


# async def main() -> None:
#     # Initialize Bot instance with default bot properties which will be passed to all API calls
#     bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

#     # And the run events dispatching
#     await dp.start_polling(bot)

# if __name__ == "__main__":
#     logging.basicConfig(level=logging.INFO, stream=sys.stdout)
#     asyncio.run(main())