from aiogram import Dispatcher
from aiogram.types import Message

from config.apps import INSTALLED_APPS

from .. import services
from ...mixins import subscription_check


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start, commands=["start"])
    dp.register_message_handler(send_my_id, commands=["id"])
    dp.register_message_handler(info, commands=["info"])


async def start(message: Message):
    user = await services.add_user(
        tg_id=message.from_user.id,
        chat_id=message.chat.id,
        first_name=message.from_user.first_name,
    )
    await message.answer("Это неофициальная тестовая версия информационного бота БЕЛАЗа.\n"
                         "Для краткого описания базовых команд нажмите: /info\n"
                         "Для начала работы нажмите: /menu")


async def send_my_id(message: Message):
    await message.answer(
        f"User Id: <b>{message.from_user.id}</b>\n" f"Chat Id: <b>{message.chat.id}</b>"
    )


@subscription_check
async def info(message: Message, **kwargs):
    await message.answer("/menu - Меню выбора раздела\n"
                         "/menu_belaz - Ветка меню с информацией о заводе\n"
                         "/menu_other - Ветка меню с прочей информацией")