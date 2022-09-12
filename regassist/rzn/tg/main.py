# import asyncio
from aiogram import executor
from create_bot import dp
from handlers import client, common

client.register_handlers_client(dp)
common.register_handlers_common(dp)

if __name__ == "__main__":
    # from rzn.tg.handlers.common import dp
    executor.start_polling(dp, skip_updates=True)
