import logging
from googletrans import Translator
from aiogram import types
from aiogram.types import FSInputFile
from config import VOICE_FILE_PATH

translator = Translator()


async def download_photo(message: types.Message):
    photo = message.photo[-1]
    file_id = photo.file_id
    file_path = f'img/{file_id}.jpg'
    await message.bot.download(photo, destination=file_path)
    logging.info(f'Фото сохранено как {file_path}')


async def send_voice_message(message: types.Message):
    voice_file = FSInputFile(VOICE_FILE_PATH)
    await message.answer_voice(voice_file)
    logging.info(f'Голосовое сообщение отправлено: {VOICE_FILE_PATH}')


def translate_text(text: str) -> str:
    result = translator.translate(text, src='ru', dest='en')
    logging.info(f'Перевод: {text} -> {result.text}')
    return result.text


def generate_ai_response():
    return ('Искусственный интеллект — это свойство искусственных интеллектуальных систем выполнять '
            'творческие функции, которые традиционно считаются прерогативой человека; наука и технология '
            'создания интеллектуальных машин, особенно интеллектуальных компьютерных программ')
