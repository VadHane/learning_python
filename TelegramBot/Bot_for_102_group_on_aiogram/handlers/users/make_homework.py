from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from random import randrange
from loader import dp, bot
from states.make_homework import make_homework
from data.config import USER_ID, ADMINS_ID
from database import insert
from main import auth_admin


@dp.message_handler(Command('make_homework'), state=None)
@auth_admin
async def begin_choose_subjects(message: types.Message):
    await message.answer('Виберіть предмет, з якого потрібно добавити домашнє завдання: \n'
                         '/математичний_аналіз \n'
                         '/алгебра_та_геометрія_лекція \n'
                         '/алгебра_та_геометрія_практика')
    await make_homework.subjects.set()


@dp.message_handler(state=make_homework.subjects)
async def choose_subjects(message: types.Message, state: FSMContext):
    choose = message.text
    await state.update_data(
        {
            'subject': choose,
            'id_user': message.from_user.id,
            'date_start': message.date.date()
        }
    )

    await message.answer(f"Ви вибрали {message.text}. \n"
                         f"Тепер введіть опис домшнього завдання:")

    await make_homework.next()


@dp.message_handler(state=make_homework.description_task)
async def create_desc_task(message: types.Message, state: FSMContext):
    description = message.text

    await state.update_data(
        {
            'description': description
        }
    )

    env_var = await state.get_data()
    name_task = env_var.get('subject')

    await message.answer(f"Ви вибрали {name_task}. \n"
                         f"Ви задали опис:\n {description} \n"
                         f"Введіть дату здачі: \n(ДД-ММ-РРРР)")
    await make_homework.next()


@dp.message_handler(state=make_homework.deadline)
async def end(message: types.Message, state: FSMContext):
    deadline = message.text
    await state.update_data(
        {
            'deadline': deadline
        }
    )

    env_var = await state.get_data()

    insert('homework', {
        'id_user': env_var.get('id_user'),
        'name_homework': env_var.get('subject'),
        'data_start': env_var.get('date_start'),
        'deadline': deadline,
        'description': env_var.get('description')
    })

    await message.answer(f"Записав в БазуДанних наступні дані: \n"
                         f"id_user: {env_var.get('id_user')} \n"
                         f"name_subject: {env_var.get('subject')} \n"
                         f"deadline: {env_var.get('deadline')} \n"
                         f"description: {env_var.get('description')}")

    await state.finish()