from aiogram.dispatcher.filters.state import StatesGroup, State


class add(StatesGroup):
    user_id = State()
