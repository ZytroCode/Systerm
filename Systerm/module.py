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
	_attrs: dict = {}
	_hidden_prefixs: list = ["_"]
	_hidden_items: list = []

	def __init__(self, name: str) -> None:
		super().__init__(name)
		for attr in dir(self):
			if self._not_hidden(attr):
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

# Add function
def add(*args) -> None:
	"""Makes a module importable"""
	error = Exception("add() unknown error")

	if len(args) == 2:
		try:
			sys.modules[args[1]].__class__ = args[0]
			return args[0](args[1])
		except TypeError as e:
			print(e)
			error = TypeError(f"add() takes 2 positional arguments but {len(args) + 1} were given")
	elif len(args) == 1:
		def wrapper(module):
			sys.modules[args[0]].__class__ = module
			return module
		return wrapper
	elif len(args) == 0:
		error = TypeError(f"add() missing 2 required positional arguments: 'module', 'test'")
	elif len(args) >= 3:
		error = TypeError(f"add() takes 2 positional arguments but {len(args)} were given")
	raise error

# ModuleMod
@add(__name__)
class ModuleMod(Module):
	"""Module class for Systerm.module"""
	add = add
	modules = modules
	Module = Module
