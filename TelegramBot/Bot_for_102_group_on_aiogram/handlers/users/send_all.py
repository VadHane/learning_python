from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from loader import dp, bot
from states.send_all import send_all_
from data.config import USER_ID
from main import auth_admin


@dp.message_handler(Command('send_all'), state=None)
@auth_admin
async def send_all(message: types.Message):
    await message.answer('Ви впевнені, що хочете відправити повідомлення усім користувачам? \n'
                         '/yes   |   /no')
    await send_all_.are_you_ready.set()


@dp.message_handler(Command('yes'), state=send_all_.are_you_ready)
async def if_yes(message: types.Message):
    await message.answer('Вводіть повідомлення: ')

    await send_all_.next()


@dp.message_handler(Command('no'), state=send_all_.are_you_ready)
async def if_no(message: types.Message, state: FSMContext):
    await message.answer('Команду відмінено.')

    await state.finish()


@dp.message_handler(state=send_all_.send)
async def send(message: types.Message, state: FSMContext):
    for user in USER_ID:
        await bot.send_message(chat_id=user, text=message.text)

    await state.finish()