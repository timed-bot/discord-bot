'''
This is the main entry point of the bot.
'''

from sys import argv
from discord import Intents, Interaction
from discord.ext import commands
from env import config_path

from services import GlobalConfigService

bot = commands.Bot(command_prefix='>', intents=Intents.all())


@bot.event
async def on_ready():
    '''
    This event is triggered when the bot is ready to receive commands.
    '''

    synced = await bot.tree.sync()
    print(f'Synced {len(synced)} commands')


@bot.command()
async def ping(ctx):
    '''
    A simple ping command.
    '''
    await ctx.send('pong')


@bot.tree.command(name='test')
async def test(interaction: Interaction):
    '''
    A simple test command.
    '''
    await interaction.response.send_message('test')


if __name__ == '__main__':
    try:
        ENV = argv[1]
    except IndexError as e:
        # TODO: Use dev env by default
        raise NotImplementedError('No environment specified') from e

    config = GlobalConfigService(config_path(ENV))
    bot.run(config.get_bot_token())

    # TODO: Add a way to listen to the stop signal
