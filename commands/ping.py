import hikari
import lightbulb

plugin = lightbulb.Plugin(name="Ping")


@plugin.command()
@lightbulb.command("ping", "check the bot's ping")
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx: lightbulb.Context):
    latency = round(ctx.bot.heartbeat_latency * 1000)
    await ctx.respond(f"Pong! Bot latency: {latency}ms")


def load(bot):
    bot.add_plugin(plugin)


def unload(bot):
    bot.remove_plugin(plugin)
