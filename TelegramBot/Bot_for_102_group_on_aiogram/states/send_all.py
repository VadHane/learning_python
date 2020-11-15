from aiogram.dispatcher.filters.state import StatesGroup, State


class send_all_(StatesGroup):
    are_you_ready = State()
    send = State()
