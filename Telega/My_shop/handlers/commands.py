from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from keyboards.kb import kb_auth, kb_act, kb_yn, get_kb_buy, save_memory
from aiogram.types import InputFile
import json

class FSMCommands(StatesGroup):
    name_state = State()
    surname_state = State()
    num_state = State()
    action_state = State()
    confirm_state = State()
    sum_state = State()
    check_bal_state = State()
    add_bal_state = State()
    cat_state = State()
    add_bask_state = State()
    bask_state = State()
    chugun_state = State()
    alum_state = State()
    electro_state = State()

async def start(message: types.Message, state: FSMContext):
    async with state.proxy() as datas:
        chugun = InputFile(r"C:\Users\Admin\PycharmProjects\edu2023\Telega\чугун.jpg")
        alum = InputFile(r"C:\Users\Admin\PycharmProjects\edu2023\Telega\люминь.jpg")
        electro = InputFile(r"C:\Users\Admin\PycharmProjects\edu2023\Telega\электро.jpg")
        datas["Колво"] = 0
        datas["Корзина"] = dict()
        # datas["Каталог"] = ["Батарея чугунная", "Батарея алюминиевая", "Батарея электрическая"]
        # datas["Фото"] = [chugun, alum, electro]
    await message.answer("Приветствуем в лучшем магазине батарей!!")
    await message.answer("Вам нужно", reply_markup=kb_auth)
    await save_memory(message, state)
async def query_auth(query: types.CallbackQuery, state: FSMContext):
    await query.message.answer("Введите имя")
    await FSMCommands.name_state.set()
    

async def name_check(message: types.Message, state: FSMContext):
    async with state.proxy() as datas:
        datas["Имя"] = message.text
    await message.answer("Введите Фамилию")
    await FSMCommands.surname_state.set()
    await save_memory(message, state)

async def surname_check(message: types.Message, state: FSMContext):
    async with state.proxy() as datas:
        datas["Фамилия"] = message.text
    await message.answer("Введите номер телефона (8**********")
    await FSMCommands.num_state.set()
    await save_memory(message, state)

async def num_check(message: types.Message, state: FSMContext):
    if message.text.isnumeric() and message.text.startswith("8") and len(message.text) == 11:
        async with state.proxy() as datas:
            datas["Номер"] = message.text
        await message.answer("Вы успешно авторизовались", reply_markup=kb_act)
        await FSMCommands.action_state.set()
    else:
        await message.answer("Неверный номер. Повторите ввод")
        return
    await save_memory(message, state)
async def actions(query: types.CallbackQuery, state: FSMContext):
    if query.data == "balance":
        await check_balance(query.message, state)
    elif query.data == "add":
        await add_balance(query.message, state)
    elif query.data == "catalog":
        await catalog(query.message, state)
    elif query.data == "basket":
        await basket_info(query, state)
    
async def check_balance(message: types.Message, state: FSMContext):
    async with state.proxy() as datas:
        if datas.get("Сумма"):
            await message.answer(f"Ваш баланс:  {datas.get('Сумма')} рублей")
        else:
            await message.answer("Ваш баланс составляет 0 рублей")
    await save_memory(message, state)

async def add_balance(message: types.Message, state: FSMContext):
    await message.answer("Введите желаемую сумму для пополнения")
    await FSMCommands.confirm_state.set()
    await save_memory(message, state)

async def confirm(message: types.Message, state: FSMContext):
    if message.text.isnumeric:
        async with state.proxy() as datas:
            datas["Пополнение"] = int(message.text)
        await message.answer("Пополнить?", reply_markup=kb_yn)
    else:
        await message.answer("Повторите ввод")
        return
    await FSMCommands.sum_state.set()
    await save_memory(message, state)

async def sum_act(query: types.CallbackQuery, state: FSMContext):
    if query.data == "yes":
        async with state.proxy() as datas:
            if datas.get("Сумма"):
                datas["Сумма"] +=  datas["Пополнение"]
            else:
                datas["Сумма"] = datas["Пополнение"]

        await query.message.answer("Счет успешно пополнен", reply_markup=kb_act)
    else:
        await query.message.answer("Выберите действие", reply_markup=kb_act)
    await FSMCommands.action_state.set()
    

