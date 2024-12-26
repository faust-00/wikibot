import logging
from aiogram import Bot, Dispatcher, executor, types

import wikipedia
wikipedia.set_lang('uz')

API_TOKEN = '8068795034:AAFIO57tFB8aL-JjqYivkTIFi-2bAWdWlQo'

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)

dp = Dispatcher(bot)



@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Salom, Wikibotga xush kelibsiz!")


@dp.message_handler()
async def send_wiki(message: types.Message):
    try:
        respond = wikipedia.summary(message.text)
        await message.reply(respond)

    except:

        await message.reply("Siz kiritgan mavzu bo'yicha ma'lumotlar topilmadi!")



if __name__ == '__main__':

    executor.start_polling(dp, skip_updates=True)