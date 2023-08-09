import random
import sqlite3

def generate_id():
    id = 0
    conn = sqlite3.Connection("data.db")
    c = conn.cursor()
    while True:
        n = random.randint(1234567, 7897897)
        search_id = c.execute(f"""SELECT * FROM users WHERE mice_id="{n}" """).fetchone()
        if not search_id:
            id += n
            break
    return id

def insert_user(tg_id, name, url):
    conn = sqlite3.Connection("data.db")
    c = conn.cursor()
    mice_id = generate_id()
    c.execute(f"""INSERT INTO users VALUES ("{tg_id}", "{name}", "{url}", "{mice_id}")""")
    conn.commit()
    conn.close()

def select_user(tg_id):
    conn = sqlite3.Connection("data.db")
    c = conn.cursor()
    res = c.execute(f""" SELECT * FROM users WHERE tg_id="{tg_id}" """).fetchone()
    conn.commit()
    conn.close()
    user = {}
    user["tg_id"] = res[0]
    user["name"] = res[1]
    user["url"] = res[2]
    user["mice_id"] = res[3]

    return user

def select_users():
    conn = sqlite3.Connection("data.db")
    c = conn.cursor()
    users = c.execute(f""" SELECT * FROM users""").fetchall()
    conn.commit()
    conn.close()
    return users

def delete_user(mice_id):
    conn = sqlite3.Connection("data.db")
    c = conn.cursor()
    c.execute(f"""DELETE FROM useers WHERE mice_id="{mice_id}" """)
    conn.commit()
    conn.close()

while True:
    question = input("Nima qilamiz? ")
    if question.lower() == "createuser":
        tg_id = input("Telegram idsini kiriting: ")
        name = input("Tizimdagi ismini kiriting: ")
        url = input("Passport rasmining url manzilini kiriting: ")
        insert_user(tg_id, name, url)
        user = select_user(tg_id)
        print(f"""\n USER QO'SHILDI!\n\n\tTelegram id: {user["tg_id"]}\n\tTizimdagi ismi: {user["name"]}\n\tPassport url manzili: {user["url"]}\n\tMaxsus id: {user["mice_id"]}""")
    elif question.lower() == "selectusers":
        s = 0
        res = "\nFOYDALANUVCHILAR RO'YHATI:\n\t"
        for i in select_users():
            s += 1
            res += f"{s}. {i[0]}  {i[1]}  {i[2]}  {i[3]}\n"
        print(res)
    elif question.lower() == "quit":
        print("Dastur to'xtatildi!")
        break
    else:
        print("Noma'lum buyruq")


    @dp.message_handler(commands=['start'])
    async def send_help(message: types.Message):
        await bot.send_chat_action(message.chat.id, types.ChatActions.TYPING)
        await message.reply("Assalamu alaykum siz Avia kargo botiga xush kelibsiz", reply_markup=panel)


    dp.message_handler(lambda message: message.text == "ID")


    async def id_olish(message: types.Message):

        await message.reply("Ism Familiyangizni jonating)", reply_markup=RMV)

        # Set the user's state to waiting_for_name
        await UserInfo.waiting_for_name.set()