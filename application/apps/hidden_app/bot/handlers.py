from typing import Union


from aiogram import Dispatcher
from aiogram.types import Message, CallbackQuery, ParseMode, MediaGroup, ContentType
from aiogram.utils.markdown import hide_link, hlink

from .keyboards import menu, menu_1, menu_shop, back_keyboard, menu_cd_contest, menu_contest, menu_2, menu_cd, \
    back_location_keyboard, back_location_keyboard2, back_keyboard2, menu_prof, menu_hiring
from ..services import get_element, get_element_contest, get_add_info
from ...mixins import subscription_check


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(simple_doc, text=["Коды расчетных"])
    dp.register_message_handler(dk, text=["Календарный график работы"])
    dp.register_message_handler(turizm, text=["Промышленный туризм"])
    dp.register_message_handler(schedule_kpp, text=["График работы проходных"])
    dp.register_message_handler(general_workshop, text=["Интерактивный телефонный справочник"])
    dp.register_message_handler(show_med_info, text=["ОЦ Дудинка"])
    dp.register_message_handler(show_schedule_bus, text=['Расписане транспорта'])
    dp.register_message_handler(show_main_menu, commands=["menu"])
    dp.register_message_handler(show_main_menu, text=["Назад"])
    dp.register_message_handler(hiring, text=["Информация по трудоустройству"])
    dp.register_message_handler(show_menu, text=["Общезаводская информация"])
    dp.register_message_handler(show_extra_menu, text=["Прочая информация"])
    dp.register_message_handler(show_extra_menu, text=["В предыдущий раздел"])
    dp.register_message_handler(contest_info, text=["Информация о конкурсах"])
    dp.register_message_handler(get_prof, text=["Профсоюз"])
    dp.register_message_handler(get_bonus, text=["Корпоративные бонусы"])
    dp.register_message_handler(get_com_org, text=["Общественные организации"])
    dp.register_message_handler(get_other_info, text=["В предыдущее меню"])
    dp.register_message_handler(get_belaz_info, commands=["menu_belaz"])
    dp.register_message_handler(get_other_info, commands=["menu_other"])
    dp.register_message_handler(get_document, content_types=ContentType.DOCUMENT)
    dp.register_message_handler(get_photo, content_types=ContentType.PHOTO)
    dp.register_callback_query_handler(navigate_workshop, menu_cd.filter())
    dp.register_callback_query_handler(navigate_contest, menu_cd_contest.filter())


@subscription_check
async def get_belaz_info(message: Message, **kwargs):
    await message.answer('Общезаводская информация', reply_markup=menu_1)


async def hiring(message: Message, **kwargs):
    await message.answer("Информация по трудоустройству", reply_markup=menu_hiring)


@subscription_check
async def get_other_info(message: Message, **kwargs):
    await message.answer('Прочая информация', reply_markup=menu_2)


@subscription_check
async def get_com_org(message: Message, **kwargs):
    await message.answer('Общественные организации', reply_markup=menu_prof)


@subscription_check
async def simple_doc(message: Message, **kwargs):
    await message.answer_document(document='BQACAgIAAxkBAAICkmOEmBUL_LpcAiGI91rgziAAAcLgEwACZyEAAi9bKUhsyUVmFJoeBSsE')


@subscription_check
async def get_document(message: Message, **kwargs):
    if message.from_user.id == 425007240:
        file_id = message.document.file_id
        await message.answer(text=file_id)


@subscription_check
async def get_photo(message: Message, **kwargs):
    if message.from_user.id == 425007240:
        photo = message.photo[-1].file_id
        await message.answer(text=photo)



@subscription_check
async def get_prof(message: Message, **kwargs):
    text = await get_add_info(item_id=1)
    await message.answer(text=text.text)


@subscription_check
async def get_bonus(message: Message, **kwargs):
    text = await get_add_info(item_id=2)
    await message.answer(text=text.text)


@subscription_check
async def schedule_kpp(message: Message, **kwargs):
    await message.answer('КПП № 1 - КРУГЛОСУТОЧНО\nКПП № 3a - 6:00-01.20\nКПП № 5 - 5:00-01.20\nКПП № 11 - 5:00-01.20\nКПП № 17 - 6:00-17.30\nКПП № 18 - 6:00-16.30\nКПП № 20 - 6:00-01.00\n')


@subscription_check
async def dk(message: Message, **kwargs):
    await message.answer_photo(photo='AgACAgIAAxkBAAO6Y3_ENL3mi6qjNoDcHGsilwmHpAMAAmvBMRtCyAABSNGULj1_TM0YAQADAgADeQADKwQ')


@subscription_check
async def show_main_menu(message: Message, **kwargs):
    #a = await message.bot.get_chat_member(chat_id='-1001608043243', user_id=message.from_user.id)
    #a = await message.bot.get_chat_member(chat_id='-1001492013579', user_id=message.from_user.id)
    await message.answer('Меню', reply_markup=menu)


