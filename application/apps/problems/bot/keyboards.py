from aiogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,
                           KeyboardButton, ReplyKeyboardMarkup,
                           ReplyKeyboardRemove)
from aiogram.utils.callback_data import CallbackData

from ..services import get_info

menu_prob = CallbackData("show_problems", "level", 'item_id')


def make_callback_data(level, item_id=0):
    return menu_prob.new(level=level, item_id=item_id)


async def menu_problem():
    CURRENT_LEVEL = 0
    markup = InlineKeyboardMarkup(row_width=2)
    items = await get_info()
    for item in items:
        button_text = f"{item.name}"
        callback_data = make_callback_data(level=CURRENT_LEVEL + 1, item_id=item.id)
        markup.insert(
            InlineKeyboardButton(text=button_text, callback_data=callback_data)
        )
    markup.row(
        InlineKeyboardButton(
            text="Закрыть",
            callback_data=make_callback_data(level=CURRENT_LEVEL+1, item_id=9999))
    )
    return markup


async def back_keyboard():
    CURRENT_LEVEL = 1
    markup = InlineKeyboardMarkup()
    markup.row(
        InlineKeyboardButton(
            text="Назад",
            callback_data=make_callback_data(level=CURRENT_LEVEL-1))
    )
    return markup


menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Просмотреть'),
            KeyboardButton(text='Сообщить'),

        ],
        [
            KeyboardButton(text='В предыдущий раздел'),

        ],
    ],
    resize_keyboard=True
)