import os


class CommandHandler:
    NONE = 0
    ALL = 1
    ADMIN = 2
    SRV_OWNER = 3
    DEVELOPER = 4

    def __init__(self, level, user_id):
        self.level = level
        self.user_id = user_id

    def is_dev(self):
        dev_env = int(os.getenv("DEVELOPER_ID"))

        if dev_env == self.user_id:
            return True

        else:
            return False

    def check_cmd_lvl(self):
        if self.level == self.DEVELOPER:
            return self.is_dev()
