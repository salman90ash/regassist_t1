from ..create_bot import bot, dp
from aiogram import types, Dispatcher


# @dp.message_handler()
async def echo(message: types.Message):
    text = message.text
    msg = '\xF0\x9F\x93\x9D'
    msg2 = '\xE2\x9C\x85'
    msg1 = '✅'
    send_msg = await bot.send_message(chat_id=message.from_user.id, text=text, parse_mode='HTML')
    # await send_msg
    print(send_msg)
    await message.delete()
    # await send_msg.edit_text('bew')


def register_handlers_common(dp: Dispatcher):
    dp.register_message_handler(echo)
