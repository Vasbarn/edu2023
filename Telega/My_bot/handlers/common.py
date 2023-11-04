from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove

from datetime import datetime
import logging

from database import memory_bot
from other import my_func


class FSMCommon(StatesGroup):

    first_state = State()

async def cmd_start(message: types.Message, state: FSMContext):
    await message.answer("Приветствую вас!\n У нас самые низкие цены!")
    await message.answer("Как тебя зовут?")

    await FSMCommon.first_state.set()

async def greetings(message: types.Message, state: FSMContext):
    await message.answer(f"Очень приятно,{message.text}")
    await message.answer("Я умею пародировать речь")
    await FSMCommon.next()


async def echo(message: types.Message, state: FSMContext):
    await message.answer(message.text)
    await message.reply(message.text)


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands="start")
    dp.register_message_handler(greetings, state=FSMCommon.first_state)

    dp.register_message_handler(echo)

    # dp.register_message_handler(cmd_authorization, commands="authorization", state="*")
