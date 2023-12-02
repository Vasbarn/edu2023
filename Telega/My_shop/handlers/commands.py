from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from keyboards.kb import kb_auth


class FSMCommands(StatesGroup):
    name_state = State()

async def start(message: types.Message, state: FSMContext):
    await message.answer("Приветствуем в лучшем магазине батарей!!")
    await message.answer("Вам нужно", reply_markup=kb_auth)

async def query_auth(query: types.CallbackQuery, state: FSMContext):
    await query.message.answer("Введите имя")
    await FSMCommands.name_state.set()




def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start, commands="start", state="*")
    dp.register_callback_query_handler(query_auth,
                                       lambda callback: callback.data == "authorization",
                                       state="*")