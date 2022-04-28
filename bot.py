import sys
import disnake
from disnake import User, CommandInteraction, ApplicationCommandInteraction
from disnake.ext.commands import command, Context, is_owner, guild_only
import os
from dotenv import load_dotenv
from pathlib import Path
from MainFunctions.CoreFunction import TD1BotClient
import subprocess
from MainFunctions.DMHandler import dm_cmd, dm_TD1_cmd
from UtilLib.CommandLevel import CommandHandler
from CoFunctions.Interpret_Logger import handle_logfile, interpret_log_base
from UtilLib.DevTools import lookup_dev_cmd
from UtilLib.EmojiHandler import get_emoji

ENV_PATH = os.path.join(Path(__file__).resolve().parent, "Discord_Token.env")

load_dotenv(dotenv_path=ENV_PATH)

# dotenv.find_dotenv(ENV_PATH)
# TOKEN = dotenv.get_key(ENV_PATH, "DISCORD_TOKEN")

TOKEN = os.getenv("DISCORD_TOKEN")
BOT_OWNER_ID = int(os.getenv("DEVELOPER_ID"))

# print(TOKEN)

client = TD1BotClient()


# Groups
@client.group(invoke_without_command=True)
async def Developer(ctx: Context):
    await ctx.send("NULL")


# Commands List
@client.command()
async def version(ctx: Context):
    return await client.version(ctx)


@client.command()
async def test_type(ctx: Context, *, args):
    async with ctx.channel.typing():
        await ctx.send(args)


@client.command()
async def shutdown(ctx: Context):
    return await client.shutdown_bot(ctx)


@client.command()
async def restart(ctx: Context):
    return await client.restart_bot(ctx)


@client.command("determine_log")
async def interpret_MasApp_log(ctx: Context):
    return await interpret_log_base(ctx)


@client.command()
async def set_init_presence(ctx: Context):
    return await client.set_init_presence(ctx)


@client.command()
async def uptime(ctx: Context):
    return await client.uptime(ctx)


@client.command("set_presence")
async def set_msg_presence(ctx: Context, activity: str, *, args):
    return await client.update_presence(ctx, activity, args)


@client.command()
async def dm(ctx: Context, recipient: User, *, args):
    return await dm_cmd(ctx, recipient, args)


@client.command()
async def dm_TD1(ctx: Context, *, args):
    return await dm_TD1_cmd(ctx, client, args)


@client.command()
async def lookup_dev(ctx: Context):
    return await lookup_dev_cmd(ctx, client)


@client.command()
async def ping(ctx: Context):
    return await client.ping_cmd(ctx)


@client.command()
async def verify(ctx: Context):
    return await ctx.reply(
        "This command is no longer used. Please follow the instructions in the channel to gain access to the server."
    )


@client.command()
async def allowable_events(ctx: Context, value):
    if hasattr(ctx.guild, "id") is False:
        return await ctx.send(f"This command can only be used in servers.")

    return client.update_serverdata_cmd(ctx, value)


@client.command()
async def emoji_test(ctx: Context, emoji_id):
    emoji = await get_emoji(ctx.guild, emoji_id)
    return await ctx.reply(f"{emoji}")


# Slash Commands
@client.slash_command(name="dm", description="Sends a Direct Message to a specified user.")
async def dm_slash(inter: ApplicationCommandInteraction, recipient: User, *, message):
    return await dm_cmd(inter, recipient, message)


@client.slash_command(name="dm_TD1", description="Sends a Direct Message to TwelfthDoctor1.")
async def dm_TD1_slash(inter: ApplicationCommandInteraction, *, message):
    return await dm_TD1_cmd(inter, client, message)


@client.slash_command(name="ping", description="Gets the network latency of the bot.")
async def ping_slash(inter: ApplicationCommandInteraction):
    return await client.ping_cmd(inter)


@client.slash_command(name="shutdown", description="Shutdown the bot through non-Python Console means.")
async def shutdown_slash(inter: ApplicationCommandInteraction):
    return await client.shutdown_bot(inter)


@client.slash_command(name="restart", description="Restart the bot through non-Python Console means.")
async def restart_slash(inter: ApplicationCommandInteraction):
    return await client.restart_bot(inter)


@client.slash_command(name="version", description="Return the current version of the Bot and various modules.")
async def version_slash(inter: ApplicationCommandInteraction):
    return await client.version(inter)


@client.slash_command(name="set_presence", description="Change the presence of the Bot.")
async def update_presence_slash(inter: ApplicationCommandInteraction, activity: str, *, message):
    return await client.update_presence(inter, activity, message)


@client.slash_command(name="set_init_presence", description="Change the presence of the bot to the one used at startup.")
async def init_presence_slash(inter: ApplicationCommandInteraction):
    return await client.set_init_presence(inter)


@client.slash_command(name="uptime", description="Shows the uptime of the bot.")
async def uptime_slash(inter: ApplicationCommandInteraction):
    return await client.uptime(inter)


@client.slash_command(name="allowable_events", description="Determines whether events by the bot should be allowed on the event channel.")
async def allowable_events_slash(inter: ApplicationCommandInteraction, value: bool):
    if hasattr(inter.guild, "id") is False:
        return await inter.response.send_message(f"This command can only be used in servers.")

    return await client.update_serverdata_cmd(inter, value)


# Bot Startup Process
# Initiate Communication with Discord API and connect to Bot Allocated Account
client.run(TOKEN)
