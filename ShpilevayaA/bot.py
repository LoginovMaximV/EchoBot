import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import CommandStart
bot = Bot(token='7181340336:AAHdYWdrP7Bws6Tk7Y2HErzKxOZJL7T4hr0')

dp = Dispatcher()

@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer("Я повторю любое ваше сообщение")

@dp.message()
async def repeat_text(message: types.Message):
    await message.answer(message.text)
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
