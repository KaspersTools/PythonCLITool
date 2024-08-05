import enum

from rich.console import Console

__all__ = ["LogLevels", "LogStyle", "err", "warn", "info", "debug", "trace"]


class LogLevels(enum.Enum):
    INFO = "INFO"
    WARNING = "WARNING"
    DEBUG = "DEBUG"
    TRACE = "TRACE"
    ERROR = "ERROR"


class LogStyle:
    info_style = "green"
    warning_style = "yellow"
    debug_style = "magenta"
    trace_style = "white"
    error_style = "bold red"

    @classmethod
    def set_styles(
            cls, info_style: str, warning_style: str, debug_style: str,
            trace_style: str, error_style: str):
        cls.info_style = info_style
        cls.warning_style = warning_style
        cls.debug_style = debug_style
        cls.trace_style = trace_style
        cls.error_style = error_style

    @classmethod
    def get_styles(cls):
        return (cls.info_style, cls.warning_style, cls.debug_style,
                cls.trace_style, cls.error_style)


def err(line: str, console: Console) -> None:
    """
    Print an error line to the console=console with the appropriate style.

    Args:
        line (str): the error message
        console (rich.Console) the rich console
    """
    console.print(line.strip(), style=LogStyle.error_style)


def warn(line: str, console: Console) -> None:
    """
    Print a warning line to the console=console with the appropriate style.

    Args:
        line (str): the warning message
        console (rich.Console) the rich console
    """
    console.print(line.strip(), style=LogStyle.warning_style)


def info(line: str, console: Console) \
        -> None:
    """
    Print an info line to the console=console with the appropriate style.

    Args:
        line (str): the info message
        console (rich.Console) the rich console
    """
    console.print(line.strip(), style=LogStyle.info_style)


def debug(line: str, console: Console) \
        -> None:
    """
    Print a debug line to the console=console with the appropriate style.

   Args:
        line (str): the debug message
        console (rich.Console) the rich console
    """
    console.print(line.strip(), style=LogStyle.debug_style)


def trace(line: str, console: Console) \
        -> None:
    """
    Print a trace line to the console=console with the appropriate style.

    Args:
        line (str): the trace message
        console (rich.Console) the rich console
    """
    console.print(line.strip(), style=LogStyle.trace_style)
