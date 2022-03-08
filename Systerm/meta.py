"""Meta is a module contains objects that will customize the behavior of python"""
import Systerm

# Metaclass
class Metaclass(ABCMeta):
	"""A metaclass to customize the behavior of all classes"""

	def __new__(self, name: str, bases: tuple, attrs: dict, **keys) -> type:
		# Creating a new class
		cls = super().__new__(self, name, bases, dict(attrs))
		
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
