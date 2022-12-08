import os
from urllib.parse import urlparse

import redis


from aiogram.types import (InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton)
from aiogram.utils.callback_data import CallbackData



menu_cd = CallbackData("show_menu", "level", 'text', 'text2', 'text3')

url = urlparse(os.environ.get("REDIS_URL"))
r = redis.Redis(host=url.hostname, port=url.port, username=url.username, password=url.password, ssl=True, ssl_cert_reqs=None)


def make_callback_data(level, text='0', text2='0', text3='0'):
    return menu_cd.new(level=level, text=text, text2=text2, text3=text3)


async def solo_question_1():
    CURRENT_LEVEL = 0
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(
                text=f'{r.get("answer1").decode("utf-8")}',

                callback_data=make_callback_data(level=CURRENT_LEVEL + 1,
                                                 text=f"{r.get('answer1').decode('utf-8')}")
            )]])
    markup.row(
        InlineKeyboardButton(
            text=f'{r.get("answer2").decode("utf-8")}',
            callback_data=make_callback_data(level=CURRENT_LEVEL + 1,
                                             text=f"{r.get('answer2').decode('utf-8')}")
        ))
    markup.row(
        InlineKeyboardButton(
            text=f'{r.get("answer3").decode("utf-8")}',
            callback_data=make_callback_data(level=CURRENT_LEVEL + 1,
                                             text=f"{r.get('answer3').decode('utf-8')}")
        ))
    markup.row(
        InlineKeyboardButton(
            text=f'{r.get("answer4").decode("utf-8")}',
            callback_data=make_callback_data(level=CURRENT_LEVEL + 1,
                                             text=f"{r.get('answer4').decode('utf-8')}")
        ))
    return markup


async def solo_question_2():
    CURRENT_LEVEL = 1
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(
                text=f'{r.get("answer1").decode("utf-8")}',

                callback_data=make_callback_data(level=CURRENT_LEVEL - 1,
                                                 text=f"{r.get('answer1').decode('utf-8')}")
            )]])
    markup.row(
        InlineKeyboardButton(
            text=f'{r.get("answer2").decode("utf-8")}',
            callback_data=make_callback_data(level=CURRENT_LEVEL - 1,
                                             text=f"{r.get('answer2').decode('utf-8')}")
        ))
    markup.row(
        InlineKeyboardButton(
            text=f'{r.get("answer3").decode("utf-8")}',
            callback_data=make_callback_data(level=CURRENT_LEVEL - 1,
                                             text=f"{r.get('answer3').decode('utf-8')}")
        ))
    markup.row(
        InlineKeyboardButton(
            text=f'{r.get("answer4").decode("utf-8")}',
            callback_data=make_callback_data(level=CURRENT_LEVEL - 1,
                                             text=f"{r.get('answer4').decode('utf-8')}")
        ))
    return markup


menu_quiz = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Розыгрыш'),
            KeyboardButton(text='Результаты розыгрыша'),
            KeyboardButton(text='Оповестить победителей'),
        ],
[
            KeyboardButton(text='Очистить списки'),
            KeyboardButton(text='Создать розыгрыш'),
            KeyboardButton(text='Канал для демонстрации'),
        ],
    ],
    resize_keyboard=True
)

