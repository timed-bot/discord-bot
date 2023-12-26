import discord
from discord.ext import commands
from env import CONFIG_PATH

from services import GlobalConfigService

intents = discord.Intents.all()
intents.message_content = True
bot = commands.Bot(command_prefix='>', intents=intents)
config = GlobalConfigService(CONFIG_PATH)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')

bot.run(config.get_bot_token())