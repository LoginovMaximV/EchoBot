import asyncio

from aiogram import Bot, Dispatcher, types
bot_token = "6914233314:AAEmAT3VUzaNLd35NfMpgNDeJrphKHPj7CU"

bot = Bot(token=bot_token)
dp = Dispatcher()

@dp.message()
async def echo(message: types.Message):
    await message.answer(message.text)
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
