from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1 = KeyboardButton('/Меню')
b2 = KeyboardButton('/10')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)

kb_client.row(b1,b2)