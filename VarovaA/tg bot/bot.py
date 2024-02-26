import logging

from aiogram import Bot, types, Dispatcher
import asyncio

from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message()
async def echo_message(msg: types.Message):
    await msg.answer(text=msg.text)

async def main():
    logging.basicConfig(level=logging.DEBUG)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())