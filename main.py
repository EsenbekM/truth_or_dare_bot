import logging
from aiogram import executor
from markups import *
from hendlers import*

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)

 
if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True) 