@subscription_check
async def show_menu(message: Message, **kwargs):
    await message.answer('Выберите раздел', reply_markup=menu_1)


@subscription_check
async def show_extra_menu(message: Message, **kwargs):
    await message.answer('Выберите раздел', reply_markup=menu_2)


@subscription_check
async def show_schedule_bus(message: Message, **kwargs):
    text = str('От термогальванического цеха\n10:45\n13:45\n\nОт УГК НТЦ\n9:45\n12:45')
    await message.answer(text=str(text), parse_mode=ParseMode.HTML)


@subscription_check
async def show_med_info(message: Message, **kwargs):
    return await message.answer(hlink('Здесь ','http://dudinka-belaz.by/')+'вы можете посмотреть подробную информацию', parse_mode=ParseMode.HTML)


@subscription_check
async def turizm(message: Message, **kwargs):
    return await message.answer('Приглашаем посетить известный во всем мире бренд – белорусский автомобильный завод\n\n'
                                'Сегодня мы рады предложить вам следующие услуги:\n'
                                'Экскурсия по заводу\n'
                                'Динамический тренажер\n'
                                'Проезда на самосвале\n'
                                'Вкусные обеды\n\n'
                                'Для более подробной информации посетите наш '
                                +hlink('сайт','https://shop.belaz.by/'), parse_mode=ParseMode.HTML)


members = ['member', 'admin', 'creator']


async def general_workshop(message: Union[CallbackQuery, Message], **kwargs):
    a = await message.bot.get_chat_member(chat_id='-1001608043243', user_id=message.from_user.id)
    print(message.from_user.first_name)
    print(a['status'])
    markup=await menu_shop()
    if isinstance(message, Message):
        await message.answer("Выберите подразделение", reply_markup=markup)
    elif isinstance(message, CallbackQuery):
        call = message
        await call.message.edit_reply_markup(markup)


async def item_text(callback: CallbackQuery, item_id, text, **kwargs):
    print('из 1 '+str(item_id))
    if item_id == 9999:
        await callback.message.delete()
    elif item_id == 27:
        markup = back_location_keyboard2(item_id)
        element = await get_element(item_id)
        text = element.text
        await callback.message.edit_text(text=str(text), reply_markup=markup, parse_mode=ParseMode.HTML)
    else:
        markup = back_location_keyboard(item_id)
        element = await get_element(item_id)
        text = element.text
        await callback.message.edit_text(text=str(text), reply_markup=markup, parse_mode=ParseMode.HTML)


async def item_text2(callback: CallbackQuery, item_id, text, **kwargs):
    print('из 3 ' + str(item_id))
    text = text
    markup = back_keyboard2(item_id)
    await callback.message.edit_text(text=text, reply_markup=markup, parse_mode=ParseMode.HTML)


async def item_location(callback: CallbackQuery, item_id, **kwargs):
    print('из 2 '+str(item_id))
    item = await get_element(item_id)
    markup = back_keyboard()
    if item.title == '460.01 - Склад электрооборудования':
        await callback.message.answer_location(latitude=item.latitude, longitude=item.longitude, reply_markup=markup)
    else:
        await callback.message.answer_location(latitude=54.0972548, longitude=28.3181615, reply_markup=markup)


async def navigate_workshop(cal: CallbackQuery, callback_data : dict):
    current_level = callback_data.get("level")
    id = int(callback_data.get('item_id'))
    text = callback_data.get('text')

    levels = {
        "0": general_workshop,
        "1": item_text,
        "2": item_location,
        "3": item_text2
    }
    current_level_function = levels[current_level]
    await current_level_function(cal, item_id=id, text=text)


async def contest_info(message: Union[CallbackQuery, Message], message_id=0, **kwargs):
    markup=await menu_contest()
    if isinstance(message, Message):
        await message.answer("Выберите конкурс", reply_markup=markup)
    if isinstance(message, CallbackQuery):
        call = message
        await call.message.edit_reply_markup(markup)


async def contest_item_text(callback:CallbackQuery, item_id, **kwargs):
    if item_id == 999:
        await callback.message.delete()
    else:
        markup = await menu_contest()
        element = await get_element_contest(item_id)
        if element.text:
            text = element.text
        else:
            text = 'Описание отутствует'
        if element.document_name:
            media = MediaGroup()
            doc = element.document_name.split(',')
            for item in doc:
                media.attach_document(document=item)
            print(media)
            await callback.message.delete()
            await callback.message.answer_media_group(media=media)
            await callback.message.answer('Выберите конкурс', reply_markup=markup)
        else:
            await callback.message.delete()
            await callback.message.answer(text=text)
            await callback.message.answer('Выберите конкурс', reply_markup=markup)


async def navigate_contest(cal: CallbackQuery, callback_data : dict):
    current_level = callback_data.get("level")
    id = int(callback_data.get('item_id'))

    levels = {
        "0": contest_info,
        "1": contest_item_text
    }
    current_level_function = levels[current_level]
    await current_level_function(cal, item_id=id)