from aiogram.types import ParseMode
from aiogram.utils.markdown import hide_link


def subscription_check(func):
    async def wrapper(*args, **kwargs):
        member = await args[0].bot.get_chat_member(chat_id='-1001492013579', user_id=args[0]['chat']['id'])
        if member['status'] == 'member':
            return await func(*args, **kwargs)
        else:
            return await args[0].answer('Для доступа к контенту необходимо подписаться на официальный канал'+hide_link('https://t.me/belaz14101961'), parse_mode=ParseMode.HTML)
    return wrapper