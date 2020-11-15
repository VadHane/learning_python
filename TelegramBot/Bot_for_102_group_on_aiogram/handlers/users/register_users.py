from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from random import randrange
from loader import dp, bot
from states.register_users import register_new_user
from data.config import USER_ID, ADMINS_ID
from database import insert
from keyboards.standart import key_help, start


@dp.message_handler(Command('reg'), state=None)
async def begin_register(message: types.Message):
    if message.from_user.id not in USER_ID:
        await message.answer("Ви розпочали реєстрацію як студент 102 групи. \n"
                             "Введіть ваше ім'я: ", reply_markup=types.ReplyKeyboardRemove())

        await register_new_user.name.set()
    else:
        await message.answer("Ви уже заєстрований студент!", reply_markup=types.ReplyKeyboardRemove())


@dp.message_handler(state=register_new_user.name)
async def add_user_name_and_id(message: types.Message, state: FSMContext):
    answer_user_name = message.text
    answer_user_id = message.from_user.id
    random_key = randrange(1000, 9999)

    await state.update_data(
        {
            'user_name': answer_user_name,
            'user_id': answer_user_id,
            'user_key': random_key
        }
    )

    for admin in ADMINS_ID:
        await bot.send_message(chat_id=admin, text=f"Зараз реєструється новий користувач. \n"
                                                   f"Name: {answer_user_name}, ID: {answer_user_id}, "
                                                   f"!KEY!: {random_key}")

    await message.answer('Попросіть у адміністратора (старости, заступника старости або профорга) випадково '
                         'згенерований ключ доступу. \n'
                         'Введіть ключ доступу: ')

    await register_new_user.next()


@dp.message_handler(state=register_new_user.user_id)
async def input_user_key(message: types.Message, state: FSMContext):
    user = await state.get_data()
    user_key = user.get('user_key')
    user_id = user.get('user_id')
    answer_user = message.text

    if int(user_key) == int(answer_user):
        await message.answer('Реєстрація успішно пройдена!')
        # функція запису ід користувача в БД
        insert('users', {
            'id_user': user_id,
            'name_user': user.get('user_name')
        })
        USER_ID.append(user_id)
        await message.answer("Вітаю! Ви успішно зареєструвались! \n"
                             "/help - Дізнайтесь, що я вмію :)", reply_markup=key_help)
    else:
        await message.answer('Ключ не співпадає! \n /reg - Спробуйте ще раз \n\n [Помилка №1]', reply_markup=start)

    await state.finish()
