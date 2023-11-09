from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove

from datetime import datetime
import logging

# from database import memory_bot
# from other import my_func


class FSMCommon(StatesGroup):

    first_state = State()
    mob_state = State()
    adress_state = State()
    order_state = State()

async def cmd_start(message: types.Message, state: FSMContext):
    await message.answer("Приветствуем вас в нашем ресторане!\n")
    await message.answer("Введите имя и фамилию")
    # await state.set_state(FSMCommon.mob_state.state)
    await FSMCommon.first_state.set()

async def name_input(message:types.Message, state: FSMContext):
    async with state.proxy() as datas:
        datas["Имя"] = message.text
    await message.answer("Очень приятно! Введите адрес")
    await FSMCommon.adress_state.set()

async def addres(message: types.Message,state: FSMContext):
    async with state.proxy() as datas:
        datas["Адрес"] = message.text
    await message.answer("Введите номер телефона (8**********)")
    await FSMCommon.mob_state.set()

async def mobile(message: types.Message, state: FSMContext):
    if not message.text.isnumeric() or len(message.text) != 11:
        await message.answer("Повторите ввод номера")
        return
    else:
        async with state.proxy() as datas:
            datas["Номер"] = message.text
        await message.answer("Данные сохранены. Что будете заказывать?")
        await FSMCommon.order_state.set()



async def order(message: types.Message, state: FSMContext):
    if message.text.lower() == "конец":
        async with state.proxy() as datas:
            result = datas
        await message.answer("Имя клиента:{name}\n Адрес:{adress}\n Номер:{number}\n Заказ:{order}".format(
            name = result.get("Имя"),
            adress = result.get("Адрес"),
            number = result.get("Номер"),
            order = ";".join(result.get("Заказ"))
            ))
        await state.finish()
    else:
        async with state.proxy() as datas:
            if datas.get("Заказ"):
                datas["Заказ"].append(message.text)
            else:
                datas["Заказ"] = [message.text]
        await message.answer("Еще один пункт добавлен. Напишите 'Конец'")











async def greetings(message: types.Message, state: FSMCommon):
    await message.answer(f"Очень приятно,{message.text}")
    await message.answer("Я умею пародировать речь")
    await FSMCommon.next()


async def echo(message: types.Message, state: FSMContext):
    await message.answer(message.text)
    await message.reply(message.text)


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands="start")
    dp.register_message_handler(name_input, state=FSMCommon.first_state)
    dp.register_message_handler(addres,state=FSMCommon.adress_state)
    dp.register_message_handler(mobile, state=FSMCommon.mob_state)
    dp.register_message_handler(order,state=FSMCommon.order_state)

