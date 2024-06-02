import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from app import app  # Убедитесь, что app импортирован из вашего Flask приложения

API_TOKEN = '7437493349:AAHzEDY6h8h6UXWGOsSTVI56Bc-r8EYw8Hw'

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Генерация веб-приложения
WEB_APP_URL = "http://localhost:5000"  # Убедитесь, что URL соответствует вашему приложению

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Привет! Нажми на кнопку ниже, чтобы начать майнинг.",
                        reply_markup=InlineKeyboardMarkup().add(
                            InlineKeyboardButton(text="Начать майнинг", web_app=types.WebAppInfo(url=WEB_APP_URL))
                        ))

if __name__ == '__main__':
    # Запуск Flask приложения
    import threading
    threading.Thread(target=lambda: app.run(host='0.0.0.0', port=5000)).start()

    # Запуск Telegram бота
    executor.start_polling(dp, skip_updates=True)
