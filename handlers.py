import random
from aiogram import Router, types, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from utils import download_photo, generate_ai_response, send_voice_message, translate_text

TRANSLATE_MODE = False

router = Router()


@router.message(CommandStart())
async def start_command(message: Message):
    await message.answer(f'Приветики, {message.from_user.first_name}')


@router.message(Command(commands=["help"]))
async def help_command(message: Message):
    help_text = (
        "Этот бот умеет выполнять следующие команды:\n"
        "/start - Запустить бота\n"
        "/help - Получить помощь по командам бота\n"
        "/voice - Отправить голосовое сообщение\n"
        "/translate_on - Включить режим переводчика, который переводит любой текст на английский\n"
        "/translate_off - Выключить режим переводчика\n"
    )
    await message.answer(help_text)


@router.message(Command(commands=["voice"]))
async def voice(message: Message):
    await send_voice_message(message)


@router.message(Command(commands=["translate_on"]))
async def translate_on(message: Message):
    global TRANSLATE_MODE
    TRANSLATE_MODE = True
    await message.answer("Режим переводчика включен.")


@router.message(Command(commands=["translate_off"]))
async def translate_off(message: Message):
    global TRANSLATE_MODE
    TRANSLATE_MODE = False
    await message.answer("Режим переводчика выключен.")


@router.message(F.photo)
async def react_photo(message: Message):
    answers_list = ['Ого, какая фотка!', 'Непонятно, что это такое', 'Не отправляй мне такое больше']
    rand_answer = random.choice(answers_list)
    await message.answer(rand_answer)
    await download_photo(message)


@router.message()
async def translate_mode(message: Message):
    global TRANSLATE_MODE
    if TRANSLATE_MODE:
        translated_text = translate_text(message.text)
        await message.answer(translated_text)


def register_handlers(dp):
    dp.include_router(router)
