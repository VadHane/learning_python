# Telegram bot v1.0
#   01.11.2020
#
#
#
#
#
#
#
#
###########################

from loader import bot, storage


async def on_shutdown(dp):
    await bot.close()
    await storage.close()


if __name__ == '__main__':
    from handlers.users.handlers import send_to_admin
    from aiogram import executor
    from handlers import dp

    executor.start_polling(dp, on_shutdown=on_shutdown, on_startup=send_to_admin)


