from aiogram import Dispatcher
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext

def register_admin_handlers(dp: Dispatcher):
    # todo: register all admin handlers
    pass

class FSMAdmin(StatesGroup):
    state = State()
    news = State()
    Fake = State()

#@Dispatcher.message_handler(commands="Загрузить", state = None)
#async def cm_start(message: types.Message):