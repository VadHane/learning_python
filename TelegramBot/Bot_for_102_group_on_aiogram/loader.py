import logging
from aiogram import Bot, Dispatcher, types
from data.config import BOT_TOKEN
from aiogram.contrib.fsm_storage.memory import MemoryStorage


bot = Bot(BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s] %(message)s',
                    level=logging.INFO)

