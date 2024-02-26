import asyncio
import logging

from aiogram import Bot
from aiogram import Dispatcher
from aiogram import types

TOKEN_API = "6759079115:AAE-kX1cWhlMPzZhWj5LIPnIANkrs_0UTRc"

bot = Bot(token=TOKEN_API)
dp = Dispatcher()

@dp.message()
async def echo_message(message: types.Message):
    await message.answer(text=message.text)

async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
