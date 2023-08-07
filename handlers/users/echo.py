from aiogram import types

from ...loader import dp


# code

@dp.message_handler(content_types=['text'])
async def replyer(message: types.Message):
    if message.text == "salom":
        await message.answer("Assalomu alaykum!")