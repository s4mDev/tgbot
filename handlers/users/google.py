
from aiogram.dispatcher.filters import Command
from aiogram import types
from loader import dp

@dp.message_handler(Command("google"))
async def answer(message:types.Message):
    await message.answer(f"https://www.google.ru/\n"
                         f"Обязательно найди там что-нибудь интересное :)")