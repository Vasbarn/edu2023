from aiogram.utils import executor
from aiogram.types import BotCommand
import logging
from my_bot import dp
from handlers import body_of_bot


logging.basicConfig(level=logging.INFO)


async def on_startup(_):
    logging.info("My_shop is starting...")
    commands = [
        BotCommand(command="start", description="Начало")
        ]
    await dp.bot.set_my_commands(body_of_bot)
body_of_bot.register_handlers(dp)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=False, on_startup=on_startup)