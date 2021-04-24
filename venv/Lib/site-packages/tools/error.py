import warnings


class ToolsError(Exception):
    """
    Base class for all custom exceptions
    defined in tools package.
    """


class DataNotFound(ToolsError, IndexError):
    """
    Raised when it is not possible to find requested
    data.
    """


class RuntimeConfigError(ToolsError):
    """
    Raised when passed parameters do not makes sense
    or conflict with something.
    """


def warn(msg):
    warnings.warn(msg, category=GrabDeprecationWarning, stacklevel=3)
