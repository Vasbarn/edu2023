from aiogram.utils import executor
from aiogram.types import BotCommand
import logging
from my_bot import dp
from handlers import commands


logging.basicConfig(level=logging.INFO)


async def on_startup(_):
    logging.info("My_shop is starting...")
    commands = [
        BotCommand(command="auth", description="Авторизация"),
        BotCommand(command="balance", description="Баланс счета"),
        BotCommand(command="add_money", description="Пополнить баланс"),
        BotCommand(command="volley", description="Корзина")
        ]
    await dp.bot.set_my_commands(commands)

commands.register_handlers(dp)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=False, on_startup=on_startup)