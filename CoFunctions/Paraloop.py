from disnake import ApplicationCommandInteraction, User
from disnake.ext.commands import Context
from MainFunctions.DMHandler import DirectMessageHandler


async def end_paraloop(cycles: int, ctx: Context or ApplicationCommandInteraction):
    """
    A function that will force out a set number of "The end is never the end" message.
    Based on The Stanley Parable reference.

    :param cycles: Number of allowable cycles (116 max)
    :param ctx: The Context or Interaction
    :return:
    """
    END_START_TXT = "The end is never the end"
    END_APPEND_TXT = " is never the end"
    END_TXT = END_START_TXT

    for i in range(cycles):
        END_TXT += END_APPEND_TXT

    await ctx.response.send_message(END_TXT) if hasattr(ctx, "response") else await ctx.send(END_TXT)


async def end_paraloop_targeted(cycles: int, target: User, ctx: Context or ApplicationCommandInteraction):
    """
    A function that will force out a set number of "The end is never the end" message to a targeted user.
    Based on The Stanley Parable reference.

    :param cycles: Number of allowable cycles (116 max)
    :param target: The User to be targeted
    :param ctx: The Context or Interaction
    :return:
    """
    dm_method = DirectMessageHandler(ctx, target)

    END_START_TXT = "The end is never the end"
    END_APPEND_TXT = " is never the end"
    END_TXT = END_START_TXT

    for i in range(cycles):
        END_TXT += END_APPEND_TXT

    await dm_method.send_message_raw(END_TXT)
