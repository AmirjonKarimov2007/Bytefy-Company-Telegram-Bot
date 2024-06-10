from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup
from loader import db
home = InlineKeyboardMarkup(row_width=2)
home.add(InlineKeyboardButton(text='Xizmatlar',callback_data='services'),
            InlineKeyboardButton(text='Ishlar',callback_data='works'),
            InlineKeyboardButton(text='Buyurtma Berish',callback_data='buy'))

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
        service_info = service[0]  # Assuming each list element contains a single dictionary
        service_btn.insert(InlineKeyboardButton(text=service_info['fullname'], callback_data=f"packages:{str(service_info['id'])}:{str(service_info['service_id'])}"))
    return service_btn
