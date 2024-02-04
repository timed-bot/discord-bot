from ui.views import TimeBotView


async def timebot(ctx):
    view = TimeBotView()
    view.ctx = ctx
    await ctx.send('Выберите действие:', view=view, ephemeral=True)
