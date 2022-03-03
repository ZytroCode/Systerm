"""Instance is used for managing instances and classes"""
import Systerm

# InstanceMod
@Systerm.module.add(__name__)
class InstanceMod(Systerm.Module):
	"""Module class for Systerm.instance"""
	def super(self, instance: object) -> object:
		"""Inherits an instance to an object"""
		def wrapper(obj):
			for attr in dir(instance):
				setattr(obj, attr, getattr(instance, attr))
			return obj
		return wrapper
