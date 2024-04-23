from loader import db,bot,dp
from aiogram import types
from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup
from magic_filter import F

from states.pages_state import PAGES_STATES

@dp.callback_query_handler(text="services",state='*')
async def services(call: types.CallbackQuery):
    await call.answer(cache_time=1)
    
    services = await db.select_all_services()
    services_btn = InlineKeyboardMarkup(row_width=2)

    for service in services:
        services_btn.insert(InlineKeyboardButton(text=service['name'],callback_data=f"service:{service['id']}"))
    services_btn.add(InlineKeyboardButton(text="⬅️Orqaga",callback_data='back_main_menu'))
    await call.message.edit_text("Xizmatlar Haqida Malumot olishingiz mumkin!",reply_markup=services_btn)


@dp.callback_query_handler(text_contains='service:',state='*')
async def service_packages(call: types.CallbackQuery):
    await call.answer(cache_time=1)
    data = call.data.rsplit(":")
    id = data[1]
    service_btn = InlineKeyboardMarkup(row_width=3)
    service_data = await db.select_service(id=int(id))
    # print(service_data)
    for service in service_data:
        if 'basic_price' in service:
            print(service['basic_price'])
            service_btn.insert(InlineKeyboardButton(text=str(service['basic_price']),callback_data=f"service:{service['name']}:{service['basic_price']}"))
        if 'standard_price' in service:
            service_btn.insert(InlineKeyboardButton(text=str(service['standard_price']),callback_data=f"service:{service['name']}:{service['standard_price']}"))
        if 'premium_price' in service:
            service_btn.insert(InlineKeyboardButton(text=str(service['premium_price']),callback_data=f"service:{service['name']}:{service['premium_price']}"))

    service_btn.add(InlineKeyboardButton(text="⬅️Orqaga",callback_data='back_main_menu'))
    
    text = f"<a href=\"{service_data[0]['photo']}\">{service_data[0]['name']}ning Tarif rejalari! </a>"
    await call.message.edit_text(text=text, reply_markup=service_btn)

