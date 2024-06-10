from loader import db,bot,dp
from aiogram import types
from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup
from magic_filter import F
from keyboards.inline.pages_keyboard import services_keyboard,service_keyboard
from states.pages_state import PAGES_STATES

@dp.callback_query_handler(text="services",state='*')
async def services(call: types.CallbackQuery):
    await call.answer(cache_time=1)
    markup = await services_keyboard()
    await call.message.edit_text("Xizmatlar Haqida Malumot olishingiz mumkin!",reply_markup=markup)


@dp.callback_query_handler(text_contains='service:',state='*')
async def service_packages(call: types.CallbackQuery):
    await call.answer(cache_time=1)
    data = call.data.rsplit(":")
    id = data[1]
    services = await db.select_all_services(id=int(id))
    markup = await service_keyboard(services)
    service = await db.select_service(id=int(id))
    print(services)
    text = f"<b><a href=\"{service[0]['photo']}\">{service[0]['fullname']}ning Tarif rejalari! </a></b>\n\n"
    text+=f"<b>{service[0]['description']}</b>\n\n"
    
    await call.message.edit_text(text=text)
@dp.message_handler(text='a')
async def funksiya(message: types.Message):
    p = await db.select_all_services(service_id=3,iid=1)
    print(p)
