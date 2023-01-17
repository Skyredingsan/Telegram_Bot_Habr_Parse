from aiogram import types, Dispatcher
from aiogram.utils.markdown import hbold, hunderline, hcode, hlink
from aiogram.dispatcher.filters import Text
from bot.misc import dp, bot
from bot.keyboards import keyboard
from bot.parser import check_news_update
import json
from pathlib import Path
import datetime


@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Welcome', reply_markup=keyboard)
        await message.delete()
    except:
        await message.reply('Общение с ботом через ЛС')


@dp.message_handler(commands=['help'])
async def command_help(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Список команд: help, start', reply_markup=keyboard)
        await message.delete()
    except:
        await message.reply('Общение с ботом через ЛС')


@dp.message_handler(Text(equals="Все новости"))
async def get_all_news(message: types.Message):
    with open(Path.home() / ("PycharmProjects\\TwitchTgBot\\bot\\parser\\news_dict.json"),
              encoding='utf-8') as json_file:
        news_dict = json.load(json_file)

    for k, v in sorted(news_dict.items()):
        news = f"{v['article_date_time']}\n " \
               f"{hlink(v['articles_title'], v['article_url'])}\n" \
               f"{v['article_desc']}\n"

        await message.answer(news)


@dp.message_handler(Text(equals="Последние 5 новостей"))
async def get_last_five_news(message: types.Message):
    with open(Path.home() / ("PycharmProjects\\TwitchTgBot\\bot\\parser\\news_dict.json"),
              encoding='utf-8') as json_file:
        news_dict = json.load(json_file)

    for k, v in sorted(news_dict.items())[-5:]:
        news = f"{v['article_date_time']}\n " \
               f"{hlink(v['articles_title'], v['article_url'])}\n" \

        await message.answer(news)


@dp.message_handler(Text(equals="Свежие новости"))
async def get_fresh_news(message: types.Message):
    fresh_news = check_news_update()

    if len(fresh_news) >= 1:
        for k, v in sorted(fresh_news.items()):
            news = f"{v['article_date_time']}\n " \
                   f"{hlink(v['articles_title'], v['article_url'])}\n" \

            await message.answer(news)
    else:
        await message.answer("Пока новых новостей нет")


def register_user_handlers(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start'])
    dp.register_message_handler(command_help, commands=['help'])
    dp.register_message_handler(get_last_five_news, Text(equals="Последние 5 новостей"))
    dp.register_message_handler(get_all_news, Text(equals="Все новости"))
    dp.register_message_handler(get_fresh_news, Text(equals="Свежие новости"))
