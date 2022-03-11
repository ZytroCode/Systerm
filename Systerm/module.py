"""Used for optimizing python modules."""
import sys
from typing import Any

import Systerm
from Systerm import _setup

# Initializing Systerm.meta
meta = _setup.init_meta()

# Modules
modules: dict = sys.modules

# Module class
class Module(sys.modules[__name__].__class__, metaclass=meta.Metaclass):
    """Creates a new python module."""
    def __init__(self, name: str) -> None:
        """The constructor for the Module class.

        Parameters:
            name - str:	The name of the module
        """
        super().__init__(name)
        for attr in dir(self):
            if name in self.__namespaces__:
                setattr(self, attr, getattr(self, attr))

    def __dir__(self) -> list:
        return self.__namespaces__

    @staticmethod
    def super(*instances: Any):
        """Creates a new class that inherits instances.

        Parameters:
            *instances - Any:	The instances to be inherit
        """
        cls = meta.Metaclass("_", (Module,), dict())

        for instance in instances:
            for name in dir(instance):
                setattr(cls, name, getattr(instance, name))

        return cls

# ModuleMod class
class ModuleMod(Module):
    pass

modules[__name__].__class__ = ModuleMod
