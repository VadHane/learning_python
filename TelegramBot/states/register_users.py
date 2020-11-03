from aiogram.dispatcher.filters.state import StatesGroup, State


class register_new_user(StatesGroup):

    def check_new_users(self):
        pass

    def add_new_user(self):
        pass

    name = State()
    user_id = State()
    key = State()
