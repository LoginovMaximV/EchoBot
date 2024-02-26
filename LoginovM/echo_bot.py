import asyncio, os
from aiogram import Bot, Dispatcher, types
from dotenv import load_dotenv

load_dotenv()
bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher()

@dp.message()
async def echo(message: types.Message):
    await message.answer(message.text)
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
