from aiogram import Bot,types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from constant import API_KEY_TELEGRAM

bot = Bot(token = API_KEY_TELEGRAM)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def echo_send(message: types.Message):
	await message.reply("Привет!\nПокаа")
	await message.answer(message.text)

@dp.message_handler()
async def echo_message(msg:types.Message):
	await msg.reply_voice(msg.from_user.id, caption='уу сука' )




executor.start_polling(dp, skip_updates=True)