async def catalog(message: types.Message, state: FSMContext):
    chugun = open("C:\\Users\\Admin\\PycharmProjects\\edu2023\\Telega\\чугун.jpg", "rb")
    alum = open("C:\\Users\\Admin\\PycharmProjects\\edu2023\\Telega\\люминь.jpg", "rb")
    electro = open("C:\\Users\\Admin\\PycharmProjects\\edu2023\\Telega\\электро.jpg", "rb")
    await message.answer_photo(chugun, caption="Батарея чугунная",reply_markup=get_kb_buy(1))
    await message.answer_photo(alum, caption="Батарея алюминиевая", reply_markup=get_kb_buy(2))
    await message.answer_photo(electro, caption="Батарея электрическая", reply_markup=get_kb_buy(3))
    await save_memory(message, state)


async def test(query: types.CallbackQuery, state: FSMContext):
    await query.message.answer(query.data)
async def add_tovar(query: types.CallbackQuery, state: FSMContext):
    await query.answer("Принято")
    print(1)
    async with state.proxy() as datas:
        await query.message.answer(query.data)
        if query.data.endswith("1"):
            print(2)
            if query.data.startswith("add"):
                if datas.get("Корзина").get("Чугунная батарея"):
                    datas["Корзина"]["Чугунная батарея"] += 1
                else:
                    datas["Корзина"]["Чугунная батарея"] = 1
            else:
                if datas.get("Корзина").get("Чугунная батарея"):
                    if datas["Корзина"]["Чугунная батарея"] > 1:
                        datas["Корзина"]["Чугунная батарея"] -= 1
                    else:
                        datas["Корзина"].pop("Чугунная батарея")

        elif query.data.endswith("2"):
            if query.data.startswith("add"):
                if datas.get("Корзина").get("Алюминиевая батарея"):
                    datas["Корзина"]["Алюминиевая батарея"] += 1
                else:
                    datas["Корзина"]["Алюминиевая батарея"] = 1
            else:
                if datas.get("Корзина").get("Алюминиевая батарея"):
                    if datas["Корзина"]["Алюминиевая батарея"] > 1:
                        datas["Корзина"]["Алюминиевая батарея"] -= 1
                    else:
                        datas["Корзина"].pop("Алюминиевая батарея")

        elif query.data.endswith("3"):
            if query.data.startswith("add"):
                if datas.get("Корзина").get("Электрическая батарея"):
                    datas["Корзина"]["Электрическая батарея"] += 1
                else:
                    datas["Корзина"]["Электрическая батарея"] = 1
            else:
                if datas.get("Корзина").get("Электрическая батарея"):
                    if datas["Корзина"]["Электрическая батарея"] > 1:
                        datas["Корзина"]["Электрическая батарея"] -= 1
                    else:
                        datas["Корзина"].pop("Электрическая батарея")
    

async def basket_info(query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as datas:
        if datas.get("Корзина"):
            await query.message.answer("В вашей корзине содержится")
            for key, value in datas["Корзина"].items():
                await query.message.answer(f"{key} = {value} шт")
    









def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start, commands="start", state="*")
    dp.register_message_handler(catalog, commands="catalog", state="*")
    dp.register_callback_query_handler(query_auth,
                                       lambda callback: callback.data == "authorization",
                                       state="*")


    dp.register_message_handler(confirm, state=FSMCommands.confirm_state)
    dp.register_callback_query_handler(sum_act, state=FSMCommands.sum_state)
    dp.register_message_handler(name_check, state=FSMCommands.name_state)
    dp.register_message_handler(surname_check, state=FSMCommands.surname_state)
    dp.register_message_handler(num_check, state=FSMCommands.num_state)
    dp.register_callback_query_handler(add_tovar, lambda callback: callback.data.startswith("add") or
                                                                   callback.data.startswith("del"), state="*" )
    dp.register_callback_query_handler(actions, state=FSMCommands.action_state)