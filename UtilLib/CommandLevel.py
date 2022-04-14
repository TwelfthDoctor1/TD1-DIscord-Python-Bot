import os
from disnake import ApplicationCommandInteraction
from disnake.ext.commands import Context
from CoFunctions.ServerDataHandler import acquire_data, acquire_admin


class CommandHandler:
    NONE = 0  # CMD_LVL should NOT be used, LVL ALL onwards should be used
    ALL = 1
    SRV_ADMIN = 2
    SRV_OWNER = 3
    ADMIN = 4
    DEVELOPER = 5

    def __init__(self, min_level=ALL, max_level=None, user_id=0, server=None):
        self.server = server
        self.min_level = min_level
        self.max_level = max_level if max_level is not None and max_level <= self.DEVELOPER else self.DEVELOPER
        self.user_id = user_id

    def is_dev(self):
        dev_env = int(os.getenv("DEVELOPER_ID"))

        if dev_env == self.user_id:
            return True

        else:
            return False

    def is_admin(self):
        if acquire_admin(self.user_id):
            return True
        else:
            return False

    def is_server_owner(self):
        owner_id = acquire_data("server_owner", self.server)
        if self.server.owner_id == owner_id:
            return True
        else:
            return False

    def is_server_admin(self):
        admins = acquire_data("server_admins", self.server)
        for admin in admins:
            if admin == self.user_id:
                return True

        return False

    def check_cmd_lvl(self, level):
        if level == self.DEVELOPER:
            return self.is_dev()
        elif level == self.ADMIN:
            return self.is_admin()
        elif level == self.SRV_OWNER:
            return self.is_server_owner()
        elif level == self.SRV_ADMIN:
            return self.is_server_admin()
        else:
            return True

    def return_set_lvl(self, level):
        if level == self.NONE:
            return "No Set Requirement (Should not be seen)"
        elif level == self.ALL:
            return "Everybody"
        elif level == self.ADMIN:
            return "Server Admin"
        elif level == self.SRV_OWNER:
            return "Server Owner"
        elif level == self.ADMIN:
            return "Bot Admin"
        elif level == self.DEVELOPER:
            return "Bot Developer"

    def return_min_lvl(self):
        return f"The minimum required rank to use this command is {self.return_set_lvl(self.min_level)}."

    def return_max_lvl(self):
        if self.max_level == self.min_level:
            return None
        else:
            return f"The maximum allowable rank is {self.return_set_lvl(self.max_level)}."

    async def check_cmd_req(self, ctx: Context or ApplicationCommandInteraction, message=None):
        if self.check_cmd_lvl(self.min_level) is False:
            if message is None:
                if self.max_level is None:
                    err_msg = f"You are not eligible to use this command. {self.return_min_lvl()}"
                else:
                    err_msg = f"You are not eligible to use this command. {self.return_min_lvl()} {self.return_max_lvl()}"
            else:
                if self.max_level is None:
                    err_msg = f"{message} {self.return_min_lvl()}"
                else:
                    err_msg = f"{message} {self.return_min_lvl()} {self.return_max_lvl()}"

            return await ctx.response.send_message(err_msg) if hasattr(ctx, "response") else await ctx.send(err_msg)
