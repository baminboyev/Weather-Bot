from aiogram import types,Dispatcher,Bot,executor
token = "5874949169:AAGAjRYJrQKAeluSxvS0NNtEdVOumLrNUS0" # Telegramdan olgan tokeningizni joylaysiz.
from weather import obhavo
bot = Bot(token=token)
dp = Dispatcher(bot)
@dp.message_handler(commands='start')
async def start(message:types.Message):
    await message.answer("Assalomu alaykum!\nOb-havo ma'lumotlarini bilish uchun shahar yoki viloyat nomini kiriting! 👇")
@dp.message_handler(content_types='text')
async def first_handler(message:types.Message):
    shahar = message.text
    data = obhavo(shahar)
    if data=='Error':
        await message.answer("Malumot topilmadi!")
    else:
        await message.answer(data)

if __name__=='__main__':
    executor.start_polling(dp)