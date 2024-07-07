import random
from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from utils import download_photo, generate_ai_response

router = Router()


@router.message(CommandStart())
async def start(message: Message):
    await message.answer(f'Приветики, {message.from_user.first_name}')


@router.message(Command(commands=["help"]))
async def help(message: Message):
    await message.answer("Этот бот умеет выполнять команды:\n/start\n/help")


@router.message(F.photo)
async def react_photo(message: Message):
    answers_list = ['Ого, какая фотка!', 'Непонятно, что это такое', 'Не отправляй мне такое больше']
    rand_answer = random.choice(answers_list)
    await message.answer(rand_answer)
    await download_photo(message)  # Используем функцию из utils.py


@router.message(F.text == "что такое ИИ?")
async def aitext(message: Message):
    response = generate_ai_response()
    await message.answer(response)


def register_handlers(dp):
    dp.include_router(router)
