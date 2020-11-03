from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from random import randrange
from loader import dp, bot
from states.register_users import register_new_user
from data.config import ADMINS_ID


@dp.message_handler(Command('reg'), state=None)
async def begin_register(message: types.Message):
    await message.answer("Ви розпочали реєстрацію як студент 102 групи. \n"
                         "Введіть ваше ім'я: ")

    await register_new_user.name.set()


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
    else:
        await message.answer('Ключ не співпадає! \n\n [Помилка №1]')

    await state.finish()