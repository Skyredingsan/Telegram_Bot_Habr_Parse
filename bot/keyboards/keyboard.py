from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup

b1 = KeyboardButton('Все новости')
b2 = KeyboardButton('Последние 5 новостей')
b3 = KeyboardButton ('Свежие новости')

keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

keyboard.add(b1).add(b2).insert(b3)