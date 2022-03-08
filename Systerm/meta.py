"""Meta is a module contains objects that will customize the behavior of python"""
import Systerm

# Metaclass
class Metaclass(ABCMeta):
	"""A metaclass to customize the behavior of all classes"""

	def __new__(self, name: str, bases: tuple, attrs: dict, **keys) -> type:
		# Creating a new class
		cls = super().__new__(self, name, bases, dict(attrs))
		cls.__setattr__ = self.setattr

		# Custom magic methods
		cls.__namespace__ = {}
		cls.__magics__ = {}
		cls.__attributes__ = {}
		cls.__public__ = {}
		cls.__private__ = {}
		cls.__protected__ = {}

		# Setting objects
		for name in dir(cls):
			value = getattr(cls, name)

			# Adds attributes to __magics__
			if name.startswith("__") and name.endswith("__"):
				cls.__magics__[name] = value

			# Adds attributes to other namespace
			else:
				# Adds attributes to __private__
				if name.startswith("__"):
					cls.__private__[name] = value
				
				# Adds attributes to __protected__
				elif name.startswith("_"):
					cls.__protected__[name] = value
				# Adds attributes to __public__
				else:
					cls.__public__[name] = value
				
				cls.__attributes__[name] = value
			
			# Adds attributes to namespace
			cls.__namespace__[name] = value
		
		return cls

	def setattr(self, name: str, value: object) -> None:
		# Adds attributes to __magics__
		if name.startswith("__") and name.endswith("__"):
			self.__magics__[name] = value
		
		# Adds attributes to other namespace
		else:
			# Adds attributes to __private__
			if name.startswith("__"):
				self.__private__[name] = value
			
			# Adds attributes to __protected__
			elif name.startswith("_"):
				self.__protected__[name] = value
			
			# Adds attributes to __public__
			else:
				self.__public__[name] = value
			
			self.__attributes__[name] = value
		
		# Adds attributes to namespace
		self.__namespace__[name] = value

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
