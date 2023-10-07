import lightbulb

import aiohttp

plugin = lightbulb.Plugin(name="Joke")


async def fetch_joke():
    async with aiohttp.ClientSession() as session:
        async with session.get("https://official-joke-api.appspot.com/random_joke") as response:
            data = await response.json()
            return data


@plugin.command()
@lightbulb.command("joke", "Tell a random joke")
@lightbulb.implements(lightbulb.SlashCommand)
async def joke(ctx: lightbulb.Context):
    try:
        joke_data = await fetch_joke()
        if joke_data:
            setup = joke_data["setup"]
            punchline = joke_data["punchline"]
            await ctx.respond(f"**Joke:** {setup}\n**Punchline:** {punchline}")
        else:
            await ctx.respond("Failed to fetch a joke.")
    except Exception as e:
        await ctx.respond(f"An error occurred: {str(e)}")


def load(bot):
    bot.add_plugin(plugin)


def unload(bot):
    bot.remove_plugin(plugin)
