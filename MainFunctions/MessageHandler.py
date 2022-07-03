from disnake import ApplicationCommandInteraction
from disnake.ext.commands import Context


class MessageHandler:
    def __init__(self, ctx: Context or ApplicationCommandInteraction):
        self.ctx = ctx
        