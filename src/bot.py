'''
This is the main bot file. It contains the bot instance and the event handlers.
'''
from discord import Intents
from discord.ext import commands
import inject

from services.global_config import GlobalConfigService
from handlers import register_handlers


def create_bot() -> commands.Bot:
    '''
    Creates a bot instance.
    '''
    GlobalConfig: GlobalConfigService = inject.instance(GlobalConfigService)

    bot = commands.Bot(
        command_prefix=GlobalConfig.default_prefix, intents=Intents.all())
    register_handlers(bot)

    return bot
