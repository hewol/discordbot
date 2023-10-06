import hikari
import lightbulb

plugin = lightbulb.Plugin(name="Hello")


@plugin.command()
@lightbulb.command("test", "Test slash commands")
@lightbulb.implements(lightbulb.SlashCommand)
async def test(ctx: lightbulb.Context):
    e = hikari.Embed(
        title="Test embed!",
        description="Test",
        color=hikari.Color.from_hex_code("#315d6e"),
    )
    await ctx.respond(e)


def load(bot):
    bot.add_plugin(plugin)


def unload(bot):
    bot.remove_plugin(plugin)
