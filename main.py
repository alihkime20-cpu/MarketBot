import asyncio
from aiogram import Bot, Dispatcher

from config import BOT_TOKEN
from database import init_db


async def main():
    # إنشاء قاعدة البيانات
    init_db()

    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    print("Bot is running...")

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
