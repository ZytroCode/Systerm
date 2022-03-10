"""Meta is a module contains objects that will customize the behavior of python."""
from abc import ABC
from abc import ABCMeta
from abc import abstractmethod
from typing import Any
from typing import Callable

import Systerm

# Metaclass
class Metaclass(ABCMeta):
	"""A metaclass to customize the behavior of all classes."""

	def __new__(self, name: str, bases: tuple, attrs: dict, **keys: Any) -> type:
		"""The static constructor for the Metaclass.

		Parameters:
			name - str:		The name of the class
			bases - tuple:	A tuple of classes to be inherited
			attrs - dict:	A dictionary of attributes of the class
		"""
		# Creating a new class
		cls = super().__new__(self, name, bases, dict(attrs), **keys)
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

def get_namespaces(object: Object):
	"""Gets the namespaces of an object."""
	return object.__namespaces__

def get_magics(object: Object):
	"""Gets the magic methods of an object."""
	return object.__magics__

def get_attributes(object: Object):
	"""Gets the attributes of an object."""
	return object.__attributes__

def get_publics(object: Object):
	"""Gets the public namespaces of an object."""
	return object.__publics__

def get_privates(object: Object):
	"""Gets the private namespaces of an object."""
	return object.__privates__

def get_protecteds(object: Object):
	"""Gets the protected namespaces of an object."""
	return object.__protecteds__

# Initializing Systerm.module
from Systerm._setup import init_module
module = init_module()

# MetaMod class
class MetaMod(module.Module):
	pass

module.modules[__name__].__class__ = MetaMod
