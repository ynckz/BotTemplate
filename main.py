import logging # imports
import asyncio
import os
from handlers.dbAPI import *
from handlers.commandswhy import *
from dotenv import load_dotenv
from aiogram.types import Message
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram import Bot, Dispatcher, Router
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.default import DefaultBotProperties
from apscheduler.schedulers.asyncio import AsyncIOScheduler

load_dotenv()
scheduler = AsyncIOScheduler(timezone='Europe/Moscow')

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

bot = Bot(token=os.getenv("token"), default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher(storage=MemoryStorage())
router = Router(name=__name__)

async def main():
    dp.include_routers(zRouter)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

@router.message(CommandStart())
async def cmdStart(message: Message):
    await message.answer('Бот пипохуй.')
    await getUserInfo(TGid=message.from_user.id, username=message.from_user.username, fName=message.from_user.first_name)

if __name__ == "__main__":
    asyncio.run(main())