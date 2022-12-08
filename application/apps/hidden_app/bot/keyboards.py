
from aiogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,
                           KeyboardButton, ReplyKeyboardMarkup,
                           ReplyKeyboardRemove)
from aiogram.utils.callback_data import CallbackData

from ...hidden_app.services import get_info, get_contest

menu_cd = CallbackData("show_menu", "level", 'item_id', 'text')


def make_callback_data(level, item_id=0, text=''):
    return menu_cd.new(level=level, item_id=item_id, text=text)


menu_cd_contest = CallbackData("show_menu_contest", "level", 'item_id')


def make_callback_data_contest(level, item_id=0):
    return menu_cd_contest.new(level=level, item_id=item_id)


menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Общезаводская информация'),
            KeyboardButton(text='Прочая информация'),

        ],
    ],
    resize_keyboard=True
)


menu_prof = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Профсоюз'),
            KeyboardButton(text='БРСМ'),

        ],
        [
            KeyboardButton(text='Белая Русь'),
            KeyboardButton(text='Союз Женщин'),

        ],
        [
            KeyboardButton(text='В предыдущий раздел')
        ]
    ],
    resize_keyboard=True
)


menu_hiring = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Актуальные вакансии'),
            KeyboardButton(text='Алгоритм трудоустройства'),

        ],
        [
            KeyboardButton(text='Необходимые документы'),

        ],
        [
            KeyboardButton(text='В предыдущее меню')
        ]
    ],
    resize_keyboard=True
)


menu_1 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Расписане транспорта'),
            KeyboardButton(text='Коды расчетных'),
            KeyboardButton(text='Календарный график работы')
        ],
[
            KeyboardButton(text='Интерактивный телефонный справочник'),
            KeyboardButton(text='График работы проходных'),

        ],
[
            KeyboardButton(text='Назад'),

        ],
    ],
    resize_keyboard=True
)

menu_2 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Информация о конкурсах'),
            KeyboardButton(text='Услуги населению'),
            KeyboardButton(text='ОЦ Дудинка')
        ],
[
            KeyboardButton(text='Корпоративные бонусы'),
            KeyboardButton(text='Информация по трудоустройству')

        ],
        [
            KeyboardButton(text='Общественные организации'),
        ],
[
            KeyboardButton(text='Промышленный туризм'),
            KeyboardButton(text="Сообщить о проблеме")

        ],
[
            KeyboardButton(text='Назад'),

        ],
    ],
    resize_keyboard=True
)


async def menu_shop():
    CURRENT_LEVEL = 0
    markup = InlineKeyboardMarkup(row_width=2)
    items = await get_info()
    for item in items:
        button_text = f"{item.title}"
        callback_data = make_callback_data(level=CURRENT_LEVEL + 1, item_id=item.id)
        markup.insert(
            InlineKeyboardButton(text=button_text, callback_data=callback_data)
        )
    return markup


def back_location_keyboard(item_id):
    CURRENT_LEVEL = 1
    markup = InlineKeyboardMarkup()
    markup.row(
        InlineKeyboardButton(
            text="Назад",
            callback_data=make_callback_data(level=CURRENT_LEVEL-1))
    )
    markup.row(
        InlineKeyboardButton(
            text="Показать на карте",
            callback_data=make_callback_data(level=CURRENT_LEVEL+1, item_id=item_id))
    )
    return markup


def back_location_keyboard2(item_id):
    CURRENT_LEVEL = 1
    markup = InlineKeyboardMarkup()
    markup.row(
        InlineKeyboardButton(
            text="КБ Компоновки",
            callback_data=make_callback_data(level=CURRENT_LEVEL+2, item_id=item_id, text='нач. бюро - 95-68'))
    )
    markup.row(
        InlineKeyboardButton(
            text="КБ Cпец. транспорта ",
            callback_data=make_callback_data(level=CURRENT_LEVEL +2, item_id=item_id, text='нач. бюро - 93-82'))
    )
    markup.row(
        InlineKeyboardButton(
            text="КБ Рам и платформ",
            callback_data=make_callback_data(level=CURRENT_LEVEL + 2, item_id=item_id, text='нач бюро - 92-95'))
    )
    markup.row(
        InlineKeyboardButton(
            text="КБ Кабин",
            callback_data=make_callback_data(level=CURRENT_LEVEL +2, item_id=item_id, text='нач бюро - 92-29'))
    )
    markup.row(
        InlineKeyboardButton(
            text="КБ Оперения",
            callback_data=make_callback_data(level=CURRENT_LEVEL +2, item_id=item_id, text='нач бюро - 92-26'))
    )
    markup.row(
        InlineKeyboardButton(
            text="Назад",
            callback_data=make_callback_data(level=CURRENT_LEVEL-1, item_id=item_id))
    )

    markup.row(
        InlineKeyboardButton(
            text="Показать на карте",
            callback_data=make_callback_data(level=CURRENT_LEVEL+1, item_id=item_id))
    )
    return markup


def back_keyboard():
    CURRENT_LEVEL = 2
    markup = InlineKeyboardMarkup()
    markup.row(
        InlineKeyboardButton(
            text="Закрыть",
            callback_data=make_callback_data(level=CURRENT_LEVEL-1, item_id=9999))
    )
    return markup


def back_keyboard2(item_id):
    CURRENT_LEVEL = 3
    markup = InlineKeyboardMarkup()
    markup.row(
        InlineKeyboardButton(
            text="Назад",
            callback_data=make_callback_data(level=CURRENT_LEVEL-2, item_id=item_id))
    )
    return markup


async def menu_contest():
    CURRENT_LEVEL = 0
    markup = InlineKeyboardMarkup(row_width=1)
    items = await get_contest()
    for item in items:
        button_text = f"{item.title}"
        callback_data = make_callback_data_contest(level=CURRENT_LEVEL + 1, item_id=item.id)
        markup.insert(
            InlineKeyboardButton(text=button_text, callback_data=callback_data)
        )
    return markup

def back_contest_keyboard():
    CURRENT_LEVEL = 1
    markup = InlineKeyboardMarkup()
    markup.row(
        InlineKeyboardButton(
            text="Назад",
            callback_data=make_callback_data_contest(level=CURRENT_LEVEL-1))
    )
    return markup