from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage


storage = MemoryStorage
bot = Bot(token="6788084073:AAF9ORVReWI9G1r2bMWrkJ0tdaY_YUWuIkY")
dp = Dispatcher(bot, storage=storage())
