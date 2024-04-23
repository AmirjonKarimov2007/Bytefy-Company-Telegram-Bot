from loader import db,bot,dp
from aiogram import types
from keyboards.inline import pages_keyboard
@dp.message_handler(commands='home',state='*')
async def home_page(message: types.Message):
    await message.answer("Bo'limni Tanlang!",reply_markup=pages_keyboard.home)
    servis = await db.select_all_services()