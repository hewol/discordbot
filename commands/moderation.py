import logging

import hikari
import lightbulb

plugin = lightbulb.Plugin(name="Moderation")


@plugin.command()
@lightbulb.has_guild_permissions(hikari.Permissions.BAN_MEMBERS)
@lightbulb.command("ban", "Ban a user from the server")
@lightbulb.implements(lightbulb.SlashCommand)
async def ban(ctx: lightbulb.Context, member: hikari.User, *, reason: str = "No reason provided"):
    try:
        await ctx.get_guild().ban(member, reason=reason)
        await ctx.respond(f"{member.username} has been banned from the server for: {reason}")
    except Exception as e:
        logging.error(f"An error occurred while banning {member.username}: {e}")
        await ctx.respond(f"An error occurred while banning {member.username}")


@plugin.command()
@lightbulb.checks.has_guild_permissions(hikari.Permissions.KICK_MEMBERS)
@lightbulb.command("kick", "Kick a user from the server")
@lightbulb.implements(lightbulb.SlashCommand)
async def kick(ctx: lightbulb.Context, member: hikari.User, *, reason: str = "No reason provided"):
    try:
        await ctx.get_guild().kick(member, reason=reason)
        await ctx.respond(f"{member.username} has been kicked from the server for: {reason}")
    except Exception as e:
        logging.error(f"An error occurred while kicking {member.username}: {e}")
        await ctx.respond(f"An error occurred while kicking {member.username}")


def load(bot):
    bot.add_plugin(plugin)


def unload(bot):
    bot.remove_plugin(plugin)
