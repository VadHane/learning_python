from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from random import randrange
from loader import dp, bot
from states.add_link import add
from data.config import USER_ID, ADMINS_ID
from database import insert
from main import auth_admin


@dp.message_handler(Command('add_link'), state=None)
@auth_admin
async def start(message: types.Message):
    await message.answer('Введіть назву лінка: \n\n /stop - Зупинити процес')

    await add.name_link.set()


@dp.message_handler(Command('stop'), state=add.name_link)
async def stop(message: types.Message, state: FSMContext):
    await message.answer('Процес зупинено.')

    await state.finish()


@dp.message_handler(state=add.name_link)
async def add_name(message: types.Message, state: FSMContext):
    link_name = message.text
    await state.update_data({
        'name': link_name
    })

    await message.answer('Введіть лінк: ')
    await add.next()


@dp.message_handler(state=add.link)
async def add_link(message: types.Message, state: FSMContext):
    link = message.text
    env_ver = await state.get_data()
    name_link = env_ver.get('name')

    insert('links', {
        'name_link': name_link,
        'link': link
    })

    await message.answer(f"Записано в базу наступні данні: \n"
                         f"name_link: {name_link} \n"
                         f"link: {link}")
    await state.finish()