import aiogram.utils.markdown as md
from aiogram import Bot, Dispatcher, types
import asyncio
from aiogram import Bot, Dispatcher, executor
import csv, datetime,pymysql

API_TOKEN ='1955596683:AAEPTX0SKb3_XPWYTS0PHS-GffsCqPjdd8w'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot) 

loop = asyncio.get_event_loop()
bot = Bot(API_TOKEN, parse_mode="HTML")
dp = Dispatcher(bot, loop=loop)

if __name__ == "__main__":
	from handlers import dp
	executor.start_polling(dp)
 
