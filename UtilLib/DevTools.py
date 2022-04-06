import os
from disnake import User, ApplicationCommandInteraction
from disnake.ext.commands import Context
from UtilLib.CommandLevel import CommandHandler


async def lookup_dev_cmd(ctx: Context or ApplicationCommandInteraction, client):
    cmd_handler = CommandHandler(CommandHandler.DEVELOPER, ctx.author.id)

    if cmd_handler.check_cmd_lvl() is False:
        return await ctx.send("You are not eligible to use this command.")

    dev_usr: User = await client.fetch_user(int(os.getenv('DEVELOPER_ID')))
    await ctx.reply(f"USER: {dev_usr.display_name} | {dev_usr.discriminator}")
