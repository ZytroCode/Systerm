"""Meta is a module contains objects that will customize the behavior of python"""
import Systerm

# Metaclass
class Metaclass(ABCMeta):
	"""A metaclass to customize the behavior of all classes"""

	def __new__(self, name: str, bases: tuple, attrs: dict, **keys) -> type:
		# Creating a new class
		cls = super().__new__(self, name, bases, dict(attrs))
		
		return cls
