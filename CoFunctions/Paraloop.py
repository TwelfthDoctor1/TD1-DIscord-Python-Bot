from disnake import ApplicationCommandInteraction
from disnake.ext.commands import Context


async def end_paraloop(cycles: int, ctx: Context or ApplicationCommandInteraction):
    END_START_TXT = "The end is never the end"
    END_APPEND_TXT = " is never the end"
    END_TXT = END_START_TXT

    for i in range(cycles):
        END_TXT += END_APPEND_TXT

    await ctx.response.send_message(END_TXT) if hasattr(ctx, "response") else await ctx.send(END_TXT)
