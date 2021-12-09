from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.utils.markdown import hlink

from loader import dp


@dp.message_handler(Command("photo"))
async def get_photo(message:types.Message):
    await message.answer(f"если ты любитель фотографий\n"
                         f"на" + hlink(" фотографии","https://www.pinterest.ru/"))