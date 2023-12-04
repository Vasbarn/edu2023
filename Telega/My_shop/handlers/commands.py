from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from keyboards.kb import kb_auth, kb_act, kb_yn, kb_buy
from aiogram.types import InputFile


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
        datas["Корзина"] = []
        # datas["Каталог"] = ["Батарея чугунная", "Батарея алюминиевая", "Батарея электрическая"]
        datas["Фото"] = [chugun, alum, electro]
    await message.answer("Приветствуем в лучшем магазине батарей!!")
    await message.answer("Вам нужно", reply_markup=kb_auth)

async def query_auth(query: types.CallbackQuery, state: FSMContext):
    await query.message.answer("Введите имя")
    await FSMCommands.name_state.set()

async def name_check(message: types.Message, state: FSMContext):
    async with state.proxy() as datas:
        datas["Имя"] = message.text
    await message.answer("Введите Фамилию")
    await FSMCommands.surname_state.set()

async def surname_check(message: types.Message, state: FSMContext):
    async with state.proxy() as datas:
        datas["Фамилия"] = message.text
    await message.answer("Введите номер телефона (8**********")
    await FSMCommands.num_state.set()

async def num_check(message: types.Message, state: FSMContext):
    if message.text.isnumeric() and message.text.startswith("8") and len(message.text) == 11:
        async with state.proxy() as datas:
            datas["Номер"] = message.text
        await message.answer("Вы успешно авторизовались", reply_markup=kb_act)
        await FSMCommands.action_state.set()
    else:
        await message.answer("Неверный номер. Повторите ввод")
        return
async def actions(query: types.CallbackQuery, state: FSMContext):
    if query.data == "balance":
        await FSMCommands.check_bal_state.set()
    elif query.data == "add":
        await FSMCommands.add_bal_state.set()
    elif query.data == "catalog":
        await FSMCommands.cat_state.set()
    elif query.data == "basket":
        await FSMCommands.bask_state.set()
async def query_check_balance(message: types.Message, state: FSMContext):
    async with state.proxy() as datas:
        datas["Сумма"] = 0
        await message.answer(f"Ваш баланс:  {datas['Сумма']} рублей")
    await FSMCommands.name_state.set()

async def query_add_balance(message: types.Message, state: FSMContext):
    await message.answer("Введите желаемую сумму для пополнения")
    await FSMCommands.confirm_state.set()

async def confirm(message: types.Message, state: FSMContext):
    if message.text.isnumeric:
        async with state.proxy() as datas:
            datas["Пополнение"] = int(message.text)
        await message.answer("Пополнить?", reply_markup=kb_yn)
    else:
        await message.answer("Повторите ввод")
        return
    await FSMCommands.sum_state.set()

async def sum_act(query: types.CallbackQuery, state: FSMContext):
    if query.data == "yes":
        async with state.proxy() as datas:
                datas["Сумма"] = datas["Сумма"] +  datas["Пополнение"]
        await query.message.answer("Счет успешно пополнен", reply_markup=kb_act)
    else:
        await query.message.answer("Выберите действие", reply_markup=kb_act)

async def catalog(message: types.Message, state: FSMContext):
    async with state.proxy() as datas:
        await message.answer(f"Батарея чугунная\n {datas['Фото'][1]}", reply_markup=kb_buy)
        await FSMCommands.chugun_state.set()
        await message.answer(f"Батарея алюминиевая\n {datas['Фото'][2]}", reply_markup=kb_buy)
        await FSMCommands.alum_state.set()
        await message.answer(f"Батарея электрическая\n {datas['Фото'][3]}", reply_markup=kb_buy)
        await FSMCommands.electro_state.set()


async def add_chugun(query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as datas:
        while query.data == "add_cart":
            datas["Колво"] += 1
            datas["Корзина"].append(["Батарея чугунная",  datas["Колво"]])
async def add_alum(query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as datas:
        while query.data == "add_cart":
            datas["Колво"] += 1
            datas["Корзина"].append(["Батарея алюминиевая",  datas["Колво"]])
async def add_electro(query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as datas:
        while query.data == "add_cart":
            datas["Колво"] += 1
            datas["Корзина"].append(["Батарея электрическая",  datas["Колво"]])

async def basket













def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start, commands="start", state="*")
    dp.register_callback_query_handler(query_auth,
                                       lambda callback: callback.data == "authorization",
                                       state="*")
    dp.register_message_handler(name_check, state=FSMCommands.name_state)
    dp.register_message_handler(surname_check, state=FSMCommands.surname_state)
    dp.register_message_handler(num_check, state=FSMCommands.num_state)
