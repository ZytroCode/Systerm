"""Module is used for optimizing python modules"""
import Systerm
import sys

from Systerm import _setup
meta = _setup.init_meta()

# Modules
modules: dict = sys.modules

# Module class
class Module(sys.modules[__name__].__class__):
	"""Module class is used for creating a python module"""
	def __init__(self, name: str) -> None:
		super().__init__(name)
		for attr in dir(self):
				setattr(self, attr, getattr(self, attr))

	def __dir__(self) -> list:
		return [attr for attr in dir(self.__class__) if self._not_hidden(attr)]

	def _not_hidden(self, item) -> bool:
		hidden = item in self._hidden_items
		if hidden: return False
		for prefix in self._hidden_prefixs:
			if item.startswith(prefix):
				hidden = True
				break

		return not hidden


# ModuleMod
@add(__name__)
class ModuleMod(Module):
	"""Module class for Systerm.module"""
	add = add
	modules = modules
	Module = Module
