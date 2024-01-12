from discord.ext.commands import Bot
from discord import Interaction


async def on_ready(bot: Bot):
    synced = await bot.tree.sync()
    print(f'Synced {len(synced)} commands')


async def on_interaction(interaction: Interaction):
    print(interaction.data)
