import inject

from discord.ext.commands import Bot, Context
from discord import Interaction
from ui import commands
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

    @bot.event
    async def on_interaction(interaction: Interaction):
        '''
        This event is triggered when the bot receives an interaction.
        '''
        await bot_events.on_interaction(interaction)

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

        @bot.tree.command(name=commands.STOP, description='A stop command.')
        async def stop_dev(interaction: Interaction):
            '''
            A simple stop command.
            '''
            await testing.stop(interaction)

        @bot.tree.command(name=commands.TEST_BUTTON, description='A stop command.')
        async def button_dev(interaction: Interaction):
            '''
            A simple stop command.
            '''
            await testing.button_dev(interaction)
