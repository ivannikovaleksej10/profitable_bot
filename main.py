import asyncio
import logging
import sys
import os

from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, html

from app.handlers import router
from app.database.models import async_main


load_dotenv()


async def main():
    await async_main()
    bot = Bot(token=os.getenv("TOKEN"))
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот выключен!")