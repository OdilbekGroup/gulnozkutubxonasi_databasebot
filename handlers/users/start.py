from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from sqlite3 import Connection
from loader import dp
from btns import mainKB

async def dataBase(f):
    conn = Connection("data.db")
    c = conn.cursor()
    f(c)
    conn.commit()
    conn.close()



@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    user = []
    @dataBase
    def send_request(c):
        user.append( c.execute(f"""SELECT * FROM users WHERE id="{message.from_user.id}" """).fetchone())
    if not user[0]:
        await message.answer("Assalomu alaykum, ismingizni kiriting.")
        await dp.register_next_step_handler(message, createuser)

async def createuser(message: types.Message):
    @dataBase
    def send_request(c):
        c.execute("""CREATE TABLE IF NOT EXISTS users(id TEXT, name TEXT, menus TEXT, filesCount TEXT)""")
        c.execute(f"""INSERT INTO users VALUES ("{message.from_user.id}", "{message.text}", "", "0")""")
    await message.answer("Siz asosiy menyudasiz!", reply_markup=mainKB)
