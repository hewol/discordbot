import lightbulb

plugin = lightbulb.Plugin(name="Hello")


@plugin.command()
@lightbulb.command("hello", "Says hello")
@lightbulb.implements(lightbulb.SlashCommand)
async def hello(ctx: lightbulb.Context):
    await ctx.respond("Hello!")


def load(bot):
    bot.add_plugin(plugin)


def unload(bot):
    bot.remove_plugin(plugin)
