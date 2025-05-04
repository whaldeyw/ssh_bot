import os

from aiogram import F, Router, Bot
from aiogram.types import Message
from aiogram.filters import CommandStart
from app.kb import create_folder
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from dotenv import load_dotenv
from aiogram.filters import StateFilter

import json

load_dotenv()
reg_router = Router()
class RegState(StatesGroup):
    regPassword = State()

secret_password = os.getenv('PASSWORD') #забираем из файла .env

@reg_router.message(StateFilter(None), F.text == 'Авторизоваться')
async def add_name(message:Message, state: FSMContext):
    with open("users.json", 'r', encoding='utf-8') as f_o:
        data_from_json = json.load(f_o)
    users_id = [i for i in data_from_json]


    if str(message.from_user.id) in users_id:

        await message.answer( f'Вы уже авторизованы {message.from_user.full_name} \n'
                             f'Введите ваш запрос, например /cmd ls или создай папку при помощи кнопки ниже', reply_markup=create_folder)


        await state.clear()

    else:

        await message.answer(f'Напиши password и получи доступ к боту ')
        await state.set_state(RegState.regPassword)

        @reg_router.message(RegState.regPassword, F.text )

        async def add_password(message:Message, state: FSMContext):
            print(message.text)
            print(secret_password)
            if str(message.text) == str(secret_password):

                with open("users.json", 'r', encoding='utf-8') as f_o:
                    data_from_json = json.load(f_o)

                user_id = message.from_user.id
                user_name = message.from_user.username
                ful_name = message.from_user.full_name

                if str(user_id) not in data_from_json:
                    data_from_json[user_id] = {'user_id': user_id}, {'user_name': user_name}, {'ful_name': ful_name}

                with open('users.json', 'w', encoding='utf-8') as f_o:
                    json.dump(data_from_json, f_o, indent=4, ensure_ascii=False)

                await message.answer( f'Авторизация прошла успешно! {message.from_user.full_name} \n'
                             f'Введите ваш запрос, например /cmd ls или создай папку при помощи кнопки ниже', reply_markup=create_folder)



                await state.clear()
            else:
                await message.answer(f'Что-то пошло не так! Попробуй еще раз !😉 \n ')



