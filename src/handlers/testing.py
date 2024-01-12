from discord import Interaction
from discord.ext.commands import Context


async def test(interaction: Interaction):
    '''
    A simple test command.
    '''
    await interaction.response.send_message('test')


async def ping(ctx: Context):
    '''
    A simple ping command.
    '''
    await ctx.send('pong')


async def stop(interaction: Interaction):
    '''
    A simple stop command.
    '''
    await interaction.response.send_message('Stopping...')
    await interaction.client.close()
