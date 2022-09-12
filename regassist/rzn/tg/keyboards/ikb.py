from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from rzn.functions.settings import RZN_TYPES

ikb_type = InlineKeyboardMarkup(row_width=1)
for btn in RZN_TYPES:
    ikb_type.add(InlineKeyboardButton(text=btn[1], callback_data='type_' + str(btn[0])))

btn_cansel = InlineKeyboardButton(text='Отмена', callback_data='btn_cansel')
ikb_type.add(btn_cansel)

ikb_cansel = InlineKeyboardMarkup(row_width=1)
ikb_cansel.add(btn_cansel)
