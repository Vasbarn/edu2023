from aiogram.filters.state import State, StatesGroup
from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
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


async def start(message: types.Message, state: FSMContext):
    async with state.proxy() as datas:
        if datas.get('id'):
            await message.answer(f"Я тебя знаю {message.from_user.id}")
        else:
            await message.answer(f"Я тебя не знаю {message.from_user.id}")
            datas['id'] = message.from_user.id
        chugun = InputFile(r"C:\Users\Admin\PycharmProjects\edu2023\Telega\чугун.jpg")
        alum = InputFile(r"C:\Users\Admin\PycharmProjects\edu2023\Telega\люминь.jpg")
        electro = InputFile(r"C:\Users\Admin\PycharmProjects\edu2023\Telega\электро.jpg")
        datas["Колво"] = 0
        datas["Корзина"] = dict()
        # datas["Каталог"] = ["Батарея чугунная", "Батарея алюминиевая", "Батарея электрическая"]
        # datas["Фото"] = [chugun, alum, electro]
    await message.answer("Приветствуем в лучшем магазине батарей!!")






