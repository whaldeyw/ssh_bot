import os, json
from aiogram import Router ,Bot, F
from aiogram.filters import Command
from aiogram.types import Message
from dotenv import load_dotenv

load_dotenv()

other_router = Router()



@other_router.message(Command("help"))
async def cmd_help(message: Message, bot: Bot):

            await bot.send_message(message.from_user.id, f" {message.from_user.full_name} Кнопка находится в разработке в разработке")

@other_router.message(F.text == 'посетители')
async def cmd_help(message: Message, bot: Bot):
    if str(message.from_user.id) == os.getenv('ADMIN_ID'):

        with open("us.json", 'r', encoding='utf-8') as f_o:
            data_from_json = json.load(f_o)
        for i, v in data_from_json.items():
            full_name = v[2]['ful_name']
            user_name = v[1]["user_name"]
            await message.answer(f'User_Name  - {user_name}, Полное Имя: {full_name}')

    else:
        await bot.send_message(message.from_user.id, f" {message.from_user.full_name} Кнопка находится в разработке в разработке")