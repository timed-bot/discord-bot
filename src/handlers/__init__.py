import inject

from discord.ext.commands import Bot, Context
from discord import Interaction
from data import commands
from services.global_config import GlobalConfigService
from . import testing
from . import bot_events


def register_handlers(bot: Bot):
    globalConfigService: GlobalConfigService = inject.instance(
        GlobalConfigService)

    @bot.event
    async def on_ready():
        '''
        This event is triggered when the bot is ready to receive commands.
        '''
        await bot_events.on_ready(bot)

    @bot.command(name=commands.PING)
    async def ping(ctx: Context):
        '''
        A simple ping command.
        '''
        await testing.ping(ctx)

    if globalConfigService.env == 'dev':
        @bot.tree.command(name=commands.TEST, description='A simple test command.')
        async def test_dev(interaction: Interaction):
            '''
            A simple test command.
            '''
            await testing.test(interaction)

        @bot.tree.command(name=commands.STOP, description='A simple ping command.')
        async def stop_dev(interaction: Interaction):
            '''
            A simple stop command.
            '''
            await testing.stop(interaction)
