"""Meta is a module contains objects that will customize the behavior of python"""
import Systerm
import sys

from abc import ABC, ABCMeta
from abc import abstractmethod
from functools import wraps
from typing import Callable

# Metaclass
class Metaclass(ABCMeta):
	"""A metaclass to customize the behavior of all classes"""
	def __new__(self, name: str, bases: tuple, attrs: dict, **keys) -> type:
		# Creating a new class
		cls = super().__new__(self, name, bases, dict(attrs))
		cls.__setattr__ = self.setattr

		# Custom magic methods
		cls.__namespaces__ = {}
		cls.__magics__ = {}
		cls.__attributes__ = {}
		cls.__publics__ = {}
		cls.__privates__ = {}
		cls.__protecteds__ = {}

		# Setting objects
		for name in dir(cls):
			value = getattr(cls, name)

			# Adds attributes to __magics__
			if name.startswith("__") and name.endswith("__"):
				cls.__magics__[name] = value

			# Adds attributes to other namespace
			else:
				# Adds attributes to __privates__
				if name.startswith("__"):
					cls.__privates__[name] = value
				
				# Adds attributes to __protecteds__
				elif name.startswith("_"):
					cls.__protecteds__[name] = value
				# Adds attributes to __publics__
				else:
					cls.__publics__[name] = value
				
				cls.__attributes__[name] = value
			
			# Adds attributes to namespace
			cls.__namespaces__[name] = value
		
		return cls

	def setattr(self, name: str, value: object) -> None:
		# Adds attributes to __magics__
		if name.startswith("__") and name.endswith("__"):
			self.__magics__[name] = value
		
		# Adds attributes to other namespace
		else:
			# Adds attributes to __privates__
			if name.startswith("__"):
				self.__privates__[name] = value
			
			# Adds attributes to __protecteds__
			elif name.startswith("_"):
				self.__protecteds__[name] = value
			
			# Adds attributes to __publics__
			else:
				self.__publics__[name] = value
			
			self.__attributes__[name] = value
		
		# Adds attributes to namespace
		self.__namespaces__[name] = value

# Object class
class Object(object, metaclass=Metaclass):
	pass

# List class
class List(list, metaclass=Metaclass):
	pass

# Dictionary class
class Dictionary(dict, metaclass=Metaclass):
	"""Replacement for the python's builtin dict"""
	def __getattr__(self, name: str) -> None:
		try:
			return self[name]
		except KeyError as e:
			try:
				return super().__getattr__(name)
			except AttributeError:
				raise e
	
	def __setattr__(self, name: str, value: object) -> None:
		self[name] = value

# Recreating ABC
ABC = Metaclass(ABC.__name__, ABC.__bases__, {name: getattr(ABC, name) for name in dir(ABC)})

# Initializing Systerm.module
from Systerm._setup import init_module
module = init_module()

# MetaMod class
class MetaMod(module.Module):
	"""MetaMod class will handle the behavior of Systerm.meta"""

module.modules[__name__].__class__ = MetaMod
