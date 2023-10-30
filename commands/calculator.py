import lightbulb

plugin = lightbulb.Plugin(name="Hello")


@plugin.command()
@lightbulb.option(
    "expression", "Enter the expression in the format '26*3' or '345/5', etc.", type=str
)
@lightbulb.command("calculator", "Calculate the given expression")
@lightbulb.implements(lightbulb.SlashCommand)
async def calculator(ctx: lightbulb.Context):
    try:
        if ctx.options.expression in ["0/0", "0 / 0"]:
            return await ctx.respond("I don't know")
        result = eval(ctx.options.expression)
    except ZeroDivisionError:
        return await ctx.respond("Not Approved")
    except (SyntaxError, NameError):
        return await ctx.respond(
            "Please enter a valid expression like `/calc 69*69` or `/calc 69+69` or `/calc 69/14` or `/calc 69-14`"
        )
    await ctx.respond(result)


def load(bot):
    bot.add_plugin(plugin)


def unload(bot):
    bot.remove_plugin(plugin)
