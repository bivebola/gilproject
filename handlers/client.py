from aiogram import types
from create_bot import dp, bot

@dp.message_handler(commands=['start','help'])
async def command_start(message : types.Message):
    try:
        await message.answer('Привет! Это бот с расписанием уроков школы №14.')
        await message.delete()
    except:
        await message.reply('Общение с ботом через ЛС, напишите ему:\nhttps://t.me/https://t.me/Times_Table_bot')

@dp.message_handler(commands=['Расписание_уроков'])
async def time_table(message : types.Message):
    await message.answer('Расписание:')
