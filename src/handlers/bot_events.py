from discord.ext.commands import Bot


async def on_ready(bot: Bot):
    synced = await bot.tree.sync()
    print(f'Synced {len(synced)} commands')
