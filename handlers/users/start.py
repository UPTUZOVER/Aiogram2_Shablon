
from Aiogram-Bot-Template.loader import dp

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart



@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Assalomu alaykum, {message.from_user.full_name}!Men tarjimon botman")
