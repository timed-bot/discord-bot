from discord import Intents, Interaction
from discord.ext import commands
from env import CONFIG_PATH

from services import GlobalConfigService

bot = commands.Bot(command_prefix='>', intents=Intents.all())
config = GlobalConfigService(CONFIG_PATH)

@bot.event
async def on_ready():
    try:
        synced = await bot.tree.sync()
        print(f'Synced {len(synced)} commands')
    except Exception as e:
        print(e)

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.tree.command(name='test')
async def test(interaction : Interaction):
    await interaction.response.send_message('test')


bot.run(config.get_bot_token())