from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Запустить бота"),
            types.BotCommand("menu", "Показать меню"),
            types.BotCommand("menu_quiz", "Показать меню розыгрышей"),
            types.BotCommand("menu_belaz", "Показать меню с заводской информацией"),
            types.BotCommand("menu_other", "Показать меню с прочей информацией"),
        ]
    )
