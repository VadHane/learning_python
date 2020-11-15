from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from loader import dp, bot
from states.add_new_admin import add
from data.config import USER_ID, ADMINS_ID
from database import insert, fetchall
from keyboards.standart import key_help, start
from main import auth_admin


@dp.message_handler(Command('add_new_admin'), state=None)
@auth_admin
async def start(message: types.Message):
    db = fetchall('users', '*')
    _text_answer = []
    text_answer = ''
    for obj in db:
        _text_answer.append(f"{obj[0]} | {obj[1]}")
    for obj in _text_answer:
        text_answer += f"{obj} \n\n"

    await message.answer(
        f"id user |  name user \n\n{text_answer} \n\n Введіть id користувача!", reply_markup=types.ReplyKeyboardRemove()
    )
    await add.user_id.set()


@dp.message_handler(state=add.user_id)
async def add_user(message: types.Message, state: FSMContext):
    id_user = int(message.text)
    if id_user in USER_ID and id_user not in ADMINS_ID:
        insert('admins', {
            'id_user': id_user
        })
        await bot.send_message(
            chat_id=id_user, text='Вам надано права адміністратора. \n /help - Список усіх доступних програм'
        )
        await message.answer('Права адміністратора успішно обновлені.')

    elif id_user not in USER_ID:
        await message.answer('Не знайдено користувача!')
    elif id_user in ADMINS_ID:
        await message.answer('У цього користувача уже є права адміністратора.')

    await state.finish()