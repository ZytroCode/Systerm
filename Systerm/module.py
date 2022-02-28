"""Module is used for optimizing python modules"""
import Systerm
import sys

# Module class
class Module(sys.modules[__name__].__class__):
	"""Module class is used for creating a python module"""
	def __init__(self, name):
		super().__init__(name)
		sys.modules[name].__class__ = self.__class__
