from aiogram import Bot, Dispatcher
import asyncio
from app.commands import set_commands
from app.start import start_router
from app.registr import reg_router
from app.ssh_coonect import router_ssh
from app.other import other_router
from dotenv import load_dotenv
import os, logging, sys


load_dotenv()
dp = Dispatcher()

async def main():

    token = os.getenv('TG_TOKEN')
    bot = Bot(token=token)

    dp.include_router(start_router)
    dp.include_router(router_ssh)
    dp.include_router(reg_router)
    dp.include_router(other_router)

    await set_commands(bot)
    await dp.start_polling(bot)




if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')


