from main import bot
from loader import dp
from aiogram.dispatcher.filters import Text, Command
from aiogram.types import Message
from data.config import ADMINS_ID, USER_ID


async def send_to_admin(dp):
    for ADMIN in ADMINS_ID:
        await bot.send_message(chat_id=ADMIN, text="Bot is started")


@dp.message_handler(Command('start'))
async def hello_new_user(message: Message):
    await message.answer('Радий вітати! \n'
                         'Розпочни користуватись мною, зареєструвавшись. \n'
                         '/reg - Для реєстрації. \n'
                         'Щоб переглянути цю, та інші функції - /help \n\n'
                         'by @hanevuch')


@dp.message_handler(Command('help'))
async def show_all_command(message: Message):
    if message.from_user.id in ADMINS_ID:
        await message.answer('Список доступних команд: \n'
                             '1) /reg - Зареєструватись як новий користувач \n'
                             '2) /stop - Зупинити розсилку матеріалу \n'
                             '3) /link - Список статичний лінків на пару \n'
                             '4) Скоро буде... ')
    elif message.from_user.id in USER_ID:
        await message.answer('Список доступних команд: \n'
                             '1) /reg - Зареєструватись як новий користувач \n'
                             '2) /stop - Зупинити розсилку матеріалу \n'
                             '3) /link - Список статичний лінків на пару \n'
                             '4) Скоро буде... ')
    else:
        await message.answer('Зареєструйтесь для роботи!')


@dp.message_handler(Command('link'))
async def show_const_link(message: Message):
    if message.from_user.id in USER_ID:
        await message.answer('/math_a - Математичний аналіз \n'
                             '/discretna - Дискретна математика \n'
                             '/english - English \n'
                             '/history - Історія \n'
                             '/a_and_g - Алгебра та геометрія (лекція) \n')
    else:
        await message.answer('Зареєструйтесь для роботи!')


# @dp.message_handler(id(USER_ID))
# async def echo(message: Message):
#    text = message.text
#    await bot.send_message(chat_id=message.from_user.id, text=text)
#
#    await message.answer(text=text)


# @dp.message_handler(text="1")
# async def get_message_all_users(message: Message):
#     if message.from_user.id == ADMINS_ID:
#         for user in USER_ID:
#             try:
#                 await bot.send_message(chat_id=user, text=message.text)
#             except Exception as ex:
#                 print(f"Error {ex}; \nUser id {user}")
#     else:
#         print(message.from_user.id)
