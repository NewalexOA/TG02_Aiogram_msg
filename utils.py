import aiofiles
import aiohttp
from aiogram import types
from config import BOT_TOKEN
import logging


async def download_photo(message: types.Message):
    photo = message.photo[-1]  # Берем фотографию с наибольшим разрешением
    file_id = photo.file_id
    file_path = f'img/{file_id}.jpg'
    await message.bot.download(photo, destination=file_path)
    logging.info(f'Фото сохранено как {file_path}')


def generate_ai_response():
    return ('Искусственный интеллект — это свойство искусственных интеллектуальных систем выполнять '
            'творческие функции, которые традиционно считаются прерогативой человека; наука и технология '
            'создания интеллектуальных машин, особенно интеллектуальных компьютерных программ')
