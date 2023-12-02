from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

kb_auth = InlineKeyboardMarkup(row_width=1)
button = InlineKeyboardButton(text="Авторизоваться", callback_data="authorization")
kb_auth.insert(button)