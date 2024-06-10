from loader import db,bot,dp
from aiogram import types
from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup
from magic_filter import F
from keyboards.inline.pages_keyboard import services_keyboard,service_keyboard,package_keyboard
from states.pages_state import PAGES_STATES

from aiogram.utils.exceptions import MessageNotModified

@dp.callback_query_handler(text="services", state='*')
async def services(call: types.CallbackQuery):
    try:
        await call.answer(cache_time=1)
    except:
        pass

    markup = await services_keyboard()
    new_text = "<b>Xizmatlarimiz Haqida Malumot olishingiz mumkin!</b>"

    if call.message.text != new_text or call.message.reply_markup != markup:
        try:
            await call.message.edit_text(text=new_text, reply_markup=markup)
        except MessageNotModified:
            pass  
    else:
        await call.answer("Message is already up to date.", show_alert=False)

@dp.callback_query_handler(text_contains='service:',state='*')
async def service_packages(call: types.CallbackQuery):
    try:
        await call.answer(cache_time=1)
    except:
        pass
    data = call.data.rsplit(":")
    id = data[1]
    services = await db.select_all_services(id=int(id))
    markup = await service_keyboard(services)
    service = await db.select_service(id=int(id))
    text = f"<b><a href=\"{service[0]['photo']}\">{service[0]['fullname']}ning Tarif rejalari! </a></b>\n\n"
    text+=f"<b>{service[0]['description']}</b>\n\n"
    for servis in services:
        text+=f"<b>🔰{servis[0]['fullname']}: {servis[0]['price']}💲\n</b>"

    text+=f"\n<b>Bizning Kanal:👉 @Euro_Asia_Project_Rasmiy</b>"
    
    
    await call.message.edit_text(text=text,reply_markup=markup)


@dp.callback_query_handler(text_contains='packages:',state='*')
async def service_packages(call: types.CallbackQuery):
    try:
        await call.answer(cache_time=1)
    except:
        pass
    data = call.data.rsplit(":")
    id = data[1]
    service_id = data[2]
    service = await db.select_all_services(service_id=int(service_id),iid=int(id))
    name = await db.select_service(id=int(service_id))
    service_name = name[0]['fullname']
    for servis in service:
        package_name = servis[0]['fullname']
    text = f"<b><a href='{name[0]['photo']}'>{service_name} Xizmatimizning {package_name} paketi</a></b>\n\n"
    text += f"<b>▪️Qulayliklar</b>\n"
    text +=f"<b>{servis[0]['description']}</b>\n"
    text+=f"\n<b>Bizning Kanal:👉 @Euro_Asia_Project_Rasmiy</b>"

    markup = await package_keyboard(id=service_id)
    await call.message.edit_text(text=text,reply_markup=markup)