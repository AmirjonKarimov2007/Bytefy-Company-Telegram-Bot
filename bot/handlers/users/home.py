from loader import db,bot,dp
from aiogram import types
from keyboards.inline import pages_keyboard
@dp.callback_query_handler(text='home',state='*')
async def home_page(call: types.CallbackQuery):
    await call.message.edit_text("Bo'limni Tanlang!",reply_markup=pages_keyboard.home)
    