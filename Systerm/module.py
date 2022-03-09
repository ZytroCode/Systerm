"""Module is used for optimizing python modules"""
import Systerm
import sys

from Systerm import _setup
meta = _setup.init_meta()

# Modules
modules: dict = sys.modules

# Module class
class Module(sys.modules[__name__].__class__, metaclass=meta.Metaclass):

	"""Module class is used for creating a python module"""
	def __init__(self, name: str) -> None:
		super().__init__(name)
		for attr in dir(self):
			if name in self.__namespaces__:
				setattr(self, attr, getattr(self, attr))
	
	@staticmethod
	def super(*instances):
		cls = meta.Metaclass("_", (Module,), dict())

		for instance in instances:
			for name in dir(instance):
				setattr(cls, name, getattr(instance, name))
		
		return cls

	def __dir__(self) -> list:
		return self.__namespaces__

# ModuleMod
class ModuleMod(Module):
	
	"""Module class for Systerm.module"""
