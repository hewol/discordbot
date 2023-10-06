import lightbulb
import aiohttp
import time

plugin = lightbulb.Plugin(name="PingWeb")


@plugin.command()
@lightbulb.option("url", "The website to ping.", required=True, type=str)
@lightbulb.command("pingweb", "Ping a website and measure response time")
@lightbulb.implements(lightbulb.SlashCommand)
async def ping_website(ctx: lightbulb.Context):
    try:
        start_time = time.time()
        async with aiohttp.ClientSession() as session:
            async with session.get(ctx.options.url) as response:
                if response.ok:
                    end_time = time.time()
                    response_time = round(
                        (end_time - start_time) * 1000
                    )  # Convert to milliseconds
                    await ctx.respond(
                        f"Website `{ctx.options.url}` is online. response time: {response_time}ms"
                    )
                else:
                    await ctx.respond(
                        f"Website `{ctx.options.url}` returned status code: {response.status}"
                    )
    except Exception as e:
        await ctx.respond(f"An error occurred: {str(e)}")


def load(bot):
    bot.add_plugin(plugin)


def unload(bot):
    bot.remove_plugin(plugin)
