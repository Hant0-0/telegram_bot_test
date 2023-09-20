import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from bot.api import create_user
import buttons as kb
from core.settings import BOT_TOKEN

logging.basicConfig(level=logging.INFO)

# Токен вашого бота


bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.answer(f'Привіт, {message.from_user.username}, підпишись на наш канал', reply_markup=kb.special)

    create_user(int(message.from_user.id), message.from_user.username, message.from_user.first_name,
                message.from_user.last_name, '', True, True)


@dp.message_handler(text='Підписатися')
async def catalog(message: types.Message):
    await message.answer(f"Дякую за підписку")







if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)





# bot = Bot(token='6369633574:AAHmgNNhtCVJ9ebb-qEOD27RZPM58Rza3_4')
# dp = Dispatcher(bot)


# @dp.message_handler(commands=['start'])
# async def cmd_start(message: types.Message):
#     await message.answer("Привіт")
#
#
#
# @dp.message_handler(text='Підписатися')
# async def subscription(message: types.Message):
#     await message.answer('Нажми щоб підписатися на канал' , reply_markup=bt.main)
#     create_user(int(message.from_user.id), message.from_user.username, message.from_user.first_name,
#                 message.from_user.last_name, '', True, True)