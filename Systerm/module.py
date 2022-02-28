"""Module is used for optimizing python modules"""
import Systerm
import sys

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
