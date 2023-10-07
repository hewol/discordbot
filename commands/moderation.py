import logging

import hikari
import lightbulb

plugin = lightbulb.Plugin(name="Moderation")


@plugin.command()
@lightbulb.option(
    "reason", "Reason for the ban", type=str, required=True
)
@lightbulb.option(
    "member", "The person to ban", type=hikari.Member, required=True
)
@lightbulb.add_checks(lightbulb.has_guild_permissions(hikari.Permissions.BAN_MEMBERS))
@lightbulb.command("ban", "Ban a user from the server")
@lightbulb.implements(lightbulb.SlashCommand)
async def ban(ctx: lightbulb.Context):
    try:
        await ctx.get_guild().ban(ctx.options.member, reason=ctx.options.reason)
        await ctx.respond(f"{ctx.options.member} has been banned from the server for: {ctx.options.reason}")
    except Exception as e:
        logging.error(f"An error occurred while banning {str(ctx.options.member)}: {e}")
        await ctx.respond(f"An error occurred while banning {str(ctx.options.member)}")


@plugin.command()
@lightbulb.option(
    "reason", "Reason for the kick", type=str, required=True
)
@lightbulb.option(
    "member", "The person to kick", type=hikari.Member, required=True
)
@lightbulb.add_checks(lightbulb.has_guild_permissions(hikari.Permissions.KICK_MEMBERS))
@lightbulb.command("kick", "Kick a user from the server")
@lightbulb.implements(lightbulb.SlashCommand)
async def kick(ctx: lightbulb.Context):
    try:
        await ctx.get_guild().kick(ctx.options.member, reason=ctx.options.reason)
        await ctx.respond(f"{str(ctx.options.member)} has been kicked from the server for: {ctx.options.reason}")
    except Exception as e:
        logging.error(f"An error occurred while kicking {str(ctx.options.member)}: {e}")
        await ctx.respond(f"An error occurred while kicking {str(ctx.options.member)}")


def load(bot):
    bot.add_plugin(plugin)


def unload(bot):
    bot.remove_plugin(plugin)
