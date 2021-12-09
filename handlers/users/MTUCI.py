from aiogram import types
from aiogram.dispatcher.filters import Command

from loader import dp


@dp.message_handler(Command("MTUCI"))
async def mtuci(message: types.Message):
    await message.answer(f"https://lms.mtuci.ru/lms/")
