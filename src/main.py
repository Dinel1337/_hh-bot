import os
import asyncio
import sys
import logging

from .config import DEBUG
from aiogram import Dispatcher, Bot
from dotenv import load_dotenv 

load_dotenv()

logging.basicConfig(
    level=logging.INFO if DEBUG else logging.ERROR,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler('bot.log', encoding='utf-8')
    ]
)
logger = logging.getLogger(__name__)

bot = Bot(os.getenv('BOT_TOKEN'))
dp = Dispatcher()

async def main():
    logger.info('Бот стартанул')
    try:
        await dp.start_polling(bot)
    except:
        logger.error('Бот умер')
    finally:
        logger.error('Завершена работа')
if __name__ == "__main__":
    asyncio.run(main())