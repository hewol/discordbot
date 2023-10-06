import lightbulb
import hikari
import tanjun
import aiohttp

plugin = lightbulb.Plugin(name="Hello")

@plugin.command()
@lightbulb.command("pingweb", "ping a website and measure response time")
@lightbulb.implements(tanjun.SlashCommand)
async def ping_website(ctx: tanjun.abc.Context, website_url: str):
    try:
        start_time = ctx.timestamp
        async with aiohttp.ClientSession() as session:
            async with session.get(website_url) as response:
                if response.status == 200:
                    end_time = ctx.timestamp
                    response_time = (end_time - start_time).total_seconds() * 1000  # Convert to milliseconds
                    await ctx.respond(f"website {website_url} is online. response time: {response_time:.2f}ms")
                else:
                    await ctx.respond(f"website {website_url} returned status code {response.status}")
    except Exception as e:
        await ctx.respond(f"an error occurred: {str(e)}")

def load(bot):
    bot.add_plugin(plugin)

def unload(bot):
    bot.remove_plugin(plugin)
