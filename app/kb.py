from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


auth = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Авторизоваться')],
], resize_keyboard=True, input_field_placeholder='Введите пароль')


create_folder = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Создать папку')],
], resize_keyboard=True)

