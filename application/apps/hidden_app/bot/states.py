from aiogram.dispatcher.filters.state import State, StatesGroup


class Problems(StatesGroup):
    Photo = State()
    Description = State()
