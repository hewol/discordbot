import lightbulb
import aiohttp

plugin = lightbulb.Plugin(name="Quote")


async def fetch_random_quote():
    async with aiohttp.ClientSession() as session:
        async with session.get("https://api.quotable.io/random") as response:
            data = await response.json()
            return data


@plugin.command()
@lightbulb.command("quote", "Fetch a random quote")
@lightbulb.implements(lightbulb.SlashCommand)
async def quote(ctx: lightbulb.Context):
    try:
        quote_data = await fetch_random_quote()
        if quote_data:
            content = quote_data["content"]
            author = quote_data["author"]
            await ctx.respond(f"**Quote:** {content}\n**Author:** {author}")
        else:
            await ctx.respond("Failed to fetch a quote.")
    except Exception as e:
        await ctx.respond(f"An error occurred: {str(e)}")


def load(bot):
    bot.add_plugin(plugin)


def unload(bot):
    bot.remove_plugin(plugin)
