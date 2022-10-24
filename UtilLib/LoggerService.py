import enum
from MasterApprenticeLib.TD1_Lib_MasterLogger import MasterLogger


class LoggerServiceEnums(enum):
    pass


class BaseLoggerService(MasterLogger):
    """
    This is a Base Logger Service using the MasterLogger as Framework. All services should make a new
    class referencing this base class.

    This logger service aims to bridge the MasterLogger and the Python Console where any logging will
    be printed onto the Python Console.

    Usage:
    class XXXService(BaseLoggerService):
        pass

        OR

        def __init__(self):
            super(BaseLoggerService, self).__init__(
                module_name=XXX,
                main_owner=XXX,
                additional_content=XXX
            )
    """
    def __init__(self, module_name=None, main_owner=None, additional_context=None):
        super(BaseLoggerService, self).__init__(
            module_name=self.__class__.__name__ if module_name is None else module_name,
            main_owner="TwelfthDoctor1" if main_owner is None else main_owner,
            additional_context=None if additional_context is None else additional_context
        )

    def info(self, message, owner=None, to_console=True):
        super(BaseLoggerService, self).info(
            message=message,
            owner=owner
        )

        if to_console is True:
            print(message)

    def log(self, message, owner=None, to_console=True):
        super(BaseLoggerService, self).log(
            message=message,
            owner=owner
        )

        if to_console is True:
            print(message)

    def debug(self, message, owner=None, to_console=True):
        super(BaseLoggerService, self).debug(
            message=message,
            owner=owner
        )

        if to_console is True:
            print(message)

    def warn(self, message, owner=None, to_console=True):
        super(BaseLoggerService, self).warn(
            message=message,
            owner=owner
        )

        if to_console is True:
            print(message)

    def error(self, message, owner=None, to_console=True):
        super(BaseLoggerService, self).error(
            message=message,
            owner=owner
        )

        if to_console is True:
            print(message)

    def assert_error(self, message, owner=None, to_console=True):
        super(BaseLoggerService, self).assert_error(
            message=message,
            owner=owner
        )

        if to_console is True:
            print(message)

    def exception(self, message, owner=None, to_console=True):
        super(BaseLoggerService, self).exception(
            message=message,
            owner=owner
        )

        if to_console is True:
            print(message)

    @property
    def get_service_name(self):
        return self.__class__.__name__
