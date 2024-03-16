import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command, CommandStart

logging.basicConfig(level=logging.INFO)

bot = Bot(token="7181531660:AAHdvp0J6kPdQK237ct0ySbjcB6QSTCv2ko")
dp = Dispatcher()

@dp.message(CommandStart())
async def cmd_start(message:types.Message):
    await message.answer("Проверка запущена")

# @dp.message(CommandStart())
# async def cmd_start(message:types.Message):
#     await message.answer("Проверка запущена")

async def main():
    await dp.start_polling((bot))

if __name__ == "__main__":
    asyncio.run(main())