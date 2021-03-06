"""Systerm is a multipurpose python library.

Systerm is a powerful extension-like library to python and gives python much more flexibility and power."""
import sys
sys.path.append("..")

# Importing libraries in Systerm
from Systerm import meta
from Systerm import module

from Systerm import console
from Systerm import exit
from Systerm import file
from Systerm import math
from Systerm import random
from Systerm import time

from Systerm.meta import ABC
from Systerm.meta import abstractmethod
from Systerm.file import BaseFile
from Systerm.meta import Dictionary
from Systerm.file import File
from Systerm.meta import List
from Systerm.console import Logger
from Systerm.meta import Metaclass
from Systerm.module import Module
from Systerm.module import modules
from Systerm.meta import Object

# SystermMod class
class SystermMod(Module):
    __version__ = version = "0.4.0"

    logger: Logger = Logger(console.formats["Systerm"])
    extensions: dict = dict(
        # Classes
        Metaclass = Metaclass,
        ABC = ABC,
        list = List,
        dict = Dictionary,
        object = Object,

        # Methods
        abstractmethod = abstractmethod,
        open = BaseFile,
        exit = exit,
    )

    def get_installed(self) -> bool:
        """Returns True if Systerm is installed in runtime."""
        return bool(getattr(modules["builtins"], "__systerm__", False))

    def install(self, ext: bool=False, warn: bool=True) -> None:
        """Installs Systerm on runtime."""
        setattr(modules["builtins"], "__systerm__", modules[__name__])
        if ext:
            for index, value in self.extensions.items():
                setattr(modules["builtins"], index, value)
        if warn:
            if not console.supports_color():
                self.logger.log(name="Systerm", msg="Warning! Console doesn't supports color")

modules[__name__].__class__ = SystermMod
