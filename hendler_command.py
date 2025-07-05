from aiogram.filters import Command

from response_to_handlers_commands import cmd_start

async def handlers_commands(dp):
    dp.message.register(cmd_start, Command('start'))

