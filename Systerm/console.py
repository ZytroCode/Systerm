"""Console is used for interpreting the stream."""
import builtins
import os
from typing import Any, Callable, Optional, Union

import Systerm

# Log formats
formats: dict = dict(
    Systerm = "[%(name)s] %(msg)s",
    basic = "%(msg)s",
)

# Logger class
class Logger(object):
    """
    Creates a logger object that logs values and listens for inputs in the stream.

    Attributes:
        format - str:	The format of the log and the listen method

    Methods:
        log(**values):		Logs values in the stream
        listen(**values):	Listens for an input in the stream
    """
    def __init__(self, format: Optional[str]=formats["basic"]) -> None:
        """The constructor for the Logger class.

        Parameters:
            format - Optional[str]:	The format of the log and the listen method
        """
        self.format: str = format

    def log(self, **values: Optional[Any]) -> None:
        """Logs values in the stream.

        Parameters:
            **values - Optional[Any]:	The values to be log in the stream
        """
        print(self.format % values)

    def listen(self, **values: Optional[Any]) -> Any:
        """Listens for an input in the stream.

        Parameters:
            **values - Optional[Any]:	The values to be ask in the stream
        """
        return input(self.format % values)

# ConsoleMod class
class ConsoleMod(Systerm.module.Module):
    send = write = print =	builtins.print
    scan = input = listen =	builtins.input

    call: Callable[[Union[str, bytes]], int] = lambda command:os.system(command)

Systerm.module.modules[__name__].__class__ = ConsoleMod
