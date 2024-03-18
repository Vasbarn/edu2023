from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage


storage = MemoryStorage
bot = Bot(token="7181531660:AAHdvp0J6kPdQK237ct0ySbjcB6QSTCv2ko")
dp = Dispatcher(bot, storage=storage())