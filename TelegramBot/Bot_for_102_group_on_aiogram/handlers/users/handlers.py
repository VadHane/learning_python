from main import bot
from loader import dp
from aiogram.dispatcher.filters import Text, Command
from aiogram.types import Message, ReplyKeyboardRemove
from data.config import USER_ID, ADMINS_ID
from main import auth_user, auth_admin
from database import fetchall, insert
from keyboards.standart import start, help_a, help_u, key_help


async def send_to_admin(dp):
    for ADMIN in ADMINS_ID:
        await bot.send_message(chat_id=ADMIN, text="Bot is started")


@dp.message_handler(Command('start'))
async def hello_new_user(message: Message):
    await message.answer('Радий вітати! \n'
                         'Розпочни користуватись мною, зареєструвавшись. \n'
                         '/reg - Для реєстрації. \n'
                         'Щоб переглянути цю, та інші функції - /help \n\n'
                         'by @hanevuch', reply_markup=start)


@dp.message_handler(Command('help'))
@auth_user
async def show_all_command(message: Message):
    if message.from_user.id in ADMINS_ID:
        await message.answer('Список доступних команд: \n'
                             '1) /reg - Зареєструватись як новий користувач \n'
                             '2) /add_link - Добавити лінк \n'
                             '3) /link - Список статичний лінків на пару \n'
                             '4) /make_homework - Додати запис про дз в базу \n'
                             '5) /send_all - Надіслати повідомлення усім користувачам \n'
                             '6) /homework - Подивитись усі записи з дз \n'
                             '7) /add_new_admin - Добавити нового адміністратора \n'
                             '7) Скоро буде... ', reply_markup=help_a)
    elif message.from_user.id in USER_ID:
        await message.answer('Список доступних команд: \n'
                             '1) /reg - Зареєструватись як новий користувач \n'
                             '2) /stop - Зупинити розсилку матеріалу \n'
                             '3) /link - Список статичний лінків на пару \n'
                             '4) /homework - Подивитись усі записи з дз \n'
                             '5) Скоро буде... ', reply_markup=help_u)


@dp.message_handler(Command('homework'))
@auth_user
async def show_all_homework(message: Message):
    db = fetchall('homework', '*')
    _text_answer = []
    text_answer = ''
    for obj in db:
        _text_answer.append(f"{obj[2]} | {obj[4]} | {obj[5]}")
    for obj in _text_answer:
        text_answer += f"{obj} \n\n"

    await message.answer(
        f"Назва предмету | Дата здачі | Опис завдання  \n\n\n{text_answer}", reply_markup= key_help
    )


@dp.message_handler(Command('link'))
@auth_user
async def show_all_homework(message: Message):
    db = fetchall('links', '*')
    _text_answer = []
    text_answer = ''
    for obj in db:
        _text_answer.append(f"{obj[1]} | {obj[2]}")
    for obj in _text_answer:
        text_answer += f"{obj} \n\n"

    await message.answer(f"Назва предмету |  LINK \n{text_answer}", reply_markup=key_help)


