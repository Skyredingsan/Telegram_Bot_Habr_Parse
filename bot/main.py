from aiogram import Dispatcher
from bot.misc import dp
from aiogram.utils import executor

from bot.filters import register_all_filters
from bot.handlers import register_all_handlers

async def __on_start_up(dp: Dispatcher):
    register_all_filters(dp)
    register_all_handlers(dp)

def start_bot():
    executor.start_polling(dp, skip_updates=True, on_startup=__on_start_up)
    print('Bot start')