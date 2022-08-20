from aiogram import Bot,types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from constant import API_KEY_TELEGRAM,API_KEY_IMDB

import requests

bot = Bot(token = API_KEY_TELEGRAM)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def echo_send(message: types.Message):
	await message.reply("Привет!\nПокаа")
	await message.answer(message.text)


@dp.message_handler(commands=["top-10-movie"])
async def echo_top_movie(msg: types.Message):
	respone = requests.get(f"https://imdb-api.com/en/API/Top250Movies/{API_KEY_IMDB}").json()['items']
	list_of_films = []
	for i in range(0,10):
		list_of_films.append(respone[i]['title'])
	
	for i in range(0,len(list_of_films)):
		await msg.reply(list_of_films[i])



executor.start_polling(dp, skip_updates=True)