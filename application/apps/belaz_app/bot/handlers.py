import os
import requests
from urllib.parse import urlparse
from collections import defaultdict
from datetime import datetime
from typing import Union
import redis

from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.webhook import SendMessage
from aiogram.types import Message, CallbackQuery, ParseMode

from .keyboards import menu_cd, solo_question_2, menu_quiz, solo_question_1
from .states import Question

url = urlparse(os.environ.get("REDIS_URL"))
r = redis.Redis(host=url.hostname, port=url.port, username=url.username, password=url.password, ssl=True, ssl_cert_reqs=None)


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(clear_list, text=["Очистить списки"])
    dp.register_message_handler(start_solo, text=['Розыгрыш'])
    dp.register_message_handler(result_single, text=['Результаты розыгрыша'])
    dp.register_message_handler(send_message1, text=['Оповестить победителей'])
    dp.register_message_handler(send_channel, text=['Канал для демонстрации'])
    dp.register_message_handler(show_quiz_menu, commands=["menu_quiz"])
    dp.register_callback_query_handler(nav, menu_cd.filter())
    dp.register_message_handler(create_quiz, text=['Создать розыгрыш'])
    dp.register_message_handler(create_first_answer, state=Question.Q1)
    dp.register_message_handler(create_2_answer, state=Question.a1)
    dp.register_message_handler(create_3_answer, state=Question.a2)
    dp.register_message_handler(create_4_answer, state=Question.a3)
    dp.register_message_handler(create_right_answer, state=Question.a4)
    dp.register_message_handler(end_create, state=Question.ar)


winners = defaultdict(list)
winners_solo = defaultdict(list)
losers_solo = defaultdict(list)
winners_for_send = []
# Create your handlers here


async def create_quiz(message: Message):
    if message.from_user.id == 425007240:
        await message.answer('Напишите вопрос')
        await Question.Q1.set()
    else:
        await message.answer('У вас нет прав для создания розыгрышей')


async def send_channel(message: Message):
    await message.answer('https://t.me/test_zdn')


async def create_first_answer(message: Message, state: FSMContext):
    question = message.text
    r.set('question', question)
    await state.update_data(question = question)
    await message.answer('Напишите Первый вариант ответа')
    await Question.a1.set()


async def create_2_answer(message: Message, state: FSMContext):
    answer1 = message.text
    r.set('answer1', answer1)
    await state.update_data(answer1 = answer1)
    await message.answer('Напишите второй вариант ответа')
    await Question.a2.set()


async def create_3_answer(message: Message, state: FSMContext):
    answer2 = message.text
    r.set('answer2', answer2)
    await state.update_data(answer2 = answer2)
    await message.answer('Напишите третий вариант ответа')
    await Question.a3.set()


async def create_4_answer(message: Message, state: FSMContext):
    answer3 = message.text
    r.set('answer3', answer3)
    await state.update_data(answer3 = answer3)
    await message.answer('Напишите четвертый вариант ответа')
    await Question.a4.set()


async def create_right_answer(message: Message, state: FSMContext):
    answer4 = message.text
    r.set('answer4', answer4)
    await state.update_data(answer4 = answer4)
    await message.answer('Напишите правильный ответ')
    await Question.ar.set()


async def end_create(message: Message, state: FSMContext):
    right_answer = message.text
    r.set('right_answer', right_answer)
    await state.update_data(right_answer=right_answer)
    await message.answer('Готово!')
    await state.finish()


async def clear_list(message: Message):
    if message.from_user.id == 425007240:
        winners_solo.clear()
        losers_solo.clear()
        await message.answer('Списки пользователей очищены')
    await message.answer('У вас нет прав для создания розыгрышей')


async def start_solo(message: Union[CallbackQuery, Message], **kwargs):
    if message.from_user.id == 425007240:
        markup = await solo_question_1()
        text=f'{r.get("question").decode("utf-8")}'
        await message.bot.send_message(chat_id='-1001608043243', text=text, reply_markup=markup)
        await message.answer(text=text, reply_markup=markup)
    await message.answer('У вас нет прав для создания розыгрышей')


async def solo_question(message: Union[CallbackQuery, Message],answer, **kwargs):
    markup = await solo_question_1()
    if isinstance(message, Message):
        await message.answer(reply_markup=markup, parse_mode=ParseMode.HTML)
    elif isinstance(message, CallbackQuery):
        call = message
        if call.from_user.id in (winners_solo.keys() or losers_solo.keys()):
            await call.answer(f'Вы уже отвечали')
        else:
            if str(r.get("right_answer").decode("utf-8")) == answer:
                winners_solo[call.from_user.id].append(answer)
                time = str(datetime.now())
                winners_solo[call.from_user.id].append(str(time[11:-7]))
                winners_solo[call.from_user.id].append(call.from_user.first_name)
                await call.answer(f'Ваш ответ: {answer} принят')
            else:
                losers_solo[call.from_user.id].append(answer)
                await call.answer(f'Ваш ответ: {answer} принят')
        print(winners_solo, 'Winners')
        print(losers_solo, 'Losers')
        await call.message.edit_reply_markup(markup)


async def single_question(message: Union[CallbackQuery, Message], answer, **kwargs):
    markup = await solo_question_2()
    if isinstance(message, Message):
        await message.answer(reply_markup=markup, parse_mode=ParseMode.HTML)
    elif isinstance(message, CallbackQuery):
        call = message
        if call.from_user.id in (winners_solo.keys() or losers_solo.keys()):
            await call.answer(f'Вы уже отвечали')
        else:
            if str(r.get("right_answer").decode("utf-8")) == answer:
                winners_solo[call.from_user.id].append(answer)
                time = str(datetime.now())
                winners_solo[call.from_user.id].append(str(time[11:-7]))
                winners_solo[call.from_user.id].append(call.from_user.first_name)
                await call.answer(f'Ваш ответ: {answer} принят')
            else:
                losers_solo[call.from_user.id].append(answer)
                await call.answer(f'Ваш ответ: {answer} принят')
        print(winners_solo, 'Winners')
        print(losers_solo, 'Losers')
        await call.message.edit_reply_markup(markup)


async def result_single(message: Message):
    if message.from_user.id == 425007240:
        sorted_winners = dict(sorted(winners_solo.items(), key=lambda x: x[1]))
        print(sorted_winners)
        for i in range(5):
            text = list(sorted_winners.keys())[i]
            answer = sorted_winners[text][0]
            time = sorted_winners[text][1]
            username = sorted_winners[text][2]
            await message.answer(text=f"{username}, id:{text}, Ответ: {answer}, Время: {time}")
        winners_for_send.append(sorted_winners)

    else:
        await message.answer("У вас недостаточно прав")


async def nav(cal: CallbackQuery, callback_data: dict):
    current_level = callback_data.get("level")
    answer = callback_data.get("text")
    levels = {
        "0": solo_question,
        "1": single_question,

    }
    current_level_function = levels[current_level]
    await current_level_function(cal, answer=answer)


async def show_quiz_menu(message: Message):
    await message.answer('Меню розыгрышей', reply_markup=menu_quiz)


async def send_message1(message: Message):
    sorted_winners = dict(sorted(winners_solo.items(), key=lambda x: x[1]))
    for winner in sorted_winners.keys():
        method = 'https://api.telegram.org/bot' + os.getenv("BOT_API_TOKEN")+'/sendMessage'
        req = requests.post(method, data={'chat_id': winner,
                                          'text': f'Сообщение о выигрыше:\nВаш ответ: {sorted_winners[winner][0]}\nВремя: {sorted_winners[winner][1]}'})
    await message.answer('Отправлено')





