from aiogram import Bot, Dispatcher, types
import asyncio


BOT = Bot(token="6975949398:AAFdx2pllQWhIIR9dSMfCjKVf_WImO2Urfw")

dp = Dispatcher()

@dp.message()
async def echo(message: types.Message):
    await message.answer(message.text)

async def main():
    await dp.start_polling(BOT)
asyncio.run(main())


