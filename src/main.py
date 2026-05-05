import asyncio
import logging
from aiogram import Bot, Dispatcher
from .config import Settings

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

settings = Settings()
bot = Bot(token=settings.BOT_TOKEN)
dp = Dispatcher()

async def main():
    logger.info("Бот запущен")
    try:
        await dp.start_polling(bot)
    except Exception as e:
        logger.error("Бот упал: %s", e)
    finally:
        await bot.session.close()
        logger.info("Бот остановлен")

if __name__ == "__main__":
    asyncio.run(main())