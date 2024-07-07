import logging
import asyncio
import os
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import BotCommand
from config import BOT_TOKEN
from handlers import register_handlers

# Установка уровня логирования
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(storage=MemoryStorage())

# Убедимся, что папка для изображений существует
if not os.path.exists('img'):
    os.makedirs('img')


async def on_startup():
    await bot.set_my_commands([
        BotCommand(command="/start", description="Запустить бота"),
        BotCommand(command="/help", description="Получить помощь"),
        BotCommand(command="/voice", description="Отправить голосовое сообщение"),
        BotCommand(command="/translate_on", description="Включить режим переводчика"),
        BotCommand(command="/translate_off", description="Выключить режим переводчика")
    ])


async def main():
    register_handlers(dp)
    await on_startup()
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
