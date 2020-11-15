from aiogram.dispatcher.filters.state import StatesGroup, State


class add(StatesGroup):
    name_link = State()
    link = State()
