from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

zRouter = Router(name=__name__)

@zRouter.message(Command('help'))
async def cmdHelp(message: Message):
     await message.answer('Тут расписаны все команды, их значения и как их использовать.\n /start - Перезапуск бота \n /help - выводит это сообщение')