from aiogram import types
from loader import dp
from sqlite3 import Connection

async def dataBase(f):
    conn = Connection("data.db")
    c = conn.cursor()
    f(c)
    conn.commit()
    conn.close()


# code

@dp.message_handler()
async def replyer(message: types.Message):
    await message.answer(message.text)