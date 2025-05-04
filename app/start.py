import asyncio
import json
from aiogram import Router , F, Bot
from aiogram.filters import CommandStart
from aiogram.types import Message

from app.kb import auth
from app.kb import create_folder
start_router = Router()



@start_router.message(CommandStart())
async def cmd_start(message: Message, bot: Bot):
        with open("users.json", 'r', encoding='utf-8') as f_o:
            data_from_json = json.load(f_o)
        users_id = [i for i in data_from_json]

        if str(message.from_user.id) in users_id:
            await message.answer(f'Вы уже авторизованы {message.from_user.full_name} \n'
                                 f'Введите ваш запрос, например /cmd ls или создай папку при помощи кнопки ниже', reply_markup=create_folder )

        else:
            await bot.send_message(message.from_user.id, f"Привет, 👏 {message.from_user.full_name} "
                                                     f"Пройди простую авторизацию", reply_markup=auth)
