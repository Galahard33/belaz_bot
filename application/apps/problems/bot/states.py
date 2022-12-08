from aiogram.dispatcher.filters.state import State, StatesGroup


class Problems(StatesGroup):
    Subdivision = State()
    Name = State()
    Photo = State()
    Description = State()