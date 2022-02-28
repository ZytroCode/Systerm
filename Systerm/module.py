"""Module is used for optimizing python modules"""
import Systerm
import sys

# Modules
modules = sys.modules

# Module class
class Module(sys.modules[__name__].__class__):
	"""Module class is used for creating a python module
	If you don't want an attribute to be in the module, use __ before the name of the attribute"""
	def __init__(self, name):
		super().__init__(name)
		for attr in dir(self):
			if len(attr) <= 2:
				setattr(self, attr, getattr(self, attr))
			elif attr[0] != "_" and attr[1] != "_":
				setattr(self, attr, getattr(self, attr))

# Add function
def add(*args):
	"""Makes a module importable"""
	error = Exception("add() unknown error")

	if len(args) == 2:
		try:
			sys.modules[args[1]] = args[0](args[1])
			return args[0](args[1])
		except TypeError:
			error = TypeError(f"add() takes 2 positional arguments but {len(args) + 1} were given")
	elif len(args) == 1:
		def wrapper(module):
			sys.modules[args[0]] = module(args[0])
			return module
		return wrapper
	elif len(args) == 0:
		error = TypeError(f"add() missing 2 required positional arguments: 'module', 'test'")
	elif len(args) >= 3:
		error = TypeError(f"add() takes 2 positional arguments but {len(args)} were given")
	raise error
