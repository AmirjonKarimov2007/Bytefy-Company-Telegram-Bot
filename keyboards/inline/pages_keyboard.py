from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup
home = InlineKeyboardMarkup(row_width=2)
home.add(InlineKeyboardButton(text='Xizmatlar',callback_data='services'),
            InlineKeyboardButton(text='Ishlar',callback_data='works'),
            InlineKeyboardButton(text='Buyurtma Berish',callback_data='buy'))
