from typing import Union

from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, ContentType, CallbackQuery, ParseMode

from .keyboards import menu_problem, back_keyboard, menu_prob, menu
from ..services import get_info, add_problems, get_item
from .states import Problems
from ...mixins import subscription_check


def register_handlers(dp: Dispatcher):

    dp.register_message_handler(menu_problems, text=['Сообщить о проблеме'])
    dp.register_message_handler(menu_problems, commands=['problem_menu'])
    dp.register_message_handler(create_problems, text=['Сообщить'])
    #dp.register_message_handler(create_problems, state=Problems.Subdivision)
    dp.register_message_handler(create_name, state=Problems.Name)
    dp.register_message_handler(create_photo, state=Problems.Description)
    dp.register_message_handler(menu_probl, text=['Просмотреть'])
    dp.register_message_handler(finish, state=Problems.Photo, content_types=ContentType.PHOTO)
    dp.register_message_handler(finish, state=Problems.Photo)
    dp.register_callback_query_handler(navigate, menu_prob.filter())


async def menu_problems(message: Message):
    await message.answer('Сообщить о проблеме', reply_markup=menu)


async def create_problems(message: Message, state: FSMContext):
    await message.answer('Вы вошли в режим состояний \n'
                         'В данном режиме недоступны другие функции бота до окончания заполнения заявки\n'
                         'Чтобы продолжить напишите заголовок проблемы\n'
                         'Чтобы выйти из режима состояний отправьте /stop')
    await Problems.Name.set()


async def create_name(message: Message, state: FSMContext):
    if message.text == '/stop':
        await state.finish()
        await message.answer('Вы остановили заполнение заявки')
    else:
        name = message.text
        await state.update_data(name=name)
        await message.answer('Чтобы выйти из режима состояний отправьте /stop \n\n'
                             'Опишите проблему')
        await Problems.Description.set()


async def create_photo(message: Message, state: FSMContext):
    if message.text == '/stop':
        await state.finish()
        await message.answer('Вы остановили заполнение заявки')
    else:
        description = message.text
        await state.update_data(description=description)
        await message.answer('Чтобы выйти из режима состояний отправьте /stop \n\n'
                             'Прикрепите фотографию\n'
                             'Если фото отсутствует, отправьте любое текстовое сообщение')
        await Problems.Photo.set()


async def finish(message: Message, state: FSMContext):
    if message.text == '/stop':
        await state.finish()
        await message.answer('Вы остановили заполнение заявки')
    else:
        data = await state.get_data()
        name = data.get('name')
        description = data.get('description')
        try:
            photo = message.photo[-1].file_id
        except:
            photo ='AgACAgIAAxkBAAIJaGORtWMq4iyYQSgMaoTH3YhZ8EJ1AAIWwDEbqVmRSGo52Kg2WwIGAQADAgADbQADKwQ'
        await message.answer_photo(photo=photo, caption=f'<b>{name}</b>\n\n{description}')
        await add_problems(descriptions=description,
                           name=name,
                           photo=photo)
        await state.finish()
        await message.answer('Сообщить о проблеме', reply_markup=menu)


async def menu_probl(message: Union[CallbackQuery, Message], **kwargs):
    markup=await menu_problem()
    if isinstance(message, Message):
        await message.answer("Текущие заявки", reply_markup=markup)
    elif isinstance(message, CallbackQuery):
        call = message
        await call.message.edit_reply_markup(markup)


async def problem_info(callback: CallbackQuery, item_id, **kwargs):
    print(item_id)
    if item_id == 9999:
        await callback.message.delete()
    else:
        markup = await back_keyboard()
        element = await get_item(item_id)
        text = element.descriptions
        await callback.message.delete()
        await callback.message.answer_photo(photo=element.photo, caption=f'{element.name}\n\n{text}',reply_markup=markup)


async def navigate(cal: CallbackQuery, callback_data : dict):
    current_level = callback_data.get("level")
    id = int(callback_data.get('item_id'))

    levels = {
        "0": menu_probl,
        "1": problem_info,
    }
    current_level_function = levels[current_level]
    await current_level_function(cal, item_id=id)