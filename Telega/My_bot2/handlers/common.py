from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


import datetime
import logging
import requests
from bs4 import BeautifulSoup

slovar = {}
def values(dictionary: dict):
    url = "https://finance.rambler.ru/currencies/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")
    ten_val = soup.find("a", title="Казахских тенге")
    dol_val = soup.find("a", title="Доллар США")
    eur_val = soup.find("a", title="Евро")
    ju_val = soup.find("a", title="Китайских юаней")
    tenge_val = ten_val.find("div",
                             class_="finance-currency-table__cell finance-currency-table__cell--value").text.strip()
    dollar_val = dol_val.find("div",
                             class_="finance-currency-table__cell finance-currency-table__cell--value").text.strip()
    euro_val = eur_val.find("div",
                             class_="finance-currency-table__cell finance-currency-table__cell--value").text.strip()
    juang_val = ju_val.find("div",
                             class_="finance-currency-table__cell finance-currency-table__cell--value").text.strip()

    dictionary["Тенге"] = round(float(tenge_val)/100, 4)
    dictionary["Доллар"] = float(dollar_val)
    dictionary["Евро"] = float(euro_val)
    dictionary["Юань"] = float(juang_val) / 10

values(slovar)
class FSMCommon(StatesGroup):
    chose_state = State()
    get_val_state = State()
    convert_state = State()
    rub_change_state = State()
    other_change_state = State()
async def cmd_start(message: types.Message, state: FSMContext):
    values(slovar)
    await message.answer("Привет! Я бот-валютчик.\n Я умею парсить курсы валют. Выберите действие:")
    kb = ReplyKeyboardMarkup(row_width=2)
    kb.insert(KeyboardButton(text="Хочу узнать курс"))
    kb.insert(KeyboardButton(text="Хочу конвертировать валюту"))
    await message.answer("Выберите действие:",reply_markup=kb)
    await FSMCommon.chose_state.set()

async def chose_func(message: types.Message, state: FSMContext):
    print("fuck you")
    if message.text == "Хочу узнать курс":
        rb = ReplyKeyboardMarkup(row_width=2)
        rb.insert(KeyboardButton(text="Евро"))
        rb.insert(KeyboardButton(text="Доллар"))
        rb.insert(KeyboardButton(text="Тенге"))
        rb.insert(KeyboardButton(text="Юань"))
        await message.answer("Выберите нужную валюту", reply_markup=rb)
        await FSMCommon.get_val_state.set()
    elif message.text == "Хочу конвертировать валюту":
        convert_kb = ReplyKeyboardMarkup(row_width=2)
        convert_kb.insert(KeyboardButton(text="Рубль -> Доллар"))
        convert_kb.insert(KeyboardButton(text="Доллар -> Рубль"))
        convert_kb.insert(KeyboardButton(text="Рубль -> Евро"))
        convert_kb.insert(KeyboardButton(text="Евро -> Рубль"))
        convert_kb.insert(KeyboardButton(text="Рубль -> Юань"))
        convert_kb.insert(KeyboardButton(text="Юань -> Рубль"))
        convert_kb.insert(KeyboardButton(text="Рубль -> Тенге"))
        convert_kb.insert(KeyboardButton(text="Тенге -> Рубль"))
        await message.answer("Выберите способ конвертации", reply_markup=convert_kb)
        await FSMCommon.convert_state.set()
async def get_val(message: types.Message, state: FSMContext):
    dt = datetime.date.today()
    if message.text == "Евро":
        await message.answer(f"На {dt} курс евро составляет {slovar['Евро']} рублей")
    elif message.text == "Доллар":
        await message.answer(f"На {dt} курс доллара составляет {slovar['Доллар']} рублей")
    elif message.text == "Юань":
        await message.answer(f"На {dt} курс юаня составляет {slovar['Юань']} рублей")
    elif message.text == "Тенге":
        await message.answer(f"На {dt} курс тенге составляет {slovar['Тенге']} рублей")

async def convert_val(message: types.Message, state: FSMContext):
    async with state.proxy() as dataset:
        for i in range(4):
            key = list(slovar.keys())[i]
            if message.text == f"Рубль -> {key}":
                dataset["Выбранная валюта"] = key
                await message.answer("Введите желаемую сумму для конвертации")
                await FSMCommon.rub_change_state.set()
            elif message.text == f"{key} -> Рубль":
                dataset["Выбранная валюта"] = key
                await message.answer("Введите желаемую сумму для конвертации")
                await FSMCommon.other_change_state.set()

async def rub_change(message: types.Message, state: FSMContext):
    async with state.proxy() as dataset:
        summa = int(message.text)
        await message.answer(f'{summa} рублей = {round(summa/slovar[dataset["Выбранная валюта"]], 3)} '
                         f'{dataset["Выбранная валюта"]}')
        kb = ReplyKeyboardMarkup(row_width=2)
        kb.insert(KeyboardButton(text="Хочу узнать курс"))
        kb.insert(KeyboardButton(text="Хочу конвертировать валюту"))
        await message.answer("Выберите действие:", reply_markup=kb)
        await FSMCommon.chose_state.set()

async def other_change(message: types.Message, state: FSMContext):
    async with state.proxy() as dataset:
        summa = int(message.text)
        await message.answer(f'{summa} {dataset["Выбранная валюта"]} ='
                             f' {round(summa*slovar[dataset["Выбранная валюта"]], 3)} рублей')
        kb = ReplyKeyboardMarkup(row_width=2)
        kb.insert(KeyboardButton(text="Хочу узнать курс"))
        kb.insert(KeyboardButton(text="Хочу конвертировать валюту"))
        await message.answer("Выберите действие:", reply_markup=kb)
        await FSMCommon.chose_state.set()
def register_handlers(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands = "start", state="*")
    dp.register_message_handler(chose_func, state=FSMCommon.chose_state)
    dp.register_message_handler(get_val, state=FSMCommon.get_val_state)
    dp.register_message_handler(convert_val, state=FSMCommon.convert_state)
    dp.register_message_handler(rub_change, state=FSMCommon.rub_change_state)
    dp.register_message_handler(other_change, state=FSMCommon.other_change_state)








