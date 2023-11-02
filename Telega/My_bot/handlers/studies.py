import os
from datetime import datetime
import pandas as pd
import asyncio

from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove

from handlers.common import variants_actions
from database import memory_bot
from other import my_func


class FSMStudies(StatesGroup):
    enter_family = State()
    enter_family_select_num = State()



async def enter_family(message: types.Message, state: FSMContext):
    pass


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(enter_family, state=FSMStudies.enter_family)
    dp.register_message_handler(enter_family_select_num, state=FSMStudies.enter_family_select_num)


