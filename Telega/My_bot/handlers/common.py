from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove

from datetime import datetime
import logging

from database import memory_bot
from other import my_func


class FSMCommon(StatesGroup):
    authorization = State()

async def cmd_start(message: types.Message, state: FSMContext):
    await state.reset_state(with_data=True)
    async with state.proxy() as data:
        data["id_telegram"] = message.from_user.id
        kb = InlineKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
        kb.insert(InlineKeyboardButton(text="Авторизоваться", callback_data="authorization"))
        await message.answer("Привет, {USERNAME}! Я буду помогать тебе с обучением.\n"
                             "Но, сначала мне нужно найти тебя в базе.\n"
                             "Нажми на кнопку ниже"
                             .format(USERNAME=message.from_user.first_name),
                             reply_markup=kb)
        await FSMCommon.authorization.set()

    await memory_bot.save_memory(state)



def register_handlers(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands="start", state="*")
    dp.register_message_handler(cmd_authorization, commands="authorization", state="*")
