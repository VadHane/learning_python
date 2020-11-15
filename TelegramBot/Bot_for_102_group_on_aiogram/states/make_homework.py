from aiogram.dispatcher.filters.state import StatesGroup, State


class make_homework(StatesGroup):
    subjects = State()
    description_task = State()
    deadline = State()
