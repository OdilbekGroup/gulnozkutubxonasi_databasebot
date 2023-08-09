from aiogram import types

def createReplyKeyboardMurkup(lst, width):
    KB = types.ReplyKeyboardMarkup(row_width=width, resize_keyboard=True)
    KB.add(lst)
    return KB

mainKB = createReplyKeyboardMurkup(["Taqdimotlar", "Videodarslar", "Dars ishlanmalar", "Ko'rgazmalar", "Dasturlar", "Dastur kodlari"], 2)

