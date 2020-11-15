# Telegram bot v1.0
#   01.11.2020
#   Створено основні функції бота
#   Створено реєстрацію
#
#   15.11.2020
#   Додано БД
#   Додано функції /make_homework (adm), /send_all (adm), /show_all_homework, /link, /add_link (adm)
#
#
###########################

from loader import bot, storage
from aiogram import types
from data.config import ADMINS_ID, USER_ID


async def on_shutdown(dp):
    await bot.close()
    await storage.close()


def auth_user(func):
    async def wrapper(message: types.Message):
        if message.from_user.id not in USER_ID:
            return await message.answer("У вас не має прав на використання цієї функції!\n"
                                        "/reg - Зареєструйтесь!")
        return await func(message)
    return wrapper


def auth_admin(func):
    async def wrapper(message: types.Message):
        if message.from_user.id not in ADMINS_ID:
            return await message.answer("У вас не має прав на використання цієї функції!")
        return await func(message)
    return wrapper


if __name__ == '__main__':
    from handlers.users.handlers import send_to_admin
    from aiogram import executor
    from handlers import dp

    executor.start_polling(dp, on_shutdown=on_shutdown, on_startup=send_to_admin)


