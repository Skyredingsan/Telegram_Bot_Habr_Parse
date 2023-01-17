from aiogram import Bot, Dispatcher
from bot.misc import TgKey
from aiogram.contrib.fsm_storage.memory import MemoryStorage

bot = Bot(token=TgKey.TOKEN, parse_mode='HTML')
dp = Dispatcher(bot)