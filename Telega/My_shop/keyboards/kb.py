from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import json
kb_auth = InlineKeyboardMarkup(row_width=1)
button = InlineKeyboardButton(text="Авторизоваться", callback_data="authorization")
kb_auth.insert(button)

kb_act = InlineKeyboardMarkup(row_width=2)
button1 = InlineKeyboardButton(text="Проверить баланс", callback_data="balance")
button2 = InlineKeyboardButton(text="Пополнить баланс", callback_data="add")
button3 = InlineKeyboardButton(text="Каталог", callback_data="catalog")
button4 = InlineKeyboardButton(text="Корзина", callback_data="basket")
kb_act.insert(button1)
kb_act.insert(button2)
kb_act.insert(button3)
kb_act.insert(button4)

kb_yn = InlineKeyboardMarkup(row_width=2)
yes = InlineKeyboardButton(text="Да", callback_data="yes")
no = InlineKeyboardButton(text="Нет", callback_data="no")
kb_yn.insert(yes)
kb_yn.insert(no)

kb_buy = InlineKeyboardMarkup(row_width=2)
add_cart = InlineKeyboardButton(text="Добавить в корзину", callback_data="add_cart")
delete_cart = InlineKeyboardButton(text="Убрать из корзины", callback_data="del_cart")
kb_buy.insert(add_cart)
kb_buy.insert(delete_cart)

def get_kb_buy(index: int)-> InlineKeyboardMarkup:
    kb_buy = InlineKeyboardMarkup(row_width=2)
    add_cart = InlineKeyboardButton(text="Добавить в корзину", callback_data=f"add_cart_{index}")
    delete_cart = InlineKeyboardButton(text="Убрать из корзины", callback_data=f"del_cart_{index}")
    kb_buy.insert(add_cart)
    kb_buy.insert(delete_cart)
    return kb_buy
def get_kb_basket(index: int) -> InlineKeyboardMarkup:
    kb_basket = InlineKeyboardMarkup(row_width=1)
    delete_bask = InlineKeyboardButton(text="Убрать из корзины", callback_data=f"del_bask{index}")
    kb_basket.insert(delete_bask)
    return kb_basket

kb_basket_buy = InlineKeyboardMarkup(row_width=2)
buy = InlineKeyboardButton(text="Купить", callback_data="buy")
cancel = InlineKeyboardButton(text="Отмена", callback_data="cancel")
kb_basket_buy.insert(buy)
kb_basket_buy.insert(cancel)
