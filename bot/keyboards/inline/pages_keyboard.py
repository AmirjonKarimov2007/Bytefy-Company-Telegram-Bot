from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup
from loader import db
from data.config import ADMINS
ADMINS = [int(i) for i in ADMINS]
async def home_keyboard(telegram_id):
    home = InlineKeyboardMarkup(row_width=2)
    home.add(InlineKeyboardButton(text='Xizmatlar',callback_data='services'),
        InlineKeyboardButton(text='Ishlar',callback_data='works'),
        InlineKeyboardButton(text='Buyurtma Berish',callback_data='buy'))
    if telegram_id in ADMINS:
        home.add(InlineKeyboardButton(text="◀️Orqaga",callback_data='back_to_main_menu'))
        
    return home
async def services_keyboard():
    services_btn = InlineKeyboardMarkup(row_width=2)
    services = await db.select_services()
    for service in services:
        services_btn.insert(InlineKeyboardButton(text=service['fullname'],callback_data=f"service:{service['id']}"))
    services_btn.add(InlineKeyboardButton(text="◀️Orqaga",callback_data='home'))
    return services_btn
    

async def service_keyboard(services):
    service_btn = InlineKeyboardMarkup(row_width=3)
    for service in services:
        service_info = service[0]  
        service_btn.insert(InlineKeyboardButton(text=service_info['fullname'], callback_data=f"packages:{str(service_info['iid'])}:{str(service_info['service_id'])}"))
    service_btn.add(InlineKeyboardButton(text="◀️Orqaga",callback_data=f"services"))

    return service_btn

async def package_keyboard(id):
    package_btn = InlineKeyboardMarkup(row_width=1)
    package_btn.insert(InlineKeyboardButton(text="🛒Buyurtma Berish",callback_data='buy'))
    package_btn.add(InlineKeyboardButton(text="◀️Orqaga",callback_data=f"service:{str(id)}"))
    return package_btn
