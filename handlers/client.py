from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client

# @dp.message_handler(commands=['start','help'])
async def command_start(message : types.Message):
    try:
        await message.answer('Привет! Укажи свой класс:', reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply('Общение с ботом через ЛС, напишите ему:\nhttps://t.me/https://t.me/Times_Table_bot')

# @dp.message_handler(commands=['Расписание_уроков'])
async def time_table(message : types.Message):
    await message.answer('Расписание:')


def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(command_start, commands=['start','help'])
    dp.register_message_handler(time_table,commands=['Расписание_уроков'